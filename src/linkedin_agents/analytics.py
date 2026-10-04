"""Dauerhafte, kampagnenbezogene LinkedIn-Messreihen."""
from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path
import yaml
from pydantic import BaseModel, Field

from . import queue as q


class MetricSnapshot(BaseModel):
    captured_at: str
    reactions: int | None = None
    comments: int | None = None
    replies: int | None = None
    reposts: int | None = None
    impressions: int | None = None


class AnalyticsRecord(BaseModel):
    item_id: str
    campaign: str
    campaign_version: int = 1
    kind: q.ItemKind
    text: str = ""
    source_url: str | None = None
    published_url: str | None = None
    published_at: str | None = None
    last_checked_at: str | None = None
    last_error: str = ""
    snapshots: list[MetricSnapshot] = Field(default_factory=list)


def path_for(campaign_path: str | Path) -> Path:
    return Path(campaign_path).parent / "queue" / "analytics.yaml"


def load(campaign_path: str | Path) -> list[AnalyticsRecord]:
    path = path_for(campaign_path)
    if not path.exists():
        return []
    try:
        raw = yaml.safe_load(path.read_text(encoding="utf-8")) or []
        return [AnalyticsRecord.model_validate(entry) for entry in raw]
    except (ValueError, yaml.YAMLError):
        return []


def save(campaign_path: str | Path, records: list[AnalyticsRecord]) -> None:
    path = path_for(campaign_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = [record.model_dump(mode="json") for record in records]
    temporary_path = path.with_suffix(f"{path.suffix}.tmp")
    temporary_path.write_text(
        yaml.safe_dump(payload, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )
    temporary_path.replace(path)


def register(
    campaign_path: str | Path,
    item: q.QueueItem,
    published_url: str | None = None,
) -> AnalyticsRecord:
    records = load(campaign_path)
    record = next((entry for entry in records if entry.item_id == item.id), None)
    if record is None:
        record = AnalyticsRecord(
            item_id=item.id,
            campaign=item.campaign,
            campaign_version=item.campaign_version,
            kind=item.kind,
        )
        records.append(record)
    record.text = (
        item.note
        if item.kind == "reshare" and not item.reshare_with_comment
        else item.text
    )
    record.campaign_version = item.campaign_version
    record.source_url = item.url or record.source_url
    record.published_url = published_url or item.published_url or record.published_url
    record.published_at = item.published_at or item.publish_at or record.published_at
    save(campaign_path, records)
    return record


def sync_log(campaign_path: str | Path) -> list[AnalyticsRecord]:
    """Importiert auch historische Log-Einträge, ohne Messreihen zu überschreiben."""
    log_path = Path(campaign_path).parent / "queue" / "log.md"
    for item in q.parse(log_path):
        if item.kind != "connection":
            register(campaign_path, item)
    return load(campaign_path)


def add_snapshot(
    campaign_path: str | Path,
    item_id: str,
    values: dict[str, int | None],
    *,
    error: str = "",
) -> AnalyticsRecord | None:
    records = load(campaign_path)
    record = next((entry for entry in records if entry.item_id == item_id), None)
    if record is None:
        return None
    now = datetime.now().isoformat(timespec="seconds")
    record.last_checked_at = now
    record.last_error = error
    if not error:
        record.snapshots.append(MetricSnapshot(captured_at=now, **values))
        record.snapshots = record.snapshots[-180:]
    save(campaign_path, records)
    return record


def set_published_url(
    campaign_path: str | Path, item_id: str, url: str
) -> AnalyticsRecord | None:
    records = load(campaign_path)
    record = next((entry for entry in records if entry.item_id == item_id), None)
    if record is None:
        return None
    record.published_url = url
    record.last_error = ""
    save(campaign_path, records)
    return record


def _number(value: str) -> int:
    compact = value.strip().replace("\u00a0", "").replace(" ", "")
    suffix = compact[-1:].lower()
    multiplier = {"k": 1_000, "m": 1_000_000, "b": 1_000_000_000}.get(suffix, 1)
    if multiplier != 1:
        compact = compact[:-1].replace(",", ".")
        return round(float(compact) * multiplier)
    if re.fullmatch(r"\d{1,3}([.,]\d{3})+", compact):
        compact = compact.replace(".", "").replace(",", "")
    else:
        compact = compact.replace(",", "").replace(".", "")
    return int(compact or "0")


def extract_counts(text: str, *, comment: bool = False) -> dict[str, int | None]:
    """Extrahiert DE/EN-Kennzahlen aus sichtbarem LinkedIn-Text/ARIA-Labels."""
    number = r"(\d[\d.,\u00a0 ]*(?:[KkMmBb])?)"
    patterns: dict[str, tuple[str, ...]] = {
        "reactions": (
            rf"{number}\s*(?:reactions?|reaktionen?|likes?|gefällt[- ]mir)",
            rf"{number}\s+(?:others?|weitere)\s+(?:reacted|reagierten)",
        ),
        "comments": (rf"{number}\s*(?:comments?|kommentare?)",),
        "replies": (rf"{number}\s*(?:replies|antworten)",),
        "reposts": (rf"{number}\s*(?:reposts?|shares?|mal geteilt)",),
        "impressions": (rf"{number}\s*(?:impressions?|impressionen)",),
    }
    values: dict[str, int | None] = {}
    for key, candidates in patterns.items():
        found: list[int] = []
        for pattern in candidates:
            for match in re.finditer(pattern, text, re.I):
                try:
                    value = _number(match.group(1))
                    if "other" in match.group(0).lower() or "weitere" in match.group(0).lower():
                        value += 1
                    found.append(value)
                except ValueError:
                    continue
        values[key] = max(found) if found else None
    if comment:
        values["comments"] = None
        values["reposts"] = None
        values["impressions"] = None
    return values


def dashboard(campaign_path: str | Path) -> dict:
    records = sync_log(campaign_path)
    rows = []
    totals = {key: 0 for key in ("reactions", "comments", "replies", "reposts", "impressions")}
    measured = 0
    for record in records:
        latest = record.snapshots[-1].model_dump() if record.snapshots else None
        first = record.snapshots[0].model_dump() if record.snapshots else None
        if latest:
            measured += 1
            for key in totals:
                totals[key] += latest.get(key) or 0
        rows.append({
            **record.model_dump(exclude={"snapshots"}),
            "latest": latest,
            "first": first,
            "snapshot_count": len(record.snapshots),
        })
    rows.sort(key=lambda row: row.get("published_at") or "", reverse=True)
    return {
        "records": rows,
        "summary": {
            "published": len(records),
            "posts": sum(row["kind"] == "post" for row in rows),
            "comments_authored": sum(row["kind"] == "comment" for row in rows),
            "reshares": sum(row["kind"] == "reshare" for row in rows),
            "measured": measured,
            "missing_published_urls": sum(
                row["kind"] in {"post", "reshare"} and not row["published_url"]
                for row in rows
            ),
            **totals,
        },
    }
