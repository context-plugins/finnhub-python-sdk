from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CompanyNewsStatistics(SdkBaseModel):
    articles_in_last_week: Optional[int] = Field(default=UNSET, alias="articlesInLastWeek")
    buzz: Optional[float] = UNSET
    weekly_average: Optional[float] = Field(default=UNSET, alias="weeklyAverage")


class CompanyNewsStatisticsDict(TypedDict):
    articles_in_last_week: NotRequired[int]
    buzz: NotRequired[float]
    weekly_average: NotRequired[float]
