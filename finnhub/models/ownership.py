from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .ownership_info import OwnershipInfo, OwnershipInfoDict


class Ownership(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol of the company."""

    ownership: Optional[list[OwnershipInfo]] = UNSET
    """Array of investors with detailed information about their holdings."""


class OwnershipDict(TypedDict):
    symbol: NotRequired[str]
    ownership: NotRequired[list[OwnershipInfo | OwnershipInfoDict]]
