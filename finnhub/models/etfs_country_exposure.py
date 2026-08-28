from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .etfcountry_exposure_data import EtfcountryExposureData, EtfcountryExposureDataDict


class EtfsCountryExposure(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """ETF symbol."""

    country_exposure: Optional[list[EtfcountryExposureData]] = Field(default=UNSET, alias="countryExposure")
    """Array of countries and and exposure levels."""


class EtfsCountryExposureDict(TypedDict):
    symbol: NotRequired[str]
    country_exposure: NotRequired[list[EtfcountryExposureData | EtfcountryExposureDataDict]]
