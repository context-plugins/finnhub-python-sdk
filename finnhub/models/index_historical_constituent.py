from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class IndexHistoricalConstituent(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol"""

    action: Optional[str] = UNSET
    """<code>add</code> or <code>remove</code>."""

    date: Optional[Date] = UNSET
    """Date of joining or leaving the index."""


class IndexHistoricalConstituentDict(TypedDict):
    symbol: NotRequired[str]
    action: NotRequired[str]
    date: NotRequired[Date]
