"""Bild-Rendering-Backends.

Provider-agnostisch: der Designer-Agent liefert den Prompt, der Generator
rendert ihn. Standard-Provider ``none`` schreibt nur den Prompt als Brief
(Dry-Run für Bilder). Provider ``openai`` rendert via OpenAI Images API.
"""
from __future__ import annotations

import base64
from pathlib import Path

import httpx

from .. import timeouts
from ..utils.logging import get_logger

log = get_logger("imaging.generator")

IMAGE_DIR = Path(".runs/images")


class ImageGenerator:
    def __init__(self, provider: str, openai_api_key: str, model: str) -> None:
        self._provider = provider.lower()
        self._openai_key = openai_api_key
        self._model = model
        IMAGE_DIR.mkdir(parents=True, exist_ok=True)

    async def render(self, prompt: str, name: str) -> str | None:
        """Rendert ein Bild und gibt den Dateipfad zurück (oder None)."""
        if self._provider == "openai" and self._openai_key:
            return await self._render_openai(prompt, name)

        # Fallback: kein echter Renderer -> Prompt als Brief ablegen.
        brief = IMAGE_DIR / f"{name}.txt"
        brief.write_text(prompt, encoding="utf-8")
        log.info("[IMAGE DRY-RUN] Bild-Brief gespeichert: %s", brief)
        return None

    async def _render_openai(self, prompt: str, name: str) -> str | None:
        try:
            root = Path(__file__).resolve().parents[3]
            timeout = timeouts.load(root).image_generation * 60
            async with httpx.AsyncClient(timeout=timeout) as client:
                resp = await client.post(
                    "https://api.openai.com/v1/images/generations",
                    headers={"Authorization": f"Bearer {self._openai_key}"},
                    json={
                        "model": self._model,
                        "prompt": prompt,
                        "size": "1024x1024",
                        "n": 1,
                    },
                )
                resp.raise_for_status()
                data = resp.json()["data"][0]
                out = IMAGE_DIR / f"{name}.png"
                if data.get("b64_json"):
                    out.write_bytes(base64.b64decode(data["b64_json"]))
                elif data.get("url"):
                    img = await client.get(data["url"])
                    img.raise_for_status()
                    out.write_bytes(img.content)
                else:
                    return None
                log.info("Bild gerendert: %s", out)
                return str(out)
        except Exception as exc:
            log.error("Bildgenerierung fehlgeschlagen: %s", exc)
            return None
