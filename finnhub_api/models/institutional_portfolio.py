from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .institutional_portfolio_group import InstitutionalPortfolioGroup, InstitutionalPortfolioGroupDict


class InstitutionalPortfolio(SdkBaseModel):
    name: Optional[str] = UNSET
    """Investor's name."""

    cik: Optional[str] = UNSET
    """CIK."""

    data: Optional[list[InstitutionalPortfolioGroup]] = UNSET
    """Array of positions."""


class InstitutionalPortfolioDict(TypedDict):
    name: NotRequired[str]
    cik: NotRequired[str]
    data: NotRequired[list[InstitutionalPortfolioGroup | InstitutionalPortfolioGroupDict]]
