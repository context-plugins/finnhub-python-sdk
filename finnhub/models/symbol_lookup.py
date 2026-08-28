from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .symbol_lookup_info import SymbolLookupInfo, SymbolLookupInfoDict


class SymbolLookup(SdkBaseModel):
    result: Optional[list[SymbolLookupInfo]] = UNSET
    """Array of search results."""

    count: Optional[int] = UNSET
    """Number of results."""


class SymbolLookupDict(TypedDict):
    result: NotRequired[list[SymbolLookupInfo | SymbolLookupInfoDict]]
    count: NotRequired[int]
