from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Sentiment(SdkBaseModel):
    bearish_percent: Optional[float] = Field(default=UNSET, alias="bearishPercent")
    bullish_percent: Optional[float] = Field(default=UNSET, alias="bullishPercent")


class SentimentDict(TypedDict):
    bearish_percent: NotRequired[float]
    bullish_percent: NotRequired[float]
