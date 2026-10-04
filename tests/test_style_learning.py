from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path

from linkedin_agents.models.campaign import Campaign
from linkedin_agents import queue as q
from linkedin_agents.auto_approval import apply_for_job, approve_above_score
from linkedin_agents.automation import Frequency, JobDef
from linkedin_agents.queue import QueueItem
from linkedin_agents.style_learning import (
    apply_learned_patterns,
    auto_approval_stats,
    evaluate_text,
    learn_approval,
    learn_edit,
    learn_rejection,
    learn_rewrite,
    job_trust,
    load_state,
    learning_status,
    prepare_items,
    score_threshold,
)


class StyleLearningTests(unittest.TestCase):
    def test_json_envelopes_are_removed_from_learning_history(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "team/style/learning.json"
            path.parent.mkdir(parents=True)
            path.write_text(
                json.dumps(
                    {
                        "edits": [{"before": '{"content_type":"post","text":"Klartext"}', "after": "Final"}],
                        "directives": [{"before": "Alt", "after": '{"text":"Klartext"}'}],
                    }
                ),
                encoding="utf-8",
            )

            state = load_state(root)

        self.assertEqual(state["edits"][0]["before"], "Klartext")
        self.assertEqual(state["directives"][0]["after"], "Klartext")

    def campaign(self) -> Campaign:
        return Campaign(
            name="Test",
            objective="Testen",
            audience="Fachleute",
            voice="Persönlich und klar",
            max_post_chars=500,
            max_comment_chars=300,
            schedule={"active_hours": [8, 18]},
        )

    def test_prepare_adds_score_original_and_time_suggestion(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            item = QueueItem(
                id="post-1",
                kind="post",
                text="Ich finde: Gute Automatisierung fühlt sich an wie ein ruhiger Kollege. Sie hilft, ohne großes Theater zu machen.",
            )
            prepared = prepare_items(
                root,
                self.campaign(),
                [item],
                {item.id},
                [],
                now=datetime(2026, 9, 10, 8, 0),
            )

        self.assertEqual(item.generated_text, item.text)
        self.assertIsNotNone(item.evaluation_score)
        self.assertEqual(item.publish_at, "2026-09-10T09:00")
        self.assertEqual(prepared[0]["id"], "post-1")

    def test_user_edit_becomes_reusable_pattern_only_after_approval(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            item = QueueItem(id="post-1", kind="post", text="Das ist ein echter Game Changer heute.")
            learn_edit(
                root,
                item,
                "Das ist ein echter Game Changer heute.",
                "Das ist heute wirklich hilfreich.",
            )
            pending, pending_applied = apply_learned_patterns(
                root, "Für Teams ist das ein echter Game Changer heute."
            )
            item.generated_text = item.text
            item.text = "Das ist heute wirklich hilfreich."
            learn_approval(root, item)
            revised, applied = apply_learned_patterns(
                root, "Für Teams ist das ein echter Game Changer heute."
            )

        self.assertEqual(pending, "Für Teams ist das ein echter Game Changer heute.")
        self.assertFalse(pending_applied)
        self.assertIn("wirklich hilfreich", revised)
        self.assertTrue(applied)

    def test_rejection_lowers_score_for_similar_future_text(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            text = "Ich nenne dieses Produkt einen revolutionären Game Changer für jedes Team."
            score_before, _ = evaluate_text(root, text, "post", 500)
            learn_rejection(
                root,
                QueueItem(id="post-no", kind="post", text=text, evaluation_score=score_before),
            )
            score_after, reasons = evaluate_text(root, text, "post", 500)

        self.assertLess(score_after, score_before)
        self.assertTrue(any("abgelehnten Beispielen" in reason for reason in reasons))

    def test_rejected_edit_does_not_become_active_pattern(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            before = "Das ist ein echter Game Changer heute."
            after = "Das ist heute wirklich hilfreich."
            item = QueueItem(id="post-no", kind="post", text=before, generated_text=before)
            learn_edit(root, item, before, after)
            item.text = after
            learn_rejection(root, item)
            revised, applied = apply_learned_patterns(
                root, "Für Teams ist das ein echter Game Changer heute."
            )

        self.assertEqual(revised, "Für Teams ist das ein echter Game Changer heute.")
        self.assertFalse(applied)

    def test_rewrite_instruction_becomes_preference_only_after_approval(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            item = QueueItem(
                id="post-rewrite", kind="post", text="Alter Entwurf", generated_text="Alter Entwurf"
            )
            item.text = "Persönlicher und kürzer."
            learn_rewrite(
                root,
                item,
                "Alter Entwurf",
                item.text,
                "Kürzer und persönlicher schreiben",
            )
            pending = load_state(root)
            learn_approval(root, item)
            approved = load_state(root)

        self.assertEqual(pending["directives"][0]["outcome"], "pending")
        self.assertEqual(pending["directive_preferences"], [])
        self.assertEqual(approved["directives"][0]["outcome"], "approved")
        self.assertEqual(
            approved["directive_preferences"][0]["instruction"],
            "Kürzer und persönlicher schreiben",
        )

    def test_approval_is_saved_as_strong_signal_and_corpus(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            item = QueueItem(id="comment-1", kind="comment", text="Für mich ist das der wichtige Punkt.")
            learn_approval(root, item)

            state = load_state(root)
            corpus = list((root / "team/style/approved").glob("*.md"))

        self.assertEqual(state["approvals"][0]["item_id"], "comment-1")
        self.assertEqual(len(corpus), 1)

    def test_user_memory_note_is_confirmed_with_approval(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            item = QueueItem(
                id="post-note",
                kind="post",
                text="Ein persönlicher Post.",
                user_memory_note="Diesen direkten Einstieg künftig öfter verwenden.",
            )
            learn_approval(root, item)
            state = load_state(root)
            status = learning_status(root)

        self.assertEqual(
            state["approvals"][0]["user_memory_note"],
            "Diesen direkten Einstieg künftig öfter verwenden.",
        )
        self.assertEqual(state["user_notes"][0]["outcome"], "approved")
        self.assertEqual(status["user_notes"], 1)

    def test_user_memory_note_is_negative_signal_with_rejection(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            item = QueueItem(
                id="post-no-note",
                kind="post",
                text="Ein zu werblicher Post.",
                user_memory_note="Zu werblich und zu wenig eigene Haltung.",
            )
            learn_rejection(root, item)
            state = load_state(root)

        self.assertEqual(
            state["rejections"][0]["user_memory_note"],
            "Zu werblich und zu wenig eigene Haltung.",
        )
        self.assertEqual(state["user_notes"][0]["outcome"], "rejected")

    def test_ten_unchanged_manual_approvals_unlock_job(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for index in range(10):
                text = f"Ich erkläre den Punkt persönlich und klar Nummer {index}."
                learn_approval(
                    root,
                    QueueItem(
                        id=f"post-{index}",
                        kind="post",
                        source_job_id="job-1",
                        text=text,
                        generated_text=text,
                        evaluation_score=0.50 + index * 0.05,
                    ),
                )

            trust = job_trust(root, "job-1")
            threshold = score_threshold(root, "job-1", 20)

        self.assertTrue(trust["unlocked"])
        self.assertEqual(trust["unchanged_streak"], 10)
        self.assertEqual(threshold, 0.9)

    def test_auto_approval_moves_only_new_item_above_percentile(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign_file = root / "Kampagnen/test/kampagne.yaml"
            campaign_file.parent.mkdir(parents=True)
            campaign_file.write_text(
                "name: Test\nobjective: Test\naudience: Test\nvoice: Klar\n",
                encoding="utf-8",
            )
            for index in range(10):
                text = f"Mein freigegebener Beispieltext Nummer {index}."
                learn_approval(
                    root,
                    QueueItem(
                        id=f"history-{index}",
                        kind="post",
                        source_job_id="job-1",
                        text=text,
                        generated_text=text,
                        evaluation_score=0.50 + index * 0.05,
                    ),
                )
            approvals = root / "Kampagnen/test/queue/approvals.md"
            schedule = root / "Kampagnen/test/queue/schedule.md"
            items = [
                QueueItem(
                    id="high",
                    kind="post",
                    source_job_id="job-1",
                    text="Hoher Score",
                    evaluation_score=0.92,
                    publish_at="2026-09-12T09:00",
                ),
                QueueItem(
                    id="low",
                    kind="post",
                    source_job_id="job-1",
                    text="Niedriger Score",
                    evaluation_score=0.70,
                    publish_at="2026-09-12T13:00",
                ),
            ]
            q.write(approvals, items, "Freigaben", "Test")
            q.write(schedule, [], "Planung", "Test")
            job = JobDef(
                id="job-1",
                task="draft-posts",
                campaign="Kampagnen/test/kampagne.yaml",
                approval_mode="top_20",
                freq=Frequency(kind="daily", time="09:00"),
            )

            result = apply_for_job(root, job, {"high", "low"})
            pending_ids = [item.id for item in q.parse(approvals)]
            scheduled_ids = [item.id for item in q.parse(schedule)]
            state = load_state(root)
            auto_stats = auto_approval_stats(root, "job-1")
            status = learning_status(root)

        self.assertEqual(result["approved"], ["high"])
        self.assertEqual(pending_ids, ["low"])
        self.assertEqual(scheduled_ids, ["high"])
        self.assertEqual(len(state["approvals"]), 10)
        self.assertEqual(state["auto_approvals"][0]["item_id"], "high")
        self.assertEqual(auto_stats["total"], 1)
        self.assertEqual(status["auto_approvals"], 1)

    def test_bulk_auto_approval_caps_four_per_weekday(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign = "Kampagnen/test/kampagne.yaml"
            campaign_file = root / campaign
            campaign_file.parent.mkdir(parents=True)
            campaign_file.write_text(
                "name: Test\nobjective: Test\naudience: Test\nvoice: Klar\n",
                encoding="utf-8",
            )
            approvals = campaign_file.parent / "queue/approvals.md"
            schedule = campaign_file.parent / "queue/schedule.md"
            q.write(
                approvals,
                [
                    QueueItem(
                        id=f"post-{index}", kind="post", text=f"Text {index}",
                        evaluation_score=0.9,
                    )
                    for index in range(9)
                ],
                "Freigaben",
                "Test",
            )

            result = approve_above_score(root, campaign, 0.8)
            scheduled = q.parse(schedule)
            auto_stats = auto_approval_stats(root)

        per_day: dict[str, int] = {}
        for item in scheduled:
            day = item.publish_at[:10]
            per_day[day] = per_day.get(day, 0) + 1
            self.assertLess(datetime.fromisoformat(item.publish_at).weekday(), 5)
            self.assertEqual(item.approval_origin, "automatic")
            self.assertEqual(item.auto_approval_threshold, 0.8)
        self.assertEqual(result["count"], 9)
        self.assertEqual(auto_stats["total"], 9)
        self.assertTrue(all(count <= 4 for count in per_day.values()))

    def test_low_campaign_fit_blocks_high_style_score(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign = "Kampagnen/test/kampagne.yaml"
            campaign_file = root / campaign
            campaign_file.parent.mkdir(parents=True)
            campaign_file.write_text(
                "name: Test\nobjective: Test\naudience: Test\nvoice: Klar\n",
                encoding="utf-8",
            )
            approvals = campaign_file.parent / "queue/approvals.md"
            q.write(
                approvals,
                [
                    QueueItem(
                        id="poor-fit",
                        kind="comment",
                        text="Gut formulierter Kommentar",
                        evaluation_score=0.95,
                        fit_score=0.2,
                    ),
                    QueueItem(
                        id="good-fit",
                        kind="comment",
                        text="Passender und gut formulierter Kommentar",
                        evaluation_score=0.9,
                        fit_score=0.85,
                    ),
                ],
                "Freigaben",
                "Test",
            )

            result = approve_above_score(root, campaign, 0.8)
            pending_ids = [item.id for item in q.parse(approvals)]

        self.assertEqual(result["approved"], ["good-fit"])
        self.assertEqual(pending_ids, ["poor-fit"])

    def test_legacy_auto_approval_events_initialize_counter(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "team/style/learning.json"
            path.parent.mkdir(parents=True)
            path.write_text(
                json.dumps({
                    "auto_approvals": [
                        {"item_id": "one", "source_job_id": "job-1", "mode": "top_20"},
                        {"item_id": "two", "source_job_id": "job-1", "mode": "top_20"},
                    ]
                }),
                encoding="utf-8",
            )

            stats = auto_approval_stats(root, "job-1")
            status = learning_status(root)

        self.assertEqual(stats["total"], 2)
        self.assertEqual(status["auto_approvals"], 2)

    def test_auto_daily_limit_is_shared_across_campaigns(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign = "Kampagnen/second/kampagne.yaml"
            campaign_file = root / campaign
            campaign_file.parent.mkdir(parents=True)
            campaign_file.write_text(
                "name: Second\nobjective: Test\naudience: Test\nvoice: Klar\n",
                encoding="utf-8",
            )
            day = datetime.now().date()
            while day.weekday() >= 5:
                day += timedelta(days=1)
            other_schedule = root / "Kampagnen/first/queue/schedule.md"
            q.write(
                other_schedule,
                [
                    QueueItem(
                        id=f"existing-{index}", kind="post", text="Schon automatisch",
                        approval_origin="automatic",
                        publish_at=f"{day.isoformat()}T{hour}",
                    )
                    for index, hour in enumerate(("09:00", "11:30", "14:00", "16:30"))
                ],
                "Planung",
                "Test",
            )
            approvals = campaign_file.parent / "queue/approvals.md"
            q.write(
                approvals,
                [QueueItem(id="new", kind="post", text="Neu", evaluation_score=0.95)],
                "Freigaben",
                "Test",
            )

            approve_above_score(root, campaign, 0.8)
            planned = q.parse(campaign_file.parent / "queue/schedule.md")[0]

        self.assertGreater(planned.publish_at[:10], day.isoformat())


if __name__ == "__main__":
    unittest.main()
