from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .employee_count import EmployeeCount, EmployeeCountDict


class HistoricalEmployeeCount(SdkBaseModel):
    data: Optional[list[EmployeeCount]] = UNSET
    """Array of market data."""

    symbol: Optional[str] = UNSET
    """Symbol"""


class HistoricalEmployeeCountDict(TypedDict):
    data: NotRequired[list[EmployeeCount | EmployeeCountDict]]
    symbol: NotRequired[str]
