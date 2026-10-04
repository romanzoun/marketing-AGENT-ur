from __future__ import annotations

import random
import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

from linkedin_agents import planning
from linkedin_agents import queue as q
from linkedin_agents.web import app as web


class PlanningTests(unittest.TestCase):
    def test_settings_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            planning.save(root, planning.PlanningSettings(days_ahead=21, sunday_start="17:00"))
            loaded = planning.load(root)

            self.assertEqual(loaded.days_ahead, 21)
            self.assertEqual(loaded.sunday_start, "17:00")

    def test_suggestion_uses_a_least_busy_day_and_its_window(self) -> None:
        settings = planning.PlanningSettings(days_ahead=2)
        now = datetime(2026, 9, 21, 8, 0)  # Montag
        scheduled = ["2026-09-21T09:00", "2026-09-21T13:00", "2026-09-22T10:00"]

        result = planning.suggest(settings, scheduled, now=now, rng=random.Random(3))

        self.assertEqual(result.date().isoformat(), "2026-09-23")
        self.assertGreaterEqual(result.strftime("%H:%M"), "09:00")
        self.assertLessEqual(result.strftime("%H:%M"), "16:00")

    def test_weekend_windows_are_used(self) -> None:
        settings = planning.PlanningSettings(days_ahead=1)

        saturday = planning.suggest(
            settings, ["2026-09-27T16:00"], now=datetime(2026, 9, 26, 8), rng=random.Random(1)
        )
        sunday = planning.suggest(
            settings, ["2026-09-28T09:00"], now=datetime(2026, 9, 27, 8), rng=random.Random(1)
        )

        self.assertGreaterEqual(saturday.strftime("%H:%M"), "09:00")
        self.assertLessEqual(saturday.strftime("%H:%M"), "13:00")
        self.assertGreaterEqual(sunday.strftime("%H:%M"), "16:00")
        self.assertLessEqual(sunday.strftime("%H:%M"), "20:00")

    def test_web_configuration_round_trip_and_suggestion(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign = "Kampagnen/test/kampagne.yaml"
            q.write(
                root / "Kampagnen/test/queue/schedule.md",
                [q.QueueItem(id="post-1", kind="post", text="Text", publish_at="2026-09-23T09:00")],
                "Planung",
                "Test",
            )
            configured = planning.PlanningSettings(days_ahead=7, saturday_end="12:00")
            with (
                patch.object(web, "ROOT", root),
                patch.object(planning, "suggest", return_value=datetime(2026, 9, 24, 11, 37)),
            ):
                saved = web.put_planning_settings(configured)
                visible = web.get_planning_settings()
                suggestion = web.planning_suggestion(campaign)

        self.assertTrue(saved["ok"])
        self.assertEqual(visible["days_ahead"], 7)
        self.assertEqual(suggestion, {"publish_at": "2026-09-24T11:37", "day_load": 0})

    def test_suggestion_never_reuses_an_occupied_minute(self) -> None:
        settings = planning.PlanningSettings(
            days_ahead=1,
            weekdays_start="09:00",
            weekdays_end="09:01",
        )
        occupied = ["2026-09-21T09:00", "2026-09-22T09:00", "2026-09-22T09:01"]

        result = planning.suggest(
            settings,
            occupied,
            now=datetime(2026, 9, 21, 8),
            rng=random.Random(1),
        )

        self.assertEqual(result.isoformat(timespec="minutes"), "2026-09-21T09:01")

    def test_all_items_combines_campaign_schedules(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for folder, name, item_id in (("one", "Kampagne Eins", "post-1"), ("two", "Kampagne Zwei", "post-2")):
                campaign_file = root / f"Kampagnen/{folder}/kampagne.yaml"
                campaign_file.parent.mkdir(parents=True)
                campaign_file.write_text(
                    f"name: {name}\nobjective: Test\naudience: Test\nvoice: Klar\n",
                    encoding="utf-8",
                )
                q.write(
                    campaign_file.parent / "queue/schedule.md",
                    [q.QueueItem(id=item_id, kind="post", text="Text", publish_at="2026-09-24T10:00")],
                    "Planung",
                    "Test",
                )

            with patch.object(web, "ROOT", root):
                combined = web.all_items("schedule")

        self.assertEqual([item["campaign_name"] for item in combined], ["Kampagne Eins", "Kampagne Zwei"])
        self.assertEqual(
            {item["campaign_path"] for item in combined},
            {"Kampagnen/one/kampagne.yaml", "Kampagnen/two/kampagne.yaml"},
        )


if __name__ == "__main__":
    unittest.main()