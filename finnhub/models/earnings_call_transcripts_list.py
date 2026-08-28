from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .stock_transcripts import StockTranscripts, StockTranscriptsDict


class EarningsCallTranscriptsList(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Company symbol."""

    transcripts: Optional[list[StockTranscripts]] = UNSET
    """Array of transcripts' metadata"""


class EarningsCallTranscriptsListDict(TypedDict):
    symbol: NotRequired[str]
    transcripts: NotRequired[list[StockTranscripts | StockTranscriptsDict]]
