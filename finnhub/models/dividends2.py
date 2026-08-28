from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dividends2_info import Dividends2Info, Dividends2InfoDict


class Dividends2(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol"""

    data: Optional[list[Dividends2Info]] = UNSET


class Dividends2Dict(TypedDict):
    symbol: NotRequired[str]
    data: NotRequired[list[Dividends2Info | Dividends2InfoDict]]
