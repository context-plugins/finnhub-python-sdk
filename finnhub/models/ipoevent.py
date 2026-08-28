from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class Ipoevent(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol."""

    date: Optional[Date] = UNSET
    """IPO date."""

    exchange: Optional[str] = UNSET
    """Exchange."""

    name: Optional[str] = UNSET
    """Company's name."""

    status: Optional[str] = UNSET
    """IPO status. Can take 1 of the following values:
    <code>expected</code>,<code>priced</code>,<code>withdrawn</code>,<code>filed</code>"""

    price: Optional[str] = UNSET
    """Projected price or price range."""

    number_of_shares: Optional[float] = Field(default=UNSET, alias="numberOfShares")
    """Number of shares offered during the IPO."""

    total_shares_value: Optional[float] = Field(default=UNSET, alias="totalSharesValue")
    """Total shares value."""


class IpoeventDict(TypedDict):
    symbol: NotRequired[str]
    date: NotRequired[Date]
    exchange: NotRequired[str]
    name: NotRequired[str]
    status: NotRequired[str]
    price: NotRequired[str]
    number_of_shares: NotRequired[float]
    total_shares_value: NotRequired[float]
