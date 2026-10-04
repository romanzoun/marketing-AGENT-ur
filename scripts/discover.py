"""Read-only Playwright-Discovery für LinkedIn — testet alle Team-Aktionen.

Dockt an die laufende Edge/Chrome-Session (CDP) an und prüft, ob alle Aktionen
funktionieren: Feed sammeln, Wall sammeln, Post-Composer (inkl. Post-/Medien-Button),
Kommentar-Button und Repost-Button auf einem echten Feed-Post.

WICHTIG: Es wird NICHTS abgesendet. Dialoge/Menüs werden nur geöffnet und mit
Escape geschlossen. Aufruf:

    PYTHONPATH=src python scripts/discover.py
"""
from __future__ import annotations

import asyncio
import json
import re

from linkedin_agents.browser.linkedin import FEED_URL, LinkedInClient
from linkedin_agents.config import load_settings
from linkedin_agents.imaging.generator import ImageGenerator

# Container-Selektor der neuen Feed-Variante (siehe Discovery-Befunde).
NEW_FEED = "div[role='listitem'][componentkey^='update-card-focus']"
RESULTS: list[dict] = []


def record(action: str, ok: bool, detail: str = "") -> None:
    RESULTS.append({"action": action, "ok": ok, "detail": detail})
    print(f"  {'✓' if ok else '✗'} {action}: {detail}", flush=True)


async def close_overlay(page) -> None:
    await page.keyboard.press("Escape")
    await page.wait_for_timeout(500)
    discard = page.get_by_role("button", name=re.compile(r"(discard|verwerfen)", re.I))
    if await discard.count():
        try:
            await discard.first.click()
            await page.wait_for_timeout(400)
        except Exception:
            pass


async def main() -> None:
    settings = load_settings()
    print(f"CDP: {settings.cdp_endpoint}\n== LinkedIn Discovery (read-only) ==")

    async with LinkedInClient(settings.cdp_endpoint) as client:
        page = client.page
        print(f"Aktiver Tab: {page.url}")

        logged_in = await client.ensure_logged_in()
        record("Login-Status", logged_in, "eingeloggt" if logged_in else "NICHT eingeloggt")
        if not logged_in:
            return _emit_summary()

        # 1) Feed sammeln (variantensicher über den Client)
        feed = await client.collect_feed([], limit=5)
        record("Feed sammeln", len(feed) > 0,
               f"{len(feed)} Beiträge; erster Autor={feed[0].author!r}" if feed else "0")

        # 2) Kommentar-/Repost-Interaktion auf erstem echten Feed-Post (neue Variante)
        await page.goto(FEED_URL, wait_until="domcontentloaded")
        await page.wait_for_timeout(3000)
        for _ in range(2):
            await page.mouse.wheel(0, 2200)
            await page.wait_for_timeout(1000)
        node = page.locator(NEW_FEED).first
        if await node.count():
            await node.scroll_into_view_if_needed()
            cbtn = node.get_by_role("button", name=re.compile(r"comment|kommentier", re.I))
            record("Feed: Kommentar-Button", await cbtn.count() > 0, f"{await cbtn.count()} Treffer")
            # Kommentar-Box tatsächlich öffnen (nicht senden)
            if await cbtn.count():
                try:
                    await cbtn.first.click()
                    await page.wait_for_timeout(1500)
                    box = node.get_by_role("textbox")
                    record("Feed: Kommentar-Box öffnet", await box.count() > 0, f"{await box.count()} Textbox")
                    await close_overlay(page)
                except Exception as exc:
                    record("Feed: Kommentar-Box öffnet", False, f"Fehler: {exc}")

            rbtn = node.get_by_role("button", name=re.compile(r"repost|teilen", re.I))
            record("Feed: Repost-Button", await rbtn.count() > 0, f"{await rbtn.count()} Treffer")
        else:
            record("Feed: Kommentar-Button", False, "kein Feed-Container gefunden")

        # 2b) Repost-Menü auf frischem Feed (getrennt, um Layout-Interferenz zu vermeiden)
        try:
            await page.goto(FEED_URL, wait_until="domcontentloaded")
            await page.wait_for_timeout(3000)
            await page.mouse.wheel(0, 1500)
            await page.wait_for_timeout(1200)
            rnode = page.locator(NEW_FEED).first
            rbtn2 = rnode.get_by_role("button", name=re.compile(r"repost|teilen", re.I))
            if await rbtn2.count():
                await rbtn2.first.scroll_into_view_if_needed()
                await rbtn2.first.click()
                await page.wait_for_timeout(1800)
                items = page.get_by_role(
                    "button", name=re.compile(r"repost (with thoughts|instantly)|mit meinung|sofort", re.I)
                )
                labels = []
                for i in range(min(await items.count(), 6)):
                    labels.append((await items.nth(i).inner_text()).strip()[:30])
                record("Feed: Repost-Menü öffnet", await items.count() > 0, f"Items: {labels}")
                await close_overlay(page)
            else:
                record("Feed: Repost-Menü öffnet", False, "kein Repost-Button")
        except Exception as exc:
            record("Feed: Repost-Menü öffnet", False, f"Fehler: {exc}")

        # 3) Post-Composer öffnen (Dialog-Scope, verifizierte Namen)
        try:
            await page.goto(FEED_URL, wait_until="domcontentloaded")
            await page.wait_for_timeout(2000)
            start = page.get_by_role("button", name=re.compile(r"(start a post|beitrag)", re.I))
            record("Post: 'Beitrag starten'-Button", await start.count() > 0, f"{await start.count()} Treffer")
            if await start.count():
                await start.first.click()
                dialog = page.get_by_role("dialog").first
                await dialog.wait_for(state="visible", timeout=8000)
                await page.wait_for_timeout(1500)  # Buttons rendern kurz verzögert
                editor = dialog.get_by_role("textbox")
                record("Post: Editor öffnet", await editor.count() > 0, f"{await editor.count()} Textbox")
                postbtn = dialog.get_by_role("button", name=re.compile(r"^(post|posten)$", re.I))
                record("Post: 'Post'-Button", await postbtn.count() > 0, f"{await postbtn.count()} Treffer")
                media = dialog.get_by_role("button", name=re.compile(r"(add media|medien|bild|foto)", re.I))
                record("Post: 'Add media'-Button", await media.count() > 0, f"{await media.count()} Treffer")
                await close_overlay(page)
        except Exception as exc:
            record("Post: Editor öffnet", False, f"Fehler: {exc}")

        # 4) Wall sammeln
        wall = await client.collect_wall([], limit=5)
        record("Wall sammeln", len(wall) > 0,
               f"{len(wall)} Beiträge; erste id={wall[0].id!r}" if wall else "0")

        await page.goto(FEED_URL, wait_until="domcontentloaded")

    # 5) Bild-Tool (Provider none schreibt nur einen Brief, kein Upload)
    try:
        gen = ImageGenerator(settings.image_provider, settings.openai_api_key, settings.image_model)
        path = await gen.render("discovery test prompt", "discovery_check")
        record("Bild-Tool", True, f"provider={settings.image_provider}; ergebnis={path}")
    except Exception as exc:
        record("Bild-Tool", False, f"Fehler: {exc}")

    _emit_summary()


def _emit_summary() -> None:
    ok = sum(1 for r in RESULTS if r["ok"])
    print(f"\n== Zusammenfassung: {ok}/{len(RESULTS)} Checks ok ==")
    print(json.dumps(RESULTS, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
