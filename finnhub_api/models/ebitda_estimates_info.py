from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class EbitdaEstimatesInfo(SdkBaseModel):
    ebitda_avg: Optional[float] = Field(default=UNSET, alias="ebitdaAvg")
    """Average EBITDA estimates including Finnhub's proprietary estimates."""

    ebitda_high: Optional[float] = Field(default=UNSET, alias="ebitdaHigh")
    """Highest estimate."""

    ebitda_low: Optional[float] = Field(default=UNSET, alias="ebitdaLow")
    """Lowest estimate."""

    number_analysts: Optional[int] = Field(default=UNSET, alias="numberAnalysts")
    """Number of Analysts."""

    period: Optional[Date] = UNSET
    """Period."""

    year: Optional[int] = UNSET
    """Fiscal year."""

    quarter: Optional[int] = UNSET
    """Fiscal quarter."""


class EbitdaEstimatesInfoDict(TypedDict):
    ebitda_avg: NotRequired[float]
    ebitda_high: NotRequired[float]
    ebitda_low: NotRequired[float]
    number_analysts: NotRequired[int]
    period: NotRequired[Date]
    year: NotRequired[int]
    quarter: NotRequired[int]
