from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class GrossIncomeEstimatesInfo(SdkBaseModel):
    gross_income_avg: Optional[float] = Field(default=UNSET, alias="grossIncomeAvg")
    """Average gross income estimates including Finnhub's proprietary estimates."""

    gross_income_high: Optional[float] = Field(default=UNSET, alias="grossIncomeHigh")
    """Highest estimate."""

    gross_income_low: Optional[float] = Field(default=UNSET, alias="grossIncomeLow")
    """Lowest estimate."""

    number_analysts: Optional[int] = Field(default=UNSET, alias="numberAnalysts")
    """Number of Analysts."""

    period: Optional[Date] = UNSET
    """Period."""

    year: Optional[int] = UNSET
    """Fiscal year."""

    quarter: Optional[int] = UNSET
    """Fiscal quarter."""


class GrossIncomeEstimatesInfoDict(TypedDict):
    gross_income_avg: NotRequired[float]
    gross_income_high: NotRequired[float]
    gross_income_low: NotRequired[float]
    number_analysts: NotRequired[int]
    period: NotRequired[Date]
    year: NotRequired[int]
    quarter: NotRequired[int]
