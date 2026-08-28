from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TranscriptContent(SdkBaseModel):
    name: Optional[str] = UNSET
    """Speaker's name"""

    speech: Optional[list[str]] = UNSET
    """Speaker's speech"""

    session: Optional[str] = UNSET
    """Earnings calls section (management discussion or Q&A)"""


class TranscriptContentDict(TypedDict):
    name: NotRequired[str]
    speech: NotRequired[list[str]]
    session: NotRequired[str]
