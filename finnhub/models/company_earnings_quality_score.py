from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .company_earnings_quality_score_data import CompanyEarningsQualityScoreData, CompanyEarningsQualityScoreDataDict


class CompanyEarningsQualityScore(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol"""

    freq: Optional[str] = UNSET
    """Frequency"""

    data: Optional[list[CompanyEarningsQualityScoreData]] = UNSET
    """Array of earnings quality score."""


class CompanyEarningsQualityScoreDict(TypedDict):
    symbol: NotRequired[str]
    freq: NotRequired[str]
    data: NotRequired[list[CompanyEarningsQualityScoreData | CompanyEarningsQualityScoreDataDict]]
