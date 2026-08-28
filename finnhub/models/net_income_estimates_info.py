from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class NetIncomeEstimatesInfo(SdkBaseModel):
    net_income_avg: Optional[float] = Field(default=UNSET, alias="netIncomeAvg")
    """Average net income estimates including Finnhub's proprietary estimates."""

    net_income_high: Optional[float] = Field(default=UNSET, alias="netIncomeHigh")
    """Highest estimate."""

    net_income_low: Optional[float] = Field(default=UNSET, alias="netIncomeLow")
    """Lowest estimate."""

    number_analysts: Optional[int] = Field(default=UNSET, alias="numberAnalysts")
    """Number of Analysts."""

    period: Optional[Date] = UNSET
    """Period."""

    year: Optional[int] = UNSET
    """Fiscal year."""

    quarter: Optional[int] = UNSET
    """Fiscal quarter."""


class NetIncomeEstimatesInfoDict(TypedDict):
    net_income_avg: NotRequired[float]
    net_income_high: NotRequired[float]
    net_income_low: NotRequired[float]
    number_analysts: NotRequired[int]
    period: NotRequired[Date]
    year: NotRequired[int]
    quarter: NotRequired[int]
