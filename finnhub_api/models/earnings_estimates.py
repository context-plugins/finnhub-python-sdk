from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .earnings_estimates_info import EarningsEstimatesInfo, EarningsEstimatesInfoDict


class EarningsEstimates(SdkBaseModel):
    data: Optional[list[EarningsEstimatesInfo]] = UNSET
    """List of estimates"""

    freq: Optional[str] = UNSET
    """Frequency: annual or quarterly."""

    symbol: Optional[str] = UNSET
    """Company symbol."""


class EarningsEstimatesDict(TypedDict):
    data: NotRequired[list[EarningsEstimatesInfo | EarningsEstimatesInfoDict]]
    freq: NotRequired[str]
    symbol: NotRequired[str]
