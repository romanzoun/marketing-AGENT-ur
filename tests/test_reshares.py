from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import yaml
from fastapi import HTTPException

from linkedin_agents import jobs
from linkedin_agents import queue as q
from linkedin_agents.models.content import FeedPost
from linkedin_agents.web import app as web


class ReshareApprovalTests(unittest.TestCase):
    def _campaign(self, root: Path) -> tuple[str, Path]:
        rel = "Kampagnen/test/kampagne.yaml"
        path = root / rel
        path.parent.mkdir(parents=True)
        path.write_text(
            yaml.safe_dump(
                {
                    "name": "Test",
                    "objective": "Awareness",
                    "audience": "Fachleute",
                    "voice": "Persönlich",
                    "schedule": {"active_hours": [0, 24]},
                }
            ),
            encoding="utf-8",
        )
        return rel, path

    def test_empty_awareness_reshare_can_be_approved(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign, path = self._campaign(root)
            approvals = path.parent / "queue/approvals.md"
            q.write(
                approvals,
                [
                    q.QueueItem(
                        id="reshare-1",
                        kind="reshare",
                        text="",
                        url="https://www.linkedin.com/posts/example",
                        reshare_with_comment=False,
                    )
                ],
                "Freigaben",
                "Test",
            )
            with patch.object(web, "ROOT", root):
                result = web.approve_item("reshare-1", web.ApproveBody(campaign=campaign))

            scheduled = q.parse(path.parent / "queue/schedule.md")

        self.assertTrue(result["ok"])
        self.assertEqual(len(scheduled), 1)
        self.assertFalse(scheduled[0].reshare_with_comment)

    def test_empty_commentary_reshare_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign, path = self._campaign(root)
            q.write(
                path.parent / "queue/approvals.md",
                [q.QueueItem(id="reshare-1", kind="reshare", text="")],
                "Freigaben",
                "Test",
            )
            with patch.object(web, "ROOT", root):
                with self.assertRaises(HTTPException) as raised:
                    web.approve_item("reshare-1", web.ApproveBody(campaign=campaign))

        self.assertEqual(raised.exception.status_code, 400)


class ResharePublishingTests(unittest.IsolatedAsyncioTestCase):
    async def test_find_reshares_creates_campaign_candidates(self) -> None:
        collection_calls = []

        class FakeClient:
            def __init__(self, _endpoint: str) -> None:
                pass

            async def __aenter__(self):
                return self

            async def __aexit__(self, *_args):
                return None

            async def ensure_logged_in(self) -> bool:
                return True

            async def collect_feed(self, keywords, limit, with_urls):
                collection_calls.append((keywords, limit, with_urls))
                return [
                    FeedPost(
                        id="urn:li:activity:1",
                        author="Ada",
                        text="Feed post\nAda\nEin relevanter Beitrag über digitale Identität.",
                        url="https://www.linkedin.com/posts/relevant",
                    )
                ]

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign = root / "Kampagnen/test/kampagne.yaml"
            campaign.parent.mkdir(parents=True)
            campaign.write_text(
                yaml.safe_dump(
                    {
                        "name": "Test",
                        "objective": "Awareness",
                        "audience": "Fachleute",
                        "voice": "Persönlich",
                        "keywords_to_engage": ["digitale identität"],
                    }
                ),
                encoding="utf-8",
            )
            with (
                patch.object(jobs, "load_settings", return_value=SimpleNamespace(cdp_endpoint="x")),
                patch.object(jobs, "LinkedInClient", FakeClient),
            ):
                result = await jobs.job_find_reshares(
                    SimpleNamespace(campaign=str(campaign), limit=3)
                )

            candidates = q.parse(campaign.parent / "queue/approvals.md")

        self.assertEqual(result, 0)
        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0].kind, "reshare")
        self.assertTrue(candidates[0].reshare_with_comment)
        self.assertEqual(candidates[0].url, "https://www.linkedin.com/posts/relevant")
        self.assertEqual(collection_calls, [([], 3, True)])

    async def test_run_due_publishes_with_and_without_commentary(self) -> None:
        calls: list[tuple[str, str | None]] = []

        class FakeClient:
            def __init__(self, _endpoint: str) -> None:
                pass

            async def __aenter__(self):
                return self

            async def __aexit__(self, *_args):
                return None

            async def ensure_logged_in(self) -> bool:
                return True

            async def reshare_by_url(self, url: str, thoughts: str | None) -> bool:
                calls.append((url, thoughts))
                return True

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            approvals = root / "approvals.md"
            schedule = root / "schedule.md"
            log = root / "log.md"
            q.write(approvals, [], "Freigaben", "Test")
            q.write(
                schedule,
                [
                    q.QueueItem(
                        id="reshare-comment",
                        kind="reshare",
                        text="Meine Perspektive mit CTA.",
                        url="https://www.linkedin.com/posts/one",
                        publish_at="2020-01-01T09:00",
                    ),
                    q.QueueItem(
                        id="reshare-awareness",
                        kind="reshare",
                        text="Dieser Text wird nicht gesendet.",
                        url="https://www.linkedin.com/posts/two",
                        reshare_with_comment=False,
                        publish_at="2020-01-01T10:00",
                    ),
                ],
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
            history = q.parse(log)

        self.assertEqual(result, 0)
        self.assertEqual(
            calls,
            [
                ("https://www.linkedin.com/posts/one", "Meine Perspektive mit CTA."),
                ("https://www.linkedin.com/posts/two", None),
            ],
        )
        self.assertEqual(remaining, [])
        self.assertEqual(len(history), 2)


if __name__ == "__main__":
    unittest.main()
