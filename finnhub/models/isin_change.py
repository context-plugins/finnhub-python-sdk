from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .isin_change_info import IsinChangeInfo, IsinChangeInfoDict


class IsinChange(SdkBaseModel):
    from_date: Optional[str] = Field(default=UNSET, alias="fromDate")
    """From date."""

    to_date: Optional[str] = Field(default=UNSET, alias="toDate")
    """To date."""

    data: Optional[list[IsinChangeInfo]] = UNSET
    """Array of ISIN change events."""


class IsinChangeDict(TypedDict):
    from_date: NotRequired[str]
    to_date: NotRequired[str]
    data: NotRequired[list[IsinChangeInfo | IsinChangeInfoDict]]
