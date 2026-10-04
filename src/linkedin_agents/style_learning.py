"""Lokale, nachvollziehbare Stilbewertung und Lernen aus Nutzerkorrekturen.

Das ist kein verborgenes Training eines Modells. Änderungen und Freigaben werden
als kleine, lesbare Lernhistorie gespeichert. Codex und der lokale Evaluator nutzen
diese Historie bei späteren Entwürfen.
"""
from __future__ import annotations

import difflib
import json
import math
import re
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path

from .models.campaign import Campaign
from .queue import QueueItem


def _unwrap_text_envelope(value: object) -> str:
    """Hält versehentliche JSON-Hüllen aus dem Stil-Lernmaterial heraus."""
    current = value
    for _ in range(4):
        if isinstance(current, dict):
            current = current.get("text") or current.get("content") or ""
            continue
        if not isinstance(current, str):
            return str(current)
        text = current.strip()
        try:
            nested = json.loads(text)
        except (json.JSONDecodeError, TypeError):
            return text
        if not isinstance(nested, (dict, str)):
            return text
        current = nested
    return str(current).strip()


def _state_path(root: Path) -> Path:
    return root / "team" / "style" / "learning.json"


def _empty_state() -> dict:
    return {
        "version": 2, "edits": [], "patterns": [], "approvals": [],
        "rejections": [], "directives": [], "directive_preferences": [],
        "user_notes": [],
        "job_trust": {}, "auto_approvals": [],
        "auto_approval_totals": {"all": 0, "by_job": {}, "by_mode": {}},
    }


def _ensure_auto_approval_totals(state: dict) -> None:
    """Migriert den dauerhaften Counter aus vorhandenen Audit-Ereignissen."""
    totals = state.get("auto_approval_totals")
    if not isinstance(totals, dict):
        events = state.get("auto_approvals", [])
        totals = {
            "all": len(events),
            "by_job": dict(Counter(
                str(event.get("source_job_id") or "unbekannt") for event in events
            )),
            "by_mode": dict(Counter(
                str(event.get("mode") or "unbekannt") for event in events
            )),
        }
        state["auto_approval_totals"] = totals
    totals.setdefault("all", 0)
    totals.setdefault("by_job", {})
    totals.setdefault("by_mode", {})


def load_state(root: Path) -> dict:
    path = _state_path(root)
    if not path.exists():
        return _empty_state()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return _empty_state()
    data["version"] = 2
    data.setdefault("edits", [])
    data.setdefault("patterns", [])
    data.setdefault("approvals", [])
    data.setdefault("rejections", [])
    data.setdefault("directives", [])
    data.setdefault("directive_preferences", [])
    data.setdefault("user_notes", [])
    data.setdefault("job_trust", {})
    data.setdefault("auto_approvals", [])
    _ensure_auto_approval_totals(data)
    for event in [*data["edits"], *data["directives"]]:
        for key in ("before", "after"):
            if key in event:
                event[key] = _unwrap_text_envelope(event[key])
    return data


def _save_state(root: Path, state: dict) -> None:
    path = _state_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def _words(text: str) -> list[str]:
    return re.findall(r"[\wÄÖÜäöüß'-]+", text.lower())


def _similarity(left: str, right: str) -> float:
    a, b = set(_words(left)), set(_words(right))
    return len(a & b) / len(a | b) if a and b else 0.0


def _patterns(before: str, after: str) -> list[tuple[str, str]]:
    """Kurze, exakte Wortgruppen aus einer Nutzerkorrektur extrahieren."""
    old, new = before.split(), after.split()
    matcher = difflib.SequenceMatcher(a=old, b=new, autojunk=False)
    result: list[tuple[str, str]] = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag not in {"replace", "delete"}:
            continue
        source = " ".join(old[i1:i2]).strip()
        target = " ".join(new[j1:j2]).strip()
        if not (2 <= len(source.split()) <= 8 and len(target.split()) <= 10):
            continue
        if "http" in source.lower() or source.startswith("#"):
            continue
        result.append((source, target))
    return result[:8]


def _rebuild_patterns(state: dict) -> None:
    """Nur durch eine spätere Freigabe bestätigte Korrekturen aktivieren."""
    counts: Counter[tuple[str, str]] = Counter()
    display: dict[tuple[str, str], str] = {}
    for edit in state["edits"]:
        if not edit.get("approved") and edit.get("outcome") != "approved":
            continue
        for source, target in _patterns(edit.get("before", ""), edit.get("after", "")):
            key = (source.casefold(), target)
            counts[key] += 1
            display.setdefault(key, source)
    state["patterns"] = [
        {"from": display[key], "to": key[1], "count": count}
        for key, count in counts.most_common(100)
    ]


def _rebuild_directive_preferences(state: dict) -> None:
    counts: Counter[str] = Counter()
    display: dict[str, str] = {}
    for event in state["directives"]:
        if event.get("outcome") != "approved":
            continue
        instruction = " ".join(event.get("instruction", "").split()).strip()
        if not instruction:
            continue
        key = instruction.casefold()
        counts[key] += 1
        display.setdefault(key, instruction)
    state["directive_preferences"] = [
        {"instruction": display[key], "count": count}
        for key, count in counts.most_common(100)
    ]


def _confirm_feedback_chain(state: dict, item_id: str, final_text: str) -> None:
    """Die lückenlose Edit-/Rewrite-Kette bis zum finalen Text bestätigen."""
    events = [
        event for group in (state["edits"], state["directives"])
        for event in group if event.get("item_id") == item_id
    ]
    current = final_text
    while True:
        match = next(
            (
                event for event in reversed(events)
                if event.get("outcome", "pending") == "pending"
                and event.get("after") == current
            ),
            None,
        )
        if match is None:
            break
        match["outcome"] = "approved"
        if "approved" in match:
            match["approved"] = True
        current = match.get("before", current)


def learn_edit(root: Path, item: QueueItem, before: str, after: str) -> None:
    """Änderung vormerken; positiv wird sie erst mit der späteren Freigabe."""
    if before.strip() == after.strip() or not after.strip():
        return
    state = load_state(root)
    event = {
        "at": datetime.now().isoformat(timespec="seconds"),
        "item_id": item.id,
        "kind": item.kind,
        "source_job_id": item.source_job_id,
        "before": before,
        "after": after,
        "approved": False,
        "outcome": "pending",
    }
    if not any(
        edit.get("item_id") == item.id
        and edit.get("before") == before
        and edit.get("after") == after
        for edit in state["edits"][-50:]
    ):
        state["edits"].append(event)

    state["edits"] = state["edits"][-200:]
    _save_state(root, state)


def learn_rewrite(
    root: Path,
    item: QueueItem,
    before: str,
    after: str,
    instruction: str,
) -> None:
    """Regieanweisung samt Ergebnis vormerken, bis der Nutzer final entscheidet."""
    if before.strip() == after.strip() or not instruction.strip() or not after.strip():
        return
    state = load_state(root)
    state["directives"].append(
        {
            "at": datetime.now().isoformat(timespec="seconds"),
            "item_id": item.id,
            "kind": item.kind,
            "source_job_id": item.source_job_id,
            "instruction": " ".join(instruction.split()),
            "before": before,
            "after": after,
            "outcome": "pending",
        }
    )
    state["directives"] = state["directives"][-200:]
    _save_state(root, state)


def learn_approval(root: Path, item: QueueItem) -> None:
    """Finalen Text als starkes Lernsignal und als freigegebenes Beispiel speichern."""
    state = load_state(root)
    _confirm_feedback_chain(state, item.id, item.text)
    unchanged = bool(
        item.generated_text is not None
        and item.generated_text.strip() == item.text.strip()
    )
    if not any(a.get("item_id") == item.id for a in state["approvals"]):
        state["approvals"].append(
            {
                "at": datetime.now().isoformat(timespec="seconds"),
                "item_id": item.id,
                "kind": item.kind,
                "source_job_id": item.source_job_id,
                "text": item.text,
                "source_text": item.note if item.kind == "reshare" else None,
                "reshare_with_comment": (
                    item.reshare_with_comment if item.kind == "reshare" else None
                ),
                "score_before_approval": item.evaluation_score,
                "user_memory_note": item.user_memory_note.strip() or None,
                "unchanged": unchanged,
                "automatic": False,
            }
        )
        if item.source_job_id:
            trust = state["job_trust"].setdefault(
                item.source_job_id, {"unchanged_streak": 0, "unlocked": False}
            )
            trust["unchanged_streak"] = (
                int(trust.get("unchanged_streak", 0)) + 1 if unchanged else 0
            )
            if trust["unchanged_streak"] >= 10:
                trust["unlocked"] = True
    if item.user_memory_note.strip() and not any(
        note.get("item_id") == item.id and note.get("outcome") == "approved"
        for note in state["user_notes"]
    ):
        state["user_notes"].append(
            {
                "at": datetime.now().isoformat(timespec="seconds"),
                "item_id": item.id,
                "kind": item.kind,
                "source_job_id": item.source_job_id,
                "note": " ".join(item.user_memory_note.split()),
                "outcome": "approved",
                "text": item.text,
            }
        )
    state["user_notes"] = state["user_notes"][-200:]
    state["approvals"] = state["approvals"][-200:]
    _rebuild_patterns(state)
    _rebuild_directive_preferences(state)
    _save_state(root, state)

    if item.text.strip():
        corpus = root / "team" / "style" / "approved"
        corpus.mkdir(parents=True, exist_ok=True)
        safe_id = re.sub(r"[^a-zA-Z0-9_-]+", "-", item.id).strip("-")
        path = corpus / f"{datetime.now():%Y-%m-%d}-{safe_id}.md"
        path.write_text(item.text.strip() + "\n", encoding="utf-8")


def learn_rejection(root: Path, item: QueueItem, reason: str = "deleted") -> None:
    """Explizites Ablehnen als negatives, aber nicht automatisch löschendes Signal lernen."""
    state = load_state(root)
    if not any(entry.get("item_id") == item.id for entry in state["rejections"]):
        state["rejections"].append(
            {
                "at": datetime.now().isoformat(timespec="seconds"),
                "item_id": item.id,
                "kind": item.kind,
                "source_job_id": item.source_job_id,
                "text": item.text,
                "generated_text": item.generated_text,
                "score_at_rejection": item.evaluation_score,
                "edited": bool(
                    item.generated_text is not None
                    and item.generated_text.strip() != item.text.strip()
                ),
                "reason": reason,
                "user_memory_note": item.user_memory_note.strip() or None,
            }
        )
    if item.user_memory_note.strip() and not any(
        note.get("item_id") == item.id and note.get("outcome") == "rejected"
        for note in state["user_notes"]
    ):
        state["user_notes"].append(
            {
                "at": datetime.now().isoformat(timespec="seconds"),
                "item_id": item.id,
                "kind": item.kind,
                "source_job_id": item.source_job_id,
                "note": " ".join(item.user_memory_note.split()),
                "outcome": "rejected",
                "text": item.text,
            }
        )
    for edit in state["edits"]:
        if edit.get("item_id") == item.id and not edit.get("approved"):
            edit["outcome"] = "rejected"
    for directive in state["directives"]:
        if directive.get("item_id") == item.id and directive.get("outcome") == "pending":
            directive["outcome"] = "rejected"
    state["rejections"] = state["rejections"][-200:]
    state["user_notes"] = state["user_notes"][-200:]
    _rebuild_patterns(state)
    _rebuild_directive_preferences(state)
    _save_state(root, state)


def learning_status(root: Path) -> dict:
    """Kompakter, in der UI sichtbarer Stand der nachvollziehbaren Lerndaten."""
    state = load_state(root)
    return {
        "approvals": len(state["approvals"]),
        "approved_edits": sum(
            1 for edit in state["edits"]
            if edit.get("approved") or edit.get("outcome") == "approved"
        ),
        "pending_edits": sum(
            1 for edit in state["edits"] if edit.get("outcome", "pending") == "pending"
        ),
        "rejections": len(state["rejections"]),
        "patterns": len(state["patterns"]),
        "approved_directives": sum(
            1 for event in state["directives"] if event.get("outcome") == "approved"
        ),
        "pending_directives": sum(
            1 for event in state["directives"] if event.get("outcome") == "pending"
        ),
        "user_notes": len(state["user_notes"]),
        "auto_approvals": int(state["auto_approval_totals"]["all"]),
    }


def job_trust(root: Path, job_id: str) -> dict:
    trust = load_state(root)["job_trust"].get(job_id, {})
    streak = int(trust.get("unchanged_streak", 0))
    unlocked = bool(trust.get("unlocked", False))
    return {
        "unchanged_streak": streak,
        "required": 10,
        "remaining": max(0, 10 - streak),
        "unlocked": unlocked,
    }


def score_threshold(root: Path, job_id: str, top_percent: int) -> float | None:
    """Grenzwert des historischen oberen Perzentils manueller Freigaben."""
    scores = sorted(
        float(entry["score_before_approval"])
        for entry in load_state(root)["approvals"]
        if entry.get("source_job_id") == job_id
        and not entry.get("automatic")
        and entry.get("score_before_approval") is not None
    )
    if len(scores) < 10:
        return None
    index = min(len(scores) - 1, math.floor((1 - top_percent / 100) * len(scores)))
    return scores[index]


def record_auto_approval(
    root: Path, item: QueueItem, job_id: str, mode: str, threshold: float
) -> None:
    """Automatische Freigaben auditierbar speichern, aber nicht als Nutzertraining werten."""
    state = load_state(root)
    state["auto_approvals"].append(
        {
            "at": datetime.now().isoformat(timespec="seconds"),
            "item_id": item.id,
            "source_job_id": job_id,
            "mode": mode,
            "score": item.evaluation_score,
            "threshold": threshold,
        }
    )
    state["auto_approvals"] = state["auto_approvals"][-200:]
    totals = state["auto_approval_totals"]
    totals["all"] = int(totals.get("all", 0)) + 1
    by_job = totals.setdefault("by_job", {})
    by_job[job_id] = int(by_job.get(job_id, 0)) + 1
    by_mode = totals.setdefault("by_mode", {})
    by_mode[mode] = int(by_mode.get(mode, 0)) + 1
    _save_state(root, state)


def auto_approval_stats(root: Path, job_id: str | None = None) -> dict:
    """Dauerhafter Auto-Counter plus jüngstes Audit-Ereignis für die UI."""
    state = load_state(root)
    totals = state["auto_approval_totals"]
    events = [
        event for event in state["auto_approvals"]
        if job_id is None or event.get("source_job_id") == job_id
    ]
    total = (
        int(totals.get("all", 0))
        if job_id is None
        else int(totals.get("by_job", {}).get(job_id, 0))
    )
    return {
        "total": total,
        "last_at": events[-1].get("at") if events else None,
        "last_score": events[-1].get("score") if events else None,
    }


def apply_learned_patterns(root: Path, text: str) -> tuple[str, list[str]]:
    """Wiederkehrende, exakte Nutzerkorrekturen vorsichtig auf neue Texte anwenden."""
    state = load_state(root)
    revised = text
    applied: list[str] = []
    patterns = sorted(state["patterns"], key=lambda p: int(p.get("count", 1)), reverse=True)
    for pattern in patterns:
        source, target = pattern.get("from", ""), pattern.get("to", "")
        if not source or len(applied) >= 4:
            continue
        changed, n = re.subn(re.escape(source), target, revised, count=1, flags=re.I)
        if n:
            revised = re.sub(r" {2,}", " ", changed)
            applied.append(f"„{source}“ → „{target or 'entfernt'}“")
    return revised.strip(), applied


def evaluate_text(root: Path, text: str, kind: str, max_chars: int) -> tuple[float, list[str]]:
    """Erklärbarer Schätzwert, wie gut ein Text zu bisherigem Nutzerverhalten passt."""
    words = _words(text)
    score = 0.42
    reasons: list[str] = []

    if 20 <= len(words) and len(text) <= max_chars:
        score += 0.10
        reasons.append("passende Länge")
    elif len(text) > max_chars:
        score -= 0.20
        reasons.append(f"über dem Zeichenlimit ({len(text)}/{max_chars})")

    personal = re.search(r"\b(ich|wir|mein\w*|unser\w*|i|we|my|our)\b", text, re.I)
    if personal:
        score += 0.10
        reasons.append("persönliche Perspektive")
    else:
        reasons.append("wenig persönliche Perspektive")

    if re.search(r"(happy|augenzwinker|wie ein|statt|für mich|ehrlich|mal ehrlich)", text, re.I):
        score += 0.08
        reasons.append("erkennbare persönliche Marker")

    buzzwords = re.findall(
        r"\b(game.?changer|revolutionär|bahnbrechend|einzigartig|synergien|best.?in.?class)\b",
        text,
        re.I,
    )
    if buzzwords:
        score -= min(0.16, 0.05 * len(buzzwords))
        reasons.append("Marketing-Sprech erkannt")
    else:
        score += 0.06

    sentence_lengths = [len(_words(s)) for s in re.split(r"[.!?]+", text) if _words(s)]
    average = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0
    if 6 <= average <= 22:
        score += 0.07
        reasons.append("natürlicher Satzrhythmus")

    if kind in {"comment", "connection"}:
        if not re.search(r"https?://", text):
            score += 0.04
        if len(sentence_lengths) <= 5:
            score += 0.04

    state = load_state(root)
    approved = [
        a.get("text", "") for a in state["approvals"]
        if a.get("text") and a.get("kind") == kind
    ]
    if approved:
        similarity = max(_similarity(text, example) for example in approved)
        score += 0.16 * similarity
        reasons.append(f"Nähe zu freigegebenen Beispielen {round(similarity * 100)} %")
    else:
        reasons.append("noch wenig persönliche Lerndaten")

    # Direkte Nutzerformulierungen zählen stärker als alte Agentenformulierungen.
    edited_finals = [
        e.get("after", "") for e in state["edits"]
        if e.get("after") and (e.get("approved") or e.get("outcome") == "approved")
        and e.get("kind") == kind
    ]
    if edited_finals:
        similarity = max(_similarity(text, example) for example in edited_finals)
        score += 0.10 * similarity

    rejected = []
    for entry in state["rejections"]:
        if entry.get("kind") != kind:
            continue
        rejected.extend(
            candidate for candidate in (entry.get("text", ""), entry.get("generated_text", ""))
            if candidate
        )
    if rejected:
        similarity = max(_similarity(text, example) for example in rejected)
        score -= 0.20 * similarity
        reasons.append(f"Nähe zu abgelehnten Beispielen {round(similarity * 100)} %")

    return round(max(0.05, min(0.95, score)), 2), reasons[:6]


def _candidate_slots(campaign: Campaign, kind: str) -> list[int]:
    lo, hi = campaign.schedule.active_hours
    preferred = [10, 12, 14, 16] if kind == "comment" else [9, 13, 16]
    slots = [hour for hour in preferred if lo <= hour < hi]
    return slots or list(range(lo, hi)) or [9]


def suggest_publish_at(
    campaign: Campaign,
    kind: str,
    used: set[str],
    now: datetime | None = None,
) -> str:
    """Nächsten freien, gut lesbaren Terminvorschlag innerhalb der Kampagne wählen."""
    now = now or datetime.now()
    earliest = now + timedelta(minutes=30)
    start = campaign.schedule.start or now.date()
    end = campaign.schedule.end
    for offset in range(92):
        day = max(start, now.date()) + timedelta(days=offset)
        if end and day > end:
            break
        for hour in _candidate_slots(campaign, kind):
            candidate = datetime.combine(day, datetime.min.time()).replace(hour=hour)
            value = candidate.isoformat(timespec="minutes")
            if candidate >= earliest and value not in used:
                return value
    # Außerhalb eines abgelaufenen Kampagnenfensters nicht still in der Vergangenheit planen.
    fallback = earliest.replace(second=0, microsecond=0)
    return fallback.isoformat(timespec="minutes")


def prepare_items(
    root: Path,
    campaign: Campaign,
    items: list[QueueItem],
    target_ids: set[str],
    scheduled: list[QueueItem],
    now: datetime | None = None,
) -> list[dict]:
    """Neue Texte lernen/anpassen, bewerten und mit einem Terminvorschlag versehen."""
    used = {i.publish_at for i in scheduled + items if i.publish_at}
    result: list[dict] = []
    for item in items:
        if item.id not in target_ids or not item.text.strip():
            continue
        new_baseline = item.generated_text is None
        revised, applied = apply_learned_patterns(root, item.text)
        item.text = revised
        if new_baseline:
            # Das ist die automatisch vorbereitete Fassung, die der Nutzer sieht.
            item.generated_text = item.text
        max_chars = (
            300
            if item.kind == "connection"
            else campaign.max_comment_chars
            if item.kind == "comment"
            else campaign.max_post_chars
        )
        score, reasons = evaluate_text(root, item.text, item.kind, max_chars)
        item.evaluation_score = score
        note = "; ".join(reasons)
        if applied:
            note += "; gelernte Anpassung: " + ", ".join(applied)
        item.evaluation_note = note
        item.evaluated_at = datetime.now().isoformat(timespec="minutes")
        if not item.publish_at:
            item.publish_at = suggest_publish_at(campaign, item.kind, used, now=now)
            used.add(item.publish_at)
        result.append(
            {
                "id": item.id,
                "score": score,
                "publish_at": item.publish_at,
                "adjusted": bool(applied),
            }
        )
    return result
