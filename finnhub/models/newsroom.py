from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .newsroom_article import NewsroomArticle, NewsroomArticleDict


class Newsroom(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Company symbol."""

    data: Optional[list[NewsroomArticle]] = UNSET
    """Array of articles."""


class NewsroomDict(TypedDict):
    symbol: NotRequired[str]
    data: NotRequired[list[NewsroomArticle | NewsroomArticleDict]]
