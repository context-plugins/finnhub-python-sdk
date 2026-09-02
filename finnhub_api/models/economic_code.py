from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EconomicCode(SdkBaseModel):
    code: Optional[str] = UNSET
    """Finnhub economic code used to get historical data"""

    country: Optional[str] = UNSET
    """Country"""

    name: Optional[str] = UNSET
    """Indicator name"""

    unit: Optional[str] = UNSET
    """Unit"""


class EconomicCodeDict(TypedDict):
    code: NotRequired[str]
    country: NotRequired[str]
    name: NotRequired[str]
    unit: NotRequired[str]
