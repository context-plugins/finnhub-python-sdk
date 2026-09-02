from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EarningsCallLiveResult(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol."""

    event: Optional[str] = UNSET
    """Event name."""

    time: Optional[str] = UNSET
    """Date time in UTC."""

    year: Optional[int] = UNSET
    """Earnings year."""

    quarter: Optional[int] = UNSET
    """Earnings quarter."""

    live_audio: Optional[str] = Field(default=UNSET, alias="liveAudio")
    """Live audio streaming file."""

    recording: Optional[str] = UNSET
    """Recoding in mp3 format."""


class EarningsCallLiveResultDict(TypedDict):
    symbol: NotRequired[str]
    event: NotRequired[str]
    time: NotRequired[str]
    year: NotRequired[int]
    quarter: NotRequired[int]
    live_audio: NotRequired[str]
    recording: NotRequired[str]
