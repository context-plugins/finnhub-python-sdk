from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .institutional_portfolio_info import InstitutionalPortfolioInfo, InstitutionalPortfolioInfoDict


class InstitutionalPortfolioGroup(SdkBaseModel):
    report_date: Optional[str] = Field(default=UNSET, alias="reportDate")
    """Report date."""

    filing_date: Optional[str] = Field(default=UNSET, alias="filingDate")
    """Filing date."""

    portfolio: Optional[list[InstitutionalPortfolioInfo]] = UNSET
    """Array of positions."""


class InstitutionalPortfolioGroupDict(TypedDict):
    report_date: NotRequired[str]
    filing_date: NotRequired[str]
    portfolio: NotRequired[list[InstitutionalPortfolioInfo | InstitutionalPortfolioInfoDict]]
