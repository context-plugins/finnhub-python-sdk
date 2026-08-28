from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CompanyNews(SdkBaseModel):
    category: Optional[str] = UNSET
    """News category."""

    datetime: Optional[int] = UNSET
    """Published time in UNIX timestamp."""

    headline: Optional[str] = UNSET
    """News headline."""

    id: Optional[int] = UNSET
    """News ID. This value can be used for <code>minId</code> params to get the latest news only."""

    image: Optional[str] = UNSET
    """Thumbnail image URL."""

    related: Optional[str] = UNSET
    """Related stocks and companies mentioned in the article."""

    source: Optional[str] = UNSET
    """News source."""

    summary: Optional[str] = UNSET
    """News summary."""

    url: Optional[str] = UNSET
    """URL of the original article."""


class CompanyNewsDict(TypedDict):
    category: NotRequired[str]
    datetime: NotRequired[int]
    headline: NotRequired[str]
    id: NotRequired[int]
    image: NotRequired[str]
    related: NotRequired[str]
    source: NotRequired[str]
    summary: NotRequired[str]
    url: NotRequired[str]
