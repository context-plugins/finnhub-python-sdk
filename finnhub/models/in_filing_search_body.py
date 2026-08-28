from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class InFilingSearchBody(SdkBaseModel):
    query: str
    """Search query"""

    filing_id: str = Field(alias="filingId")
    """Filing Id to search"""


class InFilingSearchBodyDict(TypedDict):
    query: str
    filing_id: str
