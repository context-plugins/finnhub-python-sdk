from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SearchFilter(SdkBaseModel):
    id: Optional[str] = UNSET
    """Filter id, use with respective field in search query body."""

    name: Optional[str] = UNSET
    """Display name."""


class SearchFilterDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
