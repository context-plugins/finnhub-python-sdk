from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class DpsEstimatesInfo(SdkBaseModel):
    dps_avg: Optional[float] = Field(default=UNSET, alias="dpsAvg")
    """Average DPS estimates including Finnhub's proprietary estimates."""

    dps_high: Optional[float] = Field(default=UNSET, alias="dpsHigh")
    """Highest estimate."""

    dps_low: Optional[float] = Field(default=UNSET, alias="dpsLow")
    """Lowest estimate."""

    number_analysts: Optional[int] = Field(default=UNSET, alias="numberAnalysts")
    """Number of Analysts."""

    period: Optional[Date] = UNSET
    """Period."""

    year: Optional[int] = UNSET
    """Fiscal year."""

    quarter: Optional[int] = UNSET
    """Fiscal quarter."""


class DpsEstimatesInfoDict(TypedDict):
    dps_avg: NotRequired[float]
    dps_high: NotRequired[float]
    dps_low: NotRequired[float]
    number_analysts: NotRequired[int]
    period: NotRequired[Date]
    year: NotRequired[int]
    quarter: NotRequired[int]
