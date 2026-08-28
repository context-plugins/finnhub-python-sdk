from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .index_historical_constituent import IndexHistoricalConstituent, IndexHistoricalConstituentDict


class IndicesHistoricalConstituents(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Index's symbol."""

    historical_constituents: Optional[list[IndexHistoricalConstituent]] = Field(
        default=UNSET, alias="historicalConstituents"
    )
    """Array of historical constituents."""


class IndicesHistoricalConstituentsDict(TypedDict):
    symbol: NotRequired[str]
    historical_constituents: NotRequired[list[IndexHistoricalConstituent | IndexHistoricalConstituentDict]]
