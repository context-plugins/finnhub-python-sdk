from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class PretaxIncomeEstimatesInfo(SdkBaseModel):
    pretax_income_avg: Optional[float] = Field(default=UNSET, alias="pretaxIncomeAvg")
    """Average pretax income estimates including Finnhub's proprietary estimates."""

    pretax_income_high: Optional[float] = Field(default=UNSET, alias="pretaxIncomeHigh")
    """Highest estimate."""

    pretax_income_low: Optional[float] = Field(default=UNSET, alias="pretaxIncomeLow")
    """Lowest estimate."""

    number_analysts: Optional[int] = Field(default=UNSET, alias="numberAnalysts")
    """Number of Analysts."""

    period: Optional[Date] = UNSET
    """Period."""

    year: Optional[int] = UNSET
    """Fiscal year."""

    quarter: Optional[int] = UNSET
    """Fiscal quarter."""


class PretaxIncomeEstimatesInfoDict(TypedDict):
    pretax_income_avg: NotRequired[float]
    pretax_income_high: NotRequired[float]
    pretax_income_low: NotRequired[float]
    number_analysts: NotRequired[int]
    period: NotRequired[Date]
    year: NotRequired[int]
    quarter: NotRequired[int]
