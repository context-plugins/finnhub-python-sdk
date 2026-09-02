from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VisaApplication(SdkBaseModel):
    year: Optional[int] = UNSET
    """Year."""

    quarter: Optional[int] = UNSET
    """Quarter."""

    symbol: Optional[str] = UNSET
    """Symbol."""

    case_number: Optional[str] = Field(default=UNSET, alias="caseNumber")
    """Case number."""

    case_status: Optional[str] = Field(default=UNSET, alias="caseStatus")
    """Case status."""

    received_date: Optional[str] = Field(default=UNSET, alias="receivedDate")
    """Received date."""

    visa_class: Optional[str] = Field(default=UNSET, alias="visaClass")
    """Visa class."""

    job_title: Optional[str] = Field(default=UNSET, alias="jobTitle")
    """Job Title."""

    soc_code: Optional[str] = Field(default=UNSET, alias="socCode")
    """SOC Code. A list of SOC code can be found <a href="https://www.bls.gov/oes/current/oes_stru.htm"
    target="_blank">here</a>."""

    full_time_position: Optional[str] = Field(default=UNSET, alias="fullTimePosition")
    """Full-time position flag."""

    begin_date: Optional[str] = Field(default=UNSET, alias="beginDate")
    """Job's start date."""

    end_date: Optional[str] = Field(default=UNSET, alias="endDate")
    """Job's end date."""

    employer_name: Optional[str] = Field(default=UNSET, alias="employerName")
    """Company's name."""

    worksite_address: Optional[str] = Field(default=UNSET, alias="worksiteAddress")
    """Worksite address."""

    worksite_city: Optional[str] = Field(default=UNSET, alias="worksiteCity")
    """Worksite city."""

    worksite_county: Optional[str] = Field(default=UNSET, alias="worksiteCounty")
    """Worksite county."""

    worksite_state: Optional[str] = Field(default=UNSET, alias="worksiteState")
    """Worksite state."""

    worksite_postal_code: Optional[str] = Field(default=UNSET, alias="worksitePostalCode")
    """Worksite postal code."""

    wage_range_from: Optional[float] = Field(default=UNSET, alias="wageRangeFrom")
    """Wage range from."""

    wage_range_to: Optional[float] = Field(default=UNSET, alias="wageRangeTo")
    """Wage range to."""

    wage_unit_of_pay: Optional[str] = Field(default=UNSET, alias="wageUnitOfPay")
    """Wage unit of pay."""

    wage_level: Optional[str] = Field(default=UNSET, alias="wageLevel")
    """Wage level."""

    h1b_dependent: Optional[str] = Field(default=UNSET, alias="h1bDependent")
    """H1B dependent flag."""


class VisaApplicationDict(TypedDict):
    year: NotRequired[int]
    quarter: NotRequired[int]
    symbol: NotRequired[str]
    case_number: NotRequired[str]
    case_status: NotRequired[str]
    received_date: NotRequired[str]
    visa_class: NotRequired[str]
    job_title: NotRequired[str]
    soc_code: NotRequired[str]
    full_time_position: NotRequired[str]
    begin_date: NotRequired[str]
    end_date: NotRequired[str]
    employer_name: NotRequired[str]
    worksite_address: NotRequired[str]
    worksite_city: NotRequired[str]
    worksite_county: NotRequired[str]
    worksite_state: NotRequired[str]
    worksite_postal_code: NotRequired[str]
    wage_range_from: NotRequired[float]
    wage_range_to: NotRequired[float]
    wage_unit_of_pay: NotRequired[str]
    wage_level: NotRequired[str]
    h1b_dependent: NotRequired[str]
