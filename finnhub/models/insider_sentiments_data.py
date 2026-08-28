from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InsiderSentimentsData(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol."""

    year: Optional[int] = UNSET
    """Year."""

    month: Optional[int] = UNSET
    """Month."""

    change: Optional[int] = UNSET
    """Net buying/selling from all insiders' transactions."""

    mspr: Optional[float] = UNSET
    """Monthly share purchase ratio."""


class InsiderSentimentsDataDict(TypedDict):
    symbol: NotRequired[str]
    year: NotRequired[int]
    month: NotRequired[int]
    change: NotRequired[int]
    mspr: NotRequired[float]
