from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsptoPatent(SdkBaseModel):
    application_number: Optional[str] = Field(default=UNSET, alias="applicationNumber")
    """Application Number."""

    company_filing_name: Optional[list[str]] = Field(default=UNSET, alias="companyFilingName")
    """Array of companies' name on the patent."""

    filing_date: Optional[str] = Field(default=UNSET, alias="filingDate")
    """Filing date."""

    description: Optional[str] = UNSET
    """Description."""

    filing_status: Optional[str] = Field(default=UNSET, alias="filingStatus")
    """Filing status."""

    patent_number: Optional[str] = Field(default=UNSET, alias="patentNumber")
    """Patent number."""

    publication_date: Optional[str] = Field(default=UNSET, alias="publicationDate")
    """Publication date."""

    patent_type: Optional[str] = Field(default=UNSET, alias="patentType")
    """Patent's type."""

    url: Optional[str] = UNSET
    """URL of the original article."""


class UsptoPatentDict(TypedDict):
    application_number: NotRequired[str]
    company_filing_name: NotRequired[list[str]]
    filing_date: NotRequired[str]
    description: NotRequired[str]
    filing_status: NotRequired[str]
    patent_number: NotRequired[str]
    publication_date: NotRequired[str]
    patent_type: NotRequired[str]
    url: NotRequired[str]
