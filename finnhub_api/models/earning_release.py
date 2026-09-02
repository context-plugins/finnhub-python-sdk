from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class EarningRelease(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol."""

    date: Optional[Date] = UNSET
    """Date."""

    hour: Optional[str] = UNSET
    """Indicates whether the earnings is announced before market open(<code>bmo</code>), after market
    close(<code>amc</code>), or during market hour(<code>dmh</code>)."""

    year: Optional[int] = UNSET
    """Earnings year."""

    quarter: Optional[int] = UNSET
    """Earnings quarter."""

    eps_estimate: Optional[float] = Field(default=UNSET, alias="epsEstimate")
    """EPS estimate."""

    eps_actual: Optional[float] = Field(default=UNSET, alias="epsActual")
    """EPS actual."""

    revenue_estimate: Optional[float] = Field(default=UNSET, alias="revenueEstimate")
    """Revenue estimate including Finnhub's proprietary estimates."""

    revenue_actual: Optional[float] = Field(default=UNSET, alias="revenueActual")
    """Revenue actual."""


class EarningReleaseDict(TypedDict):
    symbol: NotRequired[str]
    date: NotRequired[Date]
    hour: NotRequired[str]
    year: NotRequired[int]
    quarter: NotRequired[int]
    eps_estimate: NotRequired[float]
    eps_actual: NotRequired[float]
    revenue_estimate: NotRequired[float]
    revenue_actual: NotRequired[float]
