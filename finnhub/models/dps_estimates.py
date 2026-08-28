from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dps_estimates_info import DpsEstimatesInfo, DpsEstimatesInfoDict


class DpsEstimates(SdkBaseModel):
    data: Optional[list[DpsEstimatesInfo]] = UNSET
    """List of estimates"""

    freq: Optional[str] = UNSET
    """Frequency: annual or quarterly."""

    symbol: Optional[str] = UNSET
    """Company symbol."""


class DpsEstimatesDict(TypedDict):
    data: NotRequired[list[DpsEstimatesInfo | DpsEstimatesInfoDict]]
    freq: NotRequired[str]
    symbol: NotRequired[str]
