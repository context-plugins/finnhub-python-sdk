from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class CompanyProfile2(SdkBaseModel):
    country: Optional[str] = UNSET
    """Country of company's headquarter."""

    currency: Optional[str] = UNSET
    """Currency used in company filings."""

    exchange: Optional[str] = UNSET
    """Listed exchange."""

    name: Optional[str] = UNSET
    """Company name."""

    ticker: Optional[str] = UNSET
    """Company symbol/ticker as used on the listed exchange."""

    ipo: Optional[Date] = UNSET
    """IPO date."""

    market_capitalization: Optional[float] = Field(default=UNSET, alias="marketCapitalization")
    """Market Capitalization."""

    share_outstanding: Optional[float] = Field(default=UNSET, alias="shareOutstanding")
    """Number of oustanding shares."""

    logo: Optional[str] = UNSET
    """Logo image."""

    phone: Optional[str] = UNSET
    """Company phone number."""

    weburl: Optional[str] = UNSET
    """Company website."""

    finnhub_industry: Optional[str] = Field(default=UNSET, alias="finnhubIndustry")
    """Finnhub industry classification."""


class CompanyProfile2Dict(TypedDict):
    country: NotRequired[str]
    currency: NotRequired[str]
    exchange: NotRequired[str]
    name: NotRequired[str]
    ticker: NotRequired[str]
    ipo: NotRequired[Date]
    market_capitalization: NotRequired[float]
    share_outstanding: NotRequired[float]
    logo: NotRequired[str]
    phone: NotRequired[str]
    weburl: NotRequired[str]
    finnhub_industry: NotRequired[str]
