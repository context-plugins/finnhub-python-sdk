from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .indices_constituents_breakdown import IndicesConstituentsBreakdown, IndicesConstituentsBreakdownDict


class IndicesConstituents(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Index's symbol."""

    constituents: Optional[list[str]] = UNSET
    """Array of constituents."""

    constituents_breakdown: Optional[list[IndicesConstituentsBreakdown]] = Field(
        default=UNSET, alias="constituentsBreakdown"
    )
    """Array of constituents' details."""


class IndicesConstituentsDict(TypedDict):
    symbol: NotRequired[str]
    constituents: NotRequired[list[str]]
    constituents_breakdown: NotRequired[list[IndicesConstituentsBreakdown | IndicesConstituentsBreakdownDict]]
