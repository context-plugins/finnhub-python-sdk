from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .excerpt_response import ExcerptResponse, ExcerptResponseDict


class DocumentResponse(SdkBaseModel):
    document_id: Optional[str] = Field(default=UNSET, alias="documentId")
    """AlphaResearch internal document id."""

    title: Optional[str] = UNSET
    """Title for this document."""

    hits: Optional[str] = UNSET
    """Number of hit in this document"""

    url: Optional[str] = UNSET
    """Link to render this document"""

    format: Optional[str] = UNSET
    """Format of this document (can be html or pdf)"""

    excerpts: Optional[list[ExcerptResponse]] = UNSET
    """Highlighted excerpts for this document"""


class DocumentResponseDict(TypedDict):
    document_id: NotRequired[str]
    title: NotRequired[str]
    hits: NotRequired[str]
    url: NotRequired[str]
    format: NotRequired[str]
    excerpts: NotRequired[list[ExcerptResponse | ExcerptResponseDict]]
