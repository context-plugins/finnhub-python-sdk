from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class EtfprofileData(SdkBaseModel):
    name: Optional[str] = UNSET
    """Name"""

    asset_class: Optional[str] = Field(default=UNSET, alias="assetClass")
    """Asset Class."""

    investment_segment: Optional[str] = Field(default=UNSET, alias="investmentSegment")
    """Investment Segment."""

    aum: Optional[float] = UNSET
    """AUM."""

    nav: Optional[float] = UNSET
    """NAV."""

    nav_currency: Optional[str] = Field(default=UNSET, alias="navCurrency")
    """NAV currency."""

    expense_ratio: Optional[float] = Field(default=UNSET, alias="expenseRatio")
    """Expense ratio. For non-US funds, this is the <a
    href="https://www.esma.europa.eu/sites/default/files/library/2015/11/09_1028_final_kid_ongoing_charges_methodology_for_publication_u_2_.pdf"
    target="_blank">KID ongoing charges<a/>."""

    tracking_index: Optional[str] = Field(default=UNSET, alias="trackingIndex")
    """Tracking Index."""

    etf_company: Optional[str] = Field(default=UNSET, alias="etfCompany")
    """ETF issuer."""

    domicile: Optional[str] = UNSET
    """ETF domicile."""

    inception_date: Optional[Date] = Field(default=UNSET, alias="inceptionDate")
    """Inception date."""

    website: Optional[str] = UNSET
    """ETF's website."""

    logo: Optional[str] = UNSET
    """Logo."""

    isin: Optional[str] = UNSET
    """ISIN."""

    cusip: Optional[str] = UNSET
    """CUSIP."""

    price_to_earnings: Optional[float] = Field(default=UNSET, alias="priceToEarnings")
    """P/E."""

    price_to_book: Optional[float] = Field(default=UNSET, alias="priceToBook")
    """P/B."""

    avg_volume: Optional[float] = Field(default=UNSET, alias="avgVolume")
    """30-day average volume."""

    description: Optional[str] = UNSET
    """ETF's description."""

    is_inverse: Optional[bool] = Field(default=UNSET, alias="isInverse")
    """Whether the ETF is inverse"""

    is_leveraged: Optional[bool] = Field(default=UNSET, alias="isLeveraged")
    """Whether the ETF is leveraged"""

    leverage_factor: Optional[float] = Field(default=UNSET, alias="leverageFactor")
    """Leverage factor."""

    dividend_yield: Optional[float] = Field(default=UNSET, alias="dividendYield")
    """Dividend yield."""


class EtfprofileDataDict(TypedDict):
    name: NotRequired[str]
    asset_class: NotRequired[str]
    investment_segment: NotRequired[str]
    aum: NotRequired[float]
    nav: NotRequired[float]
    nav_currency: NotRequired[str]
    expense_ratio: NotRequired[float]
    tracking_index: NotRequired[str]
    etf_company: NotRequired[str]
    domicile: NotRequired[str]
    inception_date: NotRequired[Date]
    website: NotRequired[str]
    logo: NotRequired[str]
    isin: NotRequired[str]
    cusip: NotRequired[str]
    price_to_earnings: NotRequired[float]
    price_to_book: NotRequired[float]
    avg_volume: NotRequired[float]
    description: NotRequired[str]
    is_inverse: NotRequired[bool]
    is_leveraged: NotRequired[bool]
    leverage_factor: NotRequired[float]
    dividend_yield: NotRequired[float]
