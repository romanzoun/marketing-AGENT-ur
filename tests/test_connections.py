from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import yaml
from fastapi import HTTPException

from linkedin_agents import jobs
from linkedin_agents import queue as q
from linkedin_agents.automation import Frequency, JobDef
from linkedin_agents.auto_approval import approve_above_score
from linkedin_agents.browser.linkedin import LinkedInClient
from linkedin_agents.models.content import ProfileCandidate
from linkedin_agents.web import app as web


class ConnectionWorkflowTests(unittest.IsolatedAsyncioTestCase):
    def test_profile_name_drops_linkedin_connection_degree(self) -> None:
        self.assertEqual(
            LinkedInClient._clean_profile_name("Ibrahima Wague • 2nd\nCompliance Officer"),
            "Ibrahima Wague",
        )

    async def test_client_selects_only_marked_automation_tab(self) -> None:
        personal = MagicMock(url="https://www.linkedin.com/feed/")
        personal.evaluate = AsyncMock(return_value="")
        worker = MagicMock(url="https://www.linkedin.com/feed/")
        worker.evaluate = AsyncMock(return_value="linkedin-automation-worker")
        context = SimpleNamespace(pages=[personal, worker])

        selected = await LinkedInClient._pick_automation_page(context)

        self.assertIs(selected, worker)

    async def test_run_due_reports_failed_linkedin_action(self) -> None:
        class FakeClient:
            def __init__(self, _endpoint: str) -> None:
                pass

            async def __aenter__(self):
                return self

            async def __aexit__(self, *_args):
                return None

            async def ensure_logged_in(self) -> bool:
                return True

            async def create_post(self, _text: str, image_path=None) -> bool:
                return False

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            approvals = root / "approvals.md"
            schedule = root / "schedule.md"
            log = root / "log.md"
            q.write(approvals, [], "Freigaben", "Test")
            q.write(
                schedule,
                [q.QueueItem(
                    id="post-1",
                    kind="post",
                    text="Freigegebener Post",
                    publish_at="2020-01-01T09:00",
                )],
                "Planung",
                "Test",
            )
            with (
                patch.object(jobs, "_paths", return_value=(approvals, schedule, log)),
                patch.object(jobs, "load_settings", return_value=SimpleNamespace(cdp_endpoint="x")),
                patch.object(jobs, "LinkedInClient", FakeClient),
            ):
                result = await jobs.job_run_due(
                    SimpleNamespace(campaign="unused", dry_run=False)
                )

            remaining = q.parse(schedule)

        self.assertEqual(result, 1)
        self.assertEqual([item.id for item in remaining], ["post-1"])

    async def test_find_connections_adds_only_new_candidates_and_caps_limit(self) -> None:
        calls = []

        class FakeClient:
            def __init__(self, _endpoint: str) -> None:
                pass

            async def __aenter__(self):
                return self

            async def __aexit__(self, *_args):
                return None

            async def ensure_logged_in(self) -> bool:
                return True

            async def collect_people(self, query: str, limit: int):
                calls.append((query, limit))
                return [
                    ProfileCandidate(name="Ada", headline="CIO bei Beispiel", url="https://www.linkedin.com/in/ada/"),
                    ProfileCandidate(name="Bob", headline="CTO bei Beispiel", url="https://www.linkedin.com/in/bob/"),
                ]

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign = root / "Kampagnen/test/kampagne.yaml"
            campaign.parent.mkdir(parents=True)
            campaign.write_text(
                "name: Test\nobjective: Netzwerk\naudience: CIOs\nvoice: Persönlich\n",
                encoding="utf-8",
            )
            approvals = campaign.parent / "queue/approvals.md"
            q.write(
                approvals,
                [q.QueueItem(id="connection-old", kind="connection", url="https://www.linkedin.com/in/ada/")],
                "Freigaben",
                "Test",
            )
            with (
                patch.object(jobs, "load_settings", return_value=SimpleNamespace(cdp_endpoint="x")),
                patch.object(jobs, "LinkedInClient", FakeClient),
            ):
                result = await jobs.job_find_connections(
                    SimpleNamespace(campaign=str(campaign), query="CIO Dokumentenmanagement", limit=50)
                )
            candidates = q.parse(approvals)

        self.assertEqual(result, 0)
        self.assertEqual(calls, [("CIO Dokumentenmanagement", 5)])
        self.assertEqual([item.author for item in candidates], ["", "Bob"])

    async def test_run_due_sends_approved_connection_with_note(self) -> None:
        sent = []

        class FakeClient:
            def __init__(self, _endpoint: str) -> None:
                pass

            async def __aenter__(self):
                return self

            async def __aexit__(self, *_args):
                return None

            async def ensure_logged_in(self) -> bool:
                return True

            async def send_connection_by_url(self, url: str, note: str) -> bool:
                sent.append((url, note))
                return True

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            approvals = root / "approvals.md"
            schedule = root / "schedule.md"
            log = root / "log.md"
            q.write(approvals, [], "Freigaben", "Test")
            q.write(
                schedule,
                [q.QueueItem(
                    id="connection-1",
                    kind="connection",
                    text="Hallo Ada, ich würde mich gern vernetzen.",
                    url="https://www.linkedin.com/in/ada/",
                    publish_at="2020-01-01T09:00",
                )],
                "Planung",
                "Test",
            )
            with (
                patch.object(jobs, "_paths", return_value=(approvals, schedule, log)),
                patch.object(jobs, "load_settings", return_value=SimpleNamespace(cdp_endpoint="x")),
                patch.object(jobs, "LinkedInClient", FakeClient),
            ):
                result = await jobs.job_run_due(SimpleNamespace(campaign="unused", dry_run=False))

            self.assertEqual(result, 0)
            self.assertEqual(sent, [("https://www.linkedin.com/in/ada/", "Hallo Ada, ich würde mich gern vernetzen.")])
            self.assertEqual(q.parse(schedule), [])
            self.assertEqual(q.parse(log)[0].kind, "connection")

    async def test_browser_rejects_missing_or_oversized_note_before_navigation(self) -> None:
        client = LinkedInClient("http://localhost:9222")
        client._page = MagicMock()

        self.assertFalse(await client.send_connection_by_url("https://example.com", ""))
        self.assertFalse(await client.send_connection_by_url("https://example.com", "x" * 301))
        client.page.context.new_page.assert_not_called()

    async def test_run_due_respects_connection_daily_limit(self) -> None:
        sent = []

        class FakeClient:
            def __init__(self, _endpoint: str) -> None:
                pass

            async def __aenter__(self):
                return self

            async def __aexit__(self, *_args):
                return None

            async def ensure_logged_in(self) -> bool:
                return True

            async def send_connection_by_url(self, url: str, note: str) -> bool:
                sent.append(url)
                return True

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            approvals = root / "approvals.md"
            schedule = root / "schedule.md"
            log = root / "log.md"
            q.write(approvals, [], "Freigaben", "Test")
            q.write(
                log,
                [q.QueueItem(
                    id=f"sent-{index}", kind="connection", text="Notiz",
                    published_at=f"{jobs.datetime.now().date().isoformat()}T09:0{index}",
                ) for index in range(2)],
                "Log",
                "Test",
            )
            q.write(
                schedule,
                [q.QueueItem(
                    id=f"due-{index}", kind="connection", text="Notiz",
                    url=f"https://www.linkedin.com/in/person-{index}/",
                    publish_at="2020-01-01T09:00",
                ) for index in range(5)],
                "Planung",
                "Test",
            )
            with (
                patch.object(jobs, "_paths", return_value=(approvals, schedule, log)),
                patch.object(jobs, "load_settings", return_value=SimpleNamespace(cdp_endpoint="x")),
                patch.object(jobs, "LinkedInClient", FakeClient),
            ):
                result = await jobs.job_run_due(SimpleNamespace(campaign="unused", dry_run=False))

            remaining = q.parse(schedule)

        self.assertEqual(result, 0)
        self.assertEqual(len(sent), 3)
        self.assertEqual(len(remaining), 2)


class ConnectionApprovalTests(unittest.TestCase):
    def test_connection_job_type_is_available(self) -> None:
        job = JobDef(
            id="job-connection",
            task="find-and-write-connections",
            campaign="Kampagnen/test/kampagne.yaml",
            count=3,
            freq=Frequency(kind="daily", time="09:00"),
        )

        self.assertEqual(job.task, "find-and-write-connections")

    def test_manual_connection_task_rejects_more_than_five_people(self) -> None:
        with self.assertRaises(HTTPException) as raised:
            web.run_task(
                "find-and-write-connections",
                web.JobBody(campaign="Kampagnen/test/kampagne.yaml", count=6),
            )

        self.assertEqual(raised.exception.status_code, 422)

    def test_connection_is_never_bulk_auto_approved(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign = "Kampagnen/test/kampagne.yaml"
            campaign_file = root / campaign
            campaign_file.parent.mkdir(parents=True)
            campaign_file.write_text(
                "name: Test\nobjective: Netzwerk\naudience: CIOs\nvoice: Persönlich\n",
                encoding="utf-8",
            )
            approvals = campaign_file.parent / "queue/approvals.md"
            q.write(
                approvals,
                [q.QueueItem(
                    id="connection-1",
                    kind="connection",
                    text="Hallo Ada, ich würde mich gern vernetzen.",
                    evaluation_score=0.95,
                    fit_score=0.95,
                )],
                "Freigaben",
                "Test",
            )

            result = approve_above_score(root, campaign, 0.8)

        self.assertEqual(result["count"], 0)

    def test_connection_note_over_300_characters_is_rejected(self) -> None:
        item = q.QueueItem(
            id="connection-1", kind="connection", text="x" * 301,
            url="https://www.linkedin.com/in/ada/",
        )

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign = "Kampagnen/test/kampagne.yaml"
            path = root / campaign
            path.parent.mkdir(parents=True)
            path.write_text(
                yaml.safe_dump({"name": "Test", "objective": "Netzwerk", "audience": "CIOs", "voice": "Persönlich"}),
                encoding="utf-8",
            )
            q.write(path.parent / "queue/approvals.md", [item], "Freigaben", "Test")
            with patch.object(web, "ROOT", root):
                with self.assertRaises(HTTPException) as raised:
                    web.approve_item(item.id, web.ApproveBody(campaign=campaign))

        self.assertEqual(raised.exception.status_code, 400)


if __name__ == "__main__":
    unittest.main()