from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pretax_income_estimates_info import PretaxIncomeEstimatesInfo, PretaxIncomeEstimatesInfoDict


class PretaxIncomeEstimates(SdkBaseModel):
    data: Optional[list[PretaxIncomeEstimatesInfo]] = UNSET
    """List of estimates"""

    freq: Optional[str] = UNSET
    """Frequency: annual or quarterly."""

    symbol: Optional[str] = UNSET
    """Company symbol."""


class PretaxIncomeEstimatesDict(TypedDict):
    data: NotRequired[list[PretaxIncomeEstimatesInfo | PretaxIncomeEstimatesInfoDict]]
    freq: NotRequired[str]
    symbol: NotRequired[str]
