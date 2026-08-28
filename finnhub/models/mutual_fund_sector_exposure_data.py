from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MutualFundSectorExposureData(SdkBaseModel):
    sector: Optional[str] = UNSET
    """Sector"""

    exposure: Optional[float] = UNSET
    """Percent of exposure."""


class MutualFundSectorExposureDataDict(TypedDict):
    sector: NotRequired[str]
    exposure: NotRequired[float]
