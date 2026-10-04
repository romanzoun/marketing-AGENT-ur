"""Konfigurierbare Terminvorschlaege fuer freigegebene Aktionen."""
from __future__ import annotations

import random
from collections import Counter
from datetime import datetime, time, timedelta
from pathlib import Path

import yaml
from pydantic import BaseModel, Field, field_validator, model_validator


class PlanningSettings(BaseModel):
    days_ahead: int = Field(default=14, ge=1, le=90)
    weekdays_start: str = "09:00"
    weekdays_end: str = "16:00"
    saturday_start: str = "09:00"
    saturday_end: str = "13:00"
    sunday_start: str = "16:00"
    sunday_end: str = "20:00"

    @field_validator("weekdays_start", "weekdays_end", "saturday_start", "saturday_end", "sunday_start", "sunday_end")
    @classmethod
    def valid_time(cls, value: str) -> str:
        try:
            datetime.strptime(value, "%H:%M")
        except ValueError as exc:
            raise ValueError("Zeit muss im Format HH:MM angegeben werden") from exc
        return value

    @model_validator(mode="after")
    def valid_windows(self) -> PlanningSettings:
        for label, start, end in (
            ("Montag bis Freitag", self.weekdays_start, self.weekdays_end),
            ("Samstag", self.saturday_start, self.saturday_end),
            ("Sonntag", self.sunday_start, self.sunday_end),
        ):
            if start >= end:
                raise ValueError(f"{label}: Startzeit muss vor der Endzeit liegen")
        return self

    def window_for(self, when: datetime) -> tuple[time, time]:
        if when.weekday() == 5:
            values = self.saturday_start, self.saturday_end
        elif when.weekday() == 6:
            values = self.sunday_start, self.sunday_end
        else:
            values = self.weekdays_start, self.weekdays_end
        return tuple(datetime.strptime(value, "%H:%M").time() for value in values)  # type: ignore[return-value]


def path(root: Path) -> Path:
    return root / "config" / "planning.yaml"


def load(root: Path) -> PlanningSettings:
    target = path(root)
    if not target.exists():
        return PlanningSettings()
    return PlanningSettings.model_validate(yaml.safe_load(target.read_text(encoding="utf-8")) or {})


def save(root: Path, settings: PlanningSettings) -> None:
    target = path(root)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        yaml.safe_dump(settings.model_dump(), allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )


def suggest(
    settings: PlanningSettings,
    scheduled_at: list[str],
    *,
    now: datetime | None = None,
    rng: random.Random | None = None,
) -> datetime:
    current = now or datetime.now()
    randomizer = rng or random.SystemRandom()
    counts = Counter(value[:10] for value in scheduled_at if value)
    occupied = {value[:16] for value in scheduled_at if value}
    candidates: list[tuple[int, datetime, list[int]]] = []
    for offset in range(settings.days_ahead + 1):
        day = current + timedelta(days=offset)
        start, end = settings.window_for(day)
        earliest = datetime.combine(day.date(), start)
        latest = datetime.combine(day.date(), end)
        if latest <= current:
            continue
        if earliest < current:
            earliest = current.replace(second=0, microsecond=0) + timedelta(minutes=1)
        if earliest > latest:
            continue
        first_minute = earliest.hour * 60 + earliest.minute
        last_minute = latest.hour * 60 + latest.minute
        available = [
            minute for minute in range(first_minute, last_minute + 1)
            if f"{day.date().isoformat()}T{minute // 60:02d}:{minute % 60:02d}" not in occupied
        ]
        if available:
            candidates.append((counts[day.date().isoformat()], day, available))
    if not candidates:
        raise ValueError("Kein gueltiges Zeitfenster im konfigurierten Vorlauf gefunden.")
    minimum = min(candidate[0] for candidate in candidates)
    least_busy = [candidate for candidate in candidates if candidate[0] == minimum]
    _, day, available = randomizer.choice(least_busy)
    minute = randomizer.choice(available)
    return datetime.combine(day.date(), time(minute // 60, minute % 60))