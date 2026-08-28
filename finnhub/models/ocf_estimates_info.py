from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class OcfEstimatesInfo(SdkBaseModel):
    ocf_avg: Optional[float] = Field(default=UNSET, alias="ocfAvg")
    """Average OCF estimates including Finnhub's proprietary estimates."""

    ocf_high: Optional[float] = Field(default=UNSET, alias="ocfHigh")
    """Highest estimate."""

    ocf_low: Optional[float] = Field(default=UNSET, alias="ocfLow")
    """Lowest estimate."""

    number_analysts: Optional[int] = Field(default=UNSET, alias="numberAnalysts")
    """Number of Analysts."""

    period: Optional[Date] = UNSET
    """Period."""

    year: Optional[int] = UNSET
    """Fiscal year."""

    quarter: Optional[int] = UNSET
    """Fiscal quarter."""


class OcfEstimatesInfoDict(TypedDict):
    ocf_avg: NotRequired[float]
    ocf_high: NotRequired[float]
    ocf_low: NotRequired[float]
    number_analysts: NotRequired[int]
    period: NotRequired[Date]
    year: NotRequired[int]
    quarter: NotRequired[int]
