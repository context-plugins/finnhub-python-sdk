from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transactions import Transactions, TransactionsDict


class InsiderTransactions(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol of the company."""

    data: Optional[list[Transactions]] = UNSET
    """Array of insider transactions."""


class InsiderTransactionsDict(TypedDict):
    symbol: NotRequired[str]
    data: NotRequired[list[Transactions | TransactionsDict]]
