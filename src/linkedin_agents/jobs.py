"""Job-Runner für den Kampagnen-Betrieb (cron-tauglich).

Ablauf: Vorschlag → Freigabe (Checkbox in approvals.md) → Einplanung (schedule.md)
→ automatische Ausführung zum geplanten Zeitpunkt → log.md.

Jobs:
    add             Entwurf (Post/Kommentar/Reshare) in die Freigabe-Liste legen
    find-comments   Passende Feed-Beiträge suchen und als Kommentar-Kandidaten ablegen
    find-reshares   Passende Feed-Beiträge als Reshare-Kandidaten ablegen
    image           Bild zu einem Eintrag setzen (generiert oder Web-Bild mit Quelle)
    schedule        Freigegebene Einträge einplanen (Datum/Uhrzeit vergeben)
    run-due         Fällige Einträge veröffentlichen  ← der eigentliche Cron-Job
    status          Übersicht
    analytics       Kampagnen-URLs und Kennzahlen aktualisieren

Beispiele:
    ./bin/li-jobs status   --campaign "Kampagnen/document validator/kampagne.yaml"
    ./bin/li-jobs add      --campaign ... --kind post --text "..."
    ./bin/li-jobs find-comments --campaign ... --limit 5
    ./bin/li-jobs schedule --campaign ... --start-date 2026-09-11 --slots 09:00,13:00
    ./bin/li-jobs run-due  --campaign ...
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

from . import analytics
from . import queue as q
from .browser.linkedin import LinkedInClient
from .config import load_settings
from .imaging.workflow import (
    AUTO_IMAGE_MIN_SCORE,
    quota_selects_next,
    score_allows_auto_image,
    set_generated_image,
    set_web_image,
)
from .models.campaign import load_campaign
from .style_learning import prepare_items
from .utils.logging import get_logger, setup_logging

APPROVALS_TITLE = "Freigaben — warten auf deine Bestätigung"
APPROVALS_HINT = (
    "Kreuze `- [x] freigeben` an, was raus darf. Danach `li-jobs schedule` ausführen. "
    "Texte dürfen hier direkt bearbeitet werden."
)
SCHEDULE_TITLE = "Einplanung — freigegeben, wartet auf den Zeitpunkt"
SCHEDULE_HINT = "Wird von `li-jobs run-due` automatisch ausgeführt, sobald `publish_at` erreicht ist."
LOG_TITLE = "Log — ausgeführt"
LOG_HINT = "Bereits ausgeführte Einträge (Historie)."
CONNECTION_NOTE_MAX_CHARS = 300
CONNECTIONS_PER_RUN = 5


def _paths(campaign_path: str) -> tuple[Path, Path, Path]:
    base = Path(campaign_path).parent / "queue"
    return base / "approvals.md", base / "schedule.md", base / "log.md"


def _emit(payload: dict) -> None:
    json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


async def job_add(args) -> int:
    approvals, schedule, log_p = _paths(args.campaign)
    campaign = load_campaign(args.campaign)
    if args.awareness and args.kind != "reshare":
        _emit({"ok": False, "error": "awareness_is_only_valid_for_reshares"})
        return 2
    existing = q.parse(approvals)
    item = q.QueueItem(
        id=q.next_id(args.kind, existing),
        kind=args.kind,
        campaign=campaign.name,
        campaign_version=campaign.version,
        source_job_id=os.environ.get("LI_JOB_ID"),
        text=args.text or "",
        url=args.url,
        note=args.note or "",
        publish_at=args.publish_at,
        reshare_with_comment=not args.awareness,
    )
    existing.append(item)
    prepared = prepare_items(
        Path(__file__).resolve().parents[2],
        campaign,
        existing,
        {item.id},
        q.parse(schedule),
    )
    image_selected_by_quota = False
    image_selected = False
    image_ok = None
    if item.kind == "post" and campaign.images.enabled:
        existing_posts = [
            queued
            for path in (approvals, schedule, log_p)
            for queued in q.parse(path)
            if queued.kind == "post"
        ]
        image_selected_by_quota = quota_selects_next(
            existing_posts, campaign.images.ratio
        )
        image_selected = image_selected_by_quota and score_allows_auto_image(item)
        item.image_auto_selected = image_selected
        if image_selected:
            image_ok = await set_generated_image(item, campaign, load_settings())
    q.write(approvals, existing, APPROVALS_TITLE, APPROVALS_HINT)
    _emit({
        "ok": True,
        "added": item.id,
        "file": str(approvals),
        "evaluation": prepared[0] if prepared else None,
        "image": {
            "selected_by_quota": image_selected_by_quota,
            "selected_by_score": score_allows_auto_image(item),
            "minimum_score_exclusive": AUTO_IMAGE_MIN_SCORE,
            "selected": image_selected,
            "ok": image_ok,
            "path": item.image_path,
            "error": item.image_error or None,
        },
    })
    return 0


async def job_find_comments(args) -> int:
    """Sucht kampagnenrelevante Beiträge und legt Kommentar-Kandidaten zur Freigabe ab."""
    return await _find_engagement_candidates(args, "comment")


async def job_find_reshares(args) -> int:
    """Sucht kampagnenrelevante Fremdbeiträge für Reshares mit/ohne Begleittext."""
    return await _find_engagement_candidates(args, "reshare")


async def job_find_connections(args) -> int:
    """Sucht noch nicht vernetzte Personen und legt sie zur Freigabe ab."""
    settings = load_settings()
    campaign = load_campaign(args.campaign)
    approvals, schedule, log_p = _paths(args.campaign)
    existing_urls = {
        item.url
        for path in (approvals, schedule, log_p)
        for item in q.parse(path)
        if item.kind == "connection" and item.url
    }
    async with LinkedInClient(settings.cdp_endpoint) as client:
        if not await client.ensure_logged_in():
            _emit({"ok": False, "error": "not_logged_in"})
            return 2
        people = await client.collect_people(
            args.query, limit=min(args.limit, CONNECTIONS_PER_RUN)
        )

    existing = q.parse(approvals)
    new: list[q.QueueItem] = []
    for person in people:
        if person.url in existing_urls:
            continue
        new.append(
            q.QueueItem(
                id=q.next_id("connection", existing + new),
                kind="connection",
                campaign=campaign.name,
                campaign_version=campaign.version,
                source_job_id=os.environ.get("LI_JOB_ID"),
                url=person.url,
                author=person.name,
                note=person.headline,
                text="",
            )
        )
    q.append(approvals, new, APPROVALS_TITLE, APPROVALS_HINT)
    _emit({"ok": True, "kandidaten": len(new), "query": args.query, "file": str(approvals)})
    return 0


async def _find_engagement_candidates(args, kind: q.ItemKind) -> int:
    settings = load_settings()
    campaign = load_campaign(args.campaign)
    approvals, schedule, log_p = _paths(args.campaign)

    already = {
        item.url
        for path in (approvals, schedule, log_p)
        for item in q.parse(path)
        if item.kind == kind and item.url
    }

    async with LinkedInClient(settings.cdp_endpoint) as client:
        if not await client.ensure_logged_in():
            _emit({"ok": False, "error": "not_logged_in"})
            return 2
        # Für die Freigabe bewusst nicht vorab nach Keywords verwerfen: Der
        # semantische Passungsscore entscheidet später über Reihenfolge und Automatik.
        posts = await client.collect_feed([], limit=args.limit, with_urls=True)

    existing = q.parse(approvals)
    new: list[q.QueueItem] = []
    for p in posts:
        if not p.url or p.url in already:
            continue
        lines = [l.strip() for l in p.text.split("\n") if l.strip() and l.strip().lower() != "feed post"]
        item = q.QueueItem(
            id=q.next_id(kind, existing + new),
            kind=kind,
            campaign=campaign.name,
            campaign_version=campaign.version,
            source_job_id=os.environ.get("LI_JOB_ID"),
            url=p.url,
            author=(p.author or (lines[0] if lines else ""))[:120],
            note=p.text.strip(),
            text="",  # wird beim Text-Job vom Copywriter gefüllt
            reshare_with_comment=kind == "reshare",
        )
        new.append(item)

    q.append(approvals, new, APPROVALS_TITLE, APPROVALS_HINT)
    _emit({"ok": True, "kandidaten": len(new), "file": str(approvals)})
    return 0


async def job_image(args) -> int:
    """Setzt ein Bild für einen Eintrag: Web-Suche (mit Quelle) oder Generator."""
    settings = load_settings()
    approvals, schedule, _ = _paths(args.campaign)

    for path, title, hint in ((approvals, APPROVALS_TITLE, APPROVALS_HINT), (schedule, SCHEDULE_TITLE, SCHEDULE_HINT)):
        items = q.parse(path)
        for item in items:
            if item.id != args.id:
                continue
            if item.kind != "post":
                _emit({"ok": False, "error": "images_are_only_supported_for_posts"})
                return 2
            ok = (
                await set_web_image(item, args.query)
                if args.source == "web"
                else await set_generated_image(item, load_campaign(args.campaign), settings, args.query)
            )
            q.write(path, items, title, hint)
            _emit({
                "ok": ok,
                "id": item.id,
                "image_path": item.image_path,
                "image_source": item.image_source,
                "error": item.image_error or None,
            })
            return 0 if ok else 1

    _emit({"ok": False, "error": f"id_not_found:{args.id}"})
    return 1


async def job_schedule(args) -> int:
    """Verschiebt freigegebene Einträge in die Einplanung und vergibt Zeitpunkte."""
    approvals, schedule, _ = _paths(args.campaign)
    campaign = load_campaign(args.campaign)

    pending = q.parse(approvals)
    approved = [
        item for item in pending
        if item.approved and (
            item.kind == "post"
            or item.text.strip()
            or (item.kind == "reshare" and not item.reshare_with_comment)
        )
    ]
    if not approved:
        _emit({"ok": True, "eingeplant": 0, "hinweis": "nichts freigegeben (oder Kommentartext fehlt)"})
        return 0

    slots = [s.strip() for s in args.slots.split(",") if s.strip()]
    start = datetime.fromisoformat(args.start_date) if args.start_date else datetime.now() + timedelta(minutes=5)
    lo, hi = campaign.schedule.active_hours

    scheduled = q.parse(schedule)
    used = {i.publish_at for i in scheduled if i.publish_at}
    day_offset, slot_idx = 0, 0
    for item in approved:
        if item.publish_at:  # bereits fix gesetzt
            scheduled.append(item)
            continue
        while True:
            day = (start + timedelta(days=day_offset)).date()
            hh, mm = (slots[slot_idx].split(":") + ["0"])[:2] if slots else ("09", "00")
            when = datetime.combine(day, datetime.min.time()).replace(hour=int(hh), minute=int(mm))
            slot_idx += 1
            if slot_idx >= max(len(slots), 1):
                slot_idx, day_offset = 0, day_offset + 1
            if when.isoformat(timespec="minutes") in used or when < datetime.now():
                continue
            if not (lo <= when.hour < hi):
                continue
            break
        item.publish_at = when.isoformat(timespec="minutes")
        used.add(item.publish_at)
        scheduled.append(item)

    q.write(schedule, scheduled, SCHEDULE_TITLE, SCHEDULE_HINT)
    rest = [i for i in pending if i not in approved]
    q.write(approvals, rest, APPROVALS_TITLE, APPROVALS_HINT)
    _emit({
        "ok": True,
        "eingeplant": len(approved),
        "termine": [{"id": i.id, "publish_at": i.publish_at} for i in approved],
    })
    return 0


async def job_run_due(args) -> int:
    """Führt alle fälligen, zuvor freigegebenen Aktionen aus."""
    settings = load_settings()
    _, schedule, log_p = _paths(args.campaign)
    log = get_logger("jobs.run-due")

    items = q.parse(schedule)
    due = [i for i in items if i.due()]
    if not due:
        _emit({"ok": True, "faellig": 0})
        return 0

    done: list[q.QueueItem] = []
    results = []
    today = datetime.now().date()
    connection_attempts = sum(
        item.kind == "connection"
        and bool(item.published_at)
        and datetime.fromisoformat(item.published_at).date() == today
        for item in q.parse(log_p)
    )
    tracking_enabled = Path(args.campaign).is_file()
    async with LinkedInClient(settings.cdp_endpoint) as client:
        if not await client.ensure_logged_in():
            _emit({"ok": False, "error": "not_logged_in"})
            return 2
        for item in due:
            text = item.text
            if item.image_source and (
                item.image_origin == "web"
                or (
                    item.image_origin is None
                    and item.image_source != "Bild: KI-generiert"
                )
            ):
                text = f"{text}\n\n{item.image_source}"  # Quelle immer mit angeben
            if args.dry_run:
                log.info("[DRY-RUN] %s (%s) -> %s", item.id, item.kind, item.url or "eigener Post")
                ok = True
            elif item.kind == "post":
                ok = await client.create_post(text, image_path=item.image_path)
            elif item.kind == "comment" and item.url:
                ok = await client.comment_by_url(item.url, text)
            elif item.kind == "reshare" and item.url:
                thoughts = text if item.reshare_with_comment else None
                ok = await client.reshare_by_url(item.url, thoughts)
            elif item.kind == "connection" and item.url:
                if connection_attempts >= CONNECTIONS_PER_RUN:
                    continue
                connection_attempts += 1
                ok = await client.send_connection_by_url(item.url, text)
            else:
                ok = False
            results.append({"id": item.id, "kind": item.kind, "ok": bool(ok)})
            if ok and not args.dry_run:
                item.published_at = datetime.now().isoformat(timespec="seconds")
                if tracking_enabled and item.kind != "connection":
                    try:
                        activity_text = (
                            item.note
                            if item.kind == "reshare" and not item.reshare_with_comment
                            else item.text
                        )
                        item.published_url = await client.find_recent_activity_url(
                            item.kind, activity_text
                        )
                    except Exception as exc:
                        log.warning("Permalink für %s noch nicht gefunden: %s", item.id, exc)
                    analytics.register(args.campaign, item, item.published_url)
                done.append(item)

    if done:
        finished = {i.id for i in done}
        q.append(log_p, done, LOG_TITLE, LOG_HINT)
        q.write(schedule, [i for i in items if i.id not in finished], SCHEDULE_TITLE, SCHEDULE_HINT)

    failed = [result for result in results if not result["ok"]]
    payload = {"ok": not failed, "faellig": len(due), "ergebnisse": results}
    if failed:
        payload["error"] = (
            f"{len(failed)} von {len(results)} ausgeführten LinkedIn-Aktionen fehlgeschlagen"
        )
    _emit(payload)
    return 1 if failed else 0


async def job_analytics(args) -> int:
    """Aktualisiert Messreihen, ohne fremde Post-Reichweite uns zuzuschreiben."""
    settings = load_settings()
    log = get_logger("jobs.analytics")
    records = analytics.sync_log(args.campaign)
    if not records:
        _emit({"ok": True, "gemessen": 0, "hinweis": "Noch nichts veröffentlicht"})
        return 0

    results = []
    async with LinkedInClient(settings.cdp_endpoint) as client:
        if not await client.ensure_logged_in():
            _emit({"ok": False, "error": "not_logged_in"})
            return 2
        for record in records:
            measurement_url = record.published_url
            if record.kind == "comment":
                # Der eigene Kommentar wird anhand seines Textes im Originalpost gesucht.
                measurement_url = measurement_url or record.source_url
            elif not measurement_url:
                try:
                    measurement_url = await client.find_recent_activity_url(
                        record.kind, record.text
                    )
                except Exception as exc:
                    log.warning("Permalink-Suche für %s fehlgeschlagen: %s", record.item_id, exc)
                if measurement_url:
                    analytics.set_published_url(args.campaign, record.item_id, measurement_url)

            if not measurement_url:
                error = "Eigener Permalink noch nicht gefunden"
                analytics.add_snapshot(args.campaign, record.item_id, {}, error=error)
                results.append({"id": record.item_id, "ok": False, "error": error})
                continue
            try:
                values = await client.get_engagement_metrics(
                    measurement_url, record.kind, record.text
                )
            except Exception as exc:
                values = None
                log.warning("Messung für %s fehlgeschlagen: %s", record.item_id, exc)
            if values is None:
                error = (
                    "Eigener Kommentar auf der LinkedIn-Seite nicht gefunden"
                    if record.kind == "comment"
                    else "Kennzahlen am Permalink nicht lesbar"
                )
                analytics.add_snapshot(args.campaign, record.item_id, {}, error=error)
                results.append({"id": record.item_id, "ok": False, "error": error})
                continue
            analytics.add_snapshot(args.campaign, record.item_id, values)
            results.append({"id": record.item_id, "ok": True, "metrics": values})

    summary = analytics.dashboard(args.campaign)["summary"]
    _emit({
        "ok": True,
        "gemessen": sum(result["ok"] for result in results),
        "fehlgeschlagen": sum(not result["ok"] for result in results),
        "summary": summary,
        "ergebnisse": results,
    })
    return 0


async def job_status(args) -> int:
    approvals, schedule, log_p = _paths(args.campaign)
    a, s, l = q.parse(approvals), q.parse(schedule), q.parse(log_p)
    _emit({
        "ok": True,
        "freigabe_offen": len(a),
        "davon_angekreuzt": sum(1 for i in a if i.approved),
        "eingeplant": len(s),
        "faellig_jetzt": sum(1 for i in s if i.due()),
        "veroeffentlicht": len(l),
        "naechste": [{"id": i.id, "kind": i.kind, "publish_at": i.publish_at} for i in sorted(
            (i for i in s if i.publish_at), key=lambda x: x.publish_at or "")][:5],
        "dateien": {"approvals": str(approvals), "schedule": str(schedule), "log": str(log_p)},
    })
    return 0


JOBS = {
    "add": job_add,
    "find-comments": job_find_comments,
    "find-reshares": job_find_reshares,
    "find-connections": job_find_connections,
    "image": job_image,
    "schedule": job_schedule,
    "run-due": job_run_due,
    "status": job_status,
    "analytics": job_analytics,
}


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="li-jobs", description=__doc__)
    parser.add_argument("--campaign", required=True, help="Pfad zur Kampagnen-YAML")
    sub = parser.add_subparsers(dest="job", required=True)

    p_add = sub.add_parser("add", help="Entwurf zur Freigabe hinzufügen")
    p_add.add_argument(
        "--kind", choices=["post", "comment", "reshare", "connection"], required=True
    )
    p_add.add_argument("--text", default="")
    p_add.add_argument("--url", default=None, help="Ziel-Permalink (bei Kommentaren)")
    p_add.add_argument("--note", default="")
    p_add.add_argument("--publish-at", default=None, help="ISO-Zeit, sonst automatisch")
    p_add.add_argument(
        "--awareness", action="store_true",
        help="Reshare ohne eigenen Begleittext (nur bei --kind reshare)",
    )

    p_find = sub.add_parser("find-comments", help="Kommentar-Kandidaten suchen")
    p_find.add_argument("--limit", type=int, default=5)

    p_reshare = sub.add_parser("find-reshares", help="Reshare-Kandidaten suchen")
    p_reshare.add_argument("--limit", type=int, default=5)

    p_connections = sub.add_parser(
        "find-connections", help="Noch nicht vernetzte Personen suchen"
    )
    p_connections.add_argument("--query", required=True, help="Rolle oder Suchbegriff")
    p_connections.add_argument("--limit", type=int, default=5)

    p_img = sub.add_parser("image", help="Bild setzen (web|gen)")
    p_img.add_argument("--id", required=True)
    p_img.add_argument("--query", required=True, help="Suchbegriff bzw. Bild-Prompt")
    p_img.add_argument("--source", choices=["web", "gen"], default="web")

    p_sch = sub.add_parser("schedule", help="Freigegebenes einplanen")
    p_sch.add_argument("--start-date", default=None, help="YYYY-MM-DD (Standard: heute)")
    p_sch.add_argument("--slots", default="09:00,13:00", help="Uhrzeiten pro Tag")

    p_run = sub.add_parser("run-due", help="Fällige Einträge veröffentlichen")
    p_run.add_argument("--dry-run", action="store_true")

    sub.add_parser("status", help="Übersicht")
    sub.add_parser("analytics", help="Kampagnen-Kennzahlen aktualisieren")
    return parser.parse_args(argv)


def main() -> None:
    args = _parse_args(sys.argv[1:])
    setup_logging(load_settings().log_level)
    raise SystemExit(asyncio.run(JOBS[args.job](args)))


if __name__ == "__main__":
    main()
