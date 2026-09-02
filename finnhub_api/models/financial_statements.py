from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FinancialStatements(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol of the company."""

    financials: Optional[list[Any]] = UNSET
    """An array of map of key, value pairs containing the data for each period."""


class FinancialStatementsDict(TypedDict):
    symbol: NotRequired[str]
    financials: NotRequired[list[Any]]
