from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Report(SdkBaseModel):
    access_number: Optional[str] = Field(default=UNSET, alias="accessNumber")
    """Access number."""

    symbol: Optional[str] = UNSET
    """Symbol."""

    cik: Optional[str] = UNSET
    """CIK."""

    year: Optional[int] = UNSET
    """Year."""

    quarter: Optional[int] = UNSET
    """Quarter."""

    form: Optional[str] = UNSET
    """Form type."""

    start_date: Optional[str] = Field(default=UNSET, alias="startDate")
    """Period start date <code>%Y-%m-%d %H:%M:%S</code>."""

    end_date: Optional[str] = Field(default=UNSET, alias="endDate")
    """Period end date <code>%Y-%m-%d %H:%M:%S</code>."""

    filed_date: Optional[str] = Field(default=UNSET, alias="filedDate")
    """Filed date <code>%Y-%m-%d %H:%M:%S</code>."""

    accepted_date: Optional[str] = Field(default=UNSET, alias="acceptedDate")
    """Accepted date <code>%Y-%m-%d %H:%M:%S</code>."""

    report: Optional[Any] = UNSET


class ReportDict(TypedDict):
    access_number: NotRequired[str]
    symbol: NotRequired[str]
    cik: NotRequired[str]
    year: NotRequired[int]
    quarter: NotRequired[int]
    form: NotRequired[str]
    start_date: NotRequired[str]
    end_date: NotRequired[str]
    filed_date: NotRequired[str]
    accepted_date: NotRequired[str]
    report: NotRequired[Any]
