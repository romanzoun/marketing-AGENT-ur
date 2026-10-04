from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from linkedin_agents import timeouts
from linkedin_agents.web import app as web


class TimeoutSettingsTests(unittest.TestCase):
    def test_defaults_raise_idea_limit_to_thirty_minutes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            settings = timeouts.load(root)

        self.assertEqual(settings.ideas_to_posts, 30)
        self.assertEqual(timeouts.task_seconds(root, "ideas-to-posts"), 30 * 60)

    def test_settings_are_persisted_outside_the_container(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            configured = timeouts.TimeoutSettings(ideas_to_posts=47, image_generation=8)
            timeouts.save(root, configured)
            loaded = timeouts.load(root)

            self.assertEqual(loaded.ideas_to_posts, 47)
            self.assertEqual(loaded.image_generation, 8)
            self.assertTrue((root / "config/timeouts.yaml").is_file())

    def test_idea_process_limit_scales_with_count_and_revision(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            timeouts.save(
                root,
                timeouts.TimeoutSettings(ideas_to_posts=30, style_revision=15),
            )

            self.assertEqual(
                timeouts.process_seconds(root, "ideas-to-posts", count=3),
                (3 * (30 + 15) + 5) * 60,
            )

    def test_web_configuration_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            configured = timeouts.TimeoutSettings(ideas_to_posts=55)
            with patch.object(web, "ROOT", root):
                result = web.put_timeouts(configured)
                visible = web.get_timeouts()

        self.assertTrue(result["ok"])
        self.assertEqual(visible["ideas_to_posts"], 55)


if __name__ == "__main__":
    unittest.main()
