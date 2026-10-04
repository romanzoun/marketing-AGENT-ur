"""Health-Check: Edge/LinkedIn sowie Codex CLI einsatzbereit?

Ohne offenen CDP-Port und eingeloggte Session laufen alle Cron-Jobs ins Leere.
Dieses Skript prüft beides, startet Edge bei Bedarf und meldet Probleme
(macOS-Benachrichtigung + Logdatei).

    ./bin/li-health              # prüfen, Edge bei Bedarf starten
    ./bin/li-health --no-start   # nur prüfen (für Cron vor dem Posten)
    ./bin/li-health --quiet      # ohne Benachrichtigung

Exit: 0 = ok | 1 = nicht eingeloggt | 2 = CDP nicht erreichbar
"""
from __future__ import annotations

import argparse
import asyncio
import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / ".runs" / "health.log"
START_LOCK = ROOT / ".runs" / "health.start-lock"
START_COOLDOWN_MIN = 15  # nicht öfter als alle 15 Min versuchen, Edge zu starten
EDGE = "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
PROFILE = Path.home() / "edge-linkedin"


def log(line: str) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(f"{datetime.now().isoformat(timespec='seconds')} | {line}\n")
    print(line, flush=True)


def notify(title: str, message: str, quiet: bool) -> None:
    if quiet or sys.platform != "darwin":
        return
    try:
        subprocess.run(
            ["osascript", "-e", f'display notification "{message}" with title "{title}"'],
            timeout=5,
            capture_output=True,
        )
    except Exception:
        pass


def cdp_alive(endpoint: str, attempts: int = 3) -> dict | None:
    """Mehrere Versuche, bevor der Port als tot gilt (vermeidet Fehlalarme unter Last)."""
    for i in range(attempts):
        try:
            r = httpx.get(f"{endpoint}/json/version", timeout=4)
            r.raise_for_status()
            return r.json()
        except Exception:
            if i < attempts - 1:
                time.sleep(1.5)
    return None


def edge_running() -> bool:
    try:
        out = subprocess.run(["pgrep", "-f", "Microsoft Edge"], capture_output=True, text=True, timeout=5)
        return bool(out.stdout.strip())
    except Exception:
        return False


def start_cooldown_active() -> bool:
    """Verhindert Tab-/Fenster-Lawinen: Edge höchstens alle START_COOLDOWN_MIN starten."""
    if not START_LOCK.exists():
        return False
    age_min = (time.time() - START_LOCK.stat().st_mtime) / 60
    return age_min < START_COOLDOWN_MIN


def mark_start_attempt() -> None:
    START_LOCK.parent.mkdir(parents=True, exist_ok=True)
    START_LOCK.touch()


def linkedin_tabs(endpoint: str) -> list[str]:
    try:
        r = httpx.get(f"{endpoint}/json", timeout=3)
        r.raise_for_status()
        return [
            p.get("url", "")
            for p in r.json()
            if p.get("type") == "page" and "linkedin.com" in p.get("url", "")
        ]
    except Exception:
        return []


def start_edge(port: int) -> None:
    subprocess.Popen(
        [
            EDGE,
            f"--remote-debugging-port={port}",
            f"--user-data-dir={PROFILE}",
            "--no-first-run",
            "--no-default-browser-check",
            "https://www.linkedin.com/feed/",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )


async def session_ok(endpoint: str) -> bool:
    sys.path.insert(0, str(ROOT / "src"))
    from linkedin_agents.browser.linkedin import LinkedInClient

    try:
        async with LinkedInClient(endpoint) as client:
            return await client.ensure_logged_in()
    except Exception as exc:
        log(f"Session-Prüfung fehlgeschlagen: {exc}")
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--endpoint", default="http://localhost:9222")
    parser.add_argument("--no-start", action="store_true", help="Edge nicht automatisch starten")
    parser.add_argument("--quiet", action="store_true", help="keine Benachrichtigung")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    port = int(args.endpoint.rsplit(":", 1)[-1])
    result = {
        "cdp": False,
        "logged_in": False,
        "tabs": 0,
        "started_edge": False,
        "codex": False,
        "brain_cli": None,
    }

    sys.path.insert(0, str(ROOT / "src"))
    from linkedin_agents import brain

    cli_status = brain.cli_status()
    result["codex"] = bool(cli_status["codex"]["available"])
    result["brain_cli"] = brain.selected_engine(cli_status)
    result["brain_clis"] = cli_status
    if not result["brain_cli"]:
        log("WARNUNG: Codex CLI ist nicht einsatzbereit.")
        notify(
            "AGENT-ur: KI-CLI fehlt",
            "Codex CLI installieren und mit `codex login` einloggen.",
            args.quiet,
        )

    version = cdp_alive(args.endpoint)
    if version is None and not args.no_start:
        if edge_running():
            # Edge läuft schon (anderes Profil/Port oder kurz beschäftigt) —
            # NICHT noch einen Prozess/Tab aufmachen, nur warten und neu prüfen.
            log("Edge läuft bereits, aber CDP antwortet nicht — warte, starte NICHT neu.")
            for _ in range(5):
                time.sleep(2)
                version = cdp_alive(args.endpoint)
                if version:
                    break
        elif start_cooldown_active():
            log(f"Start-Cooldown aktiv (< {START_COOLDOWN_MIN} Min seit letztem Versuch) — überspringe Start.")
        else:
            log(f"CDP nicht erreichbar, kein Edge-Prozess gefunden — starte Edge mit --remote-debugging-port={port} …")
            mark_start_attempt()
            start_edge(port)
            result["started_edge"] = True
            for _ in range(15):
                time.sleep(2)
                version = cdp_alive(args.endpoint)
                if version:
                    break

    if version is None:
        log("FEHLER: CDP nicht erreichbar — Edge läuft nicht mit Debug-Port.")
        notify("AGENT-ur: Browser offline", "Edge mit --remote-debugging-port=9222 starten.", args.quiet)
        if args.json:
            print(json.dumps(result))
        return 2

    result["cdp"] = True
    result["browser"] = version.get("Browser", "")
    result["tabs"] = len(linkedin_tabs(args.endpoint))

    if not asyncio.run(session_ok(args.endpoint)):
        log("FEHLER: LinkedIn-Session nicht eingeloggt.")
        notify("AGENT-ur: LinkedIn-Login nötig", "Bitte im Edge-Fenster bei LinkedIn anmelden.", args.quiet)
        if args.json:
            print(json.dumps(result))
        return 1

    result["logged_in"] = True
    log(
        f"OK — {result['browser']}, {result['tabs']} LinkedIn-Tab(s), "
        f"eingeloggt, brain_cli={result['brain_cli']}."
    )
    if args.json:
        print(json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
