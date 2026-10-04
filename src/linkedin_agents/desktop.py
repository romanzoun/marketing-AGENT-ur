"""Einfaches Fenster zum Starten, Aktualisieren und Beenden der lokalen App."""
from __future__ import annotations

import os
import subprocess
import sys
from urllib.parse import urlsplit, urlunsplit
import threading
import tkinter as tk
import webbrowser
from pathlib import Path
from tkinter import messagebox

import yaml

ROOT = Path(__file__).resolve().parents[2]
URL = "http://127.0.0.1:8765"


def update_settings() -> tuple[str, str]:
    data = yaml.safe_load((ROOT / "config" / "update.yaml").read_text(encoding="utf-8")) or {}
    return str(data.get("repository") or ""), str(data.get("branch") or "main")


def authenticated_repository(repository: str, token: str) -> str:
    """Erzeugt die Abruf-URL, ohne den Token dauerhaft zu speichern."""
    parts = urlsplit(repository)
    if not token or parts.scheme not in {"https", "http"}:
        return repository
    return urlunsplit(parts._replace(netloc=f"x-access-token:{token}@{parts.netloc}"))


class AppLauncher:
    def __init__(self) -> None:
        self.process: subprocess.Popen[str] | None = None
        self.window = tk.Tk()
        self.window.title("Sara's Marketing AGENT-ur")
        self.window.geometry("460x250")
        self.window.resizable(False, False)
        self.status = tk.StringVar(value="Bereit.")
        self._build()
        self.window.protocol("WM_DELETE_WINDOW", self.quit)
        self.window.after(300, lambda: threading.Thread(target=self._ensure_latest, daemon=True).start())

    def _build(self) -> None:
        frame = tk.Frame(self.window, padx=18, pady=18)
        frame.pack(fill="both", expand=True)
        tk.Label(frame, text="LinkedIn Automation", font=("Helvetica", 18, "bold")).pack(anchor="w")
        tk.Label(
            frame,
            text="Startet die lokale Oberfläche für dieses Teammitglied.",
            wraplength=410,
            justify="left",
        ).pack(anchor="w", pady=(4, 16))
        buttons = tk.Frame(frame)
        buttons.pack(anchor="w")
        tk.Button(buttons, text="Starten", width=14, command=self.start).pack(side="left")
        tk.Button(buttons, text="Aktualisieren", width=14, command=self.update).pack(side="left", padx=8)
        tk.Button(buttons, text="Beenden", width=14, command=self.quit).pack(side="left")
        tk.Label(frame, textvariable=self.status, wraplength=410, justify="left").pack(anchor="w", pady=(18, 0))

    def start(self) -> None:
        if self.process and self.process.poll() is None:
            webbrowser.open(URL)
            self.status.set("Die Oberfläche läuft bereits.")
            return
        env = os.environ.copy()
        env["PYTHONPATH"] = str(ROOT / "src")
        self.process = subprocess.Popen(
            [sys.executable, "-m", "linkedin_agents.web.app"],
            cwd=ROOT,
            env=env,
        )
        webbrowser.open(URL)
        self.status.set("Gestartet. Browser wird geöffnet.")

    def update(self) -> None:
        threading.Thread(target=self._update, daemon=True).start()

    def _ensure_latest(self) -> None:
        if self._update(restart_when_unchanged=False):
            self._restart_after_update()

    def _update(self, *, restart_when_unchanged: bool = True) -> bool:
        self._set_status("Aktualisierung wird geprüft …")
        if not (ROOT / ".git").exists():
            self._set_status("Kein GitHub-Checkout gefunden.")
            return False
        repository, branch = update_settings()
        token = os.getenv("GITHUB_TOKEN", "").strip()
        fetch_repository = authenticated_repository(repository, token)
        try:
            subprocess.run(["git", "remote", "set-url", "origin", repository], cwd=ROOT, check=True)
            subprocess.run(
                ["git", "fetch", fetch_repository, branch],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=True,
            )
            local = subprocess.run(
                ["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True
            ).stdout.strip()
            remote = subprocess.run(
                ["git", "rev-parse", f"origin/{branch}"], cwd=ROOT, capture_output=True, text=True, check=True
            ).stdout.strip()
            if local == remote:
                self._set_status("Neueste Version ist bereits installiert.")
                return False
            dirty = subprocess.run(
                ["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True, check=True
            )
            if dirty.stdout.strip():
                self._set_status("Update gestoppt: lokale Änderungen vorhanden.")
                return False
            subprocess.run(
                ["git", "pull", "--ff-only", fetch_repository, branch],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=True,
            )
        except (OSError, subprocess.CalledProcessError, yaml.YAMLError) as exc:
            detail = getattr(exc, "stderr", "") or str(exc)
            if token:
                detail = detail.replace(token, "[verborgen]")
            self._set_status(f"Update fehlgeschlagen: {detail.strip()[:180]}")
            return False
        if restart_when_unchanged:
            self._restart_after_update()
        return True

    def _restart_after_update(self) -> None:
        if self.process and self.process.poll() is None:
            self.process.terminate()
            try:
                self.process.wait(timeout=8)
            except subprocess.TimeoutExpired:
                self.process.kill()
        self.window.after(0, self.start)
        self._set_status("Aktualisiert und neu gestartet.")

    def _set_status(self, text: str) -> None:
        self.window.after(0, self.status.set, text)

    def quit(self) -> None:
        if self.process and self.process.poll() is None:
            self.process.terminate()
        self.window.destroy()

    def run(self) -> None:
        self.window.mainloop()


def main() -> None:
    try:
        AppLauncher().run()
    except tk.TclError as exc:
        messagebox.showerror("LinkedIn Automation", f"Fenster konnte nicht geöffnet werden: {exc}")
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
