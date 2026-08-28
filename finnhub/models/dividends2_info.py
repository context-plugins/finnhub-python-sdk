from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class Dividends2Info(SdkBaseModel):
    ex_date: Optional[Date] = Field(default=UNSET, alias="exDate")
    """Ex-Dividend date."""

    amount: Optional[float] = UNSET
    """Amount in local currency."""


class Dividends2InfoDict(TypedDict):
    ex_date: NotRequired[Date]
    amount: NotRequired[float]
