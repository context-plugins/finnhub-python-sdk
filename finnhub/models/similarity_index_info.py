from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SimilarityIndexInfo(SdkBaseModel):
    cik: Optional[str] = UNSET
    """CIK."""

    item1: Optional[float] = UNSET
    """Cosine similarity of Item 1 (Business). This number is only available for Annual reports."""

    item1a: Optional[float] = UNSET
    """Cosine similarity of Item 1A (Risk Factors). This number is available for both Annual and Quarterly reports."""

    item2: Optional[float] = UNSET
    """Cosine similarity of Item 2 (Management’s Discussion and Analysis of Financial Condition and Results of
    Operations). This number is only available for Quarterly reports."""

    item7: Optional[float] = UNSET
    """Cosine similarity of Item 7 (Management’s Discussion and Analysis of Financial Condition and Results of
    Operations). This number is only available for Annual reports."""

    item7a: Optional[float] = UNSET
    """Cosine similarity of Item 7A (Quantitative and Qualitative Disclosures About Market Risk). This number is only
    available for Annual reports."""

    access_number: Optional[str] = Field(default=UNSET, alias="accessNumber")
    """Access number."""

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


class SimilarityIndexInfoDict(TypedDict):
    cik: NotRequired[str]
    item1: NotRequired[float]
    item1a: NotRequired[float]
    item2: NotRequired[float]
    item7: NotRequired[float]
    item7a: NotRequired[float]
    access_number: NotRequired[str]
    form: NotRequired[str]
    filed_date: NotRequired[str]
    accepted_date: NotRequired[str]
    report_url: NotRequired[str]
    filing_url: NotRequired[str]
