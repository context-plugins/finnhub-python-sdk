from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fund_ownership_info import FundOwnershipInfo, FundOwnershipInfoDict


class FundOwnership(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol of the company."""

    ownership: Optional[list[FundOwnershipInfo]] = UNSET
    """Array of investors with detailed information about their holdings."""


class FundOwnershipDict(TypedDict):
    symbol: NotRequired[str]
    ownership: NotRequired[list[FundOwnershipInfo | FundOwnershipInfoDict]]
