"""Playwright-Client, der sich an eine laufende Chrome/LinkedIn-Session andockt.

Verbindung erfolgt über das Chrome DevTools Protocol (CDP). Chrome muss vorher
mit ``--remote-debugging-port=9222`` gestartet und bei LinkedIn eingeloggt sein.
Der Client schließt den Browser NICHT – er stoppt nur die Playwright-Verbindung.

Hinweis: LinkedIn-Selektoren ändern sich häufig. Die Selektoren hier sind
best-effort und mehrsprachig (DE/EN) ausgelegt; ggf. anpassen.
"""
from __future__ import annotations

import random
import re
from urllib.parse import quote_plus

from playwright.async_api import (
    Page,
    TimeoutError as PlaywrightTimeoutError,
    async_playwright,
)

from ..models.content import FeedPost, ProfileCandidate
from ..analytics import extract_counts
from ..config import load_settings
from ..utils.logging import get_logger

FEED_URL = "https://www.linkedin.com/feed/"
# Eigene Aktivität/Wall (leitet auf das eigene Profil weiter)
WALL_URL = "https://www.linkedin.com/in/me/recent-activity/all/"
POSTS_URL = "https://www.linkedin.com/in/me/recent-activity/shares/"
COMMENTS_URL = "https://www.linkedin.com/in/me/recent-activity/comments/"
PEOPLE_SEARCH_URL = "https://www.linkedin.com/search/results/people/?keywords="
AUTOMATION_PAGE_KEY = "linkedin-automation-worker"

log = get_logger("browser.linkedin")


class LinkedInClient:
    def __init__(self, cdp_endpoint: str) -> None:
        self._cdp = cdp_endpoint
        self._action_delay_ms = load_settings().linkedin_action_delay_ms
        self._pw = None
        self._browser = None
        self._page: Page | None = None

    async def __aenter__(self) -> "LinkedInClient":
        self._pw = await async_playwright().start()
        log.info("Verbinde mit Chrome via CDP: %s", self._cdp)
        try:
            self._browser = await self._pw.chromium.connect_over_cdp(self._cdp)
        except Exception:
            # __aexit__ läuft bei einem Fehler in __aenter__ nicht. Ohne diesen
            # Abbau bliebe deshalb für jeden Fehlversuch ein Node-Treiber zurück.
            await self._pw.stop()
            self._pw = None
            raise
        context = (
            self._browser.contexts[0]
            if self._browser.contexts
            else await self._browser.new_context()
        )
        # Ausschließlich den persistent markierten Automationstab verwenden.
        self._page = await self._pick_automation_page(context)
        if self._page is None:
            self._page = await context.new_page()
            await self._page.goto(FEED_URL, wait_until="domcontentloaded")
            await self._mark_automation_page(self._page)
        # Zwischenablage lesen dürfen (für 'Copy link to post').
        try:
            await context.grant_permissions(
                ["clipboard-read", "clipboard-write"], origin="https://www.linkedin.com"
            )
        except Exception:
            pass
        return self

    @staticmethod
    async def _pick_automation_page(context) -> Page | None:
        for page in context.pages:
            try:
                if "linkedin.com" in (page.url or "") and await page.evaluate(
                    "window.name"
                ) == AUTOMATION_PAGE_KEY:
                    return page
            except Exception:
                continue
        return None

    @staticmethod
    async def _mark_automation_page(page: Page) -> None:
        await page.evaluate(
            "key => { window.name = key; document.title = 'LinkedIn Automation'; }",
            AUTOMATION_PAGE_KEY,
        )

    @staticmethod
    def _clean_profile_name(value: str) -> str:
        first_line = value.strip().splitlines()[0].strip()
        return re.sub(r"\s*[•·]\s*\d+(?:st|nd|rd|th)?\s*$", "", first_line, flags=re.I)

    async def __aexit__(self, *_exc: object) -> None:
        # Browser des Nutzers offen lassen; nur Playwright-Verbindung lösen.
        if self._pw is not None:
            if self._page is not None and not self._page.is_closed() and "linkedin.com" in self._page.url:
                try:
                    await self._mark_automation_page(self._page)
                except Exception:
                    pass
            await self._pw.stop()

    @property
    def page(self) -> Page:
        if self._page is None:
            raise RuntimeError("LinkedInClient nicht initialisiert (async with verwenden).")
        return self._page

    async def ensure_logged_in(self) -> bool:
        page = self.page
        try:
            await page.goto(FEED_URL, wait_until="domcontentloaded")
        except PlaywrightTimeoutError:
            # LinkedIn kann die Navigation bereits auf den Feed committed haben,
            # obwohl Playwright vergeblich auf DOMContentLoaded wartet.
            if "linkedin.com" not in (page.url or ""):
                raise
            log.warning(
                "Feed-Navigation meldete einen Timeout; prüfe den erreichten URL-Status."
            )
        if any(marker in page.url for marker in ("login", "checkpoint", "authwall")):
            log.error("Nicht eingeloggt. Bitte in der Chrome-Session bei LinkedIn anmelden.")
            return False
        return True

    def action_delay_ms(self, configured_ms: int) -> int:
        """Gibt den konfigurierten Abstand unverändert zurück."""
        return max(0, random.randint(configured_ms - 1000, configured_ms + 1000))

    async def _wait_before_write(self) -> None:
        """Begrenzt die Frequenz finaler LinkedIn-Schreibaktionen."""
        await self.page.wait_for_timeout(self.action_delay_ms(self._action_delay_ms))

    async def collect_feed(self, keywords: list[str], limit: int = 10, with_urls: bool = False) -> list[FeedPost]:
        """Sammelt Beiträge aus dem Feed, optional gefiltert nach Keywords."""
        return await self._collect(FEED_URL, keywords, limit, with_urls)

    async def collect_wall(self, keywords: list[str], limit: int = 10, with_urls: bool = False) -> list[FeedPost]:
        """Sammelt Beiträge von der eigenen Wall / Aktivität."""
        return await self._collect(WALL_URL, keywords, limit, with_urls)

    async def collect_people(self, query: str, limit: int = 5) -> list[ProfileCandidate]:
        """Sammelt noch nicht angefragte Profile mit sichtbarer Vernetzen-Aktion."""
        page = self.page
        await page.goto(
            PEOPLE_SEARCH_URL + quote_plus(query), wait_until="domcontentloaded"
        )
        await page.wait_for_timeout(self.action_delay_ms(2500))
        candidates: list[ProfileCandidate] = []
        seen: set[str] = set()
        selector = (
            "li.reusable-search__result-container, "
            "div[data-view-name='search-entity-result-universal-template'], "
            "div.entity-result, "
            "div[role='listitem']"
        )
        visible_profile_links = await page.locator("a[href*='/in/']").count()
        visible_connect_actions = await page.get_by_text(
            re.compile(r"^(connect|vernetzen)$", re.I), exact=True
        ).count()
        for _ in range(max(5, limit)):
            nodes = page.locator(selector)
            if not await nodes.count() and visible_profile_links:
                raise RuntimeError(
                    "linkedin_ui_selector_mismatch: profile links visible but no search cards found"
                )
            for index in range(await nodes.count()):
                node = nodes.nth(index)
                try:
                    text = "\n".join(
                        line.strip() for line in (await node.inner_text()).splitlines()
                        if line.strip()
                    )
                    lowered = text.casefold()
                    if re.search(r"\b(pending|ausstehend|message|nachricht)\b", lowered):
                        continue
                    connect = node.get_by_role(
                        "button", name=re.compile(r"connect|vernetzen", re.I)
                    )
                    connect_text = node.get_by_text(
                        re.compile(r"^(connect|vernetzen)$", re.I), exact=True
                    )
                    if not await connect.count() and not await connect_text.count():
                        continue
                    link = node.locator("a[href*='/in/']").first
                    href = await link.get_attribute("href")
                    if not href:
                        continue
                    if href.startswith("/"):
                        href = "https://www.linkedin.com" + href
                    profile_url = href.split("?")[0].rstrip("/") + "/"
                    if profile_url in seen:
                        continue
                    seen.add(profile_url)
                    name = self._clean_profile_name(await link.inner_text())
                    if not name:
                        continue
                    candidates.append(
                        ProfileCandidate(name=name[:120], headline=text[:2000], url=profile_url)
                    )
                except Exception:
                    continue
                if len(candidates) >= limit:
                    return candidates
            if await nodes.count():
                await nodes.last.scroll_into_view_if_needed()
            await page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
            await page.wait_for_timeout(self.action_delay_ms(900))
        if not candidates and visible_connect_actions:
            raise RuntimeError(
                "linkedin_ui_selector_mismatch: connect actions visible but no candidates parsed"
            )
        return candidates

    async def send_connection_by_url(self, url: str, note: str) -> bool:
        """Sendet eine Vernetzungsanfrage nur, wenn eine persönliche Notiz möglich ist."""
        if not note.strip() or len(note) > 300:
            return False
        page = self.page
        page.set_default_timeout(10_000)
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=20_000)
            await page.wait_for_timeout(self.action_delay_ms(1800))
            if "login" in page.url or "checkpoint" in page.url:
                return False
            if await page.get_by_text(re.compile(r"pending|ausstehend", re.I)).count():
                return False

            connect = page.get_by_role(
                "button", name=re.compile(r"connect|vernetzen", re.I)
            )
            if not await connect.count():
                more = page.get_by_role(
                    "button", name=re.compile(r"^(more|mehr)$", re.I)
                )
                if await more.count():
                    await more.first.click()
                    connect = page.get_by_role(
                        "menuitem", name=re.compile(r"connect|vernetzen", re.I)
                    )
            if not await connect.count():
                return False
            await connect.first.click()

            dialog = page.get_by_role("dialog").last
            await dialog.wait_for(state="visible")
            add_note = dialog.get_by_role(
                "button", name=re.compile(r"add a note|notiz hinzufügen", re.I)
            )
            if not await add_note.count():
                return False
            await add_note.click()
            editor = dialog.locator("textarea").first
            await editor.fill(note.strip())
            send = dialog.get_by_role(
                "button", name=re.compile(r"^(send|senden)$", re.I)
            )
            await self._wait_before_write()
            await send.click()
            await page.wait_for_timeout(self.action_delay_ms(1200))
            return True
        except Exception as exc:
            log.error("Vernetzungsanfrage fehlgeschlagen (%s): %s", url, exc)
            return False

    async def get_post_by_url(self, url: str) -> FeedPost | None:
        """Lädt einen einzelnen Permalink und gibt den vollständigen sichtbaren Beitrag zurück."""
        page = self.page
        page.set_default_timeout(10_000)
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=20_000)
            await page.wait_for_timeout(self.action_delay_ms(2500))
            if "login" in page.url or "checkpoint" in page.url:
                return None

            selectors = (
                "div.feed-shared-update-v2",
                "div[role='listitem'][componentkey^='update-card-focus']",
                "main article",
            )
            node = None
            for selector in selectors:
                candidate = page.locator(selector)
                if await candidate.count():
                    node = candidate.first
                    break
            if node is None:
                return None

            try:
                text = (await node.inner_text()).strip()
            except Exception:
                return None
            if not text:
                return None

            author = ""
            for selector in (
                "span.update-components-actor__name",
                "a.update-components-actor__meta-link span[aria-hidden='true']",
            ):
                try:
                    value = (await node.locator(selector).first.inner_text()).strip()
                except Exception:
                    continue
                if value:
                    author = value
                    break
            if not author:
                lines = [line.strip() for line in text.splitlines() if line.strip()]
                author = next((line for line in lines if line.lower() != "feed post"), "")[:120]
            return FeedPost(id=page.url, author=author, text=text, url=page.url)
        finally:
            await self._mark_automation_page(page)

    async def get_post_url(self, node) -> str | None:
        """Ermittelt die Permalink-URL eines Beitrags über '… → Copy link to post'."""
        page = self.page
        try:
            await node.scroll_into_view_if_needed()
            # Zuerst ohne Menü/Clipboard: klassische Karten tragen die URN direkt,
            # neuere Varianten meist einen bereits vorhandenen Permalink.
            for attribute in ("data-urn", "componentkey"):
                raw = await node.get_attribute(attribute)
                match = re.search(r"urn:li:(?:activity|ugcPost):\d+", raw or "")
                if match:
                    return f"https://www.linkedin.com/feed/update/{match.group(0)}/"
            links = node.locator(
                "a[href*='/feed/update/urn:li:'], a[href*='/posts/']"
            )
            for index in range(min(await links.count(), 12)):
                href = await links.nth(index).get_attribute("href")
                if not href:
                    continue
                if href.startswith("/"):
                    href = "https://www.linkedin.com" + href
                return href

            ctrl = node.get_by_role(
                "button", name=re.compile(r"(control menu|more|options|mehr|…)", re.I)
            )
            if not await ctrl.count():
                return None
            await ctrl.first.click(timeout=3000)
            await page.wait_for_timeout(self.action_delay_ms(800))
            copy = page.get_by_role(
                "menuitem", name=re.compile(r"copy link|link.*kopieren", re.I)
            )
            if not await copy.count():
                await page.keyboard.press("Escape")
                return None
            await copy.first.click(timeout=3000)
            await page.wait_for_timeout(self.action_delay_ms(900))
            url = await page.evaluate("navigator.clipboard.readText()")
            return url or None
        except Exception as exc:
            log.warning("URL konnte nicht ermittelt werden: %s", exc)
            try:
                await page.keyboard.press("Escape")
            except Exception:
                pass
            return None

    async def find_recent_activity_url(self, kind: str, text: str) -> str | None:
        """Findet nach dem Veröffentlichen den zugehörigen Aktivitäts-Permalink."""
        page = self.page
        activity_url = COMMENTS_URL if kind == "comment" else POSTS_URL if kind == "post" else WALL_URL
        probe = " ".join(text.split())[:100].lower()
        if not probe:
            return None
        await page.goto(activity_url, wait_until="domcontentloaded", timeout=20_000)
        await page.wait_for_timeout(self.action_delay_ms(2200))
        seen: set[str] = set()
        for _ in range(15):
            nodes = page.locator(
                "div.feed-shared-update-v2, "
                "div[role='listitem'][componentkey^='update-card-focus'], main article"
            )
            count = await nodes.count()
            for index in range(count):
                node = nodes.nth(index)
                try:
                    visible = " ".join((await node.inner_text()).split()).lower()
                except Exception:
                    continue
                signature = visible[:180]
                if signature in seen:
                    continue
                seen.add(signature)
                if probe in visible:
                    return await self.get_post_url(node)
            if count:
                try:
                    await nodes.nth(count - 1).scroll_into_view_if_needed()
                except Exception:
                    pass
            await page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
            await page.wait_for_timeout(self.action_delay_ms(1100))
        return None

    async def get_engagement_metrics(
        self, url: str, kind: str, text: str
    ) -> dict[str, int | None] | None:
        """Liest sichtbare Kennzahlen eines eigenen Posts/Reshares oder Kommentars."""
        page = self.page
        page.set_default_timeout(10_000)
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=25_000)
            await page.wait_for_timeout(self.action_delay_ms(2500))
            if "login" in page.url or "checkpoint" in page.url:
                return None

            node = None
            is_comment = kind == "comment"
            if is_comment:
                probe = " ".join(text.split())[:80].lower()
                candidates = page.locator(
                    "article.comments-comment-entity, div.comments-comment-entity, "
                    "li.comments-comment-item, div[data-id*='comment']"
                )
                for index in range(min(await candidates.count(), 120)):
                    candidate = candidates.nth(index)
                    try:
                        visible = " ".join((await candidate.inner_text()).split()).lower()
                    except Exception:
                        continue
                    if probe and probe in visible:
                        node = candidate
                        break
            else:
                for selector in (
                    "div.feed-shared-update-v2",
                    "div[role='listitem'][componentkey^='update-card-focus']",
                    "main article",
                ):
                    candidate = page.locator(selector)
                    if await candidate.count():
                        node = candidate.first
                        break
            if node is None:
                return None

            visible = await node.inner_text()
            labels = await node.locator("[aria-label]").evaluate_all(
                "els => els.map(el => el.getAttribute('aria-label') || '').join('\\n')"
            )
            if not is_comment:
                # Impressionen stehen bei eigenen Beiträgen teils außerhalb der Post-Karte.
                impression_nodes = page.get_by_text(
                    re.compile(r"impressions?|impressionen", re.I)
                )
                extra = []
                for index in range(min(await impression_nodes.count(), 5)):
                    try:
                        extra.append(await impression_nodes.nth(index).inner_text())
                    except Exception:
                        pass
                labels += "\n" + "\n".join(extra)
            return extract_counts(f"{visible}\n{labels}", comment=is_comment)
        finally:
            await self._mark_automation_page(page)

    async def _set_editor_text(self, editor, text: str) -> None:
        """Text sofort wie beim Einfügen setzen, statt jedes Zeichen zu tippen.

        ``fill`` unterstützt auch LinkedIns contenteditable-/Quill-Editoren und löst
        das notwendige Input-Event aus. ``insert_text`` ist der CDP-Fallback, ohne
        die Zwischenablage des Nutzers zu überschreiben.
        """
        await editor.click()
        try:
            await editor.fill(text, timeout=8000)
        except Exception as exc:
            log.warning("Direktes Einfügen via fill fehlgeschlagen, nutze CDP-Fallback: %s", exc)
            try:
                await editor.press("ControlOrMeta+A")
            except Exception:
                pass
            await self.page.keyboard.insert_text(text)

    async def _collect(
        self, url: str, keywords: list[str], limit: int = 10, with_urls: bool = False
    ) -> list[FeedPost]:
        page = self.page
        await page.goto(url, wait_until="domcontentloaded")
        await page.wait_for_timeout(self.action_delay_ms(2500))

        # Variante einmal bestimmen: klassisch (Wall) vs. neue Feed-Variante.
        classic = await page.locator("div.feed-shared-update-v2").count() > 0
        selector = (
            "div.feed-shared-update-v2"
            if classic
            else "div[role='listitem'][componentkey^='update-card-focus']"
        )
        kw = [k.lower() for k in keywords]

        posts: list[FeedPost] = []
        seen: set[str] = set()
        # Der neue Feed ist virtualisiert (wenige Nodes im DOM) → inkrementell scrollen.
        max_scrolls = max(8, limit)
        stale = 0
        for _ in range(max_scrolls):
            containers = page.locator(selector)
            count = await containers.count()
            before = len(posts)
            for i in range(count):
                node = containers.nth(i)
                try:
                    text = (await node.inner_text()).strip()
                except Exception:
                    continue
                if not text:
                    continue
                sig = " ".join(text.split())[:160]  # Dedup über Textsignatur
                if sig in seen:
                    continue
                seen.add(sig)
                if kw and not any(k in text.lower() for k in kw):
                    continue

                if classic:
                    urn = await node.get_attribute("data-urn") or f"feed-{len(posts)}"
                    author = ""
                    try:
                        author = (
                            await node.locator("span.update-components-actor__name")
                            .first.inner_text()
                        ).strip()
                    except Exception:
                        pass
                else:
                    urn = await node.get_attribute("componentkey") or f"feed-{len(posts)}"
                    lines = [ln.strip() for ln in text.split("\n") if ln.strip()]
                    author = next(
                        (ln for ln in lines if ln.lower() not in ("feed post",)), ""
                    )[:80]

                posts.append(FeedPost(id=urn, author=author, text=text))
                if with_urls:
                    try:
                        posts[-1].url = await self.get_post_url(node)
                    except Exception:
                        pass
                if len(posts) >= limit:
                    break

            if len(posts) >= limit:
                break
            # Abbruch, wenn mehrere Scrolls nichts Neues bringen.
            stale = stale + 1 if len(posts) == before else 0
            if stale >= 4:
                break
            # Virtualisierten Feed vorantreiben: letzten Node in den Blick scrollen + JS-Scroll.
            try:
                if count:
                    await containers.nth(count - 1).scroll_into_view_if_needed()
            except Exception:
                pass
            await page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
            await page.wait_for_timeout(self.action_delay_ms(1600))

        log.info("%d Beitrag/Beiträge gesammelt (%s)", len(posts), "classic" if classic else "new-feed")
        return posts

    async def create_post(self, text: str, image_path: str | None = None) -> bool:
        """Erstellt einen neuen Feed-Beitrag, optional mit Bild."""
        page = self.page
        await page.goto(FEED_URL, wait_until="domcontentloaded")
        await page.wait_for_timeout(self.action_delay_ms(1500))

        try:
            dialog = await self._open_post_dialog()
            await dialog.wait_for(state="visible", timeout=8000)
            editor = dialog.get_by_role("textbox").first
            await editor.wait_for(state="visible", timeout=8000)
            await self._set_editor_text(editor, text)
            await page.wait_for_timeout(self.action_delay_ms(800))

            if image_path:
                await self._attach_image(image_path)

            # Submit-Button heißt "Post" (bzw. "Posten"); warten bis aktiv.
            post_btn = dialog.get_by_role(
                "button", name=re.compile(r"^(post|posten)$", re.I)
            ).first
            await post_btn.wait_for(state="visible", timeout=8000)
            await self._wait_before_write()
            await post_btn.click()
            await page.wait_for_timeout(self.action_delay_ms(2000))
            log.info("Beitrag veröffentlicht%s.", " (mit Bild)" if image_path else "")
            return True
        except Exception as exc:
            log.error("Beitrag konnte nicht veröffentlicht werden: %s", exc)
            return False

    async def _open_post_dialog(self):
        pattern = re.compile(r"(start a post|beitrag (starten|verfassen))", re.I)
        starters = (
            self.page.get_by_role("button", name=pattern),
            self.page.get_by_text(pattern, exact=True),
        )
        for starter in starters:
            if await starter.count():
                await starter.first.click()
                break
        else:
            raise RuntimeError("LinkedIn-Element zum Starten eines Beitrags nicht gefunden")
        return self.page.locator('[role="dialog"]:visible').last

    async def _attach_image(self, image_path: str) -> None:
        """Hängt ein Bild an den offenen Post-Editor an (best-effort)."""
        page = self.page
        try:
            async with page.expect_file_chooser() as fc_info:
                await page.get_by_role(
                    "button", name=re.compile(r"(add media|add a photo|foto|medien|media|bild)", re.I)
                ).first.click()
            chooser = await fc_info.value
            await chooser.set_files(image_path)
            await page.wait_for_timeout(self.action_delay_ms(1500))
            # Manche Dialoge haben einen "Weiter/Fertig"-Button.
            done = page.get_by_role(
                "button", name=re.compile(r"^(next|weiter|done|fertig)$", re.I)
            )
            if await done.count() > 0:
                await done.first.click()
                await page.wait_for_timeout(self.action_delay_ms(800))
        except Exception as exc:
            log.warning("Bild konnte nicht angehängt werden: %s", exc)

    async def reshare(self, post: FeedPost, thoughts: str | None = None) -> bool:
        """Teilt (repostet) einen Feed-Beitrag, optional mit eigener Meinung."""
        try:
            node = await self._locate_post(post)
            return await self._reshare_node(node, post.id, thoughts)
        except Exception as exc:
            log.error("Reshare fehlgeschlagen (%s): %s", post.id, exc)
            return False

    async def reshare_by_url(self, url: str, thoughts: str | None = None) -> bool:
        """Teilt einen Beitrag stabil über seine gespeicherte Permalink-URL."""
        page = self.page
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=20_000)
            await page.wait_for_timeout(self.action_delay_ms(2000))
            selectors = (
                "div.feed-shared-update-v2",
                "div[role='listitem'][componentkey^='update-card-focus']",
                "main article",
            )
            node = None
            for selector in selectors:
                candidate = page.locator(selector)
                if await candidate.count():
                    node = candidate.first
                    break
            if node is None:
                raise RuntimeError("Beitragscontainer am Permalink nicht gefunden")
            return await self._reshare_node(node, page.url, thoughts)
        except Exception as exc:
            log.error("Reshare über URL fehlgeschlagen (%s): %s", url, exc)
            return False

    async def _reshare_node(self, node, identifier: str, thoughts: str | None) -> bool:
        page = self.page
        try:
            await node.scroll_into_view_if_needed()
            await node.get_by_role(
                "button", name=re.compile(r"(repost|teilen|share)", re.I)
            ).first.click()
            await page.wait_for_timeout(self.action_delay_ms(1000))

            # Menü-Einträge sind div[role=button] "Repost with thoughts" / "Repost instantly".
            if thoughts:
                await page.get_by_role(
                    "button",
                    name=re.compile(r"(repost with thoughts|with your thoughts|mit meinung|gedanken)", re.I),
                ).first.click()
                dialog = page.get_by_role("dialog").first
                await dialog.wait_for(state="visible", timeout=8000)
                editor = dialog.get_by_role("textbox").first
                await editor.wait_for(state="visible", timeout=8000)
                await self._set_editor_text(editor, thoughts)
                await page.wait_for_timeout(self.action_delay_ms(600))
                await dialog.get_by_role(
                    "button", name=re.compile(r"^(post|posten)$", re.I)
                ).first.wait_for(state="visible", timeout=8000)
                await self._wait_before_write()
                await dialog.get_by_role(
                    "button", name=re.compile(r"^(post|posten)$", re.I)
                ).first.click()
            else:
                await self._wait_before_write()
                await page.get_by_role(
                    "button", name=re.compile(r"(repost instantly|sofort|^repost$|^teilen$)", re.I)
                ).first.click()

            await page.wait_for_timeout(self.action_delay_ms(1500))
            log.info("Beitrag geteilt: %s", identifier)
            return True
        except Exception as exc:
            log.error("Reshare fehlgeschlagen (%s): %s", identifier, exc)
            return False

    async def reply_to_comment(self, post: FeedPost, text: str) -> bool:
        """Antwortet auf den ersten Kommentar unter einem Beitrag (best-effort)."""
        page = self.page
        try:
            node = await self._locate_post(post)
            await node.scroll_into_view_if_needed()
            await node.get_by_role(
                "button", name=re.compile(r"(comment|kommentieren|kommentar)", re.I)
            ).first.click()
            await page.wait_for_timeout(self.action_delay_ms(1200))
            reply_btn = node.get_by_role(
                "button", name=re.compile(r"(reply|antworten)", re.I)
            ).first
            await reply_btn.click()
            box = node.get_by_role("textbox").last
            await box.wait_for(state="visible", timeout=8000)
            await self._set_editor_text(box, text)
            await page.wait_for_timeout(self.action_delay_ms(600))
            await node.get_by_role(
                "button", name=re.compile(r"(reply|antworten|post|senden)", re.I)
            ).last.wait_for(state="visible", timeout=8000)
            await self._wait_before_write()
            await node.get_by_role(
                "button", name=re.compile(r"(reply|antworten|post|senden)", re.I)
            ).last.click()
            await page.wait_for_timeout(self.action_delay_ms(1500))
            log.info("Antwort gepostet bei %s.", post.id)
            return True
        except Exception as exc:
            log.error("Reply fehlgeschlagen (%s): %s", post.id, exc)
            return False

    async def comment_by_url(self, url: str, text: str) -> bool:
        """Kommentiert einen Beitrag direkt über seine Permalink-URL (stabil)."""
        page = self.page
        try:
            await page.goto(url, wait_until="domcontentloaded")
            await page.wait_for_timeout(self.action_delay_ms(3000))
            unavailable = page.get_by_text(
                re.compile(
                    r"post not found|this post was deleted or removed|"
                    r"beitrag nicht gefunden|beitrag wurde gelöscht oder entfernt",
                    re.I,
                )
            )
            if await unavailable.count():
                log.error(
                    "Kommentar via URL nicht möglich; Zielbeitrag ist nicht verfügbar (%s).",
                    url,
                )
                return False
            # Kommentarbox öffnen
            cbtn = page.get_by_role("button", name=re.compile(r"^comment$|kommentieren", re.I))
            if await cbtn.count():
                await cbtn.first.click()
                await page.wait_for_timeout(self.action_delay_ms(1500))
            # Semantischen Kommentar-Editor wählen (LinkedIn nutzt derzeit Tiptap/ProseMirror).
            editor = page.get_by_role(
                "textbox", name=re.compile(r"comment|kommentar", re.I)
            ).last
            await editor.wait_for(state="visible", timeout=8000)
            await self._set_editor_text(editor, text)
            await page.wait_for_timeout(self.action_delay_ms(700))
            # Absenden: der Submit-Button ist der LETZTE "Comment"-Button (nicht die Aktion).
            submit = page.get_by_role(
                "button", name=re.compile(r"^(comment|kommentieren|post|senden)$", re.I)
            ).last
            try:
                await self._wait_before_write()
                await submit.click()
            except Exception:
                await page.keyboard.press("ControlOrMeta+Enter")
            await page.wait_for_timeout(self.action_delay_ms(2500))
            # Verifizieren: erscheint eine markante Textstelle im Seiteninhalt?
            probe = " ".join(text.split())[:40]
            body = await page.evaluate("() => document.body.innerText")
            posted = probe in body
            log.info("Kommentar via URL %s: %s", "verifiziert" if posted else "gesendet(?)", url)
            return posted
        except Exception as exc:
            log.error("Kommentar via URL fehlgeschlagen (%s): %s", url, exc)
            return False

    async def _locate_post(self, post: FeedPost):
        """Findet den Container zu einem Post (klassisch via data-urn oder neue Variante)."""
        page = self.page

        def _candidates():
            # Klassisches Markup (Wall) und neue Feed-Variante (componentkey).
            classic = page.locator(f'div.feed-shared-update-v2[data-urn="{post.id}"]').first
            new = page.locator(f'div[role="listitem"][componentkey="{post.id}"]').first
            return classic, new

        classic, new = _candidates()
        if await classic.count():
            return classic
        if await new.count():
            return new

        # Nachladen und erneut suchen (Hinweis: componentkey ist nur pro Render stabil).
        await page.goto(FEED_URL, wait_until="domcontentloaded")
        await page.wait_for_timeout(self.action_delay_ms(2000))
        classic, new = _candidates()
        return classic if await classic.count() else new

    async def add_comment(self, post: FeedPost, text: str) -> bool:
        """Kommentiert einen zuvor gesammelten Feed-Beitrag."""
        page = self.page
        try:
            node = await self._locate_post(post)
            await node.scroll_into_view_if_needed()
            await node.get_by_role(
                "button", name=re.compile(r"(comment|kommentieren|kommentar)", re.I)
            ).first.click()
            box = node.get_by_role("textbox").first
            await box.wait_for(state="visible", timeout=8000)
            await self._set_editor_text(box, text)
            await page.wait_for_timeout(self.action_delay_ms(600))
            await node.get_by_role(
                "button", name=re.compile(r"(post|kommentieren|senden|comment)", re.I)
            ).last.wait_for(state="visible", timeout=8000)
            await self._wait_before_write()
            await node.get_by_role(
                "button", name=re.compile(r"(post|kommentieren|senden|comment)", re.I)
            ).last.click()
            await page.wait_for_timeout(self.action_delay_ms(1500))
            log.info("Kommentar gepostet bei %s.", post.id)
            return True
        except Exception as exc:
            log.error("Kommentar fehlgeschlagen (%s): %s", post.id, exc)
            return False
