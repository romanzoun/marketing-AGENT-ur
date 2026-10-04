"""Bildsuche im Web mit Quellenangabe (Openverse, CC-lizenziert).

Liefert ein herunterladbares Bild plus korrekte Attribution, damit wir beim Posten
die Quelle nennen können. Kein API-Key nötig (anonym, rate-limited).
"""
from __future__ import annotations

from pathlib import Path

import httpx

from ..utils.logging import get_logger

log = get_logger("imaging.websearch")

API = "https://api.openverse.org/v1/images/"
IMAGE_DIR = Path(".runs/images")


async def find_image(query: str, name: str) -> tuple[str | None, str | None]:
    """Sucht ein frei nutzbares Bild und lädt es herunter.

    Rückgabe: (lokaler_pfad, quellenangabe) – beide None bei Misserfolg.
    """
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    try:
        async with httpx.AsyncClient(timeout=45, follow_redirects=True) as client:
            resp = await client.get(
                API,
                params={
                    "q": query,
                    "license_type": "commercial,modification",
                    "page_size": 5,
                    "mature": "false",
                },
                headers={"User-Agent": "linkedin-agents/0.1 (campaign tooling)"},
            )
            resp.raise_for_status()
            results = resp.json().get("results") or []
            if not results:
                log.info("Keine Bildtreffer für %r", query)
                return None, None

            hit = results[0]
            img_url = hit.get("url")
            if not img_url:
                return None, None

            img = await client.get(img_url)
            img.raise_for_status()
            suffix = ".jpg" if "jpeg" in img.headers.get("content-type", "") else ".png"
            out = IMAGE_DIR / f"{name}{suffix}"
            out.write_bytes(img.content)

            creator = hit.get("creator") or "Unbekannt"
            license_name = (hit.get("license") or "").upper()
            license_ver = hit.get("license_version") or ""
            landing = hit.get("foreign_landing_url") or hit.get("url")
            title = hit.get("title") or "Bild"
            source = f'Bild: "{title}" von {creator}, {license_name} {license_ver} — {landing}'.strip()

            log.info("Bild gefunden: %s", out)
            return str(out), source
    except Exception as exc:
        log.error("Bildsuche fehlgeschlagen: %s", exc)
        return None, None
