from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CompanyEarningsQualityScoreData(SdkBaseModel):
    period: Optional[str] = UNSET
    """Period"""

    growth: Optional[float] = UNSET
    """Growth Score"""

    profitability: Optional[float] = UNSET
    """Profitability Score"""

    cash_generation_capital_allocation: Optional[float] = Field(default=UNSET, alias="cashGenerationCapitalAllocation")
    """Cash Generation and Capital Allocation"""

    leverage: Optional[float] = UNSET
    """Leverage Score"""

    score: Optional[float] = UNSET
    """Total Score"""

    letter_score: Optional[str] = Field(default=UNSET, alias="letterScore")
    """Letter Score"""


class CompanyEarningsQualityScoreDataDict(TypedDict):
    period: NotRequired[str]
    growth: NotRequired[float]
    profitability: NotRequired[float]
    cash_generation_capital_allocation: NotRequired[float]
    leverage: NotRequired[float]
    score: NotRequired[float]
    letter_score: NotRequired[str]
