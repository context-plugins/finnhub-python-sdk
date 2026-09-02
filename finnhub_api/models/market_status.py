from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MarketStatus(SdkBaseModel):
    exchange: Optional[str] = UNSET
    """Exchange."""

    timezone: Optional[str] = UNSET
    """Timezone."""

    session: Optional[str] = UNSET
    """Market session. Can be 1 of the following values:
    <code>pre-market</code>,<code>regular</code>,<code>post-market</code> or <code>null</code> if the market is
    closed."""

    holiday: Optional[str] = UNSET
    """Holiday event."""

    is_open: Optional[bool] = Field(default=UNSET, alias="isOpen")
    """Whether the market is open at the moment."""

    t: Optional[int] = UNSET
    """Current timestamp."""


class MarketStatusDict(TypedDict):
    exchange: NotRequired[str]
    timezone: NotRequired[str]
    session: NotRequired[str]
    holiday: NotRequired[str]
    is_open: NotRequired[bool]
    t: NotRequired[int]
