from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MutualFundEet(SdkBaseModel):
    isin: Optional[str] = UNSET
    """ISIN."""

    data: Optional[Any] = UNSET


class MutualFundEetDict(TypedDict):
    isin: NotRequired[str]
    data: NotRequired[Any]
