from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class EarningsEstimatesInfo(SdkBaseModel):
    eps_avg: Optional[float] = Field(default=UNSET, alias="epsAvg")
    """Average EPS estimates including Finnhub's proprietary estimates."""

    eps_high: Optional[float] = Field(default=UNSET, alias="epsHigh")
    """Highest estimate."""

    eps_low: Optional[float] = Field(default=UNSET, alias="epsLow")
    """Lowest estimate."""

    number_analysts: Optional[int] = Field(default=UNSET, alias="numberAnalysts")
    """Number of Analysts."""

    period: Optional[Date] = UNSET
    """Period."""

    year: Optional[int] = UNSET
    """Fiscal year."""

    quarter: Optional[int] = UNSET
    """Fiscal quarter."""


class EarningsEstimatesInfoDict(TypedDict):
    eps_avg: NotRequired[float]
    eps_high: NotRequired[float]
    eps_low: NotRequired[float]
    number_analysts: NotRequired[int]
    period: NotRequired[Date]
    year: NotRequired[int]
    quarter: NotRequired[int]
