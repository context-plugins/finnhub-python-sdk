from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Forexrates(SdkBaseModel):
    base: Optional[str] = UNSET
    """Base currency."""

    quote: Optional[Any] = UNSET


class ForexratesDict(TypedDict):
    base: NotRequired[str]
    quote: NotRequired[Any]
