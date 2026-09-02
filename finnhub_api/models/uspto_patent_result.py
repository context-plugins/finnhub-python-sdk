from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .uspto_patent import UsptoPatent, UsptoPatentDict


class UsptoPatentResult(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol."""

    data: Optional[list[UsptoPatent]] = UNSET
    """Array of patents."""


class UsptoPatentResultDict(TypedDict):
    symbol: NotRequired[str]
    data: NotRequired[list[UsptoPatent | UsptoPatentDict]]
