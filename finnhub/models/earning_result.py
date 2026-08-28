from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class EarningResult(SdkBaseModel):
    actual: Optional[float] = UNSET
    """Actual earning result."""

    estimate: Optional[float] = UNSET
    """Estimated earning."""

    surprise: Optional[float] = UNSET
    """Surprise - The difference between actual and estimate."""

    surprise_percent: Optional[float] = Field(default=UNSET, alias="surprisePercent")
    """Surprise percent."""

    period: Optional[Date] = UNSET
    """Reported period."""

    symbol: Optional[str] = UNSET
    """Company symbol."""

    year: Optional[int] = UNSET
    """Fiscal year."""

    quarter: Optional[int] = UNSET
    """Fiscal quarter."""


class EarningResultDict(TypedDict):
    actual: NotRequired[float]
    estimate: NotRequired[float]
    surprise: NotRequired[float]
    surprise_percent: NotRequired[float]
    period: NotRequired[Date]
    symbol: NotRequired[str]
    year: NotRequired[int]
    quarter: NotRequired[int]
