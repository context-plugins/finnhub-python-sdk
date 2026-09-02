from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .report import Report, ReportDict


class FinancialsAsReported(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol"""

    cik: Optional[str] = UNSET
    """CIK"""

    data: Optional[list[Report]] = UNSET
    """Array of filings."""


class FinancialsAsReportedDict(TypedDict):
    symbol: NotRequired[str]
    cik: NotRequired[str]
    data: NotRequired[list[Report | ReportDict]]
