from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BreakdownItem(SdkBaseModel):
    access_number: Optional[str] = Field(default=UNSET, alias="accessNumber")
    """Access number of the report from which the data is sourced."""

    breakdown: Optional[Any] = UNSET


class BreakdownItemDict(TypedDict):
    access_number: NotRequired[str]
    breakdown: NotRequired[Any]
