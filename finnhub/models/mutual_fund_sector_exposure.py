from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .mutual_fund_sector_exposure_data import MutualFundSectorExposureData, MutualFundSectorExposureDataDict


class MutualFundSectorExposure(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Mutual symbol."""

    sector_exposure: Optional[list[MutualFundSectorExposureData]] = Field(default=UNSET, alias="sectorExposure")
    """Array of sector and exposure levels."""


class MutualFundSectorExposureDict(TypedDict):
    symbol: NotRequired[str]
    sector_exposure: NotRequired[list[MutualFundSectorExposureData | MutualFundSectorExposureDataDict]]
