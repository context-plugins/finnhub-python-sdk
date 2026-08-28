from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .ipoevent import Ipoevent, IpoeventDict


class Ipocalendar(SdkBaseModel):
    ipo_calendar: Optional[list[Ipoevent]] = Field(default=UNSET, alias="ipoCalendar")
    """Array of IPO events."""


class IpocalendarDict(TypedDict):
    ipo_calendar: NotRequired[list[Ipoevent | IpoeventDict]]
