from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class CapexEstimatesInfo(SdkBaseModel):
    capex_avg: Optional[float] = Field(default=UNSET, alias="capexAvg")
    """Average capex estimates including Finnhub's proprietary estimates."""

    capex_high: Optional[float] = Field(default=UNSET, alias="capexHigh")
    """Highest estimate."""

    capex_low: Optional[float] = Field(default=UNSET, alias="capexLow")
    """Lowest estimate."""

    number_analysts: Optional[int] = Field(default=UNSET, alias="numberAnalysts")
    """Number of Analysts."""

    period: Optional[Date] = UNSET
    """Period."""

    year: Optional[int] = UNSET
    """Fiscal year."""

    quarter: Optional[int] = UNSET
    """Fiscal quarter."""


class CapexEstimatesInfoDict(TypedDict):
    capex_avg: NotRequired[float]
    capex_high: NotRequired[float]
    capex_low: NotRequired[float]
    number_analysts: NotRequired[int]
    period: NotRequired[Date]
    year: NotRequired[int]
    quarter: NotRequired[int]
