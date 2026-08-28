from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .institutional_profile_info import InstitutionalProfileInfo, InstitutionalProfileInfoDict


class InstitutionalProfile(SdkBaseModel):
    cik: Optional[str] = UNSET
    """CIK."""

    data: Optional[list[InstitutionalProfileInfo]] = UNSET
    """Array of investors."""


class InstitutionalProfileDict(TypedDict):
    cik: NotRequired[str]
    data: NotRequired[list[InstitutionalProfileInfo | InstitutionalProfileInfoDict]]
