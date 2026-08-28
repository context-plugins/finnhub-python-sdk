from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AirlinePriceIndex(SdkBaseModel):
    date: Optional[str] = UNSET
    """Date"""

    price_index: Optional[float] = Field(default=UNSET, alias="priceIndex")
    """Price Index"""

    daily_avg_price: Optional[float] = Field(default=UNSET, alias="dailyAvgPrice")
    """Daily average ticket price."""


class AirlinePriceIndexDict(TypedDict):
    date: NotRequired[str]
    price_index: NotRequired[float]
    daily_avg_price: NotRequired[float]
