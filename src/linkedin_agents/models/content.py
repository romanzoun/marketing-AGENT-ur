"""Content- und Feed-Datenmodelle, die zwischen den Agenten fließen."""
from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

# post = eigener Beitrag, comment = Kommentar unter fremdem Beitrag,
# reply = Antwort auf einen Kommentar, reshare = Beitrag teilen (mit Meinung)
ContentKind = Literal["post", "comment", "reply", "reshare", "connection"]


class FeedPost(BaseModel):
    """Ein im Feed gesammelter Beitrag (Grundlage für Kommentare/Replies)."""

    id: str
    author: str = ""
    text: str = ""
    url: str | None = None


class ProfileCandidate(BaseModel):
    """Ein noch nicht vernetztes LinkedIn-Profil aus der Personensuche."""

    name: str
    headline: str = ""
    url: str


class ContentIdea(BaseModel):
    """Eine vom Strategen geplante Content-Einheit."""

    kind: ContentKind
    topic: str
    angle: str = Field(..., description="Blickwinkel / Kernbotschaft")
    target_post_id: str | None = Field(
        default=None,
        description="ID des Feed-Posts, auf den kommentiert/geantwortet/den man teilt",
    )
    wants_image: bool = Field(
        default=False,
        description="Ob zu diesem Beitrag ein Bild generiert werden soll",
    )


class GeneratedContent(BaseModel):
    """Fertiger, vom Copywriter verfasster Text."""

    kind: ContentKind
    text: str
    hashtags: list[str] = Field(default_factory=list)
    target_post_id: str | None = None
    rationale: str = ""
    image_path: str | None = Field(default=None, description="Pfad zum generierten Bild")

    def full_text(self) -> str:
        tags = " ".join(h if h.startswith("#") else f"#{h}" for h in self.hashtags)
        return f"{self.text}\n\n{tags}".strip() if tags else self.text


class ReviewResult(BaseModel):
    """Ergebnis der Kampagnen-Konformitätsprüfung durch den Reviewer."""

    approved: bool
    score: float = Field(0.0, ge=0.0, le=1.0)
    reasons: list[str] = Field(default_factory=list)
    revised_text: str | None = None
