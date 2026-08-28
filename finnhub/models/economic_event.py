from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EconomicEvent(SdkBaseModel):
    actual: Optional[float] = UNSET
    """Actual release"""

    prev: Optional[float] = UNSET
    """Previous release"""

    country: Optional[str] = UNSET
    """Country"""

    unit: Optional[str] = UNSET
    """Unit"""

    estimate: Optional[float] = UNSET
    """Estimate"""

    event: Optional[str] = UNSET
    """Event"""

    impact: Optional[str] = UNSET
    """Impact level"""

    time: Optional[str] = UNSET
    """Release time"""


class EconomicEventDict(TypedDict):
    actual: NotRequired[float]
    prev: NotRequired[float]
    country: NotRequired[str]
    unit: NotRequired[str]
    estimate: NotRequired[float]
    event: NotRequired[str]
    impact: NotRequired[str]
    time: NotRequired[str]
