from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transcript_content import TranscriptContent, TranscriptContentDict
from .transcript_participant import TranscriptParticipant, TranscriptParticipantDict


class EarningsCallTranscripts(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Company symbol."""

    transcript: Optional[list[TranscriptContent]] = UNSET
    """Transcript content."""

    participant: Optional[list[TranscriptParticipant]] = UNSET
    """Participant list"""

    audio: Optional[str] = UNSET
    """Audio link."""

    id: Optional[str] = UNSET
    """Transcript's ID."""

    title: Optional[str] = UNSET
    """Title."""

    time: Optional[str] = UNSET
    """Time of the event."""

    year: Optional[int] = UNSET
    """Year of earnings result in the case of earnings call transcript."""

    quarter: Optional[int] = UNSET
    """Quarter of earnings result in the case of earnings call transcript."""


class EarningsCallTranscriptsDict(TypedDict):
    symbol: NotRequired[str]
    transcript: NotRequired[list[TranscriptContent | TranscriptContentDict]]
    participant: NotRequired[list[TranscriptParticipant | TranscriptParticipantDict]]
    audio: NotRequired[str]
    id: NotRequired[str]
    title: NotRequired[str]
    time: NotRequired[str]
    year: NotRequired[int]
    quarter: NotRequired[int]
