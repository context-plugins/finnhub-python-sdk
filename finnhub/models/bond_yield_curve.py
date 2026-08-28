from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bond_yield_curve_info import BondYieldCurveInfo, BondYieldCurveInfoDict


class BondYieldCurve(SdkBaseModel):
    data: Optional[list[BondYieldCurveInfo]] = UNSET
    """Array of data."""

    code: Optional[str] = UNSET
    """Bond's code"""


class BondYieldCurveDict(TypedDict):
    data: NotRequired[list[BondYieldCurveInfo | BondYieldCurveInfoDict]]
    code: NotRequired[str]
