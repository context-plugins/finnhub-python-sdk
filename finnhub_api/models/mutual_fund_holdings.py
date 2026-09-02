from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .mutual_fund_holdings_data import MutualFundHoldingsData, MutualFundHoldingsDataDict


class MutualFundHoldings(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol."""

    at_date: Optional[Date] = Field(default=UNSET, alias="atDate")
    """Holdings update date."""

    number_of_holdings: Optional[int] = Field(default=UNSET, alias="numberOfHoldings")
    """Number of holdings."""

    holdings: Optional[list[MutualFundHoldingsData]] = UNSET
    """Array of holdings."""


class MutualFundHoldingsDict(TypedDict):
    symbol: NotRequired[str]
    at_date: NotRequired[Date]
    number_of_holdings: NotRequired[int]
    holdings: NotRequired[list[MutualFundHoldingsData | MutualFundHoldingsDataDict]]
