from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SymbolChangeInfo(SdkBaseModel):
    at_date: Optional[str] = Field(default=UNSET, alias="atDate")
    """Event's date."""

    old_symbol: Optional[str] = Field(default=UNSET, alias="oldSymbol")
    """Old symbol."""

    new_symbol: Optional[str] = Field(default=UNSET, alias="newSymbol")
    """New symbol."""


class SymbolChangeInfoDict(TypedDict):
    at_date: NotRequired[str]
    old_symbol: NotRequired[str]
    new_symbol: NotRequired[str]
