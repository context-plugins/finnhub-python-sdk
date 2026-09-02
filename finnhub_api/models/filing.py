from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Filing(SdkBaseModel):
    access_number: Optional[str] = Field(default=UNSET, alias="accessNumber")
    """Access number."""

    symbol: Optional[str] = UNSET
    """Symbol."""

    cik: Optional[str] = UNSET
    """CIK."""

    form: Optional[str] = UNSET
    """Form type."""

    filed_date: Optional[str] = Field(default=UNSET, alias="filedDate")
    """Filed date <code>%Y-%m-%d %H:%M:%S</code>."""

    accepted_date: Optional[str] = Field(default=UNSET, alias="acceptedDate")
    """Accepted date <code>%Y-%m-%d %H:%M:%S</code>."""

    report_url: Optional[str] = Field(default=UNSET, alias="reportUrl")
    """Report's URL."""

    filing_url: Optional[str] = Field(default=UNSET, alias="filingUrl")
    """Filing's URL."""


class FilingDict(TypedDict):
    access_number: NotRequired[str]
    symbol: NotRequired[str]
    cik: NotRequired[str]
    form: NotRequired[str]
    filed_date: NotRequired[str]
    accepted_date: NotRequired[str]
    report_url: NotRequired[str]
    filing_url: NotRequired[str]
