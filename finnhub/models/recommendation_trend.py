from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RecommendationTrend(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Company symbol."""

    buy: Optional[int] = UNSET
    """Number of recommendations that fall into the Buy category"""

    hold: Optional[int] = UNSET
    """Number of recommendations that fall into the Hold category"""

    period: Optional[str] = UNSET
    """Updated period"""

    sell: Optional[int] = UNSET
    """Number of recommendations that fall into the Sell category"""

    strong_buy: Optional[int] = Field(default=UNSET, alias="strongBuy")
    """Number of recommendations that fall into the Strong Buy category"""

    strong_sell: Optional[int] = Field(default=UNSET, alias="strongSell")
    """Number of recommendations that fall into the Strong Sell category"""


class RecommendationTrendDict(TypedDict):
    symbol: NotRequired[str]
    buy: NotRequired[int]
    hold: NotRequired[int]
    period: NotRequired[str]
    sell: NotRequired[int]
    strong_buy: NotRequired[int]
    strong_sell: NotRequired[int]
