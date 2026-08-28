from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .economic_event import EconomicEvent, EconomicEventDict


class EconomicCalendar(SdkBaseModel):
    economic_calendar: Optional[list[EconomicEvent]] = Field(default=UNSET, alias="economicCalendar")
    """Array of economic events."""


class EconomicCalendarDict(TypedDict):
    economic_calendar: NotRequired[list[EconomicEvent | EconomicEventDict]]
