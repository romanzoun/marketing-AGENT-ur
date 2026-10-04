from __future__ import annotations

import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import yaml
from fastapi import HTTPException

from linkedin_agents.automation import Frequency, JobDef
from linkedin_agents import queue as q
from linkedin_agents.style_learning import load_state
from linkedin_agents.web import app as web


class ApprovalWorkflowTests(unittest.TestCase):
    def test_schedule_duplicate_id_can_be_updated_individually(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign = "Kampagnen/test/kampagne.yaml"
            schedule = root / "Kampagnen/test/queue/schedule.md"
            q.write(
                schedule,
                [
                    q.QueueItem(id="duplicate", kind="post", text="Erster", publish_at="2026-09-24T09:00"),
                    q.QueueItem(id="duplicate", kind="post", text="Zweiter", publish_at="2026-09-25T09:00"),
                ],
                "Planung",
                "Test",
            )

            with patch.object(web, "ROOT", root):
                web.patch_item(
                    "duplicate",
                    web.ItemPatch(
                        campaign=campaign,
                        stage="schedule",
                        publish_at="2026-09-26T10:00",
                        match_publish_at="2026-09-25T09:00",
                    ),
                )

            updated = q.parse(schedule)

        self.assertEqual([item.publish_at for item in updated], ["2026-09-24T09:00", "2026-09-26T10:00"])

    def test_approval_moves_item_directly_to_schedule(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign_rel = "Kampagnen/test/kampagne.yaml"
            campaign_file = root / campaign_rel
            campaign_file.parent.mkdir(parents=True)
            campaign_file.write_text(
                yaml.safe_dump(
                    {
                        "name": "Test",
                        "objective": "Testen",
                        "audience": "Tester",
                        "voice": "Klar",
                        "schedule": {"active_hours": [0, 24]},
                    }
                ),
                encoding="utf-8",
            )
            approvals = campaign_file.parent / "queue" / "approvals.md"
            q.write(
                approvals,
                [q.QueueItem(id="post-1", kind="post", text="Freigegebener Text")],
                "Freigaben",
                "Test",
            )

            with patch.object(web, "ROOT", root):
                result = web.approve_item("post-1", web.ApproveBody(campaign=campaign_rel))

            schedule = campaign_file.parent / "queue" / "schedule.md"
            self.assertTrue(result["ok"])
            self.assertEqual(q.parse(approvals), [])
            scheduled = q.parse(schedule)
            self.assertEqual(len(scheduled), 1)
            self.assertTrue(scheduled[0].approved)
            self.assertIsNotNone(scheduled[0].publish_at)

    def test_manual_approval_can_exceed_four_on_same_day(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign_rel = "Kampagnen/test/kampagne.yaml"
            campaign_file = root / campaign_rel
            campaign_file.parent.mkdir(parents=True)
            campaign_file.write_text(
                "name: Test\nobjective: Test\naudience: Test\nvoice: Klar\n",
                encoding="utf-8",
            )
            approvals = campaign_file.parent / "queue/approvals.md"
            q.write(
                approvals,
                [q.QueueItem(id=f"post-{index}", kind="post", text=f"Text {index}") for index in range(5)],
                "Freigaben",
                "Test",
            )

            with patch.object(web, "ROOT", root):
                for index in range(5):
                    web.approve_item(
                        f"post-{index}",
                        web.ApproveBody(
                            campaign=campaign_rel,
                            publish_at=f"2026-09-18T{9 + index:02d}:00",
                        ),
                    )

            scheduled = q.parse(campaign_file.parent / "queue/schedule.md")

        self.assertEqual(len(scheduled), 5)
        self.assertTrue(all(item.approval_origin == "manual" for item in scheduled))

    def test_deleting_approval_is_learned_as_rejection(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign_rel = "Kampagnen/test/kampagne.yaml"
            approvals = root / "Kampagnen/test/queue/approvals.md"
            q.write(
                approvals,
                [q.QueueItem(id="post-no", kind="post", text="Diesen Entwurf möchte ich nicht.")],
                "Freigaben",
                "Test",
            )

            with patch.object(web, "ROOT", root):
                result = web.delete_item("post-no", campaign_rel, "approvals")

            state = load_state(root)

        self.assertTrue(result["learned_as_rejection"])
        self.assertEqual(q.parse(approvals), [])
        self.assertEqual(state["rejections"][0]["item_id"], "post-no")

    def test_learning_note_is_saved_on_item_and_confirmed_on_approval(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign_rel = "Kampagnen/test/kampagne.yaml"
            campaign_file = root / campaign_rel
            campaign_file.parent.mkdir(parents=True)
            campaign_file.write_text(
                "name: Test\nobjective: Test\naudience: Test\nvoice: Klar\n",
                encoding="utf-8",
            )
            approvals = campaign_file.parent / "queue/approvals.md"
            q.write(
                approvals,
                [q.QueueItem(id="post-note", kind="post", text="Mein Text")],
                "Freigaben",
                "Test",
            )

            with patch.object(web, "ROOT", root):
                patched = web.patch_item(
                    "post-note",
                    web.ItemPatch(
                        campaign=campaign_rel,
                        stage="approvals",
                        user_memory_note="Mehr solche kurzen Einstiege.",
                    ),
                )
                web.approve_item(
                    "post-note",
                    web.ApproveBody(campaign=campaign_rel),
                )

            scheduled = q.parse(campaign_file.parent / "queue/schedule.md")
            state = load_state(root)

        self.assertEqual(
            patched["item"]["user_memory_note"], "Mehr solche kurzen Einstiege."
        )
        self.assertEqual(scheduled[0].user_memory_note, "Mehr solche kurzen Einstiege.")
        self.assertEqual(state["user_notes"][0]["outcome"], "approved")

    def test_directed_rewrite_stays_in_approvals_and_is_reevaluated(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign_rel = "Kampagnen/test/kampagne.yaml"
            campaign_file = root / campaign_rel
            campaign_file.parent.mkdir(parents=True)
            campaign_file.write_text(
                yaml.safe_dump(
                    {
                        "name": "Test",
                        "objective": "Testen",
                        "audience": "Tester",
                        "voice": "Klar",
                        "schedule": {"active_hours": [0, 24]},
                    }
                ),
                encoding="utf-8",
            )
            approvals = campaign_file.parent / "queue" / "approvals.md"
            q.write(
                approvals,
                [q.QueueItem(id="post-r", kind="post", text="Alter Entwurf")],
                "Freigaben",
                "Test",
            )

            with (
                patch.object(web, "ROOT", root),
                patch.object(
                    web.brain,
                    "rewrite_draft",
                    return_value={"ok": True, "engine": "codex", "text": "Ich schreibe jetzt persönlicher und klarer."},
                ),
            ):
                result = web.rewrite_item(
                    "post-r",
                    web.RewriteBody(campaign=campaign_rel, instruction="Persönlicher schreiben"),
                )

            stored = q.parse(approvals)
            state = load_state(root)

        self.assertTrue(result["ok"])
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0].text, "Ich schreibe jetzt persönlicher und klarer.")
        self.assertIsNotNone(stored[0].evaluation_score)
        self.assertEqual(state["directives"][0]["outcome"], "pending")


class SourcePostWorkflowTests(unittest.IsolatedAsyncioTestCase):
    async def test_refresh_source_stores_full_linkedin_post(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign = "Kampagnen/test/kampagne.yaml"
            approvals = root / "Kampagnen/test/queue/approvals.md"
            q.write(
                approvals,
                [
                    q.QueueItem(
                        id="comment-1",
                        kind="comment",
                        text="Mein Kommentar",
                        note="abgeschnitten",
                        url="https://www.linkedin.com/feed/update/urn:test",
                    )
                ],
                "Freigaben",
                "Test",
            )
            with (
                patch.object(web, "ROOT", root),
                patch.object(web, "load_settings", return_value=SimpleNamespace(cdp_endpoint="x")),
                patch.object(
                    web,
                    "_post_via_direct_cdp",
                    AsyncMock(
                        return_value={
                            "author": "Ada Beispiel",
                            "text": "Vollständiger Originalbeitrag\nmit allen Absätzen und Details.",
                            "url": "https://www.linkedin.com/feed/update/urn:test",
                        }
                    ),
                ),
            ):
                result = await web.refresh_item_source(
                    "comment-1", web.CampaignRef(campaign=campaign)
                )

            stored = q.parse(approvals)[0]

        self.assertTrue(result["ok"])
        self.assertEqual(stored.author, "Ada Beispiel")
        self.assertEqual(
            stored.note, "Vollständiger Originalbeitrag\nmit allen Absätzen und Details."
        )


class JobEndpointTests(unittest.TestCase):
    def test_job_campaign_can_be_changed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign_path = root / "Kampagnen/neu/kampagne.yaml"
            campaign_path.parent.mkdir(parents=True)
            campaign_path.write_text(
                "name: Neu\nobjective: Test\naudience: Test\nvoice: Klar\n",
                encoding="utf-8",
            )
            job = JobDef(
                id="job-0001",
                task="draft-posts",
                campaign="Kampagnen/alt/kampagne.yaml",
                freq=Frequency(kind="interval", minutes=5),
            )

            def mutate(change):
                return change([job])

            with (
                patch.object(web, "ROOT", root),
                patch.object(web.auto, "mutate", side_effect=mutate),
            ):
                result = web.patch_jobdef(
                    job.id,
                    web.JobDefPatch(campaign="Kampagnen/neu/kampagne.yaml"),
                )

        self.assertTrue(result["ok"])
        self.assertEqual(job.campaign, "Kampagnen/neu/kampagne.yaml")

    def test_auto_approval_mode_stays_locked_before_ten_unchanged_approvals(self) -> None:
        job = JobDef(
            id="job-0001",
            active=True,
            task="draft-posts",
            campaign="x",
            freq=Frequency(kind="interval", minutes=5),
        )
        def mutate(change):
            return change([job])

        with (
            patch.object(web.auto, "mutate", side_effect=mutate),
            patch.object(web, "job_trust", return_value={"unlocked": False, "unchanged_streak": 9}),
        ):
            with self.assertRaises(HTTPException) as raised:
                web.patch_jobdef(
                    job.id, web.JobDefPatch(approval_mode="top_20")
                )
        self.assertEqual(raised.exception.status_code, 409)
        self.assertEqual(job.approval_mode, "manual")

    def test_unlocked_job_can_select_top_five_percent(self) -> None:
        job = JobDef(
            id="job-0001",
            active=True,
            task="draft-posts",
            campaign="x",
            freq=Frequency(kind="interval", minutes=5),
        )
        def mutate(change):
            return change([job])

        with (
            patch.object(web.auto, "mutate", side_effect=mutate),
            patch.object(web, "job_trust", return_value={"unlocked": True, "unchanged_streak": 10}),
        ):
            result = web.patch_jobdef(
                job.id, web.JobDefPatch(approval_mode="top_5")
            )
        self.assertTrue(result["ok"])
        self.assertEqual(job.approval_mode, "top_5")

    def test_run_now_rejects_inactive_job(self) -> None:
        inactive = JobDef(
            id="job-0001",
            active=False,
            task="find-comments",
            campaign="x",
            freq=Frequency(kind="interval", minutes=5),
        )
        with patch.object(web.auto, "load", return_value=[inactive]):
            with self.assertRaises(HTTPException) as raised:
                web.run_jobdef_now(inactive.id)
        self.assertEqual(raised.exception.status_code, 409)

    def test_run_now_rejects_job_that_is_already_running(self) -> None:
        running = JobDef(
            id="job-0001",
            active=True,
            task="draft-posts",
            campaign="x",
            freq=Frequency(kind="interval", minutes=5),
            last_attempt=datetime.now().isoformat(timespec="minutes"),
            last_status="running",
        )
        with patch.object(web.auto, "load", return_value=[running]):
            with self.assertRaises(HTTPException) as raised:
                web.run_jobdef_now(running.id)
        self.assertEqual(raised.exception.status_code, 409)
        self.assertIn("läuft bereits", str(raised.exception.detail))

    def test_run_now_rejects_job_outside_working_hours_before_claim(self) -> None:
        active = JobDef(
            id="job-0001",
            active=True,
            task="draft-posts",
            campaign="x",
            freq=Frequency(kind="interval", minutes=5),
        )
        with (
            patch.object(web.auto, "load", return_value=[active]),
            patch.object(web.auto, "claim_job") as claim,
            patch(
                "linkedin_agents.scheduler.working_hours_error",
                return_value="Jobs sind außerhalb der Arbeitszeiten gesperrt (08:00–17:00).",
            ),
        ):
            with self.assertRaises(HTTPException) as raised:
                web.run_jobdef_now(active.id)

        self.assertEqual(raised.exception.status_code, 409)
        claim.assert_not_called()

    def test_failed_run_now_does_not_mark_job_as_run(self) -> None:
        active = JobDef(
            id="job-0001",
            active=True,
            task="draft-posts",
            campaign="x",
            freq=Frequency(kind="interval", minutes=5),
        )
        with (
            patch.object(web.auto, "load", return_value=[active]),
            patch.object(web.auto, "claim_job", return_value=active),
            patch.object(web.auto, "finish_job") as finish,
            patch(
                "linkedin_agents.scheduler.working_hours_error", return_value=None
            ),
            patch(
                "linkedin_agents.scheduler.run_task_result",
                return_value={"ok": False, "error": "quota", "stdout": "", "stderr": ""},
            ),
        ):
            result = web.run_jobdef_now(active.id)

        self.assertFalse(result["ok"])
        self.assertIsNone(active.last_run)
        finish.assert_called_once_with(
            active.id, ok=False, error="quota", expected_created=active.created
        )


class HealthEndpointTests(unittest.TestCase):
    def test_active_health_combines_linkedin_and_cli_probe(self) -> None:
        passive = {"cdp": True, "logged_in": True, "brain_cli": "codex"}
        probe = {"ok": True, "engine": "codex", "answer": "HEALTH_OK"}
        with (
            patch.object(web, "_health_data", return_value=passive),
            patch.object(web.brain, "probe_cli", return_value=probe),
        ):
            result = web.active_health_check("requested")

        self.assertTrue(result["overall_ok"])
        self.assertEqual(result["probe"], probe)


if __name__ == "__main__":
    unittest.main()
