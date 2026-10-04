"""Persönlicher Kontext des LinkedIn-Accounts (CV, Rolle, Expertise)."""
from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel, Field


class PersonalProfile(BaseModel):
    name: str = "Roman"
    current_role: str = ""
    company: str = ""
    headline: str = ""
    about: str = ""
    cv: str = ""
    expertise: list[str] = Field(default_factory=list)
    perspectives: list[str] = Field(default_factory=list)


def path(root: Path) -> Path:
    return root / "config" / "personal_profile.yaml"


def load(root: Path) -> PersonalProfile:
    source = path(root)
    if not source.exists():
        return PersonalProfile()
    data = yaml.safe_load(source.read_text(encoding="utf-8")) or {}
    return PersonalProfile.model_validate(data)


def save(root: Path, profile: PersonalProfile) -> None:
    target = path(root)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        yaml.safe_dump(profile.model_dump(), allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
