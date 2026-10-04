"""Deterministische LinkedIn-Werkzeuge für die Codex-CLI-Agenten.

Kein LLM hier: Codex CLI ist das Gehirn und ruft diese Befehle als Tools auf.
Jeder Befehl gibt JSON auf stdout aus (Logs gehen auf stderr), damit die Agenten
die Ergebnisse zuverlässig weiterverarbeiten können.

Beispiele:
    PYTHONPATH=src python -m linkedin_agents.tools wall --keywords ai,devops --limit 10
    PYTHONPATH=src python -m linkedin_agents.tools feed --keywords ci/cd --limit 15
    PYTHONPATH=src python -m linkedin_agents.tools post --text "..." --image .runs/images/x.png
    PYTHONPATH=src python -m linkedin_agents.tools comment --post-id urn:... --text "..."
    PYTHONPATH=src python -m linkedin_agents.tools reply   --post-id urn:... --text "..."
    PYTHONPATH=src python -m linkedin_agents.tools reshare --post-id urn:... --thoughts "..."
    PYTHONPATH=src python -m linkedin_agents.tools image   --prompt "..." --name post_1
    PYTHONPATH=src python -m linkedin_agents.tools campaign --campaign Kampagnen/x.yaml
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys

from .browser.linkedin import LinkedInClient
from .config import load_settings
from .imaging.generator import ImageGenerator
from .models.campaign import load_campaign
from .models.content import FeedPost
from .utils.logging import get_logger, setup_logging


def _emit(payload: dict) -> None:
    """Gibt ein Ergebnis als JSON auf stdout aus."""
    json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


def _split_csv(value: str | None) -> list[str]:
    return [v.strip() for v in (value or "").split(",") if v.strip()]


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="linkedin-tools", description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Schreibaktionen nur simulieren")
    sub = parser.add_subparsers(dest="command", required=True)

    for name in ("wall", "feed"):
        p = sub.add_parser(name, help=f"Beiträge von {'der eigenen Wall' if name == 'wall' else 'dem Feed'} sammeln")
        p.add_argument("--keywords", default="", help="Kommagetrennte Filter-Keywords")
        p.add_argument("--limit", type=int, default=10)
        p.add_argument("--with-urls", action="store_true", help="Permalink-URL je Beitrag miterfassen (langsamer)")

    p_post = sub.add_parser("post", help="Eigenen Beitrag erstellen")
    p_post.add_argument("--text", required=True)
    p_post.add_argument("--image", default=None, help="Pfad zu einem Bild (optional)")

    p_comment = sub.add_parser("comment", help="Beitrag kommentieren")
    p_comment.add_argument("--post-id", required=True)
    p_comment.add_argument("--text", required=True)

    p_comment_url = sub.add_parser("comment-url", help="Beitrag über seine Permalink-URL kommentieren (stabil)")
    p_comment_url.add_argument("--url", required=True)
    p_comment_url.add_argument("--text", required=True)

    p_reply = sub.add_parser("reply", help="Auf den ersten Kommentar antworten")
    p_reply.add_argument("--post-id", required=True)
    p_reply.add_argument("--text", required=True)

    p_reshare = sub.add_parser("reshare", help="Beitrag teilen")
    p_reshare.add_argument("--post-id", required=True)
    p_reshare.add_argument("--thoughts", default=None)

    p_image = sub.add_parser("image", help="Bild aus einem Prompt generieren")
    p_image.add_argument("--prompt", required=True)
    p_image.add_argument("--name", required=True)

    p_campaign = sub.add_parser("campaign", help="Kampagne validieren und anzeigen")
    p_campaign.add_argument("--campaign", required=True)

    sub.add_parser("check", help="Prüfen, ob die LinkedIn-Session eingeloggt ist")

    return parser.parse_args(argv)


async def _run(args: argparse.Namespace) -> int:
    settings = load_settings()
    setup_logging(settings.log_level)
    log = get_logger("tools")

    # Befehle ohne Browser
    if args.command == "campaign":
        campaign = load_campaign(args.campaign)
        _emit({"ok": True, "campaign": campaign.model_dump(mode="json")})
        return 0

    if args.command == "image":
        gen = ImageGenerator(settings.image_provider, settings.openai_api_key, settings.image_model)
        path = await gen.render(args.prompt, args.name)
        _emit({"ok": True, "image_path": path, "provider": settings.image_provider})
        return 0

    # Ab hier: Browser nötig
    async with LinkedInClient(settings.cdp_endpoint) as client:
        if not await client.ensure_logged_in():
            _emit({"ok": False, "error": "not_logged_in"})
            return 2

        if args.command == "check":
            _emit({"ok": True, "logged_in": True})
            return 0

        if args.command in ("wall", "feed"):
            kw = _split_csv(args.keywords)
            collect = client.collect_wall if args.command == "wall" else client.collect_feed
            posts = await collect(kw, limit=args.limit, with_urls=args.with_urls)
            _emit({"ok": True, "count": len(posts), "posts": [p.model_dump() for p in posts]})
            return 0

        if args.dry_run:
            log.info("[DRY-RUN] %s würde ausgeführt: %s", args.command, vars(args))
            _emit({"ok": True, "dry_run": True, "command": args.command})
            return 0

        target = FeedPost(id=getattr(args, "post_id", "")) if hasattr(args, "post_id") else None

        if args.command == "post":
            ok = await client.create_post(args.text, image_path=args.image)
        elif args.command == "comment":
            ok = await client.add_comment(target, args.text)
        elif args.command == "comment-url":
            ok = await client.comment_by_url(args.url, args.text)
        elif args.command == "reply":
            ok = await client.reply_to_comment(target, args.text)
        elif args.command == "reshare":
            ok = await client.reshare(target, args.thoughts)
        else:
            _emit({"ok": False, "error": f"unknown_command:{args.command}"})
            return 1

        _emit({"ok": bool(ok), "command": args.command})
        return 0 if ok else 1


def main() -> None:
    args = _parse_args(sys.argv[1:])
    raise SystemExit(asyncio.run(_run(args)))


if __name__ == "__main__":
    main()
