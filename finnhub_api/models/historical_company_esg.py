from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .company_esg2 import CompanyEsg2, CompanyEsg2Dict


class HistoricalCompanyEsg(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """symbol"""

    data: Optional[list[CompanyEsg2]] = UNSET
    """Historical ESG data points."""


class HistoricalCompanyEsgDict(TypedDict):
    symbol: NotRequired[str]
    data: NotRequired[list[CompanyEsg2 | CompanyEsg2Dict]]
