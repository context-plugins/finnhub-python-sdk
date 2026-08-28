from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .etfholdings_data import EtfholdingsData, EtfholdingsDataDict


class EtfsHoldings(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """ETF symbol."""

    at_date: Optional[Date] = Field(default=UNSET, alias="atDate")
    """Holdings update date."""

    number_of_holdings: Optional[int] = Field(default=UNSET, alias="numberOfHoldings")
    """Number of holdings."""

    holdings: Optional[list[EtfholdingsData]] = UNSET
    """Array of holdings."""


class EtfsHoldingsDict(TypedDict):
    symbol: NotRequired[str]
    at_date: NotRequired[Date]
    number_of_holdings: NotRequired[int]
    holdings: NotRequired[list[EtfholdingsData | EtfholdingsDataDict]]
