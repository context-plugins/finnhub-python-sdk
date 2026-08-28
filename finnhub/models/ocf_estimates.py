from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .ocf_estimates_info import OcfEstimatesInfo, OcfEstimatesInfoDict


class OcfEstimates(SdkBaseModel):
    data: Optional[list[OcfEstimatesInfo]] = UNSET
    """List of estimates"""

    freq: Optional[str] = UNSET
    """Frequency: annual or quarterly."""

    symbol: Optional[str] = UNSET
    """Company symbol."""


class OcfEstimatesDict(TypedDict):
    data: NotRequired[list[OcfEstimatesInfo | OcfEstimatesInfoDict]]
    freq: NotRequired[str]
    symbol: NotRequired[str]
