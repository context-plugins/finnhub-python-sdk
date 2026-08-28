from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class StockTranscripts(SdkBaseModel):
    id: Optional[str] = UNSET
    """Transcript's ID used to get the <a href="#transcripts">full transcript</a>."""

    title: Optional[str] = UNSET
    """Title."""

    time: Optional[str] = UNSET
    """Time of the event."""

    year: Optional[int] = UNSET
    """Year of earnings result in the case of earnings call transcript."""

    quarter: Optional[int] = UNSET
    """Quarter of earnings result in the case of earnings call transcript."""


class StockTranscriptsDict(TypedDict):
    id: NotRequired[str]
    title: NotRequired[str]
    time: NotRequired[str]
    year: NotRequired[int]
    quarter: NotRequired[int]
