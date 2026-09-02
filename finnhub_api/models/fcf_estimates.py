from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fcf_estimates_info import FcfEstimatesInfo, FcfEstimatesInfoDict


class FcfEstimates(SdkBaseModel):
    data: Optional[list[FcfEstimatesInfo]] = UNSET
    """List of estimates"""

    freq: Optional[str] = UNSET
    """Frequency: annual or quarterly."""

    symbol: Optional[str] = UNSET
    """Company symbol."""


class FcfEstimatesDict(TypedDict):
    data: NotRequired[list[FcfEstimatesInfo | FcfEstimatesInfoDict]]
    freq: NotRequired[str]
    symbol: NotRequired[str]
