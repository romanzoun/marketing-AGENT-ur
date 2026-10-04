"""Warteschlangen für Freigabe und Planung (Markdown als Speicher).

Zwei menschenlesbare Dateien pro Kampagne:
  - approvals.md : Posts, Kommentare und Reshares, die auf Freigabe warten
  - schedule.md  : freigegebene Einträge mit Veröffentlichungszeitpunkt
  - log.md       : ausgeführte Einträge

Format je Eintrag (Checkbox = Freigabe, YAML = Daten):

    ### <id> — post
    - [ ] freigeben

    ```yaml
    id: post-2026-09-10-0001
    kind: post
    ...
    ```
"""
from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, Field

ItemKind = Literal["post", "comment", "reshare", "connection"]

_SECTION = re.compile(r"^###\s+(?P<id>\S+)", re.M)
_YAML_FENCE = re.compile(r"```yaml\s*\n(?P<body>.*?)\n```", re.S)
_CHECKBOX = re.compile(r"^-\s*\[(?P<mark>[ xX])\]", re.M)


class QueueItem(BaseModel):
    id: str
    kind: ItemKind
    campaign: str = ""
    campaign_version: int = Field(
        default=1, ge=1, description="Kampagnenversion bei Erstellung des Inhalts"
    )
    source_job_id: str | None = Field(
        default=None, description="Job, der diesen Entwurf zuletzt erzeugt oder getextet hat"
    )
    text: str = ""
    url: str | None = Field(default=None, description="Ziel-Permalink bei Kommentaren")
    author: str = ""
    note: str = ""
    user_memory_note: str = Field(
        default="",
        max_length=2000,
        description="Optionaler Nutzerkommentar, der bei Freigabe/Ablehnung gelernt wird",
    )
    reshare_with_comment: bool = Field(
        default=True,
        description="Bei Reshares: eigener Begleittext; false = sofortiger Awareness-Reshare",
    )
    image_path: str | None = None
    image_source: str | None = Field(default=None, description="Quellenangabe zum Bild")
    image_origin: Literal["generated", "web", "upload"] | None = Field(
        default=None, description="Herkunft des Bildes"
    )
    image_prompt: str = Field(
        default="", description="Letzter Prompt oder Suchbegriff für das Bild"
    )
    image_auto_selected: bool | None = Field(
        default=None,
        description="Ob die Kampagnen-Bildquote diesen Post für ein Bild ausgewählt hat",
    )
    image_error: str = Field(
        default="", description="Letzter Fehler der automatischen Bildgenerierung"
    )
    published_url: str | None = Field(
        default=None, description="Permalink der veröffentlichten eigenen Aktion"
    )
    published_at: str | None = Field(
        default=None, description="Tatsächlicher Veröffentlichungszeitpunkt"
    )
    publish_at: str | None = Field(default=None, description="ISO-Zeitpunkt der Veröffentlichung")
    generated_text: str | None = Field(
        default=None, description="Ursprünglicher Agentenentwurf vor Nutzerkorrekturen"
    )
    evaluation_score: float | None = Field(
        default=None, ge=0, le=1, description="Geschätzte Freigabewahrscheinlichkeit"
    )
    evaluation_note: str = Field(
        default="", description="Kurze Begründung des Style-Evaluators"
    )
    fit_score: float | None = Field(
        default=None,
        ge=0,
        le=1,
        description="Semantische Passung des Originalbeitrags zur Kampagne",
    )
    fit_note: str = Field(
        default="", description="Kurze Begründung der Kampagnenpassung"
    )
    evaluated_at: str | None = None
    approval_origin: Literal["manual", "automatic"] | None = Field(
        default=None, description="Art der Freigabe; steuert ausschließlich Auto-Limits"
    )
    auto_approval_threshold: float | None = Field(default=None, ge=0, le=1)
    approved: bool = False

    def due(self, now: datetime | None = None) -> bool:
        if not self.publish_at:
            return False
        try:
            when = datetime.fromisoformat(self.publish_at)
        except ValueError:
            return False
        return when <= (now or datetime.now())


def approval_score(item: QueueItem) -> float | None:
    """Konservativer Freigabe-Score aus Textqualität und Kampagnenpassung."""
    if item.kind in {"comment", "reshare", "connection"} and item.fit_score is not None:
        if item.evaluation_score is None:
            return item.fit_score
        return min(item.evaluation_score, item.fit_score)
    return item.evaluation_score


def _render_item(item: QueueItem) -> str:
    data = item.model_dump(exclude={"approved"})
    body = yaml.safe_dump(data, allow_unicode=True, sort_keys=False).rstrip()
    mark = "x" if item.approved else " "
    head = f"### {item.id} — {item.kind}"
    if item.publish_at:
        head += f" — geplant: {item.publish_at}"
    return f"{head}\n- [{mark}] freigeben\n\n```yaml\n{body}\n```\n"


def render(items: list[QueueItem], title: str, hint: str) -> str:
    parts = [f"# {title}\n", f"> {hint}\n"]
    parts.extend(_render_item(i) for i in items)
    if not items:
        parts.append("_(leer)_\n")
    return "\n".join(parts)


def parse(path: str | Path) -> list[QueueItem]:
    """Liest Einträge aus einer Queue-Datei (fehlende Datei = leer)."""
    p = Path(path)
    if not p.exists():
        return []
    text = p.read_text(encoding="utf-8")

    items: list[QueueItem] = []
    starts = [m.start() for m in _SECTION.finditer(text)]
    for i, start in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else len(text)
        chunk = text[start:end]
        fence = _YAML_FENCE.search(chunk)
        if not fence:
            continue
        try:
            data = yaml.safe_load(fence.group("body")) or {}
        except yaml.YAMLError:
            continue
        cb = _CHECKBOX.search(chunk)
        data["approved"] = bool(cb and cb.group("mark").lower() == "x")
        try:
            items.append(QueueItem.model_validate(data))
        except Exception:
            continue
    return items


def write(path: str | Path, items: list[QueueItem], title: str, hint: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(render(items, title, hint), encoding="utf-8")


def append(path: str | Path, new_items: list[QueueItem], title: str, hint: str) -> None:
    existing = parse(path)
    known = {i.id for i in existing}
    existing.extend(i for i in new_items if i.id not in known)
    write(path, existing, title, hint)


def next_id(kind: ItemKind, existing: list[QueueItem]) -> str:
    stamp = datetime.now().strftime("%Y-%m-%d")
    prefix = f"{kind}-{stamp}-"
    n = 1 + sum(1 for i in existing if i.id.startswith(prefix))
    return f"{prefix}{n:04d}"
