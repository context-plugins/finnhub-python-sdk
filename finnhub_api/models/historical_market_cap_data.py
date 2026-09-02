from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .market_cap_data import MarketCapData, MarketCapDataDict


class HistoricalMarketCapData(SdkBaseModel):
    data: Optional[list[MarketCapData]] = UNSET
    """Array of market data."""

    symbol: Optional[str] = UNSET
    """Symbol"""

    currency: Optional[str] = UNSET
    """Currency"""


class HistoricalMarketCapDataDict(TypedDict):
    data: NotRequired[list[MarketCapData | MarketCapDataDict]]
    symbol: NotRequired[str]
    currency: NotRequired[str]
