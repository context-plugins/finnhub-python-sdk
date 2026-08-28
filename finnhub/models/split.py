from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class Split(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol."""

    date: Optional[Date] = UNSET
    """Split date."""

    from_factor: Optional[float] = Field(default=UNSET, alias="fromFactor")
    """From factor."""

    to_factor: Optional[float] = Field(default=UNSET, alias="toFactor")
    """To factor."""


class SplitDict(TypedDict):
    symbol: NotRequired[str]
    date: NotRequired[Date]
    from_factor: NotRequired[float]
    to_factor: NotRequired[float]
