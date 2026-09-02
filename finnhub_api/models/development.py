from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Development(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Company symbol."""

    datetime: Optional[str] = UNSET
    """Published time in <code>YYYY-MM-DD HH:MM:SS</code> format."""

    headline: Optional[str] = UNSET
    """Development headline."""

    description: Optional[str] = UNSET
    """Development description."""

    url: Optional[str] = UNSET
    """URL."""


class DevelopmentDict(TypedDict):
    symbol: NotRequired[str]
    datetime: NotRequired[str]
    headline: NotRequired[str]
    description: NotRequired[str]
    url: NotRequired[str]
