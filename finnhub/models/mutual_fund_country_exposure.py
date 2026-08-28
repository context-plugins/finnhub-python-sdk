from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .mutual_fund_country_exposure_data import MutualFundCountryExposureData, MutualFundCountryExposureDataDict


class MutualFundCountryExposure(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol."""

    country_exposure: Optional[list[MutualFundCountryExposureData]] = Field(default=UNSET, alias="countryExposure")
    """Array of countries and and exposure levels."""


class MutualFundCountryExposureDict(TypedDict):
    symbol: NotRequired[str]
    country_exposure: NotRequired[list[MutualFundCountryExposureData | MutualFundCountryExposureDataDict]]
