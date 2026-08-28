from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FdacomitteeMeeting(SdkBaseModel):
    from_date: Optional[str] = Field(default=UNSET, alias="fromDate")
    """Start time of the event in EST."""

    to_date: Optional[str] = Field(default=UNSET, alias="toDate")
    """End time of the event in EST."""

    event_description: Optional[str] = Field(default=UNSET, alias="eventDescription")
    """Event's description."""

    url: Optional[str] = UNSET
    """URL."""


class FdacomitteeMeetingDict(TypedDict):
    from_date: NotRequired[str]
    to_date: NotRequired[str]
    event_description: NotRequired[str]
    url: NotRequired[str]
