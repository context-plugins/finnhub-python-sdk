from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AichatResponse(SdkBaseModel):
    chat_id: Optional[str] = Field(default=UNSET, alias="chatId")
    """Chat ID."""

    content: Optional[str] = UNSET
    """Response text."""

    query_summary: Optional[str] = Field(default=UNSET, alias="querySummary")
    """Query summary"""

    related_queries: Optional[list[Any]] = Field(default=UNSET, alias="relatedQueries")
    """Related queries."""

    tickers: Optional[list[Any]] = UNSET
    """List of tickers mentioned."""

    sources: Optional[list[Any]] = UNSET
    """Sources."""

    widgets: Optional[list[Any]] = UNSET
    """Widgets."""


class AichatResponseDict(TypedDict):
    chat_id: NotRequired[str]
    content: NotRequired[str]
    query_summary: NotRequired[str]
    related_queries: NotRequired[list[Any]]
    tickers: NotRequired[list[Any]]
    sources: NotRequired[list[Any]]
    widgets: NotRequired[list[Any]]
