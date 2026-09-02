from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .ebit_estimates_info import EbitEstimatesInfo, EbitEstimatesInfoDict


class EbitEstimates(SdkBaseModel):
    data: Optional[list[EbitEstimatesInfo]] = UNSET
    """List of estimates"""

    freq: Optional[str] = UNSET
    """Frequency: annual or quarterly."""

    symbol: Optional[str] = UNSET
    """Company symbol."""


class EbitEstimatesDict(TypedDict):
    data: NotRequired[list[EbitEstimatesInfo | EbitEstimatesInfoDict]]
    freq: NotRequired[str]
    symbol: NotRequired[str]
