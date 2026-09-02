from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BondYieldCurveInfo(SdkBaseModel):
    d: Optional[str] = UNSET
    """Date of the reading"""

    v: Optional[float] = UNSET
    """Value"""


class BondYieldCurveInfoDict(TypedDict):
    d: NotRequired[str]
    v: NotRequired[float]
