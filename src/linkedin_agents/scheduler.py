"""Scheduler-Runner: prüft `automation/jobs.yaml` und führt fällige, aktive Jobs aus.

Einziger benötigter Cron-Eintrag (ersetzt manuelle Einzel-Zeilen):

    */5 * * * * cd /pfad/zum/repo && ./bin/li-scheduler >> .runs/cron.log 2>&1

Startet NIEMALS selbst Edge — bei fehlendem Browser/Login wird der betroffene
Job für diesen Takt übersprungen und geloggt (kein Tab-/Fenster-Wildwuchs).
"""
from __future__ import annotations

import json
import hashlib
import os
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

from . import automation as auto
from . import auto_approval
from . import brain
from . import timeouts
from .config import load_settings
from .utils.logging import get_logger, setup_logging

ROOT = Path(__file__).resolve().parents[2]
log = get_logger("scheduler")
UI_REPAIR_STATE = ROOT / ".runs" / "ui-repair.json"
UI_REPAIR_COOLDOWN = timedelta(hours=6)
UI_FAILURE_MARKERS = (
    "locator.",
    "waiting for get_by_",
    "waiting for locator",
    "strict mode violation",
    "element is not attached",
    "intercepts pointer events",
    "playwright._impl._errors.timeouterror",
    "locator.wait_for: timeout",
    "locator.click: timeout",
    "linkedin-element",
    "linkedin_ui_selector_mismatch",
)


def working_hours_error(now: datetime | None = None) -> str | None:
    settings = load_settings()
    current = (now or datetime.now()).time().replace(tzinfo=None)
    start = settings.working_hours_start
    end = settings.working_hours_end
    allowed = start <= current < end if start < end else current >= start or current < end
    if allowed:
        return None
    return (
        "Jobs sind außerhalb der Arbeitszeiten gesperrt "
        f"({start.strftime('%H:%M')}–{end.strftime('%H:%M')})."
    )


def _timeout_text(value: str | bytes | None, limit: int) -> str:
    if isinstance(value, bytes):
        value = value.decode(errors="replace")
    return (value or "")[-limit:]


def _health_ok() -> bool:
    proc = subprocess.run(
        [str(ROOT / "bin" / "li-health"), "--no-start", "--quiet"],
        capture_output=True, text=True, cwd=ROOT, timeout=120,
    )
    return proc.returncode == 0


def _failure_message(stdout: str, stderr: str) -> str:
    try:
        payload = json.loads(stdout)
        structured_error = str(payload.get("error") or "").strip()
        if structured_error:
            return structured_error[-1000:]
        text = "\n".join(str(payload.get(key) or "") for key in ("stderr", "stdout"))
    except (json.JSONDecodeError, TypeError):
        text = "\n".join((stderr, stdout))
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    usage = next((line for line in reversed(lines) if "usage limit" in line.lower()), None)
    return (usage or (lines[-1] if lines else "Keine Fehlerausgabe"))[-1000:]


def _looks_like_linkedin_ui_failure(job: auto.JobDef, result: dict[str, object]) -> bool:
    if job.task not in {"run-due", "analytics", "find-and-write", "find-and-write-reshares", "find-and-write-connections"}:
        return False
    details = "\n".join(str(result.get(key) or "") for key in ("error", "stderr", "stdout")).lower()
    return any(marker in details for marker in UI_FAILURE_MARKERS)


def _maybe_repair_linkedin_ui(job: auto.JobDef, result: dict[str, object]) -> dict | None:
    if not _looks_like_linkedin_ui_failure(job, result):
        return None
    details = "\n".join(str(result.get(key) or "") for key in ("error", "stderr", "stdout"))[-8000:]
    fingerprint = hashlib.sha256(details.encode("utf-8", errors="replace")).hexdigest()[:16]
    now = datetime.now()
    try:
        state = json.loads(UI_REPAIR_STATE.read_text(encoding="utf-8"))
        last_at = datetime.fromisoformat(state.get("attempted_at", ""))
        if state.get("fingerprint") == fingerprint and now - last_at < UI_REPAIR_COOLDOWN:
            return {"ok": False, "skipped": "cooldown", "fingerprint": fingerprint}
    except (FileNotFoundError, ValueError, TypeError, json.JSONDecodeError):
        pass

    UI_REPAIR_STATE.parent.mkdir(parents=True, exist_ok=True)
    UI_REPAIR_STATE.write_text(
        json.dumps({"fingerprint": fingerprint, "attempted_at": now.isoformat(timespec="seconds")}),
        encoding="utf-8",
    )
    prompt = (
        f"Scheduler-Job: {job.id} ({job.task})\nKampagne: {job.campaign}\n"
        "Vermuteter LinkedIn-UI-/Locatorfehler. Untersuche primär "
        "src/linkedin_agents/browser/linkedin.py und die zugehörigen Tests.\n\n"
        f"Prozessausgabe:\n{details}"
    )
    log.warning("Starte Codex-Reparatur für UI-Fehler %s (%s).", job.id, fingerprint)
    repair = brain.run_code_repair(prompt)
    repair["fingerprint"] = fingerprint
    return repair


def run_task_result(job: auto.JobDef) -> dict[str, object]:
    if hours_error := working_hours_error():
        return {"ok": False, "blocked": True, "error": hours_error, "stdout": "", "stderr": ""}
    content_tasks = {
        "draft-posts", "find-and-write", "write-comments", "find-and-write-reshares",
        "find-and-write-connections",
    }
    before = (
        auto_approval.snapshot(ROOT, job.campaign)
        if job.task in content_tasks and job.approval_mode != "manual"
        else {}
    )
    if job.task in {"run-due", "analytics"}:
        cmd = [str(ROOT / "bin" / "li-jobs"), "--campaign", job.campaign, job.task]
    elif job.task == "find-comments":
        cmd = [str(ROOT / "bin" / "li-jobs"), "--campaign", job.campaign, "find-comments",
               "--limit", str(job.count)]
    elif job.task == "find-reshares":
        cmd = [str(ROOT / "bin" / "li-jobs"), "--campaign", job.campaign, "find-reshares",
               "--limit", str(job.count)]
    else:  # Content-Textjobs -> Codex CLI
        cmd = [str(ROOT / "bin" / "li-brain"), "--campaign", job.campaign, job.task,
               "--count", str(job.count)]
    env = os.environ.copy()
    env["LI_JOB_ID"] = job.id
    process_timeout = timeouts.process_seconds(ROOT, job.task, job.count)
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=ROOT,
            timeout=process_timeout,
            env=env,
        )
    except subprocess.TimeoutExpired as exc:
        minutes = process_timeout // 60
        error = f"Zeitlimit von {minutes} Minuten überschritten"
        log.error("Job %s (%s) fehlgeschlagen: %s", job.id, job.task, error)
        return {
            "ok": False,
            "error": error,
            "stdout": _timeout_text(exc.stdout, 6000),
            "stderr": _timeout_text(exc.stderr, 2000),
        }
    if proc.returncode != 0:
        error = _failure_message(proc.stdout, proc.stderr)
        log.error("Job %s (%s) fehlgeschlagen: %s", job.id, job.task, error)
    else:
        log.info("Job %s (%s) ausgeführt.", job.id, job.task)
        error = None
    result = {
        "ok": proc.returncode == 0,
        "error": error,
        "stdout": proc.stdout[-6000:],
        "stderr": proc.stderr[-2000:],
    }
    if proc.returncode == 0 and job.task in content_tasks and job.approval_mode != "manual":
        candidates = auto_approval.touched_ids(ROOT, job.campaign, before)
        result["auto_approval"] = auto_approval.apply_for_job(ROOT, job, candidates)
    if not result["ok"]:
        repair = _maybe_repair_linkedin_ui(job, result)
        if repair is not None:
            result["ui_repair"] = repair
            if not repair.get("skipped"):
                suffix = (
                    "Codex-Reparatur abgeschlossen"
                    if repair.get("ok")
                    else "Codex-Reparatur fehlgeschlagen"
                )
                result["error"] = (
                    f"{result.get('error') or 'UI-Fehler'} | {suffix}; "
                    "nächster Lauf versucht erneut"
                )
    return result


def run_task(job: auto.JobDef) -> bool:
    """Kompatibler Bool-Wrapper für bestehende Aufrufer."""
    return bool(run_task_result(job)["ok"])


def main() -> int:
    setup_logging("INFO")
    jobs = auto.load()
    active_due = [j.id for j in jobs if j.active and not j.is_running() and j.is_due()]
    if not active_due:
        log.info("Kein fälliger aktiver Job.")
        return 0
    hours_error = working_hours_error()
    if hours_error:
        log.info("%s %d fällige Job(s) bleiben vorgemerkt.", hours_error, len(active_due))
        return 0

    needs_browser = {
        "run-due", "analytics", "find-and-write", "find-and-write-reshares",
        "find-and-write-connections",
    }
    browser_ok: bool | None = None
    ran = 0
    failed = 0
    for job_id in active_due:
        candidate = next((job for job in jobs if job.id == job_id), None)
        if candidate is None:
            continue
        if candidate.task in needs_browser:
            if browser_ok is None:
                browser_ok = _health_ok()
            if not browser_ok:
                log.warning(
                    "Überspringe %s (%s): Browser/Login nicht bereit.",
                    candidate.id,
                    candidate.task,
                )
                continue
        # Noch einmal unter Dateisperre prüfen. So starten parallele Scheduler
        # denselben Job nicht doppelt und gelöschte/geänderte Jobs bleiben unberührt.
        job = auto.claim_job(job_id)
        if job is None:
            continue
        result = run_task_result(job)
        ok = bool(result["ok"])
        if ok:
            ran += 1
        else:
            failed += 1
        auto.finish_job(
            job.id,
            ok=ok,
            error=None if ok else str(result.get("error") or "Unbekannter Fehler"),
            expected_created=job.created,
        )
    log.info("%d/%d fällige Job(s) erfolgreich, %d fehlgeschlagen.", ran, len(active_due), failed)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
