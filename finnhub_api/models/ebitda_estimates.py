from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .ebitda_estimates_info import EbitdaEstimatesInfo, EbitdaEstimatesInfoDict


class EbitdaEstimates(SdkBaseModel):
    data: Optional[list[EbitdaEstimatesInfo]] = UNSET
    """List of estimates"""

    freq: Optional[str] = UNSET
    """Frequency: annual or quarterly."""

    symbol: Optional[str] = UNSET
    """Company symbol."""


class EbitdaEstimatesDict(TypedDict):
    data: NotRequired[list[EbitdaEstimatesInfo | EbitdaEstimatesInfoDict]]
    freq: NotRequired[str]
    symbol: NotRequired[str]
