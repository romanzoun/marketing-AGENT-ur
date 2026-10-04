from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from linkedin_agents import analytics, jobs
from linkedin_agents import queue as q


class MetricParsingTests(unittest.TestCase):
    def test_extracts_english_and_compact_counts(self) -> None:
        values = analytics.extract_counts(
            "1,336 reactions 153 comments 1.2K reposts 12,345 impressions"
        )
        self.assertEqual(values["reactions"], 1336)
        self.assertEqual(values["comments"], 153)
        self.assertEqual(values["reposts"], 1200)
        self.assertEqual(values["impressions"], 12345)

    def test_comment_metrics_do_not_claim_source_post_reach(self) -> None:
        values = analytics.extract_counts(
            "5 Reaktionen 3 Antworten 900 Kommentare 20 Reposts", comment=True
        )
        self.assertEqual(values["reactions"], 5)
        self.assertEqual(values["replies"], 3)
        self.assertIsNone(values["comments"])
        self.assertIsNone(values["reposts"])
        self.assertIsNone(values["impressions"])


class AnalyticsStoreTests(unittest.TestCase):
    def test_historical_log_is_imported_and_snapshots_are_summarized(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            campaign = Path(directory) / "Kampagnen/test/kampagne.yaml"
            log = campaign.parent / "queue/log.md"
            q.write(
                log,
                [
                    q.QueueItem(
                        id="post-1",
                        kind="post",
                        campaign="Test",
                        campaign_version=4,
                        text="Mein Post",
                        published_url="https://www.linkedin.com/posts/me-1",
                        published_at="2026-09-14T12:00:00",
                    )
                ],
                "Log",
                "Test",
            )
            analytics.sync_log(campaign)
            analytics.add_snapshot(
                campaign,
                "post-1",
                {"reactions": 12, "comments": 3, "reposts": 2, "impressions": 800},
            )
            board = analytics.dashboard(campaign)

        self.assertEqual(board["summary"]["published"], 1)
        self.assertEqual(board["summary"]["reactions"], 12)
        self.assertEqual(board["summary"]["impressions"], 800)
        self.assertEqual(board["records"][0]["snapshot_count"], 1)
        self.assertEqual(board["records"][0]["campaign_version"], 4)


class AnalyticsJobTests(unittest.IsolatedAsyncioTestCase):
    async def test_job_measures_saved_own_post_url(self) -> None:
        class FakeClient:
            def __init__(self, _endpoint: str) -> None:
                pass

            async def __aenter__(self):
                return self

            async def __aexit__(self, *_args):
                return None

            async def ensure_logged_in(self) -> bool:
                return True

            async def get_engagement_metrics(self, url, kind, text):
                self.last = (url, kind, text)
                return {
                    "reactions": 9, "comments": 2, "replies": None,
                    "reposts": 1, "impressions": 500,
                }

        with tempfile.TemporaryDirectory() as directory:
            campaign = Path(directory) / "Kampagnen/test/kampagne.yaml"
            log = campaign.parent / "queue/log.md"
            q.write(
                log,
                [
                    q.QueueItem(
                        id="post-1", kind="post", campaign="Test", text="Posttext",
                        published_url="https://www.linkedin.com/posts/me-1",
                    )
                ],
                "Log",
                "Test",
            )
            with (
                patch.object(jobs, "load_settings", return_value=SimpleNamespace(cdp_endpoint="x")),
                patch.object(jobs, "LinkedInClient", FakeClient),
            ):
                result = await jobs.job_analytics(SimpleNamespace(campaign=str(campaign)))
            board = analytics.dashboard(campaign)

        self.assertEqual(result, 0)
        self.assertEqual(board["summary"]["measured"], 1)
        self.assertEqual(board["summary"]["reactions"], 9)


if __name__ == "__main__":
    unittest.main()
