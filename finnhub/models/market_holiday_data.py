from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MarketHolidayData(SdkBaseModel):
    event_name: Optional[str] = Field(default=UNSET, alias="eventName")
    """Holiday's name."""

    at_date: Optional[str] = Field(default=UNSET, alias="atDate")
    """Date."""

    trading_hour: Optional[str] = Field(default=UNSET, alias="tradingHour")
    """Trading hours for this day if the market is partially closed only."""


class MarketHolidayDataDict(TypedDict):
    event_name: NotRequired[str]
    at_date: NotRequired[str]
    trading_hour: NotRequired[str]
