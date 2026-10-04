"""Persistente, über die Oberfläche änderbare Laufzeitgrenzen.

Die Werte liegen bewusst unter ``config/``: Dieser Ordner ist im Docker-Betrieb
als Host-Volume eingebunden und überlebt deshalb Container-Neubauten.
"""
from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel, Field


class TimeoutSettings(BaseModel):
    """Vom Nutzer gepflegte Zeitlimits in Minuten."""

    draft_posts: int = Field(default=25, ge=1, le=180)
    find_and_write: int = Field(default=35, ge=1, le=180)
    write_comments: int = Field(default=35, ge=1, le=180)
    find_and_write_reshares: int = Field(default=35, ge=1, le=180)
    find_and_write_connections: int = Field(default=35, ge=1, le=180)
    ideas_to_posts: int = Field(default=30, ge=1, le=180)
    style_revision: int = Field(default=15, ge=1, le=180)
    rewrite: int = Field(default=10, ge=1, le=180)
    image_generation: int = Field(default=5, ge=1, le=180)


TASK_FIELDS = {
    "draft-posts": "draft_posts",
    "find-and-write": "find_and_write",
    "write-comments": "write_comments",
    "find-and-write-reshares": "find_and_write_reshares",
    "find-and-write-connections": "find_and_write_connections",
    "ideas-to-posts": "ideas_to_posts",
}


def path(root: Path) -> Path:
    return root / "config" / "timeouts.yaml"


def load(root: Path) -> TimeoutSettings:
    target = path(root)
    if not target.exists():
        return TimeoutSettings()
    data = yaml.safe_load(target.read_text(encoding="utf-8")) or {}
    return TimeoutSettings.model_validate(data)


def save(root: Path, settings: TimeoutSettings) -> None:
    target = path(root)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        yaml.safe_dump(settings.model_dump(), allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )


def task_seconds(root: Path, task: str) -> int:
    """Zeitlimit des eigentlichen KI-Aufrufs."""
    settings = load(root)
    field = TASK_FIELDS.get(task)
    if field is None:
        return 20 * 60
    return int(getattr(settings, field)) * 60


def process_seconds(root: Path, task: str, count: int = 1) -> int:
    """Grenze für den ganzen Kindprozess inklusive Evaluator und Dateiarbeit."""
    settings = load(root)
    if task == "ideas-to-posts":
        # Ideen laufen einzeln nacheinander; jede kann eine Stilrevision auslösen.
        minutes = max(1, count) * (settings.ideas_to_posts + settings.style_revision) + 5
    elif task in TASK_FIELDS:
        minutes = int(getattr(settings, TASK_FIELDS[task])) + settings.style_revision + 5
    else:
        minutes = 20
    return minutes * 60
