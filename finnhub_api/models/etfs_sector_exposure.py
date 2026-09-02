from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .etfsector_exposure_data import EtfsectorExposureData, EtfsectorExposureDataDict


class EtfsSectorExposure(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """ETF symbol."""

    sector_exposure: Optional[list[EtfsectorExposureData]] = Field(default=UNSET, alias="sectorExposure")
    """Array of industries and exposure levels."""


class EtfsSectorExposureDict(TypedDict):
    symbol: NotRequired[str]
    sector_exposure: NotRequired[list[EtfsectorExposureData | EtfsectorExposureDataDict]]
