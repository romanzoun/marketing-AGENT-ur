from __future__ import annotations

import base64
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import yaml

from linkedin_agents import jobs
from linkedin_agents import queue as q
from linkedin_agents.imaging.workflow import (
    image_prompt,
    quota_selects_next,
    score_allows_auto_image,
)
from linkedin_agents.models.campaign import Campaign
from linkedin_agents.web import app as web


class ImageQuotaTests(unittest.TestCase):
    def test_half_quota_alternates_new_posts(self) -> None:
        posts: list[q.QueueItem] = []
        decisions = []
        for number in range(4):
            selected = quota_selects_next(posts, 0.5)
            decisions.append(selected)
            posts.append(
                q.QueueItem(
                    id=f"post-{number}",
                    kind="post",
                    image_auto_selected=selected,
                )
            )
        self.assertEqual(decisions, [True, False, True, False])

    def test_auto_image_requires_score_strictly_above_85_percent(self) -> None:
        self.assertFalse(
            score_allows_auto_image(
                q.QueueItem(id="post-85", kind="post", evaluation_score=0.85)
            )
        )
        self.assertTrue(
            score_allows_auto_image(
                q.QueueItem(id="post-86", kind="post", evaluation_score=0.86)
            )
        )

    def test_image_prompt_contains_full_article_text(self) -> None:
        campaign = Campaign(
            name="Test", objective="Test", audience="Teams", voice="Klar"
        )
        text = "Erste Zeile.\n\nZweite Zeile mit vollständigem Kontext."
        prompt = image_prompt(
            campaign, q.QueueItem(id="post-1", kind="post", text=text)
        )
        self.assertIn(text, prompt)


class AutomaticImageTests(unittest.IsolatedAsyncioTestCase):
    async def test_job_add_applies_campaign_ratio(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign_path = root / "Kampagnen/test/kampagne.yaml"
            approvals = campaign_path.parent / "queue/approvals.md"
            schedule = campaign_path.parent / "queue/schedule.md"
            log = campaign_path.parent / "queue/log.md"
            campaign = Campaign(
                name="Test",
                version=3,
                objective="Test",
                audience="Teams",
                voice="Klar",
                images={"enabled": True, "ratio": 0.5, "style": "Editorial"},
            )
            args = SimpleNamespace(
                campaign=str(campaign_path), awareness=False, kind="post",
                text="Ein neuer Post", url=None, note="", publish_at=None,
            )

            async def generated(item, *_args, **_kwargs):
                item.image_path = ".runs/images/test.png"
                item.image_origin = "generated"
                return True

            def evaluated(_root, _campaign, items, target_ids, _scheduled):
                item = next(candidate for candidate in items if candidate.id in target_ids)
                item.evaluation_score = 0.91
                return [{"id": item.id, "score": 0.91}]

            with (
                patch.object(jobs, "_paths", return_value=(approvals, schedule, log)),
                patch.object(jobs, "load_campaign", return_value=campaign),
                patch.object(jobs, "load_settings", return_value=SimpleNamespace()),
                patch.object(jobs, "prepare_items", side_effect=evaluated),
                patch.object(jobs, "set_generated_image", side_effect=generated) as render,
            ):
                self.assertEqual(await jobs.job_add(args), 0)
                self.assertEqual(await jobs.job_add(args), 0)

            stored = q.parse(approvals)
            self.assertEqual(render.await_count, 1)
            self.assertEqual([item.image_auto_selected for item in stored], [True, False])
            self.assertTrue(all(item.campaign_version == 3 for item in stored))
            self.assertIsNotNone(stored[0].image_path)
            self.assertIsNone(stored[1].image_path)

    async def test_job_add_skips_api_image_at_or_below_score_threshold(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign_path = root / "Kampagnen/test/kampagne.yaml"
            approvals = campaign_path.parent / "queue/approvals.md"
            schedule = campaign_path.parent / "queue/schedule.md"
            log = campaign_path.parent / "queue/log.md"
            campaign = Campaign(
                name="Test",
                objective="Test",
                audience="Teams",
                voice="Klar",
                images={"enabled": True, "ratio": 1.0},
            )
            args = SimpleNamespace(
                campaign=str(campaign_path), awareness=False, kind="post",
                text="Ein Post mit mittlerem Score", url=None, note="", publish_at=None,
            )

            def evaluated(_root, _campaign, items, target_ids, _scheduled):
                item = next(candidate for candidate in items if candidate.id in target_ids)
                item.evaluation_score = 0.85
                return [{"id": item.id, "score": 0.85}]

            with (
                patch.object(jobs, "_paths", return_value=(approvals, schedule, log)),
                patch.object(jobs, "load_campaign", return_value=campaign),
                patch.object(jobs, "prepare_items", side_effect=evaluated),
                patch.object(jobs, "set_generated_image", new_callable=AsyncMock) as render,
            ):
                self.assertEqual(await jobs.job_add(args), 0)

            stored = q.parse(approvals)
            render.assert_not_awaited()
            self.assertFalse(stored[0].image_auto_selected)
            self.assertIsNone(stored[0].image_path)


class ImageApprovalApiTests(unittest.IsolatedAsyncioTestCase):
    async def test_generate_image_stays_in_approvals(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign_rel = "Kampagnen/test/kampagne.yaml"
            campaign_file = root / campaign_rel
            campaign_file.parent.mkdir(parents=True)
            campaign_file.write_text(
                yaml.safe_dump(
                    {
                        "name": "Test", "objective": "Test", "audience": "Teams",
                        "voice": "Klar", "images": {"enabled": True, "ratio": 0.5},
                    }
                ),
                encoding="utf-8",
            )
            approvals = campaign_file.parent / "queue/approvals.md"
            q.write(
                approvals,
                [q.QueueItem(id="post-1", kind="post", text="Mein Entwurf")],
                "Freigaben",
                "Test",
            )

            async def generated(item, *_args, **_kwargs):
                item.image_path = ".runs/images/post-1.png"
                item.image_source = "Bild: KI-generiert"
                item.image_origin = "generated"
                item.image_prompt = "Eigener Prompt"
                return True

            with (
                patch.object(web, "ROOT", root),
                patch.object(web, "load_settings", return_value=SimpleNamespace()),
                patch.object(web, "set_generated_image", side_effect=generated),
            ):
                result = await web.set_item_image(
                    "post-1",
                    web.ImageBody(
                        campaign=campaign_rel, source="generated", prompt="Eigener Prompt"
                    ),
                )

            stored = q.parse(approvals)
            self.assertTrue(result["ok"])
            self.assertEqual(len(stored), 1)
            self.assertEqual(stored[0].image_origin, "generated")

    async def test_upload_and_remove_image(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign_rel = "Kampagnen/test/kampagne.yaml"
            approvals = root / "Kampagnen/test/queue/approvals.md"
            q.write(
                approvals,
                [q.QueueItem(id="post-1", kind="post", text="Mein Entwurf")],
                "Freigaben",
                "Test",
            )
            png = b"\x89PNG\r\n\x1a\n" + b"testdata"
            body = web.ImageUploadBody(
                campaign=campaign_rel,
                filename="bild.png",
                content_type="image/png",
                data=base64.b64encode(png).decode(),
            )
            with patch.object(web, "ROOT", root):
                uploaded = web.upload_item_image("post-1", body)
                stored_path = root / uploaded["item"]["image_path"]
                self.assertTrue(stored_path.is_file())
                removed = web.delete_item_image("post-1", campaign_rel)

            self.assertTrue(removed["ok"])
            self.assertFalse(stored_path.exists())
            self.assertIsNone(q.parse(approvals)[0].image_path)


if __name__ == "__main__":
    unittest.main()
