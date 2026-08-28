from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BankBranchData(SdkBaseModel):
    branch_id: Optional[str] = Field(default=UNSET, alias="branchId")
    """Branch ID"""

    address: Optional[str] = UNSET
    """Branch address"""

    state: Optional[str] = UNSET
    """State"""

    zip_code: Optional[str] = Field(default=UNSET, alias="zipCode")
    """Zip code"""

    date: Optional[str] = UNSET
    """Date opened"""


class BankBranchDataDict(TypedDict):
    branch_id: NotRequired[str]
    address: NotRequired[str]
    state: NotRequired[str]
    zip_code: NotRequired[str]
    date: NotRequired[str]
