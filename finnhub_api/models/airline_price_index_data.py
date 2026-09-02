from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .airline_price_index import AirlinePriceIndex, AirlinePriceIndexDict


class AirlinePriceIndexData(SdkBaseModel):
    data: Optional[list[AirlinePriceIndex]] = UNSET
    """Array of price index."""

    airline: Optional[str] = UNSET
    """Airline name"""

    from_: Optional[str] = Field(default=UNSET, alias="from")
    """From date"""

    to: Optional[str] = UNSET
    """To date"""


class AirlinePriceIndexDataDict(TypedDict):
    data: NotRequired[list[AirlinePriceIndex | AirlinePriceIndexDict]]
    airline: NotRequired[str]
    from_: NotRequired[str]
    to: NotRequired[str]
