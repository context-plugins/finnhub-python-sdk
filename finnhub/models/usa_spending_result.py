from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .usa_spending import UsaSpending, UsaSpendingDict


class UsaSpendingResult(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol."""

    data: Optional[list[UsaSpending]] = UNSET
    """Array of government's spending data points."""


class UsaSpendingResultDict(TypedDict):
    symbol: NotRequired[str]
    data: NotRequired[list[UsaSpending | UsaSpendingDict]]
