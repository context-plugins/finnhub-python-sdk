from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Trend(SdkBaseModel):
    adx: Optional[float] = UNSET
    """ADX reading"""

    trending: Optional[bool] = UNSET
    """Whether market is trending or going sideway"""


class TrendDict(TypedDict):
    adx: NotRequired[float]
    trending: NotRequired[bool]
