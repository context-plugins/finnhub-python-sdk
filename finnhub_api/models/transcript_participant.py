from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TranscriptParticipant(SdkBaseModel):
    name: Optional[str] = UNSET
    """Participant's name"""

    description: Optional[str] = UNSET
    """Participant's description"""

    role: Optional[str] = UNSET
    """Whether the speak is a company's executive or an analyst"""


class TranscriptParticipantDict(TypedDict):
    name: NotRequired[str]
    description: NotRequired[str]
    role: NotRequired[str]
