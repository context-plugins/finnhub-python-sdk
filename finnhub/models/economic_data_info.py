from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EconomicDataInfo(SdkBaseModel):
    date: Optional[str] = UNSET
    """Date of the reading"""

    value: Optional[float] = UNSET
    """Value"""


class EconomicDataInfoDict(TypedDict):
    date: NotRequired[str]
    value: NotRequired[float]
