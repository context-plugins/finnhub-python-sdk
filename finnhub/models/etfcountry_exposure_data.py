from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EtfcountryExposureData(SdkBaseModel):
    country: Optional[str] = UNSET
    """Country"""

    exposure: Optional[float] = UNSET
    """Percent of exposure."""


class EtfcountryExposureDataDict(TypedDict):
    country: NotRequired[str]
    exposure: NotRequired[float]
