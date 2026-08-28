from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .etfallocation_data import EtfallocationData, EtfallocationDataDict


class EtfsAllocation(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """ETF symbol."""

    data: Optional[EtfallocationData] = UNSET


class EtfsAllocationDict(TypedDict):
    symbol: NotRequired[str]
    data: NotRequired[EtfallocationData | EtfallocationDataDict]
