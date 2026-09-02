from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PriceMetrics(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol of the company."""

    at_date: Optional[str] = Field(default=UNSET, alias="atDate")
    """Data date."""

    data: Optional[Any] = UNSET


class PriceMetricsDict(TypedDict):
    symbol: NotRequired[str]
    at_date: NotRequired[str]
    data: NotRequired[Any]
