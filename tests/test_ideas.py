from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from linkedin_agents import ideas
from linkedin_agents.personal_profile import PersonalProfile, load as load_profile
from linkedin_agents.web import app as web


class IdeaStoreTests(unittest.TestCase):
    def test_add_idea_with_optional_campaign(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first = ideas.add(root, "Deutschland hat eine neue Wallet")
            second = ideas.add(root, "Wir sind Launch-Partner", "Kampagnen/wallet.yaml")
            stored = ideas.load(root)

        self.assertEqual(first.id, "idea-0001")
        self.assertIsNone(stored[0].campaign)
        self.assertEqual(second.id, "idea-0002")
        self.assertEqual(stored[1].campaign, "Kampagnen/wallet.yaml")


class PersonalProfileTests(unittest.TestCase):
    def test_profile_roundtrip_through_api(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            profile = PersonalProfile(
                name="Roman",
                current_role="Produktmensch",
                cv="Mehrjährige Erfahrung mit digitalen Identitäten.",
                expertise=["Digitale Identität", "Automatisierung"],
            )
            with patch.object(web, "ROOT", root):
                result = web.put_personal_profile(profile)

            stored = load_profile(root)

        self.assertTrue(result["ok"])
        self.assertEqual(stored.current_role, "Produktmensch")
        self.assertEqual(stored.expertise, ["Digitale Identität", "Automatisierung"])


class IdeaEndpointTests(unittest.TestCase):
    def test_create_edit_retry_and_delete_idea(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch.object(web, "ROOT", root):
                created = web.create_idea(web.IdeaCreate(text="Meine erste Idee"))
                idea_id = created["idea"]["id"]
                changed = web.patch_idea(
                    idea_id, web.IdeaPatch(text="Meine bessere Idee", retry=True)
                )
                listed = web.list_ideas()
                deleted = web.delete_idea(idea_id)

        self.assertEqual(changed["idea"]["text"], "Meine bessere Idee")
        self.assertEqual(changed["idea"]["status"], "open")
        self.assertEqual(listed[0]["id"], idea_id)
        self.assertTrue(deleted["ok"])


if __name__ == "__main__":
    unittest.main()
