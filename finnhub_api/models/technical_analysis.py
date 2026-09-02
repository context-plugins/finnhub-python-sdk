from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .indicator import Indicator, IndicatorDict


class TechnicalAnalysis(SdkBaseModel):
    count: Optional[Indicator] = UNSET
    signal: Optional[str] = UNSET
    """Aggregate Signal"""


class TechnicalAnalysisDict(TypedDict):
    count: NotRequired[Indicator | IndicatorDict]
    signal: NotRequired[str]
