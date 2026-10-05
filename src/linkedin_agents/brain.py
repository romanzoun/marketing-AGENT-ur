"""Content-Erzeugung über Codex CLI oder GitHub Copilot CLI.

Codex liest die Teamregeln aus ``AGENTS.md`` und die spezialisierten Rollen aus
``.codex/agents/*.toml``. Copilot CLI verwendet zusätzlich die Rollen aus
``.github/agents/*.agent.md``. Alle Content-Jobs laufen nicht-interaktiv und
legen nur Vorschläge in der Freigabe-Liste ab.

    ./bin/li-brain --campaign C draft-posts --count 2
    ./bin/li-brain --campaign C find-and-write --count 5
    ./bin/li-brain --campaign C check
    ./bin/li-brain --campaign C probe
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from dotenv import load_dotenv

from . import ideas as idea_store
from . import queue as q
from . import timeouts
from .models.campaign import load_campaign
from .style_learning import load_state, prepare_items

ROOT = Path(__file__).resolve().parents[2]
PROBE_ANSWER = "HEALTH_OK"
PERSONAL_CAMPAIGN = "Kampagnen/persoenlich/kampagne.yaml"
PROBE_PROMPT = (
    "Dies ist ein reiner Health Check. Verwende keine Werkzeuge und ändere keine Dateien. "
    f"Antworte exakt mit {PROBE_ANSWER}."
)
ENGINES = ("copilot", "codex")
CODEX_AGENTS = {
    "orchestrator": "orchestrator",
    "campaign-manager": "campaign_manager",
    "engagement-scout": "engagement_scout",
    "content-strategist": "content_strategist",
    "copywriter": "copywriter",
    "art-director": "art_director",
    "style-evaluator": "style_evaluator",
    "reviewer": "reviewer",
    "operator": "operator",
}
JOB_TIMEOUTS = {
    # Mehrere Rollen laufen nacheinander; 15 Minuten endeten real vor dem Reviewer.
    "draft-posts": 1500,
    # Engagement-Läufe enthalten zusätzlich Browser-Suche und Originalpost-Prüfung.
    "find-and-write": 2100,
    "write-comments": 2100,
    "find-and-write-reshares": 2100,
    "find-and-write-connections": 2100,
    "ideas-to-posts": 1800,
}
load_dotenv(ROOT / ".env")


def _emit(payload: dict) -> None:
    json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


def _cli_environment() -> dict[str, str]:
    """Ergänzt typische CLI-Pfade, weil cron meist nur /usr/bin:/bin kennt."""
    env = os.environ.copy()
    candidates = ["/opt/homebrew/bin", "/usr/local/bin", "/usr/bin", "/bin"]
    current = env.get("PATH", "").split(os.pathsep)
    env["PATH"] = os.pathsep.join(dict.fromkeys(candidates + current))
    return env


def _find_cli(name: str) -> str | None:
    exe = shutil.which(name, path=_cli_environment()["PATH"])
    if exe:
        return exe
    for directory in (Path.home() / ".local/bin", Path.home() / ".npm-global/bin"):
        candidate = directory / name
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return str(candidate)
    return None


def codex_available() -> tuple[bool, str]:
    exe = _find_cli("codex")
    if not exe:
        return False, "Codex CLI nicht gefunden (npm install -g @openai/codex)"
    try:
        version = subprocess.run(
            [exe, "--version"], capture_output=True, text=True, timeout=30,
            env=_cli_environment(),
        )
        if version.returncode != 0:
            return False, (version.stderr or version.stdout).strip()
        auth = subprocess.run(
            [exe, "login", "status"], capture_output=True, text=True, timeout=30,
            env=_cli_environment(),
        )
        if auth.returncode != 0:
            return False, "Codex CLI ist nicht eingeloggt (`codex login`)"
        version_lines = (version.stdout or version.stderr).strip().splitlines()
        auth_lines = (auth.stdout or auth.stderr).strip().splitlines()
        version_text = version_lines[0] if version_lines else "Codex CLI"
        auth_text = auth_lines[-1] if auth_lines else "eingeloggt"
        return True, f"{version_text}; {auth_text}"
    except Exception as exc:
        return False, str(exc)


def copilot_available() -> tuple[bool, str]:
    exe = _find_cli("copilot")
    if not exe:
        return False, "Copilot CLI nicht gefunden (npm install -g @github/copilot)"
    try:
        version = subprocess.run(
            [exe, "--version"], capture_output=True, text=True, timeout=30,
            env=_cli_environment(),
        )
        if version.returncode != 0:
            return False, (version.stderr or version.stdout).strip()
        auth = subprocess.run(
            [exe, "login", "--status"], capture_output=True, text=True, timeout=30,
            env=_cli_environment(),
        )
        if auth.returncode != 0:
            return False, "Copilot CLI ist nicht eingeloggt (`copilot login`)"
        version_lines = (version.stdout or version.stderr).strip().splitlines()
        auth_lines = (auth.stdout or auth.stderr).strip().splitlines()
        version_text = version_lines[0] if version_lines else "Copilot CLI"
        auth_text = auth_lines[-1] if auth_lines else "eingeloggt"
        return True, f"{version_text}; {auth_text}"
    except Exception as exc:
        return False, str(exc)


def cli_status() -> dict[str, dict[str, object]]:
    status: dict[str, dict[str, object]] = {}
    for engine, checker in (("codex", codex_available), ("copilot", copilot_available)):
        available, info = checker()
        status[engine] = {"available": available, "info": info}
    return status


def preferred_engine() -> str:
    """Liest die gewünschte CLI, ohne ihre Verfügbarkeit zu prüfen."""
    configured = os.getenv("BRAIN_ENGINE", "auto").strip().lower()
    return configured if configured in ENGINES else "auto"


def selected_engine(status: dict[str, dict[str, object]] | None = None) -> str | None:
    current = status or cli_status()
    configured = preferred_engine()
    if configured in ENGINES:
        return configured if current.get(configured, {}).get("available") else None
    for engine in ENGINES:
        if current.get(engine, {}).get("available"):
            return engine
    return None


def _result(proc: subprocess.CompletedProcess[str], agent: str, engine: str = "codex") -> dict:
    return {
        "ok": proc.returncode == 0,
        "engine": engine,
        "agent": CODEX_AGENTS.get(agent, agent),
        "stdout": proc.stdout[-12000:],
        "stderr": proc.stderr[-4000:],
    }


def _agent_file(agent: str) -> Path:
    return ROOT / ".codex" / "agents" / f"{agent}.toml"


def _run_codex(agent: str, prompt: str, timeout: int) -> dict:
    exe = _find_cli("codex")
    if not exe:
        return {"ok": False, "engine": "codex", "error": "codex_not_found"}
    role_name = CODEX_AGENTS.get(agent)
    role_file = _agent_file(agent)
    if not role_name or not role_file.is_file():
        return {
            "ok": False,
            "engine": "codex",
            "error": f"codex_agent_not_found:{agent}",
        }
    codex_prompt = (
        f"Nutze den projektbezogenen Codex-Custom-Agent `{role_name}` als primären "
        f"Bearbeiter. Delegiere die folgende Fachaufgabe an diesen Agenten mit "
        f"`agent_type={role_name}` und `fork_turns=none` und warte "
        f"auf sein vollständiges Ergebnis. Die Rolle steht in `{role_file.relative_to(ROOT)}`; "
        "AGENTS.md und die dort beschriebene Freigabepflicht sind verbindlich. "
        "Der primäre Agent darf die weiteren Projekt-Agenten aus `.codex/agents/` "
        "für seinen vorgeschriebenen Prüfablauf ebenfalls mit `fork_turns=none` "
        "einsetzen; der jeweilige Auftrag muss deshalb den nötigen Kontext enthalten. "
        "Falls eine Delegation "
        "technisch nicht möglich ist, führe die developer_instructions der genannten "
        "Rolle selbst aus. Veröffentliche niemals direkt.\n\n"
        f"Aufgabe:\n{prompt}"
    )
    proc = subprocess.run(
        [
            exe, "exec", "--cd", str(ROOT), "--sandbox", "workspace-write",
            "--skip-git-repo-check", "--ephemeral",
            "--color", "never", codex_prompt,
        ],
        capture_output=True, text=True, cwd=ROOT, timeout=timeout,
        env=_cli_environment(),
    )
    return _result(proc, agent)


def _copilot_agent_file(agent: str) -> Path:
    return ROOT / ".github" / "agents" / f"{agent}.agent.md"


def _run_copilot(
    agent: str,
    prompt: str,
    timeout: int,
    *,
    allow_tools: bool,
    model_permission: str = "yes",
) -> dict:
    exe = _find_cli("copilot")
    if not exe:
        return {"ok": False, "engine": "copilot", "error": "copilot_not_found"}
    role_file = _copilot_agent_file(agent) if agent != "code-repair" else None
    if role_file is not None and not role_file.is_file():
        return {"ok": False, "engine": "copilot", "error": f"copilot_agent_not_found:{agent}"}
    role_instruction = (
        f"Nutze den projektbezogenen Copilot-Agenten `{agent}` aus "
        f"`{role_file.relative_to(ROOT)}`. "
        if role_file is not None else
        "Arbeite ohne Marketing-Agentenrolle. "
    )
    copilot_prompt = (
        f"{role_instruction}"
        "AGENTS.md und die dort beschriebene Freigabepflicht sind verbindlich. "
        "Delegiere Fachaufgaben an die passenden Agenten unter `.github/agents/` "
        "und gib ihnen den nötigen Kontext mit. Veröffentliche niemals direkt.\n\n"
        f"Aufgabe:\n{prompt}"
    )
    command = [
        exe, "-p", copilot_prompt, "-C", str(ROOT), "--agent", agent,
        "--no-ask-user", "--silent", "--no-color", "--model", "auto",
    ]
    if agent == "code-repair":
        command = [item for item in command if item != agent and item != "--agent"]
    if allow_tools:
        command.append("--allow-all-tools")
    else:
        command.extend(["--available-tools", "read", "--deny-tool", "shell,edit"])
    if model_permission != "yes":
        command.extend(["--allow-tool", f"model_permission:{model_permission}"])
    proc = subprocess.run(
        command,
        capture_output=True, text=True, cwd=ROOT, timeout=timeout,
        env=_cli_environment(),
    )
    return _result(proc, agent, "copilot")


def _run_engine(engine: str, agent: str, prompt: str, timeout: int) -> dict:
    if engine == "copilot":
        return _run_copilot(agent, prompt, timeout, allow_tools=True)
    return _run_codex(agent, prompt, timeout)


def repair_code(prompt: str, timeout: int = 1200) -> dict:
    """Repariert Code mit der gewählten CLI und fällt nur im Automatikmodus um."""
    engine = selected_engine()
    if engine == "copilot":
        return run_code_repair_with_copilot(prompt, timeout)
    if engine == "codex":
        return run_code_repair(prompt, timeout)
    return {"ok": False, "error": "brain_cli_unavailable", "engines": cli_status()}


def run_code_repair(prompt: str, timeout: int = 1200) -> dict:
    """Startet Codex für eng begrenzte Code-Reparaturen ohne Marketing-Agentenrolle."""
    exe = _find_cli("codex")
    if not exe:
        return {"ok": False, "engine": "codex", "error": "codex_not_found"}
    repair_prompt = (
        "Arbeite als Code-Reparatur-Agent in diesem Repository. Repariere ausschließlich "
        "den beschriebenen LinkedIn-UI-/Playwright-Fehler. Ändere keine Kampagnen-, Queue-, "
        "Freigabe-, Planungs- oder Logdateien und führe keine Live-Aktion auf LinkedIn aus. "
        "Read-only DOM-Diagnose ist erlaubt. Halte die Änderung minimal, ergänze einen "
        "fokussierten Regressionstest und führe passende Tests aus. Wenn die Ursache nicht "
        "belegbar ist, ändere nichts und berichte den Blocker.\n\n"
        f"Fehlerkontext:\n{prompt}"
    )
    proc = subprocess.run(
        [
            exe, "exec", "--cd", str(ROOT), "--sandbox", "workspace-write",
            "--skip-git-repo-check", "--ephemeral", "--color", "never", repair_prompt,
        ],
        capture_output=True, text=True, cwd=ROOT, timeout=timeout,
        env=_cli_environment(),
    )
    result = _result(proc, "code-repair")
    if not result["ok"]:
        result["error"] = (proc.stderr or proc.stdout or "codex_repair_failed")[-1000:]
    return result


def run_code_repair_with_copilot(prompt: str, timeout: int = 1200) -> dict:
    """Startet Copilot CLI für dieselbe eng begrenzte Code-Reparatur."""
    repair_prompt = (
        "Arbeite als Code-Reparatur-Agent in diesem Repository. Repariere ausschließlich "
        "den beschriebenen LinkedIn-UI-/Playwright-Fehler. Ändere keine Kampagnen-, Queue-, "
        "Freigabe-, Planungs- oder Logdateien und führe keine Live-Aktion auf LinkedIn aus. "
        "Read-only DOM-Diagnose ist erlaubt. Halte die Änderung minimal, ergänze einen "
        "fokussierten Regressionstest und führe passende Tests aus. Wenn die Ursache nicht "
        "belegbar ist, ändere nichts und berichte den Blocker.\n\n"
        f"Fehlerkontext:\n{prompt}"
    )
    try:
        result = _run_copilot("code-repair", repair_prompt, timeout, allow_tools=True)
    except subprocess.TimeoutExpired:
        return {"ok": False, "engine": "copilot", "error": "timeout"}
    except Exception as exc:
        return {"ok": False, "engine": "copilot", "error": str(exc)}
    if not result["ok"]:
        result["error"] = (result.get("stderr") or result.get("stdout") or "copilot_repair_failed")[-1000:]
    return result


def _probe_codex(timeout: int) -> dict:
    exe = _find_cli("codex")
    if not exe:
        return {"ok": False, "engine": "codex", "error": "codex_not_found"}
    started = time.monotonic()
    proc = subprocess.run(
        [
            exe, "exec", "--cd", str(ROOT), "--sandbox", "read-only",
            "--skip-git-repo-check", "--ephemeral", "--color", "never",
            PROBE_PROMPT,
        ],
        capture_output=True, text=True, cwd=ROOT, timeout=timeout,
        env=_cli_environment(),
    )
    answer = proc.stdout.strip()
    return {
        "ok": proc.returncode == 0 and PROBE_ANSWER in answer.upper(),
        "engine": "codex",
        "answer": answer[-500:],
        "error": "" if proc.returncode == 0 else proc.stderr[-2000:],
        "duration_ms": round((time.monotonic() - started) * 1000),
    }


def _probe_copilot(timeout: int) -> dict:
    started = time.monotonic()
    result = _run_copilot(
        "orchestrator", PROBE_PROMPT, timeout, allow_tools=False, model_permission="no"
    )
    answer = str(result.get("stdout", "")).strip()
    return {
        "ok": bool(result.get("ok")) and PROBE_ANSWER in answer.upper(),
        "engine": "copilot",
        "answer": answer[-500:],
        "error": "" if result.get("ok") else str(result.get("stderr", ""))[-2000:],
        "duration_ms": round((time.monotonic() - started) * 1000),
    }


def probe_cli(
    timeout: int = 120,
    status: dict[str, dict[str, object]] | None = None,
) -> dict:
    """Sendet eine minimale echte, schreibgeschützte Anfrage an die gewählte CLI."""
    current_status = status or cli_status()
    engine = selected_engine(current_status)
    if not engine:
        return {"ok": False, "error": "brain_cli_unavailable", "attempts": []}
    try:
        result = _probe_copilot(timeout) if engine == "copilot" else _probe_codex(timeout)
    except subprocess.TimeoutExpired:
        result = {"ok": False, "engine": engine, "error": "timeout"}
    except Exception as exc:
        result = {"ok": False, "engine": engine, "error": str(exc)}
    result["attempts"] = [dict(result)]
    return result


def run_agent(agent: str, prompt: str, timeout: int = 900) -> dict:
    status = cli_status()
    engine = selected_engine(status)
    if not engine:
        return {"ok": False, "error": "brain_cli_unavailable", "engines": status}
    try:
        return _run_engine(engine, agent, prompt, timeout)
    except subprocess.TimeoutExpired:
        return {"ok": False, "engine": engine, "agent": agent, "error": "timeout"}
    except Exception as exc:
        return {"ok": False, "engine": engine, "agent": agent, "error": str(exc)}


def _plain_linkedin_text(value: object) -> str:
    """Entpackt verschachtelte Modellausgaben und entfernt Markdown-Linksyntax."""
    current = value
    for _ in range(4):
        if isinstance(current, dict):
            current = current.get("text") or current.get("content") or ""
            continue
        if not isinstance(current, str):
            current = str(current)
        text = current.strip()
        if text.startswith("```") and text.endswith("```"):
            text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.I)
        try:
            nested = json.loads(text)
        except (json.JSONDecodeError, TypeError):
            current = text
            break
        if isinstance(nested, (dict, str)):
            current = nested
            continue
        current = text
        break

    text = str(current).strip()

    def unescape(part: str) -> str:
        return re.sub(r"\\([\\`*_{}\[\]()#+.!<>&-])", r"\1", part)

    def plain_link(match: re.Match[str]) -> str:
        label = unescape(match.group(1)).strip()
        target = unescape(match.group(2)).strip()
        if label.startswith(("http://", "https://")):
            return label
        target_url = target.splitlines()[0].strip()
        return f"{label}: {target_url}" if label else target_url

    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]*)\)", plain_link, text, flags=re.S)
    return unescape(text).strip()


def _rewrite_context(campaign_path: str, item: q.QueueItem, instruction: str) -> tuple[object, str]:
    target = Path(campaign_path)
    if not target.is_absolute():
        target = ROOT / target
    campaign = load_campaign(target)
    state = load_state(ROOT)
    learning_context = {
        "confirmed_directives": state.get("directive_preferences", []),
        "confirmed_user_notes": [
            row for row in state.get("user_notes", [])
            if row.get("outcome") == "approved"
        ][-20:],
        "recent_approved_examples": [
            {
                "kind": row.get("kind"),
                "text": row.get("text"),
                "source_text": row.get("source_text"),
                "reshare_with_comment": row.get("reshare_with_comment"),
                "user_memory_note": row.get("user_memory_note"),
            }
            for row in state.get("approvals", [])[-12:]
        ],
        "recent_rejected_examples": [
            {
                "kind": row.get("kind"),
                "text": row.get("text"),
                "user_memory_note": row.get("user_memory_note"),
            }
            for row in state.get("rejections", [])[-8:]
        ],
    }
    prompt = (
        "Du bist der Copywriter für einen einzelnen LinkedIn-Entwurf. Schreibe den "
        "vorhandenen Text gemäß der Regieanweisung neu. Bewahre belegte Aussagen, "
        "Zielsprache, Inhaltstyp und Kampagnenregeln. Erfinde keine Fakten, Personen, "
        "Produkte oder Erfahrungen. Bei einem Kommentar bezieht sich der Text konkret "
        "auf den Originalbeitrag. Der Wert `text` enthält ausschließlich den fertigen "
        "LinkedIn-Klartext: keine JSON-Hülle, keine Codeblöcke und keine Markdown-Links. "
        "URLs stehen unverändert als Klartext. Gib ausschließlich das verlangte "
        "strukturierte Ergebnis zurück und ändere keine Dateien.\n\n"
        f"INHALTSTYP:\n{item.kind}\n\n"
        f"REGIEANWEISUNG:\n{instruction.strip()}\n\n"
        f"AKTUELLER ENTWURF:\n{item.text}\n\n"
        f"ORIGINALBEITRAG/KONTEXT:\n{(item.note or '')[:12000]}\n\n"
        f"KAMPAGNE:\n{campaign.model_dump_json(indent=2)}\n\n"
        "BESTÄTIGTE LERNSIGNALE:\n"
        f"{json.dumps(learning_context, ensure_ascii=False)}"
    )
    return campaign, prompt


def _rewrite_with_copilot(prompt: str, timeout: int) -> dict:
    output_prompt = (
        f"{prompt}\n\n"
        "Gib nur ein JSON-Objekt mit dem Feld text zurück. Kein erklärender Text."
    )
    try:
        result = _run_copilot(
            "copywriter", output_prompt, timeout, allow_tools=False, model_permission="no"
        )
    except subprocess.TimeoutExpired:
        return {"ok": False, "engine": "copilot", "error": "timeout"}
    except Exception as exc:
        return {"ok": False, "engine": "copilot", "error": str(exc)}
    if not result.get("ok"):
        return {
            "ok": False,
            "engine": "copilot",
            "error": (result.get("stderr") or result.get("stdout") or "copilot_rewrite_failed")[-3000:],
        }
    try:
        payload = json.loads(str(result.get("stdout", "")).strip())
    except json.JSONDecodeError as exc:
        return {"ok": False, "engine": "copilot", "error": str(exc)}
    rewritten = _plain_linkedin_text(payload.get("text", ""))
    if not rewritten:
        return {"ok": False, "engine": "copilot", "error": "empty_rewrite"}
    return {"ok": True, "engine": "copilot", "text": rewritten}


def rewrite_draft(
    campaign_path: str,
    item: q.QueueItem,
    instruction: str,
    timeout: int | None = None,
) -> dict:
    """Einen einzelnen Entwurf per gewählter CLI und Regieanweisung umschreiben."""
    timeout = timeout or timeouts.load(ROOT).rewrite * 60
    status = cli_status()
    engine = selected_engine(status)
    if not engine:
        return {"ok": False, "error": "brain_cli_unavailable", "engines": status}
    _campaign, prompt = _rewrite_context(campaign_path, item, instruction)
    if engine == "copilot":
        return _rewrite_with_copilot(prompt, timeout)
    exe = _find_cli("codex")
    if not exe:
        return {"ok": False, "error": "codex_not_found"}
    schema = {
        "type": "object",
        "properties": {"text": {"type": "string", "minLength": 1}},
        "required": ["text"],
        "additionalProperties": False,
    }
    runs = ROOT / ".runs"
    runs.mkdir(parents=True, exist_ok=True)
    try:
        with tempfile.TemporaryDirectory(prefix="rewrite-", dir=runs) as directory:
            temp = Path(directory)
            schema_path = temp / "schema.json"
            output_path = temp / "result.json"
            schema_path.write_text(json.dumps(schema), encoding="utf-8")
            proc = subprocess.run(
                [
                    exe, "exec", "--cd", str(ROOT), "--sandbox", "read-only",
                    "--skip-git-repo-check", "--ephemeral", "--color", "never",
                    "--output-schema", str(schema_path),
                    "--output-last-message", str(output_path), prompt,
                ],
                capture_output=True,
                text=True,
                cwd=ROOT,
                timeout=timeout,
                env=_cli_environment(),
            )
            if proc.returncode != 0:
                return {
                    "ok": False,
                    "engine": "codex",
                    "error": (proc.stderr or proc.stdout)[-3000:].strip(),
                }
            payload = json.loads(output_path.read_text(encoding="utf-8"))
    except subprocess.TimeoutExpired:
        return {"ok": False, "engine": "codex", "error": "timeout"}
    except (OSError, json.JSONDecodeError, KeyError) as exc:
        return {"ok": False, "engine": "codex", "error": str(exc)}

    rewritten = _plain_linkedin_text(payload.get("text", ""))
    if not rewritten:
        return {"ok": False, "engine": "codex", "error": "empty_rewrite"}
    return {"ok": True, "engine": "codex", "text": rewritten}


PROMPTS = {
    "draft-posts": (
        "content-strategist",
        "Lies die Kampagne @{campaign}, @config/personal_profile.yaml und das "
        "Stilprofil @team/style/profile.md. "
        "Prüfe zuerst, ob aus einem zuvor abgebrochenen Lauf bereits genau {count} "
        "fertige, stilbestandene Posttexte existieren, die noch nicht in approvals.md "
        "liegen. Falls ja, setze genau diesen Lauf beim Reviewer fort, statt neue Ideen "
        "oder Dubletten zu erzeugen. "
        "Entwickle genau {count} konkrete Post-Ideen im Rahmen der Kampagnen-Regeln. "
        "Nutze den Codex-Agenten `copywriter` für fertige Texte in meiner Stimme "
        "(persönlich, witzig, bildhafte Vergleiche, kein Marketing-Sprech), danach "
        "den Agenten `style_evaluator` zur Prüfung gegen @team/style/learning.json und "
        "die freigegebenen Beispiele. Bei Score unter 0.70 muss der Copywriter den "
        "Text anhand der gelernten Muster überarbeiten und erneut bewerten. Danach "
        "prüft `reviewer` die Kampagnenregeln. Lege jeden geprüften "
        "Entwurf zwingend mit "
        '`./bin/li-jobs --campaign "{campaign}" add --kind post --text "..."` '
        "unmittelbar nach der einmaligen Reviewer-Prüfung in die Freigabe-Liste. "
        "Führe keine doppelten Hash-, Stil- oder Reviewer-Runden durch und halte das "
        "Team-Protokoll knapp; die Queue-Einträge haben Vorrang. Der Job ist erst "
        "erledigt, wenn genau {count} neue "
        "Post-Einträge dort vorhanden sind. Veröffentliche nichts und kreuze nichts an."
    ),
    "find-and-write": (
        "engagement-scout",
        "Lies die vollständige Kampagne @{campaign}, @config/personal_profile.yaml "
        "und @team/engagement-scout/memory.md. Sammle für diese Kampagne passende "
        "Feed-Beiträge mit "
        '`./bin/li-jobs --campaign "{campaign}" find-comments --limit {count}`. '
        "Die Sammlung enthält bewusst auch Beiträge ohne Keyword-Treffer. Behalte jeden technisch belastbar "
        "gesammelten Kandidaten in `approvals.md`; lösche keinen Kandidaten wegen geringer "
        "inhaltlicher Passung. Prüfe den vollständigen Originalpost im jeweiligen `note:` "
        "semantisch gegen objective, audience, topics, banned_topics, products und "
        "keywords_to_engage der Kampagne. Setze bei jedem neuen Kandidaten `fit_score` "
        "zwischen 0.0 und 1.0 und begründe ihn knapp in `fit_note`. Verbotene Themen oder "
        "reine Keyword-Zufallstreffer erhalten einen sehr niedrigen Score und bleiben zur "
        "transparenten manuellen Entscheidung sichtbar. Sortiere die neuen Kandidaten "
        "absteigend nach `fit_score`. Nutze danach den Codex-Agenten `copywriter`: "
        "Injiziere für jeden nicht durch `banned_topics` gesperrten Kandidaten den "
        "vollständigen Originalpost aus `note:`, die Kampagne, "
        "@config/personal_profile.yaml, @team/copywriter/memory.md, "
        "@team/style/profile.md, @team/style/learning.json und aktuelle Beispiele aus "
        "@team/style/approved/. Schreibe eine kurze persönliche Meinung in der Sprache "
        "des Ziel-Posts, ohne erfundenen Link, in 2–4 Sätzen und trage sie direkt ins "
        "`text:`-Feld ein. Der Kommentar muss konkret auf den Originalpost antworten und "
        "zugleich einen natürlichen Bezug zur Kampagnenperspektive herstellen; keine "
        "aufgesetzte Produktwerbung. Bei einem verbotenen Thema bleibt `text` leer; "
        "`fit_note` nennt den konkreten Sperrgrund. Lass jeden fertigen Kommentar vom Agenten "
        "`style_evaluator` gegen @team/style/profile.md, @team/style/learning.json und "
        "die freigegebenen Beispiele bewerten. Bei Score unter 0.70 muss der Copywriter "
        "ihn anhand der gelernten Muster überarbeiten. Danach prüft `reviewer` die "
        "Kampagnenregeln. Veröffentliche nichts und kreuze nichts an."
    ),
    "write-comments": (
        "copywriter",
        "Lies die vollständige Kampagne @{campaign}, @config/personal_profile.yaml, "
        "@team/copywriter/memory.md, @team/style/profile.md, "
        "@team/style/learning.json und aktuelle Beispiele unter @team/style/approved/. "
        "Öffne die Freigabe-Liste der Kampagne @{campaign} "
        "(Kampagnen/<ordner>/queue/approvals.md). Für jeden Kommentar-Eintrag mit "
        "leerem `text:` formuliere eine kurze, persönliche Meinung in der Sprache des "
        "Ziel-Posts. Injiziere dafür den vollständigen Originalbeitrag aus `note:` und "
        "die Kampagnenfelder objective, audience, topics, banned_topics, products und "
        "CTA. Der Text muss konkret zum Original passen und die Kampagnenperspektive "
        "natürlich einbringen, ohne Werbeantwort oder erfundene Aussage. Schreibe ohne "
        "erfundenen Link in 2–4 Sätzen. Lass jeden Text danach vom Agenten `style_evaluator` gegen "
        "@team/style/learning.json und die freigegebenen Beispiele bewerten; unter "
        "0.70 anhand seiner konkreten Hinweise überarbeiten und erneut bewerten. "
        "Anschließend prüft `reviewer` die Kampagnenregeln. Trage den finalen Text "
        "direkt im `text:`-Feld ein. Kreuze nichts an."
    ),
    "find-and-write-reshares": (
        "engagement-scout",
        "Lies @config/personal_profile.yaml, @team/engagement-scout/memory.md, "
        "@team/style/profile.md, @team/style/learning.json, aktuelle Beispiele unter "
        "@team/style/approved/ und die vollständige Kampagne @{campaign}. Sammle mit "
        "`./bin/li-jobs --campaign \"{campaign}\" "
        "find-reshares --limit {count}` exakt passende Fremdbeiträge als "
        "Reshare-Kandidaten. Die Keyword-Suche ist nur die Vorauswahl. Prüfe den "
        "vollständigen Originalpost aus `note:` semantisch gegen objective, audience, "
        "topics, banned_topics, products und CTA. Verwirf zufällige Keyword-Treffer. "
        "Lass `content_strategist` mit vollständigem Originalpost und Kampagnenkontext "
        "für jeden Kandidaten entscheiden: "
        "(a) `reshare_with_comment: true`, wenn eine eigene Perspektive echten Mehrwert "
        "liefert; dann injiziere beim `copywriter` zusätzlich "
        "@team/copywriter/memory.md und lasse einen persönlichen Begleittext in der Sprache "
        "des Originalbeitrags schreiben, der CTA und Pflicht-Hashtags der Kampagne berücksichtigt und "
        "erfindet keine Fakten, oder (b) `reshare_with_comment: false` und leeres `text:`, "
        "wenn der Originalbeitrag allein als Awareness-Signal stärker ist. Lass Begleittexte "
        "von `style_evaluator` und alle Kandidaten von `reviewer` prüfen. Bearbeite nur die "
        "neu erzeugten Reshare-Einträge in approvals.md. Veröffentliche nichts, plane nichts "
        "ein und setze keine Freigabe."
    ),
    "find-and-write-connections": (
        "engagement-scout",
        "Lies die vollständige Kampagne @{campaign}, @config/personal_profile.yaml, "
        "@team/style/profile.md und @team/style/learning.json. Leite aus audience und "
        "personas eine priorisierte Liste konkreter Rollen ab, zum Beispiel Compliance "
        "Officer, CIO, Records Management oder ECM/DMS-Verantwortliche, sofern sie zur "
        "Kampagne passen. Die erste Suche muss eine eng passende, in audience oder personas "
        "belegte Fachrolle verwenden, bevorzugt Compliance Officer, Records Manager oder "
        "ECM/DMS-Verantwortliche. CIO ist ein Mitentscheider-Fallback. Suche nicht pauschal "
        "nach Head of IT oder Digitalisierung ohne Dokument-, Records- oder Compliancebezug. "
        "Führe nacheinander höchstens drei Suchläufe mit "
        "`./bin/li-jobs --campaign \"{campaign}\" find-connections --query "
        "\"<konkrete Rolle>\" --limit <noch fehlende Anzahl>` aus und stoppe, sobald "
        "insgesamt {count} neue Kandidaten angelegt wurden. "
        "Das Werkzeug übernimmt nur Profile, die eine sichtbare Vernetzen-Aktion haben; "
        "bereits vernetzte oder ausstehend angefragte Profile sind ausgeschlossen. "
        "Falls ein Suchlauf `linkedin_ui_selector_mismatch` meldet, führe keine weiteren "
        "Suchläufe aus und gib diesen Fehlercode unverändert im Endergebnis aus, damit der "
        "Scheduler die automatische Codex-Scriptreparatur starten kann. "
        "Behalte jeden neuen Kandidaten in approvals.md. Bewerte die Rollen- und "
        "Zielgruppenpassung anhand des gespeicherten Profiltexts mit `fit_score` von 0.0 "
        "bis 1.0 und einer konkreten kurzen Begründung in `fit_note`. Erfinde keine Rolle, "
        "Firma, Gemeinsamkeit oder persönliche Beziehung. Für passende Kandidaten schreibe "
        "mit dem `copywriter` eine individuelle Vernetzungsnotiz mit höchstens 300 Zeichen "
        "in `text:`. Bei zu geringer oder nicht belegbarer Passung bleibt `text:` leer, "
        "der Kandidat aber sichtbar. Sortiere neue Kandidaten absteigend nach fit_score. "
        "Lass Notizen vom `style_evaluator` und `reviewer` prüfen. Veröffentliche nichts, "
        "sende keine Anfrage, plane nichts ein und setze keine Freigabe."
    ),
}


def _approvals(campaign: str) -> list[q.QueueItem]:
    campaign_path = Path(campaign)
    if not campaign_path.is_absolute():
        campaign_path = ROOT / campaign_path
    return q.parse(campaign_path.parent / "queue" / "approvals.md")


def _approval_path(campaign: str) -> Path:
    campaign_path = Path(campaign)
    if not campaign_path.is_absolute():
        campaign_path = ROOT / campaign_path
    return campaign_path.parent / "queue" / "approvals.md"


def _schedule_path(campaign: str) -> Path:
    campaign_path = Path(campaign)
    if not campaign_path.is_absolute():
        campaign_path = ROOT / campaign_path
    return campaign_path.parent / "queue" / "schedule.md"


def _prepare_generated_items(campaign_path: str, before: dict[str, str]) -> dict:
    """Bewertet neue/geänderte Agententexte und ergänzt den Terminvorschlag."""
    path = _approval_path(campaign_path)
    items = q.parse(path)
    target_ids = {
        item.id
        for item in items
        if item.text.strip() and (item.id not in before or before[item.id] != item.text)
    }
    if not target_ids:
        return {"items": [], "low_score_ids": []}
    source_job_id = os.environ.get("LI_JOB_ID")
    if source_job_id:
        for item in items:
            if item.id in target_ids:
                item.source_job_id = source_job_id
    campaign_file = Path(campaign_path)
    if not campaign_file.is_absolute():
        campaign_file = ROOT / campaign_file
    prepared = prepare_items(
        ROOT,
        load_campaign(campaign_file),
        items,
        target_ids,
        q.parse(_schedule_path(campaign_path)),
    )
    q.write(
        path,
        items,
        "Freigaben — warten auf deine Bestätigung",
        "Kreuze `- [x] freigeben` an, was raus darf. Texte und Terminvorschläge sind editierbar.",
    )
    return {
        "items": prepared,
        "low_score_ids": [row["id"] for row in prepared if row["score"] < 0.70],
    }


def _revise_low_scores(campaign: str, item_ids: list[str]) -> dict:
    ids = ", ".join(f"`{item_id}`" for item_id in item_ids)
    prompt = (
        f"Öffne die Freigabe-Queue der Kampagne @{campaign}. Überarbeite ausschließlich "
        f"die Textfelder der Einträge {ids}. Ihr lokaler Freigabe-Score liegt unter "
        "0.70. Lies je Eintrag `evaluation_note`, außerdem @team/style/profile.md, "
        "@team/style/learning.json und die neuesten Beispiele unter "
        "@team/style/approved/. Passe Wortwahl, persönliche Perspektive und Rhythmus "
        "an die gelernten Nutzerkorrekturen an. Bewerte nach der Überarbeitung erneut; "
        "Zielwert mindestens 0.70. Ändere niemals ID, URL, Originalbeitrag, Termin oder "
        "Freigabestatus und veröffentliche nichts."
    )
    return run_agent(
        "style-evaluator", prompt, timeout=timeouts.load(ROOT).style_revision * 60
    )


def _set_presented_baseline(campaign: str, item_ids: list[str]) -> None:
    """Automatische Revisionen gehören zum Entwurf, nicht zu Nutzeränderungen."""
    path = _approval_path(campaign)
    items = q.parse(path)
    selected = set(item_ids)
    for item in items:
        if item.id in selected:
            item.generated_text = item.text
    q.write(
        path,
        items,
        "Freigaben — warten auf deine Bestätigung",
        "Kreuze `- [x] freigeben` an, was raus darf. Texte und Terminvorschläge sind editierbar.",
    )


def _run_idea_job(count: int) -> dict:
    """Offene Ideen einzeln in nachvollziehbare Freigabe-Entwürfe verwandeln."""
    entries = idea_store.load(ROOT)
    selected = [idea for idea in entries if idea.status == "open"][:count]
    if not selected:
        return {"ok": True, "processed": 0, "results": []}

    results: list[dict] = []
    for idea in selected:
        idea.status = "processing"
        idea.last_error = None
        idea_store.save(ROOT, entries)
        campaign = idea.campaign or PERSONAL_CAMPAIGN
        before_items = _approvals(campaign)
        before_ids = {item.id for item in before_items}
        campaign_lens = (
            f"Lies und befolge zusätzlich die Kampagne @{campaign}. Nutze deren "
            "Zielgruppe, Themen, Grenzen und CTA als Kampagnenbrille."
            if idea.campaign
            else "Die Idee hat bewusst keine Kampagne. Nutze keine Produkt- oder "
            "Kampagnen-CTA und erfinde keine Fakten. Schreibe einfach einen starken "
            "persönlichen LinkedIn-Post; die persönliche Kampagne dient nur als Ablage."
        )
        prompt = (
            "Lies @config/personal_profile.yaml, @team/style/profile.md, "
            "@team/style/learning.json und die jüngsten freigegebenen Beispiele. "
            f"Aus dieser Idee soll genau ein fertiger LinkedIn-Post werden:\n\n{idea.text}\n\n"
            f"{campaign_lens} Behalte die Aussage der Idee bei und ergänze keinerlei "
            "Biografie-, Unternehmens- oder Projektdetails, die nicht in Idee oder Profil "
            "stehen. Lass `style_evaluator` bewerten und bei Score unter 0.70 durch den "
            "Copywriter überarbeiten; danach prüft `reviewer`. Lege exakt einen finalen "
            f"Entwurf mit `./bin/li-jobs --campaign \"{campaign}\" add --kind post "
            "--text \"...\"` in die Freigabe. Veröffentliche nichts und setze keine Freigabe."
        )
        agent_result = run_agent(
            "content-strategist",
            prompt,
            timeout=timeouts.task_seconds(ROOT, "ideas-to-posts"),
        )
        after = _approvals(campaign)
        created = [
            item for item in after if item.kind == "post" and item.id not in before_ids
        ]
        if agent_result.get("ok") and len(created) == 1:
            preparation = _prepare_generated_items(
                campaign, {item.id: item.text for item in before_items}
            )
            low = preparation["low_score_ids"]
            revision = None
            if low:
                revision = _revise_low_scores(campaign, low)
                baseline = {
                    item.id: ("" if item.id in low else item.text)
                    for item in _approvals(campaign)
                }
                preparation = _prepare_generated_items(campaign, baseline)
                _set_presented_baseline(campaign, low)
            idea.status = "done"
            idea.output_id = created[0].id
            idea.output_campaign = campaign
            results.append(
                {
                    "idea_id": idea.id,
                    "ok": True,
                    "output_id": idea.output_id,
                    "campaign": campaign,
                    "evaluation": preparation,
                    "style_revision": revision,
                }
            )
        else:
            idea.status = "failed"
            error = agent_result.get("error") or agent_result.get("stderr") or (
                f"expected_one_post_created:created={len(created)}"
            )
            idea.last_error = str(error)[-1000:]
            results.append({"idea_id": idea.id, "ok": False, "error": idea.last_error})
        idea_store.save(ROOT, entries)
    return {
        "ok": all(result["ok"] for result in results),
        "processed": len(results),
        "results": results,
    }


def _verify_artifacts(job: str, campaign: str, count: int, before_ids: set[str], result: dict) -> dict:
    """Queue-Artefakte sind für erzeugende Jobs die maßgebliche Erfolgskontrolle."""
    kinds = {
        "draft-posts": "post",
        "find-and-write": "comment",
        "find-and-write-reshares": "reshare",
        "find-and-write-connections": "connection",
    }
    expected_kind = kinds.get(job)
    if expected_kind is None:
        return result
    created_items = [
        item for item in _approvals(campaign)
        if item.kind == expected_kind
        and item.id not in before_ids
    ]
    created = [item.id for item in created_items]
    if expected_kind == "post":
        created = [item.id for item in created_items if item.text.strip()]
    elif expected_kind == "comment":
        created = [
            item.id for item in created_items
            if item.text.strip() or item.fit_score is not None
        ]
    elif expected_kind == "connection":
        created = [
            item.id for item in created_items
            if item.fit_score is not None
            and (not item.text.strip() or len(item.text.strip()) <= 300)
        ]
    elif expected_kind == "reshare":
        created = [
            item.id for item in created_items
            if item.text.strip() or not item.reshare_with_comment
        ]
    result["artifacts"] = {
        "created_items": created,
        f"created_{expected_kind}s": created,
        "expected": count,
    }
    if len(created) >= count:
        if not result.get("ok"):
            result["agent_warning"] = result.get("error") or "agent_exit_failed"
            result["error"] = None
            result["ok"] = True
            result["recovered_from_artifacts"] = True
        return result
    if result.get("ok"):
        result["ok"] = False
        labels = {
            "draft-posts": "Post-Entwürfe",
            "find-and-write": "Kommentar-Entwürfe",
            "find-and-write-reshares": "Reshare-Entwürfe",
            "find-and-write-connections": "Vernetzungskandidaten",
        }
        result["error"] = (
            f"Keine ausreichenden fertigen {labels[job]} erzeugt: "
            f"erwartet {count}, erstellt {len(created)}."
        )
    return result


def main() -> None:
    parser = argparse.ArgumentParser(prog="li-brain", description=__doc__)
    parser.add_argument("--campaign", required=True)
    parser.add_argument(
        "job", choices=sorted(PROMPTS) + ["ideas-to-posts", "check", "probe"]
    )
    parser.add_argument("--count", type=int, default=2)
    parser.add_argument("--dry-run", action="store_true", help="nur den Prompt zeigen")
    args = parser.parse_args()

    status = cli_status()
    engine = selected_engine(status)
    if args.job == "check":
        _emit({"ok": bool(engine), "selected": engine, "engines": status})
        raise SystemExit(0 if engine else 1)
    if args.job == "probe":
        result = probe_cli(status=status)
        result["engines"] = status
        _emit(result)
        raise SystemExit(0 if result["ok"] else 1)
    if not engine:
        _emit({"ok": False, "error": "Weder Codex noch Copilot CLI ist einsatzbereit.", "engines": status})
        raise SystemExit(1)
    if args.count < 1:
        _emit({"ok": False, "error": "count_must_be_positive"})
        raise SystemExit(2)

    if args.job == "ideas-to-posts":
        result = _run_idea_job(args.count)
        _emit(result)
        raise SystemExit(0 if result["ok"] else 1)

    agent, template = PROMPTS[args.job]
    prompt = template.format(campaign=args.campaign, count=args.count)
    if args.dry_run:
        _emit({"ok": True, "engine": engine, "agent": CODEX_AGENTS[agent], "prompt": prompt})
        raise SystemExit(0)

    before_items = _approvals(args.campaign)
    before_ids = {item.id for item in before_items}
    before_text = {item.id: item.text for item in before_items}
    result = run_agent(agent, prompt, timeout=timeouts.task_seconds(ROOT, args.job))
    result = _verify_artifacts(args.job, args.campaign, args.count, before_ids, result)
    preparation = _prepare_generated_items(args.campaign, before_text)
    result["evaluation"] = preparation

    low_score_ids = preparation["low_score_ids"]
    if result.get("ok") and low_score_ids:
        revision = _revise_low_scores(args.campaign, low_score_ids)
        result["style_revision"] = revision
        # Der zweite Durchlauf berechnet den sichtbaren Score auf dem revidierten Text.
        revised_before = {
            item.id: ("" if item.id in low_score_ids else item.text)
            for item in _approvals(args.campaign)
        }
        result["evaluation_after_revision"] = _prepare_generated_items(
            args.campaign, revised_before
        )
        _set_presented_baseline(args.campaign, low_score_ids)
        if not revision.get("ok"):
            result["evaluation_warning"] = (
                "Die automatische Stilüberarbeitung war nicht verfügbar; der Entwurf "
                "bleibt mit sichtbarem Score zur manuellen Bearbeitung erhalten."
            )
    _emit(result)
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
