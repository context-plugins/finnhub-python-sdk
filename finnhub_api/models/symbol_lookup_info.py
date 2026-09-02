from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SymbolLookupInfo(SdkBaseModel):
    description: Optional[str] = UNSET
    """Symbol description"""

    display_symbol: Optional[str] = Field(default=UNSET, alias="displaySymbol")
    """Display symbol name."""

    symbol: Optional[str] = UNSET
    """Unique symbol used to identify this symbol used in <code>/stock/candle</code> endpoint."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Security type."""


class SymbolLookupInfoDict(TypedDict):
    description: NotRequired[str]
    display_symbol: NotRequired[str]
    symbol: NotRequired[str]
    type_: NotRequired[str]
