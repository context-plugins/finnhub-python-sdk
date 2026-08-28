from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .gross_income_estimates_info import GrossIncomeEstimatesInfo, GrossIncomeEstimatesInfoDict


class GrossIncomeEstimates(SdkBaseModel):
    data: Optional[list[GrossIncomeEstimatesInfo]] = UNSET
    """List of estimates"""

    freq: Optional[str] = UNSET
    """Frequency: annual or quarterly."""

    symbol: Optional[str] = UNSET
    """Company symbol."""


class GrossIncomeEstimatesDict(TypedDict):
    data: NotRequired[list[GrossIncomeEstimatesInfo | GrossIncomeEstimatesInfoDict]]
    freq: NotRequired[str]
    symbol: NotRequired[str]
