"""Interne Job-Definitionen für den Scheduler (menschlich lesbarer Rhythmus).

Getrennt von `queue.py` (Content) und von der echten OS-Crontab: Hier legt der
Nutzer in der UI fest, WIE OFT welcher Job läuft ("täglich um 07:30", "alle 15
Minuten" …) und ob er gerade **aktiv** ist. Ein einziger Cron-Eintrag ruft
`li-scheduler` in kurzem Takt auf; der prüft diese Datei und führt nur an, was
aktiv und fällig ist.

Datei: automation/jobs.yaml (menschenlesbares YAML, eine Liste von Jobs).
"""
from __future__ import annotations

import fcntl
import os
import re
from contextlib import contextmanager
from datetime import datetime, timedelta
from pathlib import Path
from typing import Callable, Literal, TypeVar

import yaml
from pydantic import BaseModel, Field, field_validator, model_validator

from . import timeouts

ROOT = Path(__file__).resolve().parents[2]
JOBS_FILE = ROOT / "automation" / "jobs.yaml"
JOBS_LOCK = ROOT / "automation" / "jobs.lock"
T = TypeVar("T")

Task = Literal[
    "draft-posts",
    "find-and-write",
    "write-comments",
    "find-and-write-reshares",
    "find-and-write-connections",
    "ideas-to-posts",
    "find-comments",
    "find-reshares",
    "run-due",
    "analytics",
]
ApprovalMode = Literal["manual", "top_20", "top_15", "top_10", "top_5"]
FreqKind = Literal["interval", "daily", "weekly"]

WEEKDAY_NAMES = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
WEEKDAY_WORDS = {
    1: ("montag", "montags", "mo"),
    2: ("dienstag", "dienstags", "di"),
    3: ("mittwoch", "mittwochs", "mi"),
    4: ("donnerstag", "donnerstags", "do"),
    5: ("freitag", "freitags", "fr"),
    6: ("samstag", "samstags", "sonnabend", "sa"),
    7: ("sonntag", "sonntags", "so"),
}


class Frequency(BaseModel):
    kind: FreqKind
    minutes: int | None = Field(
        default=None, ge=1, le=10080, description="für interval: alle N Minuten"
    )
    time: str | None = Field(default=None, description="für daily/weekly: HH:MM")
    weekdays: list[int] = Field(default_factory=list, description="1=Mo … 7=So; leer=täglich")

    @field_validator("time")
    @classmethod
    def valid_time(cls, value: str | None) -> str | None:
        if value is None:
            return None
        match = re.fullmatch(r"([01]?\d|2[0-3]):([0-5]\d)", value.strip())
        if not match:
            raise ValueError("Uhrzeit muss zwischen 00:00 und 23:59 liegen")
        return f"{int(match.group(1)):02d}:{int(match.group(2)):02d}"

    @field_validator("weekdays")
    @classmethod
    def valid_weekdays(cls, value: list[int]) -> list[int]:
        if any(day < 1 or day > 7 for day in value):
            raise ValueError("Wochentage müssen zwischen 1 (Mo) und 7 (So) liegen")
        return sorted(set(value))

    @model_validator(mode="after")
    def complete_frequency(self) -> "Frequency":
        if self.kind == "interval" and self.minutes is None:
            raise ValueError("Für ein Intervall fehlt die Anzahl Minuten")
        if self.kind in {"daily", "weekly"} and self.time is None:
            raise ValueError("Für diesen Rhythmus fehlt die Uhrzeit")
        if self.kind == "weekly" and not self.weekdays:
            raise ValueError("Für einen Wochenrhythmus fehlt mindestens ein Wochentag")
        return self

    def human(self) -> str:
        if self.kind == "interval":
            assert self.minutes is not None
            if self.minutes == 60:
                return "Jede Stunde"
            if self.minutes % 60 == 0:
                return f"Alle {self.minutes // 60} Stunden"
            return f"Alle {self.minutes} Minuten"
        days = ", ".join(WEEKDAY_NAMES[d - 1] for d in self.weekdays)
        if self.kind == "weekly":
            return f"{days} um {self.time} Uhr"
        return f"Jeden Tag um {self.time} Uhr"


class JobDef(BaseModel):
    id: str
    active: bool = True
    task: Task
    campaign: str
    count: int = 2
    approval_mode: ApprovalMode = "manual"
    freq: Frequency
    last_run: str | None = None
    last_attempt: str | None = None
    last_status: Literal["running", "ok", "failed"] | None = None
    last_error: str | None = None
    created: str = Field(default_factory=lambda: datetime.now().isoformat(timespec="minutes"))

    def is_running(self, now: datetime | None = None) -> bool:
        """Treat a recent running state as a lock, but recover from stale crashes."""
        if self.last_status != "running" or not self.last_attempt:
            return False
        try:
            attempted = datetime.fromisoformat(self.last_attempt)
        except ValueError:
            return False
        now = now or datetime.now(tz=attempted.tzinfo)
        configured = timeouts.process_seconds(ROOT, self.task, self.count) // 60 + 5
        return timedelta(0) <= now - attempted <= timedelta(minutes=max(55, configured))

    def is_due(self, now: datetime | None = None) -> bool:
        now = now or datetime.now()
        last = datetime.fromisoformat(self.last_run) if self.last_run else None

        if self.freq.kind == "interval":
            if last is None:
                return True
            return now - last >= timedelta(minutes=self.freq.minutes or 60)

        # daily / weekly: an passendem Wochentag, zur passenden Zeit, mit Gnadenfrist
        if self.freq.weekdays and now.isoweekday() not in self.freq.weekdays:
            return False
        hh, mm = (self.freq.time or "09:00").split(":")
        target = now.replace(hour=int(hh), minute=int(mm), second=0, microsecond=0)
        if now < target:
            return False
        if last and last >= target:
            return False  # für diesen Termin schon gelaufen
        return (now - target) <= timedelta(minutes=30)  # keine Nachhol-Lawine nach Ausfall


def _load_unlocked() -> list[JobDef]:
    if not JOBS_FILE.exists():
        return []
    data = yaml.safe_load(JOBS_FILE.read_text(encoding="utf-8")) or []
    out = []
    for raw in data:
        try:
            out.append(JobDef.model_validate(raw))
        except Exception:
            continue
    return out


def _save_unlocked(jobs: list[JobDef]) -> None:
    JOBS_FILE.parent.mkdir(parents=True, exist_ok=True)
    data = [j.model_dump() for j in jobs]
    temporary = JOBS_FILE.with_name(f".{JOBS_FILE.name}.{os.getpid()}.tmp")
    try:
        temporary.write_text(
            yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8"
        )
        os.replace(temporary, JOBS_FILE)
    finally:
        temporary.unlink(missing_ok=True)


@contextmanager
def _locked():
    JOBS_LOCK.parent.mkdir(parents=True, exist_ok=True)
    with JOBS_LOCK.open("a+", encoding="utf-8") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(lock.fileno(), fcntl.LOCK_UN)


def load() -> list[JobDef]:
    # Die eigentliche Datei wird atomar ersetzt; Leser sehen daher stets eine
    # vollständige alte oder neue Version.
    return _load_unlocked()


def save(jobs: list[JobDef]) -> None:
    """Vollständigen Stand sicher schreiben (nur für bewusst aktuelle Snapshots)."""
    with _locked():
        _save_unlocked(jobs)


def mutate(change: Callable[[list[JobDef]], T]) -> T:
    """Read-modify-write als eine prozessübergreifend gesperrte Operation."""
    with _locked():
        jobs = _load_unlocked()
        result = change(jobs)
        _save_unlocked(jobs)
        return result


def claim_job(job_id: str, *, require_due: bool = True) -> JobDef | None:
    """Job atomar als laufend markieren und einen unveränderlichen Snapshot liefern."""
    now = datetime.now()

    def claim(jobs: list[JobDef]) -> JobDef | None:
        current = next((job for job in jobs if job.id == job_id), None)
        if current is None or not current.active or current.is_running(now):
            return None
        if require_due and not current.is_due(now):
            return None
        current.last_attempt = now.isoformat(timespec="seconds")
        current.last_status = "running"
        current.last_error = None
        return current.model_copy(deep=True)

    return mutate(claim)


def finish_job(
    job_id: str,
    *,
    ok: bool,
    error: str | None = None,
    expected_created: str | None = None,
) -> JobDef | None:
    """Nur Laufzeitstatus mergen; Nutzeränderungen und Löschungen bleiben erhalten."""
    now = datetime.now().isoformat(timespec="seconds")

    def finish(jobs: list[JobDef]) -> JobDef | None:
        current = next((job for job in jobs if job.id == job_id), None)
        if current is None or (
            expected_created is not None and current.created != expected_created
        ):
            return None
        if ok:
            current.last_run = now
            current.last_status = "ok"
            current.last_error = None
        else:
            current.last_status = "failed"
            current.last_error = error or "Unbekannter Fehler"
        return current.model_copy(deep=True)

    return mutate(finish)


def next_id(jobs: list[JobDef]) -> str:
    numbers = []
    for job in jobs:
        match = re.fullmatch(r"job-(\d+)", job.id)
        if match:
            numbers.append(int(match.group(1)))
    n = max(numbers, default=0) + 1
    return f"job-{n:04d}"


def parse_human_frequency(value: str) -> Frequency:
    """Parst bewusst kleine, verständliche deutsche Zeitplan-Sätze.

    Unterstützt zum Beispiel ``jeden Tag um 15 Uhr``, ``alle 30 Minuten``,
    ``alle 2 Stunden`` sowie ``montags und mittwochs um 09:30``. Ein begrenztes
    Vokabular ist hier absichtlich verlässlicher als ein vermeintlich freies
    Sprachmodell: Was nicht eindeutig ist, wird mit einer klaren Meldung abgelehnt.
    """
    original = value.strip()
    text = re.sub(
        r"\s+",
        " ",
        original.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue"),
    ).strip(" .,!;")
    if not text:
        raise ValueError("Bitte einen Zeitplan eingeben")

    interval = re.fullmatch(
        r"(?:alle|jede[nr]?)\s+(\d+)\s*(minute[n]?|min|stunde[n]?|std)", text
    )
    if interval:
        amount = int(interval.group(1))
        unit = interval.group(2)
        minutes = amount * 60 if unit.startswith(("stunde", "std")) else amount
        return Frequency(kind="interval", minutes=minutes)
    if text in {"jede stunde", "stuendlich"}:
        return Frequency(kind="interval", minutes=60)

    time_match = re.search(r"(?<!\d)([01]?\d|2[0-3])(?:[:.]([0-5]\d))?\s*(?:uhr)?\s*$", text)
    if not time_match:
        raise ValueError(
            "Uhrzeit fehlt. Beispiele: ‚jeden Tag um 15 Uhr‘ oder ‚montags um 09:30‘"
        )
    hour = int(time_match.group(1))
    minute = int(time_match.group(2) or 0)
    at = f"{hour:02d}:{minute:02d}"
    prefix = text[:time_match.start()].strip(" ,.-")

    if any(word in prefix for word in ("jeden tag", "jeder tag", "taeglich", "taglich")):
        return Frequency(kind="daily", time=at)

    if "werktag" in prefix or "wochentag" in prefix:
        return Frequency(kind="weekly", time=at, weekdays=[1, 2, 3, 4, 5])
    if "wochenende" in prefix:
        return Frequency(kind="weekly", time=at, weekdays=[6, 7])

    weekdays: list[int] = []
    for day, words in WEEKDAY_WORDS.items():
        normalized_words = tuple(
            word.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
            for word in words
        )
        if any(re.search(rf"(?<!\w){re.escape(word)}(?!\w)", prefix) for word in normalized_words):
            weekdays.append(day)
    if weekdays:
        return Frequency(kind="weekly", time=at, weekdays=weekdays)

    raise ValueError(
        "Rhythmus nicht erkannt. Beispiele: ‚jeden Tag um 15 Uhr‘, "
        "‚alle 30 Minuten‘ oder ‚montags und mittwochs um 09:30‘"
    )
