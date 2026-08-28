from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .net_income_estimates_info import NetIncomeEstimatesInfo, NetIncomeEstimatesInfoDict


class NetIncomeEstimates(SdkBaseModel):
    data: Optional[list[NetIncomeEstimatesInfo]] = UNSET
    """List of estimates"""

    freq: Optional[str] = UNSET
    """Frequency: annual or quarterly."""

    symbol: Optional[str] = UNSET
    """Company symbol."""


class NetIncomeEstimatesDict(TypedDict):
    data: NotRequired[list[NetIncomeEstimatesInfo | NetIncomeEstimatesInfoDict]]
    freq: NotRequired[str]
    symbol: NotRequired[str]
