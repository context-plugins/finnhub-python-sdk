from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .revenue_estimates_info import RevenueEstimatesInfo, RevenueEstimatesInfoDict


class RevenueEstimates(SdkBaseModel):
    data: Optional[list[RevenueEstimatesInfo]] = UNSET
    """List of estimates"""

    freq: Optional[str] = UNSET
    """Frequency: annual or quarterly."""

    symbol: Optional[str] = UNSET
    """Company symbol."""


class RevenueEstimatesDict(TypedDict):
    data: NotRequired[list[RevenueEstimatesInfo | RevenueEstimatesInfoDict]]
    freq: NotRequired[str]
    symbol: NotRequired[str]
