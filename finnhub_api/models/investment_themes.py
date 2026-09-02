from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .investment_theme_portfolio import InvestmentThemePortfolio, InvestmentThemePortfolioDict


class InvestmentThemes(SdkBaseModel):
    theme: Optional[str] = UNSET
    """Investment theme"""

    data: Optional[list[InvestmentThemePortfolio]] = UNSET
    """Investment theme portfolio."""


class InvestmentThemesDict(TypedDict):
    theme: NotRequired[str]
    data: NotRequired[list[InvestmentThemePortfolio | InvestmentThemePortfolioDict]]
