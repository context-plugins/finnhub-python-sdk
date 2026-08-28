from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .earning_release import EarningRelease, EarningReleaseDict


class EarningsCalendar(SdkBaseModel):
    earnings_calendar: Optional[list[EarningRelease]] = Field(default=UNSET, alias="earningsCalendar")
    """Array of earnings release."""


class EarningsCalendarDict(TypedDict):
    earnings_calendar: NotRequired[list[EarningRelease | EarningReleaseDict]]
