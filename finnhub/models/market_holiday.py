from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .market_holiday_data import MarketHolidayData, MarketHolidayDataDict


class MarketHoliday(SdkBaseModel):
    timezone: Optional[str] = UNSET
    """Timezone."""

    exchange: Optional[str] = UNSET
    """Exchange."""

    data: Optional[list[MarketHolidayData]] = UNSET
    """Array of holidays."""


class MarketHolidayDict(TypedDict):
    timezone: NotRequired[str]
    exchange: NotRequired[str]
    data: NotRequired[list[MarketHolidayData | MarketHolidayDataDict]]
