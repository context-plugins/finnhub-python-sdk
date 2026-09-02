from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .economic_data_info import EconomicDataInfo, EconomicDataInfoDict


class EconomicData(SdkBaseModel):
    data: Optional[list[EconomicDataInfo]] = UNSET
    """Array of economic data for requested code."""

    code: Optional[str] = UNSET
    """Finnhub economic code"""


class EconomicDataDict(TypedDict):
    data: NotRequired[list[EconomicDataInfo | EconomicDataInfoDict]]
    code: NotRequired[str]
