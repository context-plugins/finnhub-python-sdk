from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .company import Company, CompanyDict


class CompanyExecutive(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Company symbol."""

    executive: Optional[list[Company]] = UNSET
    """Array of company's executives and members of the Board."""


class CompanyExecutiveDict(TypedDict):
    symbol: NotRequired[str]
    executive: NotRequired[list[Company | CompanyDict]]
