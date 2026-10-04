"""Gemeinsamer Bild-Workflow für automatische Quote, CLI und Weboberfläche."""
from __future__ import annotations

import math
from pathlib import Path

from .. import queue as q
from ..config import Settings
from ..models.campaign import Campaign
from .generator import ImageGenerator
from .websearch import find_image

AUTO_IMAGE_MIN_SCORE = 0.85


def image_prompt(campaign: Campaign, item: q.QueueItem) -> str:
    """Baut aus Kampagnenstil und Post einen sicheren Art-Direction-Prompt."""
    post = item.text.strip()
    return (
        "Erstelle ein hochwertiges quadratisches Editorial-Bild für einen persönlichen "
        "LinkedIn-Post. Das Motiv soll die Kernaussage visuell erzählen, professionell "
        "und im Feed sofort verständlich sein. Keine Schrift, keine Buchstaben, keine "
        "Logos, keine Wasserzeichen und keine LinkedIn-Oberfläche im Bild. "
        f"Bildstil der Kampagne: {campaign.images.style}. "
        "Nutze den vollständigen finalen Artikeltext als inhaltlichen Kontext und "
        "visualisiere seine zentrale Metapher, ohne Text ins Bild zu schreiben.\n\n"
        f"VOLLSTÄNDIGER ARTIKELTEXT:\n---\n{post}\n---"
    )


def score_allows_auto_image(
    item: q.QueueItem, minimum: float = AUTO_IMAGE_MIN_SCORE
) -> bool:
    """Automatische API-Bilder gibt es nur oberhalb der Qualitätsgrenze."""
    return item.evaluation_score is not None and item.evaluation_score > minimum


def quota_selects_next(existing_posts: list[q.QueueItem], ratio: float) -> bool:
    """Verteilt die Quote stabil auf Posts, die seit Einführung markiert wurden."""
    tracked = sum(item.image_auto_selected is not None for item in existing_posts)

    def target(total: int) -> int:
        # Klassisches Runden statt Python-Banker's-Rounding: 1 * 0.5 => 1.
        return math.floor(total * ratio + 0.5)

    return target(tracked + 1) > target(tracked)


async def set_generated_image(
    item: q.QueueItem,
    campaign: Campaign,
    settings: Settings,
    prompt: str | None = None,
) -> bool:
    item.image_prompt = (prompt or image_prompt(campaign, item)).strip()
    generator = ImageGenerator(
        settings.image_provider, settings.openai_api_key, settings.image_model
    )
    path = await generator.render(item.image_prompt, item.id)
    if not path:
        item.image_error = (
            "Bildgenerierung fehlgeschlagen. Prüfe IMAGE_PROVIDER, OPENAI_API_KEY "
            "und das OpenAI-Kontingent."
        )
        return False
    item.image_path = path
    item.image_source = "Bild: KI-generiert"
    item.image_origin = "generated"
    item.image_error = ""
    return True


async def set_web_image(item: q.QueueItem, query: str) -> bool:
    item.image_prompt = query.strip()
    path, source = await find_image(item.image_prompt, item.id)
    if not path:
        item.image_error = "Kein geeignetes frei nutzbares Webbild gefunden."
        return False
    item.image_path = path
    item.image_source = source
    item.image_origin = "web"
    item.image_error = ""
    return True


def remove_image_file(root: Path, item: q.QueueItem) -> None:
    """Entfernt nur eine Bilddatei aus dem projektlokalen Bilderordner."""
    if not item.image_path:
        return
    target = (root / item.image_path).resolve()
    image_dir = (root / ".runs" / "images").resolve()
    if target.parent == image_dir and target.is_file():
        target.unlink()


def clear_image(root: Path, item: q.QueueItem) -> None:
    remove_image_file(root, item)
    item.image_path = None
    item.image_source = None
    item.image_origin = None
    item.image_error = ""
