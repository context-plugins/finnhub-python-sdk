from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MarketCapData(SdkBaseModel):
    at_date: Optional[str] = Field(default=UNSET, alias="atDate")
    """Date of the reading"""

    market_capitalization: Optional[float] = Field(default=UNSET, alias="marketCapitalization")
    """Value"""


class MarketCapDataDict(TypedDict):
    at_date: NotRequired[str]
    market_capitalization: NotRequired[float]
