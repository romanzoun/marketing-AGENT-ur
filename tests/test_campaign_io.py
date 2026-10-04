from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import yaml

from linkedin_agents import campaign_io
from linkedin_agents.models.campaign import Campaign, load_campaign


def campaign(version: int = 1, name: str = "Test Kampagne") -> Campaign:
    return Campaign(
        name=name,
        version=version,
        objective="Testen",
        audience="Teams",
        voice="Klar",
    )


class CampaignIoTests(unittest.TestCase):
    def test_save_creates_immutable_versions(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "Kampagnen/test/kampagne.yaml"
            path.parent.mkdir(parents=True)
            path.write_text(yaml.safe_dump(campaign().model_dump()), encoding="utf-8")

            updated = campaign_io.save_new_version(
                path,
                campaign(name="Geändert"),
                expected_version=1,
            )

            self.assertEqual(updated.version, 2)
            self.assertEqual(load_campaign(path).version, 2)
            self.assertTrue((path.parent / "versions/v0001.yaml").is_file())
            self.assertTrue((path.parent / "versions/v0002.yaml").is_file())

    def test_stale_save_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "Kampagnen/test/kampagne.yaml"
            path.parent.mkdir(parents=True)
            path.write_text(yaml.safe_dump(campaign(version=3).model_dump()), encoding="utf-8")
            with self.assertRaises(RuntimeError):
                campaign_io.save_new_version(path, campaign(version=2), expected_version=2)

    def test_export_import_preserves_version_and_avoids_name_collision(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            content = yaml.safe_dump(campaign(version=4).model_dump(), allow_unicode=True)

            first, first_campaign = campaign_io.import_yaml(root, "campaign.yaml", content)
            second, _ = campaign_io.import_yaml(root, "campaign.yaml", content)
            exported = campaign_io.export_yaml(first)

            self.assertEqual(first_campaign.version, 4)
            self.assertNotEqual(first, second)
            self.assertEqual(load_campaign(first).version, 4)
            self.assertEqual(yaml.safe_load(exported)["version"], 4)

    def test_import_as_version_increments_existing_campaign(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "Kampagnen/test/kampagne.yaml"
            path.parent.mkdir(parents=True)
            path.write_text(yaml.safe_dump(campaign(version=3).model_dump()), encoding="utf-8")
            content = yaml.safe_dump(campaign(version=99, name="Importiert").model_dump())

            target, imported = campaign_io.import_as_version(
                root, "Kampagnen/test/kampagne.yaml", content
            )

            self.assertEqual(target, path.resolve())
            self.assertEqual(imported.version, 4)
            self.assertEqual(load_campaign(path).name, "Importiert")
            self.assertTrue((path.parent / "versions/v0003.yaml").is_file())
            self.assertTrue((path.parent / "versions/v0004.yaml").is_file())

    def test_campaign_listing_ignores_queue_and_version_yaml(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            main = root / "Kampagnen/test/kampagne.yaml"
            main.parent.mkdir(parents=True)
            main.write_text("name: Test", encoding="utf-8")
            (main.parent / "queue").mkdir()
            (main.parent / "queue/analytics.yaml").write_text("[]", encoding="utf-8")
            (main.parent / "versions").mkdir()
            (main.parent / "versions/v0001.yaml").write_text("name: Test", encoding="utf-8")

            files = campaign_io.campaign_files(root)

        self.assertEqual(files, [main])


if __name__ == "__main__":
    unittest.main()
