from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class FcfEstimatesInfo(SdkBaseModel):
    fcf_avg: Optional[float] = Field(default=UNSET, alias="fcfAvg")
    """Average FCF estimates including Finnhub's proprietary estimates."""

    fcf_high: Optional[float] = Field(default=UNSET, alias="fcfHigh")
    """Highest estimate."""

    fcf_low: Optional[float] = Field(default=UNSET, alias="fcfLow")
    """Lowest estimate."""

    number_analysts: Optional[int] = Field(default=UNSET, alias="numberAnalysts")
    """Number of Analysts."""

    period: Optional[Date] = UNSET
    """Period."""

    year: Optional[int] = UNSET
    """Fiscal year."""

    quarter: Optional[int] = UNSET
    """Fiscal quarter."""


class FcfEstimatesInfoDict(TypedDict):
    fcf_avg: NotRequired[float]
    fcf_high: NotRequired[float]
    fcf_low: NotRequired[float]
    number_analysts: NotRequired[int]
    period: NotRequired[Date]
    year: NotRequired[int]
    quarter: NotRequired[int]
