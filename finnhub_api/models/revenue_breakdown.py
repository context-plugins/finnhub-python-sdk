from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .breakdown_item import BreakdownItem, BreakdownItemDict


class RevenueBreakdown(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol"""

    cik: Optional[str] = UNSET
    """CIK"""

    data: Optional[list[BreakdownItem]] = UNSET
    """Array of revenue breakdown over multiple periods."""


class RevenueBreakdownDict(TypedDict):
    symbol: NotRequired[str]
    cik: NotRequired[str]
    data: NotRequired[list[BreakdownItem | BreakdownItemDict]]
