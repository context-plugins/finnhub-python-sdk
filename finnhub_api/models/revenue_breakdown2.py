from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RevenueBreakdown2(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol"""

    currency: Optional[str] = UNSET
    """currency"""

    data: Optional[Any] = UNSET
    """Revenue breakdown data."""


class RevenueBreakdown2Dict(TypedDict):
    symbol: NotRequired[str]
    currency: NotRequired[str]
    data: NotRequired[Any]
