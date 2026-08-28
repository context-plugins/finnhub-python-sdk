from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class RevenueEstimatesInfo(SdkBaseModel):
    revenue_avg: Optional[float] = Field(default=UNSET, alias="revenueAvg")
    """Average revenue estimates including Finnhub's proprietary estimates."""

    revenue_high: Optional[float] = Field(default=UNSET, alias="revenueHigh")
    """Highest estimate."""

    revenue_low: Optional[float] = Field(default=UNSET, alias="revenueLow")
    """Lowest estimate."""

    number_analysts: Optional[int] = Field(default=UNSET, alias="numberAnalysts")
    """Number of Analysts."""

    period: Optional[Date] = UNSET
    """Period."""

    year: Optional[int] = UNSET
    """Fiscal year."""

    quarter: Optional[int] = UNSET
    """Fiscal quarter."""


class RevenueEstimatesInfoDict(TypedDict):
    revenue_avg: NotRequired[float]
    revenue_high: NotRequired[float]
    revenue_low: NotRequired[float]
    number_analysts: NotRequired[int]
    period: NotRequired[Date]
    year: NotRequired[int]
    quarter: NotRequired[int]
