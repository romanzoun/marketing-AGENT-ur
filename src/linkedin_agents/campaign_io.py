"""Sicherer Import, Export und unveränderliche Versionen von Kampagnen."""
from __future__ import annotations

import re
from pathlib import Path

import yaml

from .models.campaign import Campaign, load_campaign


def campaign_files(root: Path) -> list[Path]:
    base = root / "Kampagnen"
    if not base.exists():
        return []
    return sorted(
        path
        for path in base.rglob("*.yaml")
        if "queue" not in path.parts
        and "versions" not in path.parts
        and (path.parent == base or path.name == "kampagne.yaml")
    )


def resolve_campaign(root: Path, relative: str) -> Path:
    base = (root / "Kampagnen").resolve()
    target = (root / relative).resolve()
    if not target.is_relative_to(base) or target.suffix.lower() not in {".yaml", ".yml"}:
        raise ValueError("Ungültiger Kampagnenpfad.")
    return target


def _dump(campaign: Campaign) -> str:
    return yaml.safe_dump(
        campaign.model_dump(mode="json"), allow_unicode=True, sort_keys=False
    )


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(f"{path.suffix}.tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def _versions_dir(path: Path) -> Path:
    return (
        path.parent / "versions"
        if path.name == "kampagne.yaml"
        else path.parent / "versions" / path.stem
    )


def _snapshot(path: Path, campaign: Campaign) -> Path:
    snapshot = _versions_dir(path) / f"v{campaign.version:04d}.yaml"
    if not snapshot.exists():
        _atomic_write(snapshot, _dump(campaign))
    return snapshot


def ensure_current_snapshot(path: Path) -> Path:
    """Legt für vor der Versionierung vorhandene Kampagnen einmalig v1 an."""
    return _snapshot(path, load_campaign(path))


def save_new_version(path: Path, campaign: Campaign, expected_version: int) -> Campaign:
    current = load_campaign(path)
    if current.version != expected_version:
        raise RuntimeError(
            f"Kampagne wurde inzwischen geändert (aktuell v{current.version}, "
            f"Formular v{expected_version}). Bitte neu laden."
        )
    _snapshot(path, current)
    updated = campaign.model_copy(update={"version": current.version + 1})
    _atomic_write(path, _dump(updated))
    _snapshot(path, updated)
    return updated


def export_yaml(path: Path) -> str:
    return _dump(load_campaign(path))


def _slug(value: str) -> str:
    normalized = value.casefold().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
    normalized = re.sub(r"[^a-z0-9]+", "-", normalized).strip("-")
    return normalized[:80] or "kampagne"


def import_yaml(root: Path, filename: str, content: str) -> tuple[Path, Campaign]:
    if len(content.encode("utf-8")) > 250_000:
        raise ValueError("Kampagnendatei ist größer als 250 KB.")
    try:
        raw = yaml.safe_load(content) or {}
        campaign = Campaign.model_validate(raw)
    except Exception as exc:
        raise ValueError(f"Ungültige Kampagnendatei: {exc}") from exc

    fallback = Path(filename).stem if filename else campaign.name
    base = root / "Kampagnen"
    stem = _slug(campaign.name or fallback)
    target = base / stem / "kampagne.yaml"
    suffix = 2
    while target.exists():
        target = base / f"{stem}-{suffix}" / "kampagne.yaml"
        suffix += 1
    _atomic_write(target, _dump(campaign))
    _snapshot(target, campaign)
    return target, campaign


def import_as_version(
    root: Path, target_relative: str, content: str
) -> tuple[Path, Campaign]:
    """Importiert YAML als nächste Version einer bestehenden Kampagne."""
    if len(content.encode("utf-8")) > 250_000:
        raise ValueError("Kampagnendatei ist größer als 250 KB.")
    try:
        raw = yaml.safe_load(content) or {}
        imported = Campaign.model_validate(raw)
    except Exception as exc:
        raise ValueError(f"Ungültige Kampagnendatei: {exc}") from exc

    target = resolve_campaign(root, target_relative)
    if not target.is_file():
        raise ValueError("Die bestehende Kampagne wurde nicht gefunden.")
    current = load_campaign(target)
    try:
        updated = save_new_version(target, imported, current.version)
    except RuntimeError as exc:
        raise ValueError(str(exc)) from exc
    return target, updated


def versions(path: Path) -> list[dict]:
    rows: list[dict] = []
    for snapshot in sorted(_versions_dir(path).glob("v*.yaml"), reverse=True):
        try:
            campaign = load_campaign(snapshot)
        except Exception:
            continue
        rows.append(
            {
                "version": campaign.version,
                "file": snapshot.name,
                "modified_at": snapshot.stat().st_mtime,
            }
        )
    return rows
