from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class EbitEstimatesInfo(SdkBaseModel):
    ebit_avg: Optional[float] = Field(default=UNSET, alias="ebitAvg")
    """Average EBIT estimates including Finnhub's proprietary estimates."""

    ebit_high: Optional[float] = Field(default=UNSET, alias="ebitHigh")
    """Highest estimate."""

    ebit_low: Optional[float] = Field(default=UNSET, alias="ebitLow")
    """Lowest estimate."""

    number_analysts: Optional[int] = Field(default=UNSET, alias="numberAnalysts")
    """Number of Analysts."""

    period: Optional[Date] = UNSET
    """Period."""

    year: Optional[int] = UNSET
    """Fiscal year."""

    quarter: Optional[int] = UNSET
    """Fiscal quarter."""


class EbitEstimatesInfoDict(TypedDict):
    ebit_avg: NotRequired[float]
    ebit_high: NotRequired[float]
    ebit_low: NotRequired[float]
    number_analysts: NotRequired[int]
    period: NotRequired[Date]
    year: NotRequired[int]
    quarter: NotRequired[int]
