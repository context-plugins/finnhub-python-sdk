from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .institutional_ownership_group import InstitutionalOwnershipGroup, InstitutionalOwnershipGroupDict


class InstitutionalOwnership(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol."""

    cusip: Optional[str] = UNSET
    """Cusip."""

    data: Optional[list[InstitutionalOwnershipGroup]] = UNSET
    """Array of institutional investors."""


class InstitutionalOwnershipDict(TypedDict):
    symbol: NotRequired[str]
    cusip: NotRequired[str]
    data: NotRequired[list[InstitutionalOwnershipGroup | InstitutionalOwnershipGroupDict]]
