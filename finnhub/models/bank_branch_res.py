from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bank_branch_data import BankBranchData, BankBranchDataDict


class BankBranchRes(SdkBaseModel):
    data: Optional[list[BankBranchData]] = UNSET
    """Array of branches."""

    symbol: Optional[str] = UNSET
    """Symbol"""


class BankBranchResDict(TypedDict):
    data: NotRequired[list[BankBranchData | BankBranchDataDict]]
    symbol: NotRequired[str]
