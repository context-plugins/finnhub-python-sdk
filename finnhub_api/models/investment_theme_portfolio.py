from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InvestmentThemePortfolio(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol"""


class InvestmentThemePortfolioDict(TypedDict):
    symbol: NotRequired[str]
