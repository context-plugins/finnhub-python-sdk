from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Indicator(SdkBaseModel):
    buy: Optional[int] = UNSET
    """Number of buy signals"""

    neutral: Optional[int] = UNSET
    """Number of neutral signals"""

    sell: Optional[int] = UNSET
    """Number of sell signals"""


class IndicatorDict(TypedDict):
    buy: NotRequired[int]
    neutral: NotRequired[int]
    sell: NotRequired[int]
