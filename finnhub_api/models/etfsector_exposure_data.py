from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EtfsectorExposureData(SdkBaseModel):
    industry: Optional[str] = UNSET
    """Industry"""

    exposure: Optional[float] = UNSET
    """Percent of exposure."""


class EtfsectorExposureDataDict(TypedDict):
    industry: NotRequired[str]
    exposure: NotRequired[float]
