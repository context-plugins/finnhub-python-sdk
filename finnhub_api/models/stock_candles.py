from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class StockCandles(SdkBaseModel):
    o: Optional[list[float]] = UNSET
    """List of open prices for returned candles."""

    h: Optional[list[float]] = UNSET
    """List of high prices for returned candles."""

    l_: Optional[list[float]] = Field(default=UNSET, alias="l")
    """List of low prices for returned candles."""

    c: Optional[list[float]] = UNSET
    """List of close prices for returned candles."""

    v: Optional[list[float]] = UNSET
    """List of volume data for returned candles."""

    t: Optional[list[int]] = UNSET
    """List of timestamp for returned candles."""

    s: Optional[str] = UNSET
    """Status of the response. This field can either be ok or no_data."""


class StockCandlesDict(TypedDict):
    o: NotRequired[list[float]]
    h: NotRequired[list[float]]
    l_: NotRequired[list[float]]
    c: NotRequired[list[float]]
    v: NotRequired[list[float]]
    t: NotRequired[list[int]]
    s: NotRequired[str]
