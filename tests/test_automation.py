from __future__ import annotations

import unittest
import subprocess
import tempfile
from datetime import datetime, time, timedelta
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from pydantic import ValidationError

from linkedin_agents.automation import Frequency, JobDef, next_id, parse_human_frequency
from linkedin_agents import automation as auto
from linkedin_agents import scheduler


class HumanFrequencyTests(unittest.TestCase):
    def test_daily_phrase(self) -> None:
        frequency = parse_human_frequency("jeden Tag um 15 Uhr")
        self.assertEqual(frequency, Frequency(kind="daily", time="15:00"))
        self.assertEqual(frequency.human(), "Jeden Tag um 15:00 Uhr")

    def test_interval_phrases(self) -> None:
        self.assertEqual(parse_human_frequency("alle 30 Minuten").minutes, 30)
        self.assertEqual(parse_human_frequency("alle 2 Stunden").minutes, 120)
        self.assertEqual(parse_human_frequency("stündlich").human(), "Jede Stunde")

    def test_weekday_phrases(self) -> None:
        selected = parse_human_frequency("montags und mittwochs um 09:30")
        self.assertEqual(selected.weekdays, [1, 3])
        self.assertEqual(selected.human(), "Mo, Mi um 09:30 Uhr")

        workdays = parse_human_frequency("werktags um 9 Uhr")
        self.assertEqual(workdays.weekdays, [1, 2, 3, 4, 5])

    def test_ambiguous_phrase_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "Rhythmus nicht erkannt"):
            parse_human_frequency("irgendwann um 15 Uhr")

    def test_invalid_frequency_is_rejected(self) -> None:
        with self.assertRaises(ValidationError):
            Frequency(kind="daily", time="25:00")
        with self.assertRaises(ValidationError):
            Frequency(kind="interval", minutes=0)


class JobSchedulingTests(unittest.TestCase):
    def test_working_hours_are_start_inclusive_and_end_exclusive(self) -> None:
        settings = SimpleNamespace(
            working_hours_start=time(8, 0), working_hours_end=time(17, 0)
        )
        with patch.object(scheduler, "load_settings", return_value=settings):
            self.assertIsNone(scheduler.working_hours_error(datetime(2026, 9, 29, 8, 0)))
            self.assertIsNotNone(scheduler.working_hours_error(datetime(2026, 9, 29, 17, 0)))

    def test_scheduler_leaves_due_jobs_unclaimed_outside_working_hours(self) -> None:
        active = JobDef(
            id="job-0001",
            active=True,
            task="find-comments",
            campaign="x",
            freq=Frequency(kind="interval", minutes=5),
        )
        with (
            patch.object(scheduler.auto, "load", return_value=[active]),
            patch.object(scheduler, "working_hours_error", return_value="gesperrt"),
            patch.object(scheduler.auto, "claim_job") as claim,
            patch.object(scheduler, "run_task_result") as run_task,
        ):
            self.assertEqual(scheduler.main(), 0)

        claim.assert_not_called()
        run_task.assert_not_called()

    def test_task_runner_does_not_start_process_outside_working_hours(self) -> None:
        job = JobDef(
            id="job-0002",
            task="draft-posts",
            campaign="x",
            freq=Frequency(kind="interval", minutes=5),
        )
        with (
            patch.object(scheduler, "working_hours_error", return_value="gesperrt"),
            patch.object(scheduler.subprocess, "run") as run,
        ):
            result = scheduler.run_task_result(job)

        self.assertFalse(result["ok"])
        self.assertTrue(result["blocked"])
        run.assert_not_called()

    def test_finished_run_does_not_resurrect_a_deleted_job(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            jobs_file = root / "automation/jobs.yaml"
            lock_file = root / "automation/jobs.lock"
            job = JobDef(
                id="job-0001",
                task="draft-posts",
                campaign="x",
                freq=Frequency(kind="daily", time="15:00"),
            )
            with (
                patch.object(auto, "JOBS_FILE", jobs_file),
                patch.object(auto, "JOBS_LOCK", lock_file),
            ):
                auto.save([job])
                auto.mutate(lambda jobs: jobs.clear())
                finished = auto.finish_job(job.id, ok=True)

                self.assertIsNone(finished)
                self.assertEqual(auto.load(), [])

    def test_finished_run_preserves_a_changed_schedule(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            jobs_file = root / "automation/jobs.yaml"
            lock_file = root / "automation/jobs.lock"
            job = JobDef(
                id="job-0001",
                task="draft-posts",
                campaign="x",
                freq=Frequency(kind="daily", time="15:00"),
            )
            with (
                patch.object(auto, "JOBS_FILE", jobs_file),
                patch.object(auto, "JOBS_LOCK", lock_file),
            ):
                auto.save([job])

                def move_to_eleven(jobs):
                    jobs[0].freq = Frequency(kind="daily", time="11:00")

                auto.mutate(move_to_eleven)
                auto.finish_job(job.id, ok=True)
                stored = auto.load()[0]

                self.assertEqual(stored.freq.time, "11:00")
                self.assertEqual(stored.last_status, "ok")

    def test_finished_run_does_not_touch_recreated_job_with_same_id(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            jobs_file = root / "automation/jobs.yaml"
            lock_file = root / "automation/jobs.lock"
            old = JobDef(
                id="job-0007",
                task="draft-posts",
                campaign="x",
                created="2026-09-16T10:00",
                freq=Frequency(kind="daily", time="15:00"),
            )
            replacement = JobDef(
                id="job-0007",
                task="draft-posts",
                campaign="x",
                created="2026-09-16T13:00",
                freq=Frequency(kind="daily", time="11:00"),
            )
            with (
                patch.object(auto, "JOBS_FILE", jobs_file),
                patch.object(auto, "JOBS_LOCK", lock_file),
            ):
                auto.save([replacement])
                finished = auto.finish_job(
                    old.id, ok=True, expected_created=old.created
                )
                stored = auto.load()[0]

                self.assertIsNone(finished)
                self.assertIsNone(stored.last_status)
                self.assertEqual(stored.freq.time, "11:00")

    def test_runner_passes_job_id_to_content_process(self) -> None:
        job = JobDef(
            id="job-0042",
            task="draft-posts",
            campaign="x",
            freq=Frequency(kind="interval", minutes=5),
        )
        completed = subprocess.CompletedProcess([], 0, stdout="{}", stderr="")
        with patch.object(scheduler.subprocess, "run", return_value=completed) as run:
            result = scheduler.run_task_result(job)

        self.assertTrue(result["ok"])
        self.assertEqual(run.call_args.kwargs["env"]["LI_JOB_ID"], "job-0042")

    def test_runner_reports_configured_timeout_cleanly(self) -> None:
        job = JobDef(
            id="job-0043",
            task="ideas-to-posts",
            campaign="x",
            count=1,
            freq=Frequency(kind="interval", minutes=5),
        )
        expired = subprocess.TimeoutExpired(
            cmd=["li-brain"], timeout=3000, output=b"teilweise", stderr=b"zu langsam"
        )
        with patch.object(scheduler.subprocess, "run", side_effect=expired):
            result = scheduler.run_task_result(job)

        self.assertFalse(result["ok"])
        self.assertIn("Zeitlimit", result["error"])
        self.assertEqual(result["stdout"], "teilweise")

    def test_scheduler_prefers_structured_error_over_agent_summary(self) -> None:
        stdout = (
            '{"ok": false, "error": "Keine Kommentar-Entwürfe erzeugt", '
            '"stdout": "Es wurde nichts angekreuzt oder veröffentlicht."}'
        )

        message = scheduler._failure_message(stdout, "")

        self.assertEqual(message, "Keine Kommentar-Entwürfe erzeugt")

    def test_linkedin_locator_failure_starts_codex_repair_once_per_cooldown(self) -> None:
        job = JobDef(
            id="job-ui",
            task="run-due",
            campaign="Kampagnen/test/kampagne.yaml",
            freq=Frequency(kind="interval", minutes=5),
        )
        result = {
            "ok": False,
            "error": "LinkedIn-Aktion fehlgeschlagen",
            "stderr": "Locator.wait_for: Timeout 8000ms exceeded",
            "stdout": "",
        }
        with tempfile.TemporaryDirectory() as directory:
            with (
                patch.object(scheduler, "UI_REPAIR_STATE", Path(directory) / "repair.json"),
                patch.object(
                    scheduler.brain,
                    "run_code_repair",
                    return_value={"ok": True, "stdout": "repaired", "stderr": ""},
                ) as repair,
            ):
                first = scheduler._maybe_repair_linkedin_ui(job, result)
                second = scheduler._maybe_repair_linkedin_ui(job, result)

        self.assertTrue(first["ok"])
        self.assertEqual(second["skipped"], "cooldown")
        repair.assert_called_once()

    def test_content_failure_does_not_start_ui_repair(self) -> None:
        job = JobDef(
            id="job-content",
            task="draft-posts",
            campaign="Kampagnen/test/kampagne.yaml",
            freq=Frequency(kind="interval", minutes=5),
        )
        result = {"ok": False, "error": "Keine Entwürfe erzeugt", "stderr": ""}

        with patch.object(scheduler.brain, "run_code_repair") as repair:
            self.assertIsNone(scheduler._maybe_repair_linkedin_ui(job, result))

        repair.assert_not_called()

    def test_browser_process_timeout_does_not_start_ui_repair(self) -> None:
        job = JobDef(
            id="job-timeout",
            task="run-due",
            campaign="Kampagnen/test/kampagne.yaml",
            freq=Frequency(kind="interval", minutes=5),
        )
        result = {
            "ok": False,
            "error": "Zeitlimit von 20 Minuten überschritten",
            "stderr": "",
            "stdout": "",
        }

        with patch.object(scheduler.brain, "run_code_repair") as repair:
            self.assertIsNone(scheduler._maybe_repair_linkedin_ui(job, result))

        repair.assert_not_called()

    def test_connection_selector_mismatch_starts_ui_repair(self) -> None:
        job = JobDef(
            id="job-connections",
            task="find-and-write-connections",
            campaign="Kampagnen/test/kampagne.yaml",
            freq=Frequency(kind="daily", time="11:00"),
        )
        result = {
            "ok": False,
            "error": "linkedin_ui_selector_mismatch: profile links visible",
            "stderr": "",
            "stdout": "",
        }

        self.assertTrue(scheduler._looks_like_linkedin_ui_failure(job, result))

    def test_manual_runner_attaches_connection_ui_repair(self) -> None:
        job = JobDef(
            id="job-connections",
            task="find-and-write-connections",
            campaign="Kampagnen/test/kampagne.yaml",
            freq=Frequency(kind="daily", time="11:00"),
        )
        completed = subprocess.CompletedProcess(
            [],
            1,
            stdout='{"ok": false, "error": "linkedin_ui_selector_mismatch"}',
            stderr="",
        )
        with (
            patch.object(scheduler.subprocess, "run", return_value=completed),
            patch.object(
                scheduler,
                "_maybe_repair_linkedin_ui",
                return_value={"ok": True, "fingerprint": "abc"},
            ) as repair,
        ):
            result = scheduler.run_task_result(job)

        repair.assert_called_once()
        self.assertTrue(result["ui_repair"]["ok"])
        self.assertIn("Codex-Reparatur abgeschlossen", result["error"])

    def test_daily_job_runs_only_once_per_slot(self) -> None:
        job = JobDef(
            id="job-0001",
            task="run-due",
            campaign="Kampagnen/example_campaign.yaml",
            freq=Frequency(kind="daily", time="15:00"),
        )
        self.assertFalse(job.is_due(datetime(2026, 9, 10, 14, 59)))
        self.assertTrue(job.is_due(datetime(2026, 9, 10, 15, 5)))

        job.last_run = "2026-09-10T15:01"
        self.assertFalse(job.is_due(datetime(2026, 9, 10, 15, 5)))

    def test_deleted_job_id_is_not_reused(self) -> None:
        jobs = [
            JobDef(
                id="job-0001",
                task="run-due",
                campaign="x",
                freq=Frequency(kind="interval", minutes=5),
            ),
            JobDef(
                id="job-0003",
                task="run-due",
                campaign="x",
                freq=Frequency(kind="interval", minutes=5),
            ),
        ]
        self.assertEqual(next_id(jobs), "job-0004")

    def test_scheduler_executes_only_active_due_jobs(self) -> None:
        active = JobDef(
            id="job-0001",
            active=True,
            task="find-comments",
            campaign="x",
            freq=Frequency(kind="interval", minutes=5),
        )
        inactive = JobDef(
            id="job-0002",
            active=False,
            task="find-comments",
            campaign="x",
            freq=Frequency(kind="interval", minutes=5),
        )
        with (
            patch.object(scheduler.auto, "load", return_value=[active, inactive]),
            patch.object(scheduler.auto, "claim_job", return_value=active),
            patch.object(scheduler.auto, "finish_job") as finish,
            patch.object(
                scheduler, "run_task_result", return_value={"ok": True, "error": None}
            ) as run_task,
        ):
            self.assertEqual(scheduler.main(), 0)

        run_task.assert_called_once_with(active)
        finish.assert_called_once_with(
            active.id, ok=True, error=None, expected_created=active.created
        )

    def test_scheduler_skips_job_that_is_already_running(self) -> None:
        running = JobDef(
            id="job-0001",
            active=True,
            task="draft-posts",
            campaign="x",
            freq=Frequency(kind="interval", minutes=5),
            last_attempt=datetime.now().isoformat(timespec="minutes"),
            last_status="running",
        )
        with (
            patch.object(scheduler.auto, "load", return_value=[running]),
            patch.object(scheduler, "run_task_result") as run_task,
        ):
            self.assertEqual(scheduler.main(), 0)

        run_task.assert_not_called()

    def test_old_running_state_expires_after_job_timeout_buffer(self) -> None:
        attempted = datetime(2026, 9, 15, 20, 0)
        job = JobDef(
            id="job-0001",
            active=True,
            task="draft-posts",
            campaign="x",
            freq=Frequency(kind="interval", minutes=5),
            last_attempt="2026-09-15T20:00",
            last_status="running",
        )
        configured = scheduler.timeouts.process_seconds(scheduler.ROOT, job.task, job.count) // 60 + 5
        lock_minutes = max(55, configured)
        self.assertTrue(job.is_running(attempted + timedelta(minutes=lock_minutes)))
        self.assertFalse(job.is_running(attempted + timedelta(minutes=lock_minutes + 1)))

    def test_failed_scheduler_job_is_not_marked_as_run(self) -> None:
        active = JobDef(
            id="job-0001",
            active=True,
            task="draft-posts",
            campaign="x",
            freq=Frequency(kind="interval", minutes=5),
        )
        with (
            patch.object(scheduler.auto, "load", return_value=[active]),
            patch.object(scheduler.auto, "claim_job", return_value=active),
            patch.object(scheduler.auto, "finish_job") as finish,
            patch.object(
                scheduler, "run_task_result", return_value={"ok": False, "error": "quota"}
            ),
        ):
            self.assertEqual(scheduler.main(), 1)
        finish.assert_called_once_with(
            active.id, ok=False, error="quota", expected_created=active.created
        )


if __name__ == "__main__":
    unittest.main()
