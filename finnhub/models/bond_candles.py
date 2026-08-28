from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BondCandles(SdkBaseModel):
    c: Optional[list[float]] = UNSET
    """List of close prices for returned candles."""

    t: Optional[list[int]] = UNSET
    """List of timestamp for returned candles."""

    s: Optional[str] = UNSET
    """Status of the response. This field can either be ok or no_data."""


class BondCandlesDict(TypedDict):
    c: NotRequired[list[float]]
    t: NotRequired[list[int]]
    s: NotRequired[str]
