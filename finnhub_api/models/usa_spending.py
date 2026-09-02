from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsaSpending(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol."""

    recipient_name: Optional[str] = Field(default=UNSET, alias="recipientName")
    """Company's name."""

    recipient_parent_name: Optional[str] = Field(default=UNSET, alias="recipientParentName")
    """Company's name."""

    award_description: Optional[str] = Field(default=UNSET, alias="awardDescription")
    """Description."""

    country: Optional[str] = UNSET
    """Recipient's country."""

    action_date: Optional[str] = Field(default=UNSET, alias="actionDate")
    """Period."""

    total_value: Optional[float] = Field(default=UNSET, alias="totalValue")
    """Income reported by lobbying firms."""

    performance_start_date: Optional[str] = Field(default=UNSET, alias="performanceStartDate")
    """Performance start date."""

    performance_end_date: Optional[str] = Field(default=UNSET, alias="performanceEndDate")
    """Performance end date."""

    awarding_agency_name: Optional[str] = Field(default=UNSET, alias="awardingAgencyName")
    """Award agency."""

    awarding_sub_agency_name: Optional[str] = Field(default=UNSET, alias="awardingSubAgencyName")
    """Award sub-agency."""

    awarding_office_name: Optional[str] = Field(default=UNSET, alias="awardingOfficeName")
    """Award office name."""

    performance_country: Optional[str] = Field(default=UNSET, alias="performanceCountry")
    """Performance country."""

    performance_city: Optional[str] = Field(default=UNSET, alias="performanceCity")
    """Performance city."""

    performance_county: Optional[str] = Field(default=UNSET, alias="performanceCounty")
    """Performance county."""

    performance_state: Optional[str] = Field(default=UNSET, alias="performanceState")
    """Performance state."""

    performance_zip_code: Optional[str] = Field(default=UNSET, alias="performanceZipCode")
    """Performance zip code."""

    performance_congressional_district: Optional[str] = Field(default=UNSET, alias="performanceCongressionalDistrict")
    """Performance congressional district."""

    naics_code: Optional[str] = Field(default=UNSET, alias="naicsCode")
    """NAICS code."""

    permalink: Optional[str] = UNSET
    """Permalink."""


class UsaSpendingDict(TypedDict):
    symbol: NotRequired[str]
    recipient_name: NotRequired[str]
    recipient_parent_name: NotRequired[str]
    award_description: NotRequired[str]
    country: NotRequired[str]
    action_date: NotRequired[str]
    total_value: NotRequired[float]
    performance_start_date: NotRequired[str]
    performance_end_date: NotRequired[str]
    awarding_agency_name: NotRequired[str]
    awarding_sub_agency_name: NotRequired[str]
    awarding_office_name: NotRequired[str]
    performance_country: NotRequired[str]
    performance_city: NotRequired[str]
    performance_county: NotRequired[str]
    performance_state: NotRequired[str]
    performance_zip_code: NotRequired[str]
    performance_congressional_district: NotRequired[str]
    naics_code: NotRequired[str]
    permalink: NotRequired[str]
