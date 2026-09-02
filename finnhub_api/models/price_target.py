from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PriceTarget(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Company symbol."""

    target_high: Optional[float] = Field(default=UNSET, alias="targetHigh")
    """Highes analysts' target."""

    target_low: Optional[float] = Field(default=UNSET, alias="targetLow")
    """Lowest analysts' target."""

    target_mean: Optional[float] = Field(default=UNSET, alias="targetMean")
    """Mean of all analysts' targets."""

    target_median: Optional[float] = Field(default=UNSET, alias="targetMedian")
    """Median of all analysts' targets."""

    number_analysts: Optional[int] = Field(default=UNSET, alias="numberAnalysts")
    """Number of Analysts."""

    last_updated: Optional[str] = Field(default=UNSET, alias="lastUpdated")
    """Updated time of the data"""


class PriceTargetDict(TypedDict):
    symbol: NotRequired[str]
    target_high: NotRequired[float]
    target_low: NotRequired[float]
    target_mean: NotRequired[float]
    target_median: NotRequired[float]
    number_analysts: NotRequired[int]
    last_updated: NotRequired[str]
