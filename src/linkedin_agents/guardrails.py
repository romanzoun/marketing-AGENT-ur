"""Laufzeit-Guardrails: erzwingen die Mengenlimits einer Kampagne im Code."""
from __future__ import annotations

from ..models.campaign import Limits
from ..models.content import ContentKind


class RunGuardrails:
    """Zählt ausgeführte Aktionen und blockt bei Überschreiten der Limits."""

    def __init__(self, limits: Limits) -> None:
        self._limits = limits
        self._counts: dict[ContentKind, int] = {
            "post": 0,
            "comment": 0,
            "reply": 0,
            "reshare": 0,
        }

    def _limit_for(self, kind: ContentKind) -> int:
        return {
            "post": self._limits.posts_per_run,
            "comment": self._limits.comments_per_run,
            "reply": self._limits.replies_per_run,
            "reshare": self._limits.reshares_per_run,
        }[kind]

    def remaining(self, kind: ContentKind) -> int:
        return max(0, self._limit_for(kind) - self._counts[kind])

    def allows(self, kind: ContentKind) -> bool:
        return self.remaining(kind) > 0

    def record(self, kind: ContentKind) -> None:
        self._counts[kind] += 1

    def summary(self) -> str:
        return (
            f"posts={self._counts['post']}/{self._limits.posts_per_run}, "
            f"comments={self._counts['comment']}/{self._limits.comments_per_run}, "
            f"replies={self._counts['reply']}/{self._limits.replies_per_run}, "
            f"reshares={self._counts['reshare']}/{self._limits.reshares_per_run}"
        )
