from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .document_response import DocumentResponse, DocumentResponseDict


class InFilingResponse(SdkBaseModel):
    filing_id: Optional[str] = Field(default=UNSET, alias="filingId")
    """Filing Id in Alpharesearch platform"""

    title: Optional[str] = UNSET
    """Filing title"""

    filer_id: Optional[str] = Field(default=UNSET, alias="filerId")
    """Id of the entity submitted the filing"""

    symbol: Optional[Any] = UNSET
    """List of symbol associate with this filing"""

    name: Optional[str] = UNSET
    """Filer name"""

    acceptance_date: Optional[str] = Field(default=UNSET, alias="acceptanceDate")
    """Date the filing is submitted."""

    filed_date: Optional[str] = Field(default=UNSET, alias="filedDate")
    """Date the filing is make available to the public"""

    report_date: Optional[str] = Field(default=UNSET, alias="reportDate")
    """Date as which the filing is reported"""

    form: Optional[str] = UNSET
    """Filing Form"""

    amend: Optional[bool] = UNSET
    """Amendment"""

    source: Optional[str] = UNSET
    """Filing Source"""

    page_count: Optional[int] = Field(default=UNSET, alias="pageCount")
    """Estimate number of page when printing"""

    document_count: Optional[int] = Field(default=UNSET, alias="documentCount")
    """Number of document in this filing"""

    documents: Optional[list[DocumentResponse]] = UNSET
    """Document for this filing."""


class InFilingResponseDict(TypedDict):
    filing_id: NotRequired[str]
    title: NotRequired[str]
    filer_id: NotRequired[str]
    symbol: NotRequired[Any]
    name: NotRequired[str]
    acceptance_date: NotRequired[str]
    filed_date: NotRequired[str]
    report_date: NotRequired[str]
    form: NotRequired[str]
    amend: NotRequired[bool]
    source: NotRequired[str]
    page_count: NotRequired[int]
    document_count: NotRequired[int]
    documents: NotRequired[list[DocumentResponse | DocumentResponseDict]]
