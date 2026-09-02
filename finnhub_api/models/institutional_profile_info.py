from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InstitutionalProfileInfo(SdkBaseModel):
    cik: Optional[str] = UNSET
    """Investor's company CIK."""

    firm_type: Optional[str] = Field(default=UNSET, alias="firmType")
    """Firm type."""

    manager: Optional[str] = UNSET
    """Manager."""

    philosophy: Optional[str] = UNSET
    """Investing philosophy."""

    profile: Optional[str] = UNSET
    """Profile info."""

    profile_img: Optional[str] = Field(default=UNSET, alias="profileImg")
    """Profile image."""


class InstitutionalProfileInfoDict(TypedDict):
    cik: NotRequired[str]
    firm_type: NotRequired[str]
    manager: NotRequired[str]
    philosophy: NotRequired[str]
    profile: NotRequired[str]
    profile_img: NotRequired[str]
