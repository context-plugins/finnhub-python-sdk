from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .filing_response import FilingResponse, FilingResponseDict


class SearchResponse(SdkBaseModel):
    count: Optional[int] = UNSET
    """Total filing matched your search criteria."""

    took: Optional[int] = UNSET
    """Time took to execute your search query on our server, value in ms."""

    page: Optional[int] = UNSET
    """Current search page"""

    filings: Optional[list[FilingResponse]] = UNSET
    """Filing match your search criteria."""


class SearchResponseDict(TypedDict):
    count: NotRequired[int]
    took: NotRequired[int]
    page: NotRequired[int]
    filings: NotRequired[list[FilingResponse | FilingResponseDict]]
