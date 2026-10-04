"""Sara's Marketing AGENT-ur — API der Weboberfläche.

Arbeitet auf den bestehenden Markdown-Warteschlangen (`queue.py`) als einziger
Quelle der Wahrheit — dieselben Dateien, die Codex-Agenten und Cron nutzen.
Bewusst keine zusätzliche Datenbank, damit es keine zwei Wahrheiten gibt.

Start:  ./bin/li-ui   →  http://127.0.0.1:8765
"""
from __future__ import annotations

import asyncio
import base64
import binascii
import json
import os
import shlex
import subprocess
import sys
from datetime import datetime, time as dt_time, timedelta
from pathlib import Path
from typing import Literal

import yaml
import httpx
from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import FileResponse, HTMLResponse, Response
from pydantic import BaseModel, Field

from .. import automation as auto
from .. import analytics as campaign_analytics
from .. import campaign_io
from .. import brain
from .. import ideas as idea_store
from .. import planning
from .. import queue as q
from .. import timeouts
from ..browser.linkedin import LinkedInClient
from ..config import load_settings
from ..imaging.workflow import (
    clear_image,
    remove_image_file,
    set_generated_image,
    set_web_image,
)
from ..models.campaign import Campaign, load_campaign
from ..personal_profile import PersonalProfile, load as load_personal_profile
from ..personal_profile import save as save_personal_profile
from ..style_learning import (
    auto_approval_stats,
    job_trust,
    learn_approval,
    learn_edit,
    learn_rejection,
    learn_rewrite,
    learning_status,
    prepare_items,
    score_threshold,
)
from ..auto_approval import approve_above_score

ROOT = Path(__file__).resolve().parents[3]
CAMPAIGN_DIR = ROOT / "Kampagnen"
STATIC = Path(__file__).parent / "static"

STAGES = {
    "approvals": ("Freigaben — warten auf deine Bestätigung",
                  "Kreuze `- [x] freigeben` an, was raus darf."),
    "schedule": ("Einplanung — freigegeben, wartet auf den Zeitpunkt",
                 "Wird von `li-jobs run-due` zum geplanten Zeitpunkt ausgeführt."),
    "log": ("Log — ausgeführt", "Bereits ausgeführte Einträge."),
}

app = FastAPI(title="Sara's Marketing AGENT-ur")
SCHEDULER_MARKER = "# linkedin-automation-scheduler"


def _queue_path(campaign: str, stage: str) -> Path:
    if stage not in STAGES:
        raise HTTPException(400, f"Unbekannte Stufe: {stage}")
    return ROOT / Path(campaign).parent / "queue" / f"{stage}.md"


def _load(campaign: str, stage: str) -> list[q.QueueItem]:
    return q.parse(_queue_path(campaign, stage))


def _save(campaign: str, stage: str, items: list[q.QueueItem]) -> None:
    title, hint = STAGES[stage]
    q.write(_queue_path(campaign, stage), items, title, hint)


def _next_free_slot(taken: set[str], slots: list[str], active_hours) -> datetime:
    lo, hi = active_hours
    for day_offset in range(90):
        day = (datetime.now() + timedelta(days=day_offset)).date()
        for s in slots or ["09:00"]:
            hh, mm = (s.split(":") + ["0"])[:2]
            when = datetime.combine(day, dt_time(int(hh), int(mm)))
            if when < datetime.now() or not (lo <= when.hour < hi):
                continue
            if when.isoformat(timespec="minutes") in taken:
                continue
            return when
    raise HTTPException(409, "Kein freier Termin in den nächsten 90 Tagen.")


class ItemPatch(BaseModel):
    campaign: str
    stage: str
    text: str | None = None
    note: str | None = None
    user_memory_note: str | None = Field(default=None, max_length=2000)
    publish_at: str | None = None
    match_publish_at: str | None = None
    reshare_with_comment: bool | None = None


class RewriteBody(BaseModel):
    campaign: str
    instruction: str = Field(min_length=2, max_length=1200)


class ApproveBody(BaseModel):
    campaign: str
    publish_at: str | None = None
    slots: str = "09:00,13:00"


class BulkApproveBody(BaseModel):
    campaign: str
    minimum_score: float = Field(ge=0, le=1)


class ImageBody(BaseModel):
    campaign: str
    source: Literal["generated", "web"] = "generated"
    prompt: str = Field(default="", max_length=4000)


class ImageUploadBody(BaseModel):
    campaign: str
    filename: str = Field(default="upload", max_length=255)
    content_type: Literal["image/png", "image/jpeg"]
    data: str = Field(min_length=4, max_length=14_000_000)


class CampaignRef(BaseModel):
    campaign: str


class IdeaCreate(BaseModel):
    text: str = Field(min_length=1, max_length=10_000)
    campaign: str | None = None


class IdeaPatch(BaseModel):
    text: str | None = Field(default=None, min_length=1, max_length=10_000)
    campaign: str | None = None
    retry: bool = False


class JobBody(BaseModel):
    campaign: str
    limit: int = 5
    count: int = 2
    dry_run: bool = False


async def _post_via_direct_cdp(endpoint: str, url: str) -> dict:
    """Konfliktarmer Fallback, falls Playwright den Browser nicht übernehmen kann."""
    proc = await asyncio.create_subprocess_exec(
        "node",
        str(ROOT / "scripts" / "cdp_post_text.mjs"),
        endpoint,
        url,
        cwd=ROOT,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    try:
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=30)
    except TimeoutError:
        proc.kill()
        await proc.wait()
        raise RuntimeError("Direkter LinkedIn-Abruf hat das Zeitlimit überschritten.")
    if proc.returncode != 0:
        reason = stderr.decode(errors="replace").strip()
        raise RuntimeError(reason or "Direkter CDP-Abruf fehlgeschlagen.")
    return json.loads(stdout.decode())


class CampaignSave(BaseModel):
    path: str
    version: int = Field(default=1, ge=1)
    name: str
    objective: str
    language: str = "de"
    audience: str
    personas: list[str] = []
    products: list[str] = []
    voice: str
    topics: list[str] = []
    banned_topics: list[str] = []
    keywords_to_engage: list[str] = []
    required_hashtags: list[str] = []
    cta: str | None = None
    max_post_chars: int = 1300
    max_comment_chars: int = 500
    limits: dict
    images: dict
    schedule: dict


class CampaignImportBody(BaseModel):
    filename: str = Field(default="kampagne.yaml", max_length=255)
    content: str = Field(min_length=2, max_length=250_000)
    mode: Literal["new", "version"] = "new"
    target_campaign: str | None = None


class FrequencyBody(BaseModel):
    kind: str
    minutes: int | None = None
    time: str | None = None
    weekdays: list[int] = Field(default_factory=list)


class JobDefCreate(BaseModel):
    task: auto.Task
    campaign: str
    count: int = Field(default=2, ge=1, le=100)
    active: bool = True
    schedule: str | None = None
    freq: FrequencyBody | None = None


class JobDefPatch(BaseModel):
    active: bool | None = None
    campaign: str | None = None
    count: int | None = Field(default=None, ge=1, le=100)
    approval_mode: auto.ApprovalMode | None = None
    schedule: str | None = None
    freq: FrequencyBody | None = None


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    return (STATIC / "index.html").read_text(encoding="utf-8")


def _valid_optional_campaign(campaign: str | None) -> str | None:
    if not campaign:
        return None
    target = (ROOT / campaign).resolve()
    if not target.is_relative_to((ROOT / "Kampagnen").resolve()) or not target.is_file():
        raise HTTPException(422, "Die gewählte Kampagne existiert nicht.")
    return campaign


@app.get("/api/ideas")
def list_ideas() -> list[dict]:
    return [idea.model_dump() for idea in reversed(idea_store.load(ROOT))]


@app.post("/api/ideas")
def create_idea(body: IdeaCreate) -> dict:
    idea = idea_store.add(
        ROOT, body.text.strip(), _valid_optional_campaign(body.campaign)
    )
    return {"ok": True, "idea": idea.model_dump()}


@app.patch("/api/ideas/{idea_id}")
def patch_idea(idea_id: str, body: IdeaPatch) -> dict:
    entries = idea_store.load(ROOT)
    idea = next((entry for entry in entries if entry.id == idea_id), None)
    if idea is None:
        raise HTTPException(404, f"Idee nicht gefunden: {idea_id}")
    if idea.status == "processing":
        raise HTTPException(409, "Diese Idee wird gerade verarbeitet.")
    if body.text is not None:
        idea.text = body.text.strip()
    if "campaign" in body.model_fields_set:
        # Ein explizites null entfernt die Kampagnenzuordnung.
        idea.campaign = _valid_optional_campaign(body.campaign)
    if body.retry:
        idea.status = "open"
        idea.output_id = None
        idea.output_campaign = None
        idea.last_error = None
    idea_store.save(ROOT, entries)
    return {"ok": True, "idea": idea.model_dump()}


@app.delete("/api/ideas/{idea_id}")
def delete_idea(idea_id: str) -> dict:
    entries = idea_store.load(ROOT)
    rest = [idea for idea in entries if idea.id != idea_id]
    if len(rest) == len(entries):
        raise HTTPException(404, f"Idee nicht gefunden: {idea_id}")
    idea_store.save(ROOT, rest)
    return {"ok": True, "deleted": idea_id}


@app.get("/api/personal-profile")
def get_personal_profile() -> dict:
    return load_personal_profile(ROOT).model_dump()


@app.put("/api/personal-profile")
def put_personal_profile(body: PersonalProfile) -> dict:
    save_personal_profile(ROOT, body)
    return {"ok": True, "profile": body.model_dump()}


@app.get("/api/config/timeouts")
def get_timeouts() -> dict:
    return timeouts.load(ROOT).model_dump()


@app.put("/api/config/timeouts")
def put_timeouts(body: timeouts.TimeoutSettings) -> dict:
    timeouts.save(ROOT, body)
    return {"ok": True, "timeouts": body.model_dump()}


@app.get("/api/config/planning")
def get_planning_settings() -> dict:
    return planning.load(ROOT).model_dump()


@app.put("/api/config/planning")
def put_planning_settings(body: planning.PlanningSettings) -> dict:
    planning.save(ROOT, body)
    return {"ok": True, "planning": body.model_dump()}


@app.get("/api/planning/suggestion")
def planning_suggestion(campaign: str) -> dict:
    scheduled = [
        item
        for campaign_file in campaign_io.campaign_files(ROOT)
        for item in _load(str(campaign_file.relative_to(ROOT)), "schedule")
    ]
    try:
        suggested = planning.suggest(
            planning.load(ROOT),
            [item.publish_at for item in scheduled if item.publish_at],
        )
    except ValueError as exc:
        raise HTTPException(409, str(exc)) from exc
    day_load = sum(1 for item in scheduled if (item.publish_at or "")[:10] == suggested.date().isoformat())
    return {
        "publish_at": suggested.isoformat(timespec="minutes"),
        "day_load": day_load,
    }


@app.get("/api/style-learning/status")
def style_learning_status() -> dict:
    return learning_status(ROOT)


@app.get("/api/campaigns")
def campaigns() -> list[dict]:
    out: list[dict] = []
    for path in campaign_io.campaign_files(ROOT):
        rel = str(path.relative_to(ROOT))
        entry: dict = {"path": rel, "name": path.stem, "ok": True, "error": None}
        try:
            c = load_campaign(path)
            campaign_io.ensure_current_snapshot(path)
            entry.update({
                "name": c.name,
                "version": c.version,
                "language": c.language,
                "objective": c.objective.strip(),
                "audience": c.audience.strip(),
                "personas": c.personas,
                "voice": c.voice.strip(),
                "topics": c.topics,
                "products": c.products,
                "banned_topics": c.banned_topics,
                "keywords_to_engage": c.keywords_to_engage,
                "hashtags": c.required_hashtags,
                "cta": c.cta,
                "max_post_chars": c.max_post_chars,
                "max_comment_chars": c.max_comment_chars,
                "limits": c.limits.model_dump(),
                "schedule": c.schedule.model_dump(mode="json"),
                "images": c.images.model_dump(),
                "versions": campaign_io.versions(path),
            })
            for stage in STAGES:
                entry.setdefault("counts", {})[stage] = len(q.parse(_queue_path(rel, stage)))
        except Exception as exc:
            entry.update({"ok": False, "error": str(exc)})
        out.append(entry)
    return out


@app.post("/api/campaigns/save")
def save_campaign(body: CampaignSave) -> dict:
    """Speichert Kampagnenfelder zurück in die YAML-Datei (inkl. aktiv von/bis)."""
    try:
        target = campaign_io.resolve_campaign(ROOT, body.path)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    if not target.is_file():
        raise HTTPException(404, "Kampagnen-Datei nicht gefunden.")

    payload = body.model_dump(exclude={"path", "version"})
    payload["version"] = body.version
    try:
        campaign = Campaign.model_validate(payload)
    except Exception as exc:
        raise HTTPException(422, f"Ungültige Kampagne: {exc}")

    try:
        updated = campaign_io.save_new_version(target, campaign, body.version)
    except RuntimeError as exc:
        raise HTTPException(409, str(exc)) from exc
    return {"ok": True, "version": updated.version}


@app.post("/api/campaigns/import")
def import_campaign(body: CampaignImportBody) -> dict:
    try:
        if body.mode == "version":
            if not body.target_campaign:
                raise ValueError("Bitte eine bestehende Kampagne auswählen.")
            target, campaign = campaign_io.import_as_version(
                ROOT, body.target_campaign, body.content
            )
        else:
            target, campaign = campaign_io.import_yaml(
                ROOT, body.filename, body.content
            )
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc
    return {
        "ok": True,
        "path": str(target.relative_to(ROOT)),
        "name": campaign.name,
        "version": campaign.version,
    }


@app.get("/api/campaigns/export")
def export_campaign(campaign: str) -> Response:
    try:
        target = campaign_io.resolve_campaign(ROOT, campaign)
        content = campaign_io.export_yaml(target)
    except (ValueError, FileNotFoundError) as exc:
        raise HTTPException(404, str(exc)) from exc
    export_name = target.parent.name if target.name == "kampagne.yaml" else target.stem
    filename = f"{export_name}-v{load_campaign(target).version}.yaml"
    return Response(
        content=content,
        media_type="application/yaml",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


@app.get("/api/items")
def items(campaign: str, stage: str) -> list[dict]:
    result = []
    for item in _load(campaign, stage):
        d = item.model_dump()
        d["due"] = item.due()
        d["has_image"] = bool(item.image_path and (ROOT / item.image_path).exists())
        result.append(d)
    result.sort(key=lambda d: (d.get("publish_at") or "9999", d["id"]))
    return result


@app.get("/api/items/all")
def all_items(stage: str) -> list[dict]:
    if stage not in STAGES:
        raise HTTPException(400, f"Unbekannte Stufe: {stage}")
    result: list[dict] = []
    for campaign_file in campaign_io.campaign_files(ROOT):
        campaign_path = str(campaign_file.relative_to(ROOT))
        campaign = load_campaign(campaign_file)
        for item in _load(campaign_path, stage):
            data = item.model_dump()
            data["due"] = item.due()
            data["has_image"] = bool(item.image_path and (ROOT / item.image_path).exists())
            data["campaign_path"] = campaign_path
            data["campaign_name"] = campaign.name
            data["campaign_version"] = campaign.version
            result.append(data)
    result.sort(key=lambda data: (data.get("publish_at") or "9999", data["id"]))
    return result


@app.get("/api/analytics")
def analytics_dashboard(campaign: str) -> dict:
    return campaign_analytics.dashboard(ROOT / campaign)


@app.patch("/api/items/{item_id}")
def patch_item(item_id: str, body: ItemPatch) -> dict:
    items_ = _load(body.campaign, body.stage)
    for item in items_:
        if item.id != item_id or (
            body.match_publish_at is not None and item.publish_at != body.match_publish_at
        ):
            continue
        if body.text is not None:
            before = item.text
            if body.stage == "approvals" and before != body.text:
                if item.generated_text is None:
                    item.generated_text = before
                learn_edit(ROOT, item, before, body.text)
            item.text = body.text
        if body.note is not None:
            item.note = body.note
        if body.user_memory_note is not None and body.stage == "approvals":
            item.user_memory_note = body.user_memory_note.strip()
        if body.publish_at is not None:
            item.publish_at = body.publish_at or None
        if body.reshare_with_comment is not None and item.kind == "reshare":
            item.reshare_with_comment = body.reshare_with_comment
        if body.stage == "approvals" and item.text.strip():
            campaign = load_campaign(ROOT / body.campaign)
            prepare_items(
                ROOT,
                campaign,
                items_,
                {item.id},
                _load(body.campaign, "schedule"),
            )
        _save(body.campaign, body.stage, items_)
        return {"ok": True, "item": item.model_dump()}
    raise HTTPException(404, f"Nicht gefunden: {item_id}")


@app.post("/api/items/{item_id}/rewrite")
def rewrite_item(item_id: str, body: RewriteBody) -> dict:
    """Regieanweisung anwenden, neu evaluieren und in Freigaben belassen."""
    pending = _load(body.campaign, "approvals")
    item = next((candidate for candidate in pending if candidate.id == item_id), None)
    if item is None:
        raise HTTPException(404, f"Nicht gefunden: {item_id}")
    if not item.text.strip():
        raise HTTPException(400, "Ein leerer Entwurf kann nicht neu geschrieben werden.")
    instruction = body.instruction.strip()
    if not instruction:
        raise HTTPException(422, "Bitte eine Regieanweisung eingeben.")

    before = item.text
    result = brain.rewrite_draft(body.campaign, item, instruction)
    if not result.get("ok"):
        raise HTTPException(502, f"Rewrite fehlgeschlagen: {result.get('error', 'unbekannt')}")
    if item.generated_text is None:
        item.generated_text = before
    item.text = str(result["text"]).strip()
    campaign = load_campaign(ROOT / body.campaign)
    preparation = prepare_items(
        ROOT,
        campaign,
        pending,
        {item.id},
        _load(body.campaign, "schedule"),
    )
    learn_rewrite(ROOT, item, before, item.text, instruction)
    _save(body.campaign, "approvals", pending)
    return {
        "ok": True,
        "item": item.model_dump(),
        "evaluation": preparation[0] if preparation else None,
    }


@app.post("/api/items/{item_id}/refresh-source")
async def refresh_item_source(item_id: str, body: CampaignRef) -> dict:
    """Lädt den vollständigen Originalbeitrag eines Kommentar-Kandidaten nach."""
    items_ = _load(body.campaign, "approvals")
    item = next((candidate for candidate in items_ if candidate.id == item_id), None)
    if item is None:
        raise HTTPException(404, f"Nicht gefunden: {item_id}")
    if item.kind not in {"comment", "reshare"} or not item.url:
        raise HTTPException(409, "Dieser Eintrag hat keinen LinkedIn-Originalbeitrag.")

    settings = load_settings()
    direct = None
    direct_error = None
    try:
        direct = await _post_via_direct_cdp(settings.cdp_endpoint, item.url)
    except Exception as exc:
        direct_error = exc

    post = None
    if direct is None:
        try:
            async with asyncio.timeout(40):
                async with LinkedInClient(settings.cdp_endpoint) as client:
                    post = await client.get_post_by_url(item.url)
        except Exception as exc:
            reason = str(exc) or str(direct_error) or "unbekannter Fehler"
            raise HTTPException(
                502, f"Originalbeitrag konnte nicht geladen werden: {reason}"
            ) from exc

    if direct is None and post is None:
        reason = str(direct_error) or "Kein Beitrag im LinkedIn-Tab gefunden"
        raise HTTPException(502, f"Originalbeitrag konnte nicht geladen werden: {reason}")

    item.note = post.text if post is not None else direct["text"]
    author = post.author if post is not None else direct.get("author")
    resolved_url = post.url if post is not None else direct.get("url")
    if author:
        item.author = author
    if resolved_url:
        item.url = resolved_url
    _save(body.campaign, "approvals", items_)
    return {"ok": True, "item": item.model_dump()}


@app.delete("/api/items/{item_id}")
def delete_item(
    item_id: str,
    campaign: str,
    stage: str,
    match_publish_at: str | None = None,
) -> dict:
    items_ = _load(campaign, stage)
    match_index = next((
        index for index, candidate in enumerate(items_)
        if candidate.id == item_id and (
            match_publish_at is None or candidate.publish_at == match_publish_at
        )
    ), None)
    if match_index is None:
        raise HTTPException(404, f"Nicht gefunden: {item_id}")
    item = items_[match_index]
    if stage == "approvals":
        learn_rejection(ROOT, item)
    rest = items_[:match_index] + items_[match_index + 1:]
    _save(campaign, stage, rest)
    return {"ok": True, "deleted": item_id, "learned_as_rejection": stage == "approvals"}


@app.post("/api/items/{item_id}/approve")
def approve_item(item_id: str, body: ApproveBody) -> dict:
    """Freigeben = aus approvals.md nach schedule.md verschieben (mit Termin)."""
    pending = _load(body.campaign, "approvals")
    item = next((i for i in pending if i.id == item_id), None)
    if item is None:
        raise HTTPException(404, f"Nicht gefunden: {item_id}")
    if not item.text.strip() and not (
        item.kind == "reshare" and not item.reshare_with_comment
    ):
        raise HTTPException(400, "Eintrag ohne Text kann nicht freigegeben werden.")
    if item.kind == "connection" and len(item.text.strip()) > 300:
        raise HTTPException(400, "Vernetzungsnotizen dürfen höchstens 300 Zeichen haben.")

    scheduled = _load(body.campaign, "schedule")
    if body.publish_at:
        item.publish_at = body.publish_at
    elif not item.publish_at:
        item.publish_at = planning.suggest(
            planning.load(ROOT),
            [scheduled_item.publish_at for scheduled_item in scheduled if scheduled_item.publish_at],
        ).isoformat(timespec="minutes")

    learn_approval(ROOT, item)
    item.approved = True
    item.approval_origin = "manual"
    item.auto_approval_threshold = None
    scheduled.append(item)
    _save(body.campaign, "schedule", scheduled)
    _save(body.campaign, "approvals", [i for i in pending if i.id != item_id])
    return {"ok": True, "id": item_id, "publish_at": item.publish_at}


@app.post("/api/approvals/auto")
def auto_approve_items(body: BulkApproveBody) -> dict:
    """Score-basierte Sammelfreigabe: max. vier automatische Aktionen je Werktag."""
    try:
        return {"ok": True, **approve_above_score(ROOT, body.campaign, body.minimum_score)}
    except (ValueError, RuntimeError, FileNotFoundError) as exc:
        raise HTTPException(422, str(exc)) from exc


def _approval_post(item_id: str, campaign: str) -> tuple[list[q.QueueItem], q.QueueItem]:
    pending = _load(campaign, "approvals")
    item = next((candidate for candidate in pending if candidate.id == item_id), None)
    if item is None:
        raise HTTPException(404, f"Nicht gefunden: {item_id}")
    if item.kind != "post":
        raise HTTPException(409, "Eigene Bilder werden nur bei eigenen Posts unterstützt.")
    return pending, item


def _remove_replaced_image(item: q.QueueItem, old_path: str | None) -> None:
    if old_path and old_path != item.image_path:
        remove_image_file(ROOT, item.model_copy(update={"image_path": old_path}))


@app.post("/api/items/{item_id}/image")
async def set_item_image(item_id: str, body: ImageBody) -> dict:
    """Erzeugt oder sucht ein Bild und hält den Post bis zur Freigabe in der Queue."""
    pending, item = _approval_post(item_id, body.campaign)
    campaign = load_campaign(ROOT / body.campaign)
    prompt = body.prompt.strip()
    if body.source == "web" and not prompt:
        raise HTTPException(422, "Bitte einen Suchbegriff für das Webbild eingeben.")

    old_path = item.image_path
    if body.source == "generated":
        ok = await set_generated_image(
            item, campaign, load_settings(), prompt=prompt or None
        )
    else:
        ok = await set_web_image(item, prompt)
    _remove_replaced_image(item, old_path)
    _save(body.campaign, "approvals", pending)
    if not ok:
        raise HTTPException(502, item.image_error or "Bild konnte nicht erstellt werden.")
    return {"ok": True, "item": item.model_dump()}


@app.post("/api/items/{item_id}/image-upload")
def upload_item_image(item_id: str, body: ImageUploadBody) -> dict:
    """Speichert einen Browser-Upload ohne zusätzliche Multipart-Abhängigkeit."""
    pending, item = _approval_post(item_id, body.campaign)
    try:
        raw = base64.b64decode(body.data, validate=True)
    except (ValueError, binascii.Error) as exc:
        raise HTTPException(422, "Die Bilddatei ist nicht gültig kodiert.") from exc
    if not raw or len(raw) > 8 * 1024 * 1024:
        raise HTTPException(413, "Das Bild darf höchstens 8 MB groß sein.")

    if body.content_type == "image/png":
        if not raw.startswith(b"\x89PNG\r\n\x1a\n"):
            raise HTTPException(422, "Die Datei ist kein gültiges PNG-Bild.")
        suffix = ".png"
    else:
        if not raw.startswith(b"\xff\xd8\xff"):
            raise HTTPException(422, "Die Datei ist kein gültiges JPEG-Bild.")
        suffix = ".jpg"

    image_dir = ROOT / ".runs" / "images"
    image_dir.mkdir(parents=True, exist_ok=True)
    target = image_dir / f"{item.id}-upload{suffix}"
    old_path = item.image_path
    target.write_bytes(raw)
    item.image_path = str(target.relative_to(ROOT))
    item.image_source = "Eigenes Bild"
    item.image_origin = "upload"
    item.image_prompt = body.filename
    item.image_error = ""
    _remove_replaced_image(item, old_path)
    _save(body.campaign, "approvals", pending)
    return {"ok": True, "item": item.model_dump()}


@app.delete("/api/items/{item_id}/image")
def delete_item_image(item_id: str, campaign: str) -> dict:
    pending, item = _approval_post(item_id, campaign)
    clear_image(ROOT, item)
    _save(campaign, "approvals", pending)
    return {"ok": True, "item": item.model_dump()}


@app.get("/api/image")
def image(path: str) -> FileResponse:
    target = (ROOT / path).resolve()
    # Nur Bilder aus .runs/images ausliefern (kein Path-Traversal).
    image_dir = (ROOT / ".runs" / "images").resolve()
    if target.parent != image_dir or not target.is_file():
        raise HTTPException(404, "Bild nicht gefunden")
    return FileResponse(target)


def _next_cron(expr: str) -> str | None:
    """Nächste Ausführung für einfache Ausdrücke wie '*/15 * * * *'."""
    try:
        minute = expr.split()[0]
        now = datetime.now().replace(second=0, microsecond=0)
        if minute.startswith("*/"):
            step = int(minute[2:])
            return (now + timedelta(minutes=(step - now.minute % step) or step)).isoformat(
                timespec="minutes"
            )
        if minute.isdigit():
            nxt = now.replace(minute=int(minute))
            if nxt <= now:
                nxt += timedelta(hours=1)
            return nxt.isoformat(timespec="minutes")
    except Exception:
        pass
    return None


def _read_crontab(*, strict: bool = False) -> str:
    try:
        proc = subprocess.run(["crontab", "-l"], capture_output=True, text=True, timeout=5)
        if proc.returncode == 0:
            return proc.stdout
        # `crontab -l` liefert bei einer noch nicht vorhandenen Crontab Exit 1.
        if proc.returncode == 1 and "no crontab" in proc.stderr.lower():
            return ""
        if strict:
            raise HTTPException(500, proc.stderr.strip() or "Crontab konnte nicht gelesen werden.")
        return ""
    except OSError as exc:
        if strict:
            status = 501 if isinstance(exc, FileNotFoundError) else 500
            raise HTTPException(status, f"Crontab ist nicht verfügbar: {exc}") from exc
        return ""
    except subprocess.SubprocessError as exc:
        if strict:
            raise HTTPException(500, f"Crontab konnte nicht gelesen werden: {exc}") from exc
        return ""


def _scheduler_entry() -> str:
    root = shlex.quote(str(ROOT))
    runner = shlex.quote(str(ROOT / "bin" / "li-scheduler"))
    logfile = shlex.quote(str(ROOT / ".runs" / "cron.log"))
    return f"*/5 * * * * cd {root} && {runner} >> {logfile} 2>&1 {SCHEDULER_MARKER}"


@app.get("/api/cron")
def cron() -> dict:
    raw = _read_crontab()
    jobs = []
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if not any(k in line for k in ("li-scheduler", "li-jobs", "li-health", "li-brain")):
            continue
        parts = line.split()
        expr = " ".join(parts[:5])
        jobs.append({"expr": expr, "command": " ".join(parts[5:]), "next": _next_cron(expr)})

    upcoming = []
    for path in sorted(CAMPAIGN_DIR.rglob("*.yaml")):
        rel = str(path.relative_to(ROOT))
        for item in q.parse(_queue_path(rel, "schedule")):
            if item.publish_at:
                upcoming.append({
                    "campaign": rel,
                    "id": item.id,
                    "kind": item.kind,
                    "publish_at": item.publish_at,
                    "due": item.due(),
                })
    upcoming.sort(key=lambda d: d["publish_at"])
    return {
        "jobs": jobs,
        "crontab_gefunden": bool(raw.strip()),
        "scheduler_installed": any(
            "li-scheduler" in line and not line.lstrip().startswith("#")
            for line in raw.splitlines()
        ),
        "scheduler_entry": _scheduler_entry(),
        "upcoming": upcoming[:20],
    }


@app.post("/api/scheduler/install")
def install_scheduler() -> dict:
    """Installiert den einen OS-Cron-Takt, der die Jobs aus der UI prüft."""
    raw = _read_crontab(strict=True)
    if any(
        "li-scheduler" in line and not line.lstrip().startswith("#")
        for line in raw.splitlines()
    ):
        return {"ok": True, "installed": False, "message": "Scheduler war bereits aktiv."}

    entry = _scheduler_entry()
    updated = raw.rstrip()
    if updated:
        updated += "\n"
    updated += entry + "\n"
    try:
        proc = subprocess.run(
            ["crontab", "-"], input=updated, capture_output=True, text=True, timeout=10
        )
    except OSError as exc:
        status = 501 if isinstance(exc, FileNotFoundError) else 500
        raise HTTPException(status, f"Scheduler konnte nicht aktiviert werden: {exc}") from exc
    except subprocess.SubprocessError as exc:
        raise HTTPException(500, f"Scheduler konnte nicht aktiviert werden: {exc}") from exc
    if proc.returncode != 0:
        raise HTTPException(500, proc.stderr.strip() or "Scheduler konnte nicht aktiviert werden.")
    return {"ok": True, "installed": True, "message": "Automatik wurde aktiviert."}


def _health_data() -> dict:
    try:
        proc = subprocess.run(
            [str(ROOT / "bin" / "li-health"), "--no-start", "--quiet", "--json"],
            capture_output=True, text=True, cwd=ROOT, timeout=45,
        )
    except subprocess.TimeoutExpired:
        return {"cdp": False, "logged_in": False, "error": "Health-Check-Zeitüberschreitung"}
    last = proc.stdout.strip().splitlines()[-1] if proc.stdout.strip() else "{}"
    try:
        data = json.loads(last)
    except Exception:
        data = {"raw": proc.stdout[-500:]}
    data["exit_code"] = proc.returncode
    return data


def _passive_health_data() -> dict:
    """Schneller Status ohne Playwright-Navigation und ohne KI-Anfrage."""
    settings = load_settings()
    cli_status = brain.cli_status()
    result = {
        "cdp": False,
        "logged_in": False,
        "tabs": 0,
        "brain_cli": brain.selected_engine(cli_status),
        "brain_clis": cli_status,
    }
    try:
        version = httpx.get(f"{settings.cdp_endpoint}/json/version", timeout=3)
        version.raise_for_status()
        result["cdp"] = True
        result["browser"] = version.json().get("Browser", "")
        tabs = httpx.get(f"{settings.cdp_endpoint}/json", timeout=3)
        tabs.raise_for_status()
        linkedin = [
            tab.get("url", "") for tab in tabs.json()
            if tab.get("type") == "page" and "linkedin.com" in tab.get("url", "")
        ]
        result["tabs"] = len(linkedin)
        result["logged_in"] = any(
            not any(marker in url for marker in ("/login", "/checkpoint", "/authwall"))
            for url in linkedin
        )
    except Exception as exc:
        result["error"] = str(exc)
    return result


@app.get("/api/health")
def health() -> dict:
    """Passiver Check ohne Modell-Anfrage oder Kontingentverbrauch."""
    return _passive_health_data()


@app.post("/api/health/check")
def active_health_check(x_health_check: str | None = Header(default=None)) -> dict:
    """Vollcheck inklusive minimaler echter KI-Anfrage an den aktiven CLI-Pfad."""
    if x_health_check != "requested":
        raise HTTPException(400, "Der aktive Health Check muss über die Oberfläche gestartet werden.")
    data = _health_data()
    probe = brain.probe_cli(timeout=120)
    data["probe"] = probe
    data["overall_ok"] = bool(data.get("logged_in") and probe.get("ok"))
    return data


@app.post("/api/tasks/{name}")
def run_task(name: str, body: JobBody) -> dict:
    """Führt eine Aktion einmalig aus – exakt derselbe Weg wie ein geplanter Job."""
    if name == "find-and-write-connections" and body.count > 5:
        raise HTTPException(422, "Pro Vernetzungslauf sind höchstens 5 Personen erlaubt.")
    if name in {
        "find-comments", "find-reshares", "run-due", "schedule", "status", "analytics"
    }:
        cmd = [str(ROOT / "bin" / "li-jobs"), "--campaign", body.campaign, name]
        if name in {"find-comments", "find-reshares"}:
            cmd += ["--limit", str(body.limit)]
        if name == "run-due" and body.dry_run:
            cmd += ["--dry-run"]
    elif name in {
        "draft-posts", "find-and-write", "write-comments",
        "find-and-write-reshares", "find-and-write-connections", "ideas-to-posts",
    }:
        cmd = [str(ROOT / "bin" / "li-brain"), "--campaign", body.campaign, name,
               "--count", str(body.count)]
    else:
        raise HTTPException(400, f"Job nicht erlaubt: {name}")

    process_timeout = timeouts.process_seconds(ROOT, name, body.count)
    try:
        proc = subprocess.run(
            cmd, capture_output=True, text=True, cwd=ROOT, timeout=process_timeout
        )
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout.decode(errors="replace") if isinstance(exc.stdout, bytes) else exc.stdout
        stderr = exc.stderr.decode(errors="replace") if isinstance(exc.stderr, bytes) else exc.stderr
        return {
            "ok": False,
            "error": f"Zeitlimit von {process_timeout // 60} Minuten überschritten",
            "stdout": (stdout or "")[-6000:],
            "stderr": (stderr or "")[-2000:],
        }
    return {
        "ok": proc.returncode == 0,
        "stdout": proc.stdout[-6000:],
        "stderr": proc.stderr[-2000:],
    }


def _jobdef_dict(j: auto.JobDef) -> dict:
    d = j.model_dump()
    d["human"] = j.freq.human()
    d["due"] = j.is_due()
    d["approval_trust"] = job_trust(ROOT, j.id)
    d["auto_approval_stats"] = auto_approval_stats(ROOT, j.id)
    d["approval_thresholds"] = {
        f"top_{percent}": score_threshold(ROOT, j.id, percent)
        for percent in (20, 15, 10, 5)
    }
    return d


@app.get("/api/jobdefs")
def list_jobdefs() -> list[dict]:
    return [_jobdef_dict(j) for j in auto.load()]


@app.post("/api/jobdefs")
def create_jobdef(body: JobDefCreate) -> dict:
    if body.task == "find-and-write-connections" and body.count > 5:
        raise HTTPException(422, "Pro Vernetzungslauf sind höchstens 5 Personen erlaubt.")
    if body.schedule:
        try:
            frequency = auto.parse_human_frequency(body.schedule)
        except ValueError as exc:
            raise HTTPException(422, str(exc)) from exc
    elif body.freq is not None:
        try:
            frequency = auto.Frequency(**body.freq.model_dump())
        except ValueError as exc:
            raise HTTPException(422, str(exc)) from exc
    else:
        raise HTTPException(422, "Bitte einen Zeitplan angeben.")

    def add(jobs: list[auto.JobDef]) -> auto.JobDef:
        job = auto.JobDef(
            id=auto.next_id(jobs),
            active=body.active,
            task=body.task,
            campaign=body.campaign,
            count=body.count,
            freq=frequency,
        )
        jobs.append(job)
        return job.model_copy(deep=True)

    job = auto.mutate(add)
    return {"ok": True, "job": _jobdef_dict(job)}


@app.patch("/api/jobdefs/{job_id}")
def patch_jobdef(job_id: str, body: JobDefPatch) -> dict:
    selected_campaign = (
        _valid_optional_campaign(body.campaign)
        if "campaign" in body.model_fields_set
        else None
    )

    def change(jobs: list[auto.JobDef]) -> auto.JobDef:
        job = next((candidate for candidate in jobs if candidate.id == job_id), None)
        if job is None:
            raise HTTPException(404, f"Job nicht gefunden: {job_id}")
        if body.active is not None:
            job.active = body.active
        if "campaign" in body.model_fields_set:
            if selected_campaign is None:
                raise HTTPException(422, "Bitte eine Kampagne auswählen.")
            job.campaign = selected_campaign
        if body.count is not None:
            if job.task == "find-and-write-connections" and body.count > 5:
                raise HTTPException(
                    422, "Pro Vernetzungslauf sind höchstens 5 Personen erlaubt."
                )
            job.count = body.count
        if body.approval_mode is not None:
            trust = job_trust(ROOT, job.id)
            if (
                body.approval_mode != "manual"
                and job.task not in {
                    "draft-posts", "find-and-write", "write-comments",
                    "find-and-write-reshares",
                }
            ):
                raise HTTPException(422, "Auto-Freigabe ist für diesen Jobtyp nicht verfügbar.")
            if body.approval_mode != "manual" and not trust["unlocked"]:
                raise HTTPException(
                    409,
                    f"Auto-Freigabe ist noch gesperrt: {trust['unchanged_streak']}/10 "
                    "Entwürfe unverändert manuell freigegeben.",
                )
            job.approval_mode = body.approval_mode
        if body.schedule:
            try:
                job.freq = auto.parse_human_frequency(body.schedule)
            except ValueError as exc:
                raise HTTPException(422, str(exc)) from exc
        elif body.freq is not None:
            try:
                job.freq = auto.Frequency(**body.freq.model_dump())
            except ValueError as exc:
                raise HTTPException(422, str(exc)) from exc
        return job.model_copy(deep=True)

    job = auto.mutate(change)
    return {"ok": True, "job": _jobdef_dict(job)}


@app.delete("/api/jobdefs/{job_id}")
def delete_jobdef(job_id: str) -> dict:
    def delete(jobs: list[auto.JobDef]) -> None:
        for index, job in enumerate(jobs):
            if job.id == job_id:
                del jobs[index]
                return
        raise HTTPException(404, f"Job nicht gefunden: {job_id}")

    auto.mutate(delete)
    return {"ok": True, "deleted": job_id}


@app.post("/api/jobdefs/{job_id}/run-now")
def run_jobdef_now(job_id: str) -> dict:
    from .. import scheduler as sched

    jobs = auto.load()
    job = next((j for j in jobs if j.id == job_id), None)
    if job is None:
        raise HTTPException(404, f"Job nicht gefunden: {job_id}")
    if not job.active:
        raise HTTPException(409, "Der Job ist inaktiv. Bitte zuerst aktivieren.")
    if job.is_running():
        raise HTTPException(409, "Dieser Job läuft bereits. Bitte den Abschluss abwarten.")
    if hours_error := sched.working_hours_error():
        raise HTTPException(409, hours_error)
    job = auto.claim_job(job_id, require_due=False)
    if job is None:
        raise HTTPException(409, "Der Job wurde inzwischen geändert, gelöscht oder gestartet.")
    result = sched.run_task_result(job)
    ok = bool(result["ok"])
    finished = auto.finish_job(
        job.id,
        ok=ok,
        error=None if ok else str(result.get("error") or "Unbekannter Fehler"),
        expected_created=job.created,
    )
    return {**result, "ok": ok, "job": _jobdef_dict(finished or job)}


def main() -> None:
    import uvicorn

    port = int(sys.argv[1]) if len(sys.argv) > 1 else int(os.getenv("APP_PORT", "8765"))
    host = os.getenv("APP_HOST", "127.0.0.1")
    print(f"Sara's Marketing AGENT-ur → http://{host}:{port}")
    uvicorn.run(app, host=host, port=port, log_level="warning")


if __name__ == "__main__":
    main()
