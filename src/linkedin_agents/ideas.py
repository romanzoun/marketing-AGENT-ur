"""Persistente Ideen-Inbox für spätere LinkedIn-Entwürfe."""
from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, Field

IdeaStatus = Literal["open", "processing", "done", "failed"]


class Idea(BaseModel):
    id: str
    text: str = Field(min_length=1)
    campaign: str | None = None
    status: IdeaStatus = "open"
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat(timespec="minutes"))
    output_id: str | None = None
    output_campaign: str | None = None
    last_error: str | None = None


def path(root: Path) -> Path:
    return root / "ideas" / "ideas.yaml"


def load(root: Path) -> list[Idea]:
    source = path(root)
    if not source.exists():
        return []
    data = yaml.safe_load(source.read_text(encoding="utf-8")) or []
    result: list[Idea] = []
    for raw in data:
        try:
            result.append(Idea.model_validate(raw))
        except Exception:
            continue
    return result


def save(root: Path, ideas: list[Idea]) -> None:
    target = path(root)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        yaml.safe_dump(
            [idea.model_dump() for idea in ideas], allow_unicode=True, sort_keys=False
        ),
        encoding="utf-8",
    )


def next_id(ideas: list[Idea]) -> str:
    numbers = []
    for idea in ideas:
        try:
            numbers.append(int(idea.id.rsplit("-", 1)[1]))
        except (IndexError, ValueError):
            continue
    return f"idea-{max(numbers, default=0) + 1:04d}"


def add(root: Path, text: str, campaign: str | None = None) -> Idea:
    entries = load(root)
    idea = Idea(id=next_id(entries), text=text.strip(), campaign=campaign or None)
    entries.append(idea)
    save(root, entries)
    return idea
