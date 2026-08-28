from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CovidInfo(SdkBaseModel):
    state: Optional[str] = UNSET
    """State."""

    case: Optional[float] = UNSET
    """Number of confirmed cases."""

    death: Optional[float] = UNSET
    """Number of confirmed deaths."""

    updated: Optional[str] = UNSET
    """Updated time."""


class CovidInfoDict(TypedDict):
    state: NotRequired[str]
    case: NotRequired[float]
    death: NotRequired[float]
    updated: NotRequired[str]
