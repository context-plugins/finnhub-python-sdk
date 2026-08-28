from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class Transactions(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol."""

    name: Optional[str] = UNSET
    """Insider's name."""

    share: Optional[int] = UNSET
    """Number of shares held after the transaction."""

    change: Optional[int] = UNSET
    """Number of share changed from the last period. A positive value suggests a <code>BUY</code> transaction. A
    negative value suggests a <code>SELL</code> transaction."""

    filing_date: Optional[Date] = Field(default=UNSET, alias="filingDate")
    """Filing date."""

    transaction_date: Optional[Date] = Field(default=UNSET, alias="transactionDate")
    """Transaction date."""

    transaction_price: Optional[float] = Field(default=UNSET, alias="transactionPrice")
    """Average transaction price."""

    transaction_code: Optional[str] = Field(default=UNSET, alias="transactionCode")
    """Transaction code. A list of codes and their meanings can be found <a
    href="https://www.sec.gov/about/forms/form4data.pdf" target="_blank" rel="noopener">here</a>."""


class TransactionsDict(TypedDict):
    symbol: NotRequired[str]
    name: NotRequired[str]
    share: NotRequired[int]
    change: NotRequired[int]
    filing_date: NotRequired[Date]
    transaction_date: NotRequired[Date]
    transaction_price: NotRequired[float]
    transaction_code: NotRequired[str]
