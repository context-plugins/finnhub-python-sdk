from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class NewsroomArticle(SdkBaseModel):
    at_date: Optional[str] = Field(default=UNSET, alias="atDate")
    """Published time in <code>YYYY-MM-DD HH:MM:SS</code> format (EST timezone)."""

    title: Optional[str] = UNSET
    """Title."""

    full_text: Optional[str] = Field(default=UNSET, alias="fullText")
    """URL to download the full text data."""

    url: Optional[str] = UNSET
    """Original URL."""


class NewsroomArticleDict(TypedDict):
    at_date: NotRequired[str]
    title: NotRequired[str]
    full_text: NotRequired[str]
    url: NotRequired[str]
