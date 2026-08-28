from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MutualFundEetPai(SdkBaseModel):
    isin: Optional[str] = UNSET
    """ISIN."""

    data: Optional[Any] = UNSET


class MutualFundEetPaiDict(TypedDict):
    isin: NotRequired[str]
    data: NotRequired[Any]
