"""Kampagnen-Modell inkl. Guardrails/Limits.

Die Kampagne ist die *einzige Quelle der Wahrheit*. Alle Agenten müssen sich
strikt an diese Vorgaben halten; der Reviewer erzwingt sie inhaltlich, die
Guardrails erzwingen die Mengen-/Rate-Limits im Code.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

import yaml
from pydantic import BaseModel, Field, ValidationError


class Limits(BaseModel):
    posts_per_run: int = 1
    comments_per_run: int = 5
    replies_per_run: int = 3
    reshares_per_run: int = 1


class ImageConfig(BaseModel):
    """Steuert die Bildgenerierung für eigene Posts."""

    enabled: bool = False
    style: str = "clean, modern, professional, LinkedIn-tauglich"
    # Anteil der Posts, die ein Bild erhalten sollen (0.0–1.0)
    ratio: float = Field(default=0.5, ge=0.0, le=1.0)


class Schedule(BaseModel):
    """Zeitplan für den Dauerbetrieb einer Kampagne."""

    start: date | None = None
    end: date | None = None
    cycle_interval_minutes: int = Field(default=120, ge=1)
    # Aktivzeitfenster [von, bis] in Stunden (lokale Zeit); außerhalb wird pausiert.
    active_hours: tuple[int, int] = (8, 20)
    max_cycles: int | None = None


class Campaign(BaseModel):
    name: str
    version: int = Field(default=1, ge=1, description="Fortlaufende Kampagnenversion")
    objective: str = Field(..., description="Ziel der Kampagne")
    language: str = "de"
    audience: str = Field(..., description="Zielgruppe (Kurzbeschreibung)")
    personas: list[str] = Field(
        default_factory=list,
        description="Optionale, konkretere Zielgruppen-Personas",
    )
    products: list[str] = Field(
        default_factory=list,
        description="Produkte/Angebote inkl. kurzem Nutzen, über die kommuniziert wird",
    )
    voice: str = Field(..., description="Tonalität / Brand Voice")

    topics: list[str] = Field(default_factory=list, description="Erlaubte Themen")
    banned_topics: list[str] = Field(default_factory=list, description="Verbotene Themen")
    keywords_to_engage: list[str] = Field(
        default_factory=list,
        description="Schlüsselwörter, nach denen im Feed für Kommentare gesucht wird",
    )

    required_hashtags: list[str] = Field(default_factory=list)
    cta: str | None = Field(default=None, description="Call to Action")

    max_post_chars: int = 1300
    max_comment_chars: int = 500

    limits: Limits = Field(default_factory=Limits)
    images: ImageConfig = Field(default_factory=ImageConfig)
    schedule: Schedule = Field(default_factory=Schedule)

    def guardrail_summary(self) -> str:
        """Kompakte Zusammenfassung für die System-Prompts der Agenten."""
        return (
            f"Kampagne: {self.name}\n"
            f"Ziel: {self.objective}\n"
            f"Zielgruppe: {self.audience}\n"
            f"Personas: {', '.join(self.personas) or '—'}\n"
            f"Produkte/Angebote: {', '.join(self.products) or '—'}\n"
            f"Tonalität: {self.voice}\n"
            f"Sprache: {self.language}\n"
            f"Erlaubte Themen: {', '.join(self.topics) or '—'}\n"
            f"Verbotene Themen: {', '.join(self.banned_topics) or '—'}\n"
            f"Pflicht-Hashtags: {', '.join(self.required_hashtags) or '—'}\n"
            f"CTA: {self.cta or '—'}\n"
            f"Max. Zeichen Post: {self.max_post_chars} | Kommentar: {self.max_comment_chars}"
        )


def load_campaign(path: str | Path) -> Campaign:
    """Lädt und validiert eine Kampagne aus einer YAML-Datei."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Kampagnen-Datei nicht gefunden: {p}")
    data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    try:
        return Campaign.model_validate(data)
    except ValidationError as exc:  # klarere Fehlermeldung
        raise ValueError(f"Ungültige Kampagne in {p}:\n{exc}") from exc
