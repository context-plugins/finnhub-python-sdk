from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class CompanyProfile(SdkBaseModel):
    alias: Optional[list[str]] = UNSET
    """Company name alias."""

    address: Optional[str] = UNSET
    """Address of company's headquarter."""

    city: Optional[str] = UNSET
    """City of company's headquarter."""

    country: Optional[str] = UNSET
    """Country of company's headquarter."""

    currency: Optional[str] = UNSET
    """Currency used in company filings and financials."""

    estimate_currency: Optional[str] = Field(default=UNSET, alias="estimateCurrency")
    """Currency used in Estimates data."""

    market_cap_currency: Optional[str] = Field(default=UNSET, alias="marketCapCurrency")
    """Currency used in market capitalization."""

    cusip: Optional[str] = UNSET
    """CUSIP number."""

    sedol: Optional[str] = UNSET
    """Sedol number."""

    description: Optional[str] = UNSET
    """Company business summary."""

    exchange: Optional[str] = UNSET
    """Listed exchange."""

    ggroup: Optional[str] = UNSET
    """Industry group."""

    gind: Optional[str] = UNSET
    """Industry."""

    gsector: Optional[str] = UNSET
    """Sector."""

    gsubind: Optional[str] = UNSET
    """Sub-industry."""

    isin: Optional[str] = UNSET
    """ISIN number."""

    lei: Optional[str] = UNSET
    """LEI number."""

    ir_url: Optional[str] = Field(default=UNSET, alias="irUrl")
    """Investor relations website."""

    naics_national_industry: Optional[str] = Field(default=UNSET, alias="naicsNationalIndustry")
    """NAICS national industry."""

    naics: Optional[str] = UNSET
    """NAICS industry."""

    naics_sector: Optional[str] = Field(default=UNSET, alias="naicsSector")
    """NAICS sector."""

    naics_subsector: Optional[str] = Field(default=UNSET, alias="naicsSubsector")
    """NAICS subsector."""

    name: Optional[str] = UNSET
    """Company name."""

    phone: Optional[str] = UNSET
    """Company phone number."""

    state: Optional[str] = UNSET
    """State of company's headquarter."""

    ticker: Optional[str] = UNSET
    """Company symbol/ticker as used on the listed exchange."""

    weburl: Optional[str] = UNSET
    """Company website."""

    ipo: Optional[Date] = UNSET
    """IPO date."""

    market_capitalization: Optional[float] = Field(default=UNSET, alias="marketCapitalization")
    """Market Capitalization."""

    share_outstanding: Optional[float] = Field(default=UNSET, alias="shareOutstanding")
    """Number of oustanding shares."""

    employee_total: Optional[float] = Field(default=UNSET, alias="employeeTotal")
    """Number of employee."""

    logo: Optional[str] = UNSET
    """Logo image."""

    finnhub_industry: Optional[str] = Field(default=UNSET, alias="finnhubIndustry")
    """Finnhub industry classification."""


class CompanyProfileDict(TypedDict):
    alias: NotRequired[list[str]]
    address: NotRequired[str]
    city: NotRequired[str]
    country: NotRequired[str]
    currency: NotRequired[str]
    estimate_currency: NotRequired[str]
    market_cap_currency: NotRequired[str]
    cusip: NotRequired[str]
    sedol: NotRequired[str]
    description: NotRequired[str]
    exchange: NotRequired[str]
    ggroup: NotRequired[str]
    gind: NotRequired[str]
    gsector: NotRequired[str]
    gsubind: NotRequired[str]
    isin: NotRequired[str]
    lei: NotRequired[str]
    ir_url: NotRequired[str]
    naics_national_industry: NotRequired[str]
    naics: NotRequired[str]
    naics_sector: NotRequired[str]
    naics_subsector: NotRequired[str]
    name: NotRequired[str]
    phone: NotRequired[str]
    state: NotRequired[str]
    ticker: NotRequired[str]
    weburl: NotRequired[str]
    ipo: NotRequired[Date]
    market_capitalization: NotRequired[float]
    share_outstanding: NotRequired[float]
    employee_total: NotRequired[float]
    logo: NotRequired[str]
    finnhub_industry: NotRequired[str]
