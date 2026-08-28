from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BasicFinancials(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol of the company."""

    metric_type: Optional[str] = Field(default=UNSET, alias="metricType")
    """Metric type."""

    series: Optional[Any] = UNSET
    metric: Optional[Any] = UNSET


class BasicFinancialsDict(TypedDict):
    symbol: NotRequired[str]
    metric_type: NotRequired[str]
    series: NotRequired[Any]
    metric: NotRequired[Any]
