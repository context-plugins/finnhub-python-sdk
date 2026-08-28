from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .development import Development, DevelopmentDict


class PressRelease(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Company symbol."""

    major_development: Optional[list[Development]] = Field(default=UNSET, alias="majorDevelopment")
    """Array of major developments."""


class PressReleaseDict(TypedDict):
    symbol: NotRequired[str]
    major_development: NotRequired[list[Development | DevelopmentDict]]
