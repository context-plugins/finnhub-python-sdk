from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CryptoSymbol(SdkBaseModel):
    description: Optional[str] = UNSET
    """Symbol description"""

    display_symbol: Optional[str] = Field(default=UNSET, alias="displaySymbol")
    """Display symbol name."""

    symbol: Optional[str] = UNSET
    """Unique symbol used to identify this symbol used in <code>/crypto/candle</code> endpoint."""


class CryptoSymbolDict(TypedDict):
    description: NotRequired[str]
    display_symbol: NotRequired[str]
    symbol: NotRequired[str]
