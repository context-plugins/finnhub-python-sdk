from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .company_news_statistics import CompanyNewsStatistics, CompanyNewsStatisticsDict
from .sentiment import Sentiment, SentimentDict


class NewsSentiment(SdkBaseModel):
    buzz: Optional[CompanyNewsStatistics] = UNSET
    company_news_score: Optional[float] = Field(default=UNSET, alias="companyNewsScore")
    """News score."""

    sector_average_bullish_percent: Optional[float] = Field(default=UNSET, alias="sectorAverageBullishPercent")
    """Sector average bullish percent."""

    sector_average_news_score: Optional[float] = Field(default=UNSET, alias="sectorAverageNewsScore")
    """Sectore average score."""

    sentiment: Optional[Sentiment] = UNSET
    symbol: Optional[str] = UNSET
    """Requested symbol."""


class NewsSentimentDict(TypedDict):
    buzz: NotRequired[CompanyNewsStatistics | CompanyNewsStatisticsDict]
    company_news_score: NotRequired[float]
    sector_average_bullish_percent: NotRequired[float]
    sector_average_news_score: NotRequired[float]
    sentiment: NotRequired[Sentiment | SentimentDict]
    symbol: NotRequired[str]
