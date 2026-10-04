"""Vertrauensbasierte automatische Freigabe neuer Job-Entwürfe.

Automatisch freigegeben heißt ausschließlich: von approvals.md nach schedule.md
verschieben. Die Veröffentlichung übernimmt weiterhin separat `run-due`.
"""
from __future__ import annotations

from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path

from . import queue as q
from .automation import JobDef
from .models.campaign import load_campaign
from .style_learning import job_trust, record_auto_approval, score_threshold

APPROVALS_TITLE = "Freigaben — warten auf deine Bestätigung"
APPROVALS_HINT = "Texte, Scores und Terminvorschläge sind vor der Freigabe editierbar."
SCHEDULE_TITLE = "Einplanung — freigegeben, wartet auf den Zeitpunkt"
SCHEDULE_HINT = "Wird von `li-jobs run-due` veröffentlicht, sobald `publish_at` erreicht ist."
AUTO_DAILY_LIMIT = 4
AUTO_SLOTS = ("09:00", "11:30", "14:00", "16:30")


def _paths(root: Path, campaign: str) -> tuple[Path, Path]:
    campaign_path = Path(campaign)
    if not campaign_path.is_absolute():
        campaign_path = root / campaign_path
    queue_dir = campaign_path.parent / "queue"
    return queue_dir / "approvals.md", queue_dir / "schedule.md"


def snapshot(root: Path, campaign: str) -> dict[str, str]:
    approvals, _ = _paths(root, campaign)
    return {item.id: item.text for item in q.parse(approvals)}


def touched_ids(root: Path, campaign: str, before: dict[str, str]) -> set[str]:
    approvals, _ = _paths(root, campaign)
    return {
        item.id
        for item in q.parse(approvals)
        if item.id not in before or before[item.id] != item.text
    }


def _auto_slot(
    scheduled: list[q.QueueItem],
    *,
    active_hours: tuple[int, int],
    now: datetime | None = None,
) -> str:
    """Nächster Werktag-Slot; höchstens vier automatische Aktionen pro Tag."""
    now = now or datetime.now()
    used = {item.publish_at for item in scheduled if item.publish_at}
    automatic_per_day = Counter(
        item.publish_at[:10]
        for item in scheduled
        if item.publish_at and item.approval_origin == "automatic"
    )
    lo, hi = active_hours
    slots = []
    for value in AUTO_SLOTS:
        hour, minute = (int(part) for part in value.split(":"))
        if lo <= hour < hi:
            slots.append((hour, minute))
    if not slots:
        slots = [(lo, 0)]

    for day_offset in range(366):
        day = (now + timedelta(days=day_offset)).date()
        if day.weekday() >= 5 or automatic_per_day[day.isoformat()] >= AUTO_DAILY_LIMIT:
            continue
        for hour, minute in slots:
            when = datetime.combine(day, datetime.min.time()).replace(hour=hour, minute=minute)
            value = when.isoformat(timespec="minutes")
            if when <= now or value in used:
                continue
            return value
    raise RuntimeError("Kein freier automatischer Werktag-Slot im nächsten Jahr.")


def _move_automatic(
    root: Path,
    campaign_path: str,
    eligible: list[q.QueueItem],
    *,
    threshold: float,
    mode: str,
    job_id: str,
) -> list[str]:
    approvals_path, schedule_path = _paths(root, campaign_path)
    pending = q.parse(approvals_path)
    scheduled = q.parse(schedule_path)
    all_scheduled: list[q.QueueItem] = []
    known_schedule_paths = set()
    for other_schedule in (root / "Kampagnen").rglob("queue/schedule.md"):
        known_schedule_paths.add(other_schedule.resolve())
        all_scheduled.extend(q.parse(other_schedule))
    if schedule_path.resolve() not in known_schedule_paths:
        all_scheduled.extend(scheduled)
    campaign_file = Path(campaign_path)
    if not campaign_file.is_absolute():
        campaign_file = root / campaign_file
    active_hours = load_campaign(campaign_file).schedule.active_hours
    existing = {item.id for item in scheduled}
    approved_ids: list[str] = []
    for item in sorted(
        eligible,
        key=lambda candidate: (-(q.approval_score(candidate) or 0), candidate.id),
    ):
        item.approved = True
        item.approval_origin = "automatic"
        item.auto_approval_threshold = threshold
        item.publish_at = _auto_slot(all_scheduled, active_hours=active_hours)
        if item.id not in existing:
            scheduled.append(item)
            existing.add(item.id)
        all_scheduled.append(item)
        approved_ids.append(item.id)
        record_auto_approval(
            root, item, item.source_job_id or job_id, mode, threshold
        )
    approved = set(approved_ids)
    q.write(
        approvals_path,
        [item for item in pending if item.id not in approved],
        APPROVALS_TITLE,
        APPROVALS_HINT,
    )
    q.write(schedule_path, scheduled, SCHEDULE_TITLE, SCHEDULE_HINT)
    return approved_ids


def approve_above_score(root: Path, campaign: str, minimum_score: float) -> dict:
    """Explizite Sammelfreigabe, unabhängig vom Vertrauens-Hebel einzelner Jobs."""
    if not 0 <= minimum_score <= 1:
        raise ValueError("Score muss zwischen 0 und 1 liegen.")
    approvals_path, _ = _paths(root, campaign)
    eligible = [
        item
        for item in q.parse(approvals_path)
        if item.kind != "connection"
        and q.approval_score(item) is not None
        and q.approval_score(item) >= minimum_score
        and (item.text.strip() or (item.kind == "reshare" and not item.reshare_with_comment))
    ]
    approved = _move_automatic(
        root,
        campaign,
        eligible,
        threshold=minimum_score,
        mode=f"score_{round(minimum_score * 100)}",
        job_id="bulk-score",
    )
    return {
        "approved": approved,
        "count": len(approved),
        "threshold": minimum_score,
        "daily_limit": AUTO_DAILY_LIMIT,
        "weekends": False,
    }


def apply_for_job(root: Path, job: JobDef, candidates: set[str]) -> dict:
    """Qualifizierte neue/geänderte Einträge eines Jobs direkt einplanen."""
    if job.approval_mode == "manual":
        return {"mode": "manual", "approved": [], "reason": "manual"}
    trust = job_trust(root, job.id)
    if not trust["unlocked"]:
        return {
            "mode": job.approval_mode,
            "approved": [],
            "reason": "locked",
            "trust": trust,
        }

    top_percent = int(job.approval_mode.split("_")[1])
    threshold = score_threshold(root, job.id, top_percent)
    if threshold is None:
        return {
            "mode": job.approval_mode,
            "approved": [],
            "reason": "not_enough_scored_approvals",
            "trust": trust,
        }

    approvals_path, schedule_path = _paths(root, job.campaign)
    pending = q.parse(approvals_path)
    scheduled = q.parse(schedule_path)
    eligible = [
        item
        for item in pending
        if item.id in candidates
        and item.source_job_id == job.id
        and item.text.strip()
        and item.publish_at
        and q.approval_score(item) is not None
        and q.approval_score(item) >= threshold
    ]
    if not eligible:
        return {
            "mode": job.approval_mode,
            "approved": [],
            "threshold": threshold,
            "reason": "no_score_above_threshold",
            "trust": trust,
        }

    approved_ids = _move_automatic(
        root,
        job.campaign,
        eligible,
        threshold=threshold,
        mode=job.approval_mode,
        job_id=job.id,
    )
    return {
        "mode": job.approval_mode,
        "approved": sorted(approved_ids),
        "threshold": threshold,
        "top_percent": top_percent,
        "trust": trust,
    }
