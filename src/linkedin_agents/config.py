"""Laufzeit-Konfiguration aus Umgebungsvariablen (.env)."""
from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import time

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    cdp_endpoint: str
    log_level: str
    image_provider: str
    openai_api_key: str
    image_model: str
    working_hours_start: time
    working_hours_end: time
    linkedin_action_delay_ms: int


def _env_time(name: str, default: str) -> time:
    value = os.getenv(name, default).strip()
    try:
        return time.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"{name} muss eine Uhrzeit wie 08:00 enthalten") from exc


def _env_int(name: str, default: int, *, minimum: int, maximum: int) -> int:
    try:
        value = int(os.getenv(name, str(default)))
    except ValueError as exc:
        raise ValueError(f"{name} muss eine ganze Zahl enthalten") from exc
    if not minimum <= value <= maximum:
        raise ValueError(f"{name} muss zwischen {minimum} und {maximum} liegen")
    return value


def load_settings() -> Settings:
    return Settings(
        cdp_endpoint=os.getenv("CDP_ENDPOINT", "http://localhost:9222"),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
        image_provider=os.getenv("IMAGE_PROVIDER", "none"),
        openai_api_key=os.getenv("OPENAI_API_KEY", ""),
        image_model=os.getenv("IMAGE_MODEL", "gpt-image-1"),
        working_hours_start=_env_time("WORKING_HOURS_START", "08:00"),
        working_hours_end=_env_time("WORKING_HOURS_END", "17:00"),
        linkedin_action_delay_ms=_env_int(
            "LINKEDIN_ACTION_DELAY_MS", 2000, minimum=0, maximum=10_000
        ),
    )
