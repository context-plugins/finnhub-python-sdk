from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .presentation_data import PresentationData, PresentationDataDict


class StockPresentation(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Company symbol."""

    res: Optional[list[PresentationData]] = UNSET
    """Presentation data."""


class StockPresentationDict(TypedDict):
    symbol: NotRequired[str]
    res: NotRequired[list[PresentationData | PresentationDataDict]]
