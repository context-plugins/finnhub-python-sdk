from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .earnings_call_live_result import EarningsCallLiveResult, EarningsCallLiveResultDict


class EarningsCallLive(SdkBaseModel):
    event: Optional[list[EarningsCallLiveResult]] = UNSET
    """Array of earnings call events that support live streaming."""


class EarningsCallLiveDict(TypedDict):
    event: NotRequired[list[EarningsCallLiveResult | EarningsCallLiveResultDict]]
