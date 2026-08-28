from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sentiment_content import SentimentContent, SentimentContentDict


class SocialSentiment(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Company symbol."""

    data: Optional[list[SentimentContent]] = UNSET
    """Sentiment data."""


class SocialSentimentDict(TypedDict):
    symbol: NotRequired[str]
    data: NotRequired[list[SentimentContent | SentimentContentDict]]
