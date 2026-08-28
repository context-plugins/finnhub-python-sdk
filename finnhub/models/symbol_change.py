from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .symbol_change_info import SymbolChangeInfo, SymbolChangeInfoDict


class SymbolChange(SdkBaseModel):
    from_date: Optional[str] = Field(default=UNSET, alias="fromDate")
    """From date."""

    to_date: Optional[str] = Field(default=UNSET, alias="toDate")
    """To date."""

    data: Optional[list[SymbolChangeInfo]] = UNSET
    """Array of symbol change events."""


class SymbolChangeDict(TypedDict):
    from_date: NotRequired[str]
    to_date: NotRequired[str]
    data: NotRequired[list[SymbolChangeInfo | SymbolChangeInfoDict]]
