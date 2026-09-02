from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IsinChangeInfo(SdkBaseModel):
    at_date: Optional[str] = Field(default=UNSET, alias="atDate")
    """Event's date."""

    old_isin: Optional[str] = Field(default=UNSET, alias="oldIsin")
    """Old ISIN."""

    new_isin: Optional[str] = Field(default=UNSET, alias="newIsin")
    """New ISIN."""


class IsinChangeInfoDict(TypedDict):
    at_date: NotRequired[str]
    old_isin: NotRequired[str]
    new_isin: NotRequired[str]
