from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MutualFundCountryExposureData(SdkBaseModel):
    country: Optional[str] = UNSET
    """Country"""

    exposure: Optional[float] = UNSET
    """Percent of exposure."""


class MutualFundCountryExposureDataDict(TypedDict):
    country: NotRequired[str]
    exposure: NotRequired[float]
