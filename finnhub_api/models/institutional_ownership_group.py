from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .institutional_ownership_info import InstitutionalOwnershipInfo, InstitutionalOwnershipInfoDict


class InstitutionalOwnershipGroup(SdkBaseModel):
    report_date: Optional[str] = Field(default=UNSET, alias="reportDate")
    """Report date."""

    ownership: Optional[list[InstitutionalOwnershipInfo]] = UNSET
    """Array of institutional investors."""


class InstitutionalOwnershipGroupDict(TypedDict):
    report_date: NotRequired[str]
    ownership: NotRequired[list[InstitutionalOwnershipInfo | InstitutionalOwnershipInfoDict]]
