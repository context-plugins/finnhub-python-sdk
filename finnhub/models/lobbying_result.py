from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .lobbying_data import LobbyingData, LobbyingDataDict


class LobbyingResult(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol."""

    data: Optional[list[LobbyingData]] = UNSET
    """Array of lobbying activities."""


class LobbyingResultDict(TypedDict):
    symbol: NotRequired[str]
    data: NotRequired[list[LobbyingData | LobbyingDataDict]]
