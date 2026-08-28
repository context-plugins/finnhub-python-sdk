from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .insider_sentiments_data import InsiderSentimentsData, InsiderSentimentsDataDict


class InsiderSentiments(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol of the company."""

    data: Optional[list[InsiderSentimentsData]] = UNSET
    """Array of sentiment data."""


class InsiderSentimentsDict(TypedDict):
    symbol: NotRequired[str]
    data: NotRequired[list[InsiderSentimentsData | InsiderSentimentsDataDict]]
