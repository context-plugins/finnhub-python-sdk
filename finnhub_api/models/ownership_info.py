from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class OwnershipInfo(SdkBaseModel):
    name: Optional[str] = UNSET
    """Investor's name."""

    share: Optional[int] = UNSET
    """Number of shares held by the investor."""

    change: Optional[int] = UNSET
    """Number of share changed (net buy or sell) from the last period."""

    filing_date: Optional[Date] = Field(default=UNSET, alias="filingDate")
    """Filing date."""


class OwnershipInfoDict(TypedDict):
    name: NotRequired[str]
    share: NotRequired[int]
    change: NotRequired[int]
    filing_date: NotRequired[Date]
