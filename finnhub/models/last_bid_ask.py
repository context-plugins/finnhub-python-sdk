from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LastBidAsk(SdkBaseModel):
    b: Optional[float] = UNSET
    """Bid price."""

    a: Optional[float] = UNSET
    """Ask price."""

    bv: Optional[float] = UNSET
    """Bid volume."""

    av: Optional[float] = UNSET
    """Ask volume."""

    t: Optional[int] = UNSET
    """Reference UNIX timestamp in ms."""


class LastBidAskDict(TypedDict):
    b: NotRequired[float]
    a: NotRequired[float]
    bv: NotRequired[float]
    av: NotRequired[float]
    t: NotRequired[int]
