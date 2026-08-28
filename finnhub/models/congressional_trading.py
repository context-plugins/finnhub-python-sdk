from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .congressional_transaction import CongressionalTransaction, CongressionalTransactionDict


class CongressionalTrading(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol of the company."""

    data: Optional[list[CongressionalTransaction]] = UNSET
    """Array of stock trades."""


class CongressionalTradingDict(TypedDict):
    symbol: NotRequired[str]
    data: NotRequired[list[CongressionalTransaction | CongressionalTransactionDict]]
