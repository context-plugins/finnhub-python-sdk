from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SupportResistance(SdkBaseModel):
    levels: Optional[list[float]] = UNSET
    """Array of support and resistance levels."""


class SupportResistanceDict(TypedDict):
    levels: NotRequired[list[float]]
