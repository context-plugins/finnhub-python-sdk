from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .capex_estimates_info import CapexEstimatesInfo, CapexEstimatesInfoDict


class CapexEstimates(SdkBaseModel):
    data: Optional[list[CapexEstimatesInfo]] = UNSET
    """List of estimates"""

    freq: Optional[str] = UNSET
    """Frequency: annual or quarterly."""

    symbol: Optional[str] = UNSET
    """Company symbol."""


class CapexEstimatesDict(TypedDict):
    data: NotRequired[list[CapexEstimatesInfo | CapexEstimatesInfoDict]]
    freq: NotRequired[str]
    symbol: NotRequired[str]
