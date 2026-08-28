from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IndicesConstituentsBreakdown(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol."""

    name: Optional[str] = UNSET
    """Name."""

    isin: Optional[str] = UNSET
    """ISIN."""

    cusip: Optional[str] = UNSET
    """Cusip."""

    share_class_figi: Optional[str] = Field(default=UNSET, alias="shareClassFIGI")
    """Global Share Class FIGI."""

    weight: Optional[float] = UNSET
    """Weight."""


class IndicesConstituentsBreakdownDict(TypedDict):
    symbol: NotRequired[str]
    name: NotRequired[str]
    isin: NotRequired[str]
    cusip: NotRequired[str]
    share_class_figi: NotRequired[str]
    weight: NotRequired[float]
