from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CongressionalTransaction(SdkBaseModel):
    amount_from: Optional[float] = Field(default=UNSET, alias="amountFrom")
    """Transaction amount from."""

    amount_to: Optional[float] = Field(default=UNSET, alias="amountTo")
    """Transaction amount to."""

    asset_name: Optional[str] = Field(default=UNSET, alias="assetName")
    """Asset name."""

    filing_date: Optional[str] = Field(default=UNSET, alias="filingDate")
    """Filing date."""

    name: Optional[str] = UNSET
    """Name of the representative."""

    owner_type: Optional[str] = Field(default=UNSET, alias="ownerType")
    """Owner Type."""

    position: Optional[str] = UNSET
    """Position."""

    symbol: Optional[str] = UNSET
    """Symbol."""

    transaction_date: Optional[str] = Field(default=UNSET, alias="transactionDate")
    """Transaction date."""

    transaction_type: Optional[str] = Field(default=UNSET, alias="transactionType")
    """Transaction type <code>Sale</code> or <code>Purchase</code>."""


class CongressionalTransactionDict(TypedDict):
    amount_from: NotRequired[float]
    amount_to: NotRequired[float]
    asset_name: NotRequired[str]
    filing_date: NotRequired[str]
    name: NotRequired[str]
    owner_type: NotRequired[str]
    position: NotRequired[str]
    symbol: NotRequired[str]
    transaction_date: NotRequired[str]
    transaction_type: NotRequired[str]
