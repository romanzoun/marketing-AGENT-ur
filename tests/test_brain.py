from __future__ import annotations

import json
import os
import subprocess
import tempfile
import unittest
import yaml
from pathlib import Path
from unittest.mock import patch

from linkedin_agents import brain
from linkedin_agents import queue as q


READY = {"codex": {"available": True, "info": "codex test"}}


class BrainCodexTests(unittest.TestCase):
    def test_multistep_content_jobs_have_extended_timeout(self) -> None:
        self.assertEqual(brain.JOB_TIMEOUTS["draft-posts"], 1500)
        self.assertEqual(brain.JOB_TIMEOUTS["find-and-write"], 2100)
        self.assertEqual(brain.JOB_TIMEOUTS["find-and-write-reshares"], 2100)

    def test_connection_prompt_uses_bounded_role_fallbacks(self) -> None:
        _agent, prompt = brain.PROMPTS["find-and-write-connections"]

        self.assertIn("höchstens drei Suchläufe", prompt)
        self.assertIn("Compliance Officer", prompt)
        self.assertIn("Suche nicht pauschal", prompt)
        self.assertIn("linkedin_ui_selector_mismatch", prompt)

    def test_auto_prefers_copilot_when_both_are_available(self) -> None:
        status = {
            "codex": {"available": True},
            "copilot": {"available": True},
        }
        with patch.dict(os.environ, {"BRAIN_ENGINE": "auto"}):
            self.assertEqual(brain.selected_engine(status), "copilot")

    def test_auto_uses_codex_when_copilot_is_missing(self) -> None:
        status = {
            "codex": {"available": True},
            "copilot": {"available": False},
        }
        with patch.dict(os.environ, {"BRAIN_ENGINE": "auto"}):
            self.assertEqual(brain.selected_engine(status), "codex")

    def test_explicit_copilot_runs_project_agent(self) -> None:
        completed = subprocess.CompletedProcess(args=[], returncode=0, stdout="ok", stderr="")
        with (
            patch.dict(os.environ, {"BRAIN_ENGINE": "copilot"}),
            patch.object(brain, "cli_status", return_value={"copilot": {"available": True}}),
            patch.object(brain, "_find_cli", return_value="/usr/local/bin/copilot"),
            patch.object(brain.subprocess, "run", return_value=completed) as run,
        ):
            result = brain.run_agent("copywriter", "Aufgabe")

        command = run.call_args.args[0]
        self.assertTrue(result["ok"])
        self.assertEqual(result["engine"], "copilot")
        self.assertIn("--agent", command)
        self.assertIn("copywriter", command)
        self.assertIn("--allow-all-tools", command)
        self.assertIn("--no-ask-user", command)

    def test_codex_is_used_when_explicitly_selected(self) -> None:
        with (
            patch.dict(os.environ, {"BRAIN_ENGINE": "codex"}),
            patch.object(brain, "cli_status", return_value=READY),
            patch.object(
                brain,
                "_run_codex",
                return_value={"ok": True, "engine": "codex", "agent": "copywriter"},
            ) as codex,
        ):
            result = brain.run_agent("copywriter", "Schreibe einen Entwurf")

        codex.assert_called_once()
        self.assertTrue(result["ok"])
        self.assertEqual(result["engine"], "codex")

    def test_codex_uses_project_agent_and_workspace_sandbox(self) -> None:
        completed = subprocess.CompletedProcess(args=[], returncode=0, stdout="ok", stderr="")
        with (
            patch.object(brain, "_find_cli", return_value="/usr/local/bin/codex"),
            patch.object(brain, "_agent_file", return_value=Path(__file__)),
            patch.object(brain.subprocess, "run", return_value=completed) as run,
        ):
            result = brain._run_codex("copywriter", "Aufgabe", timeout=30)

        command = run.call_args.args[0]
        prompt = command[-1]
        self.assertTrue(result["ok"])
        self.assertIn("exec", command)
        self.assertIn("workspace-write", command)
        self.assertNotIn("--approve-for-me", command)
        self.assertIn("--skip-git-repo-check", command)
        self.assertIn("`copywriter`", prompt)
        self.assertNotIn("copilot", prompt.lower())
        self.assertEqual(run.call_args.kwargs["cwd"], brain.ROOT)

    def test_missing_codex_agent_fails_before_cli_call(self) -> None:
        with (
            patch.object(brain, "_find_cli", return_value="/usr/local/bin/codex"),
            patch.object(brain, "_agent_file", return_value=Path("/missing/agent.toml")),
            patch.object(brain.subprocess, "run") as run,
        ):
            result = brain._run_codex("copywriter", "Aufgabe", timeout=30)

        run.assert_not_called()
        self.assertFalse(result["ok"])
        self.assertIn("codex_agent_not_found", result["error"])

    def test_draft_success_requires_created_queue_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign = "Kampagnen/test/kampagne.yaml"
            approvals = root / "Kampagnen/test/queue/approvals.md"
            q.write(
                approvals,
                [q.QueueItem(id="post-1", kind="post", text="Neu")],
                "Freigaben",
                "Test",
            )
            with patch.object(brain, "ROOT", root):
                result = brain._verify_artifacts(
                    "draft-posts", campaign, 1, set(), {"ok": True}
                )

        self.assertTrue(result["ok"])
        self.assertEqual(result["artifacts"]["created_posts"], ["post-1"])

    def test_draft_without_queue_artifacts_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(brain, "ROOT", Path(directory)):
                result = brain._verify_artifacts(
                    "draft-posts", "Kampagnen/test/kampagne.yaml", 2, set(), {"ok": True}
                )

        self.assertFalse(result["ok"])
        self.assertEqual(
            result["error"],
            "Keine ausreichenden fertigen Post-Entwürfe erzeugt: erwartet 2, erstellt 0.",
        )

    def test_comment_candidate_remains_visible_without_generated_text(self) -> None:
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
                        text="",
                        fit_score=0.1,
                        fit_note="Verbotenes Thema Politik",
                    )
                ],
                "Freigaben",
                "Test",
            )
            with patch.object(brain, "ROOT", root):
                result = brain._verify_artifacts(
                    "find-and-write", campaign, 1, set(), {"ok": True}
                )

        self.assertTrue(result["ok"])
        self.assertEqual(result["artifacts"]["created_comments"], ["comment-1"])

    def test_missing_connection_candidates_returns_clear_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(brain, "ROOT", Path(directory)):
                result = brain._verify_artifacts(
                    "find-and-write-connections",
                    "Kampagnen/test/kampagne.yaml",
                    2,
                    set(),
                    {"ok": True},
                )

        self.assertFalse(result["ok"])
        self.assertEqual(
            result["error"],
            "Keine ausreichenden fertigen Vernetzungskandidaten erzeugt: erwartet 2, erstellt 0.",
        )

    def test_draft_timeout_is_recovered_when_all_artifacts_exist(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign = "Kampagnen/test/kampagne.yaml"
            approvals = root / "Kampagnen/test/queue/approvals.md"
            q.write(
                approvals,
                [
                    q.QueueItem(id="post-1", kind="post", text="Erster Entwurf"),
                    q.QueueItem(id="post-2", kind="post", text="Zweiter Entwurf"),
                ],
                "Freigaben",
                "Test",
            )
            with patch.object(brain, "ROOT", root):
                result = brain._verify_artifacts(
                    "draft-posts", campaign, 2, set(), {"ok": False, "error": "timeout"}
                )

        self.assertTrue(result["ok"])
        self.assertIsNone(result["error"])
        self.assertEqual(result["agent_warning"], "timeout")
        self.assertTrue(result["recovered_from_artifacts"])

    def test_comment_timeout_is_recovered_when_written_comments_exist(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign = "Kampagnen/test/kampagne.yaml"
            approvals = root / "Kampagnen/test/queue/approvals.md"
            q.write(
                approvals,
                [q.QueueItem(id="comment-1", kind="comment", text="Passt zum Post")],
                "Freigaben",
                "Test",
            )
            with patch.object(brain, "ROOT", root):
                result = brain._verify_artifacts(
                    "find-and-write", campaign, 1, set(), {"ok": False, "error": "timeout"}
                )

        self.assertTrue(result["ok"])
        self.assertEqual(result["artifacts"]["created_comments"], ["comment-1"])

    def test_rewrite_uses_structured_read_only_codex_output(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign_path = root / "Kampagnen/test/kampagne.yaml"
            campaign_path.parent.mkdir(parents=True)
            campaign_path.write_text(
                yaml.safe_dump(
                    {"name": "Test", "objective": "Klar", "audience": "Teams", "voice": "Persönlich"}
                ),
                encoding="utf-8",
            )

            def fake_run(command, **kwargs):
                output = Path(command[command.index("--output-last-message") + 1])
                output.write_text('{"text":"Der neue persönliche Entwurf."}', encoding="utf-8")
                return subprocess.CompletedProcess(command, 0, "", "")

            with (
                patch.object(brain, "ROOT", root),
                patch.object(brain, "cli_status", return_value=READY),
                patch.object(brain, "_find_cli", return_value="/usr/local/bin/codex"),
                patch.object(brain.subprocess, "run", side_effect=fake_run) as run,
            ):
                result = brain.rewrite_draft(
                    "Kampagnen/test/kampagne.yaml",
                    q.QueueItem(id="post-1", kind="post", text="Alter Entwurf"),
                    "Persönlicher schreiben",
                )

        command = run.call_args.args[0]
        self.assertTrue(result["ok"])
        self.assertEqual(result["text"], "Der neue persönliche Entwurf.")
        self.assertIn("read-only", command)
        self.assertIn("--output-schema", command)
        self.assertIn("--output-last-message", command)

    def test_rewrite_unwraps_nested_json_and_markdown_links(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            campaign_path = root / "Kampagnen/test/kampagne.yaml"
            campaign_path.parent.mkdir(parents=True)
            campaign_path.write_text(
                yaml.safe_dump(
                    {"name": "Test", "objective": "Klar", "audience": "Teams", "voice": "Klar"}
                ),
                encoding="utf-8",
            )
            nested = {
                "content_type": "post",
                "text": "Klartext\n\n[https://example.test/?utm\\_source=linkedin\\&x=1](https://example.test/?utm_source=linkedin\\&x=1)\n— CTA",
            }

            def fake_run(command, **kwargs):
                output = Path(command[command.index("--output-last-message") + 1])
                output.write_text(json.dumps({"text": json.dumps(nested)}), encoding="utf-8")
                return subprocess.CompletedProcess(command, 0, "", "")

            with (
                patch.object(brain, "ROOT", root),
                patch.object(brain, "cli_status", return_value=READY),
                patch.object(brain, "_find_cli", return_value="/usr/local/bin/codex"),
                patch.object(brain.subprocess, "run", side_effect=fake_run),
            ):
                result = brain.rewrite_draft(
                    "Kampagnen/test/kampagne.yaml",
                    q.QueueItem(id="post-1", kind="post", text="Alt"),
                    "Neu schreiben",
                )

        self.assertTrue(result["ok"])
        self.assertEqual(
            result["text"],
            "Klartext\n\nhttps://example.test/?utm_source=linkedin&x=1\n— CTA",
        )


class BrainProbeTests(unittest.TestCase):
    def test_probe_uses_codex(self) -> None:
        with patch.object(
            brain,
            "_probe_codex",
            return_value={"ok": True, "engine": "codex", "answer": "HEALTH_OK"},
        ) as probe:
            result = brain.probe_cli(status=READY)

        probe.assert_called_once()
        self.assertTrue(result["ok"])
        self.assertEqual(result["engine"], "codex")

    def test_codex_probe_is_read_only_and_ephemeral(self) -> None:
        completed = subprocess.CompletedProcess(
            args=[], returncode=0, stdout="HEALTH_OK\n", stderr=""
        )
        with (
            patch.object(brain, "_find_cli", return_value="/usr/local/bin/codex"),
            patch.object(brain.subprocess, "run", return_value=completed) as run,
        ):
            result = brain._probe_codex(timeout=30)

        command = run.call_args.args[0]
        self.assertTrue(result["ok"])
        self.assertIn("read-only", command)
        self.assertIn("--ephemeral", command)
        self.assertNotIn("--approve-for-me", command)


if __name__ == "__main__":
    unittest.main()
