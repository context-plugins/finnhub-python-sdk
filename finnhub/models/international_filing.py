from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InternationalFiling(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol."""

    company_name: Optional[str] = Field(default=UNSET, alias="companyName")
    """Company name."""

    filed_date: Optional[str] = Field(default=UNSET, alias="filedDate")
    """Filed date <code>%Y-%m-%d %H:%M:%S</code>."""

    category: Optional[str] = UNSET
    """Category."""

    title: Optional[str] = UNSET
    """Document's title."""

    description: Optional[str] = UNSET
    """Document's description."""

    url: Optional[str] = UNSET
    """Url."""

    language: Optional[str] = UNSET
    """Language."""

    country: Optional[str] = UNSET
    """Country."""


class InternationalFilingDict(TypedDict):
    symbol: NotRequired[str]
    company_name: NotRequired[str]
    filed_date: NotRequired[str]
    category: NotRequired[str]
    title: NotRequired[str]
    description: NotRequired[str]
    url: NotRequired[str]
    language: NotRequired[str]
    country: NotRequired[str]
