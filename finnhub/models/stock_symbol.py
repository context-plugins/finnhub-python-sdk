from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class StockSymbol(SdkBaseModel):
    description: Optional[str] = UNSET
    """Symbol description"""

    display_symbol: Optional[str] = Field(default=UNSET, alias="displaySymbol")
    """Display symbol name."""

    symbol: Optional[str] = UNSET
    """Unique symbol used to identify this symbol used in <code>/stock/candle</code> endpoint."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Security type."""

    mic: Optional[str] = UNSET
    """Primary exchange's MIC."""

    figi: Optional[str] = UNSET
    """FIGI identifier."""

    share_class_figi: Optional[str] = Field(default=UNSET, alias="shareClassFIGI")
    """Global Share Class FIGI."""

    currency: Optional[str] = UNSET
    """Price's currency. This might be different from the reporting currency of fundamental data."""

    symbol2: Optional[str] = UNSET
    """Alternative ticker for exchanges with multiple tickers for 1 stock such as BSE."""

    isin: Optional[str] = UNSET
    """ISIN. This field is only available for EU stocks and selected Asian markets. Entitlement from Finnhub is required
    to access this field."""


class StockSymbolDict(TypedDict):
    description: NotRequired[str]
    display_symbol: NotRequired[str]
    symbol: NotRequired[str]
    type_: NotRequired[str]
    mic: NotRequired[str]
    figi: NotRequired[str]
    share_class_figi: NotRequired[str]
    currency: NotRequired[str]
    symbol2: NotRequired[str]
    isin: NotRequired[str]
