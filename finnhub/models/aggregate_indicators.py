from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .technical_analysis import TechnicalAnalysis, TechnicalAnalysisDict
from .trend import Trend, TrendDict


class AggregateIndicators(SdkBaseModel):
    technical_analysis: Optional[TechnicalAnalysis] = Field(default=UNSET, alias="technicalAnalysis")
    trend: Optional[Trend] = UNSET


class AggregateIndicatorsDict(TypedDict):
    technical_analysis: NotRequired[TechnicalAnalysis | TechnicalAnalysisDict]
    trend: NotRequired[Trend | TrendDict]
