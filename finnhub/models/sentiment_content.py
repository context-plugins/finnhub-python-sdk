from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SentimentContent(SdkBaseModel):
    mention: Optional[int] = UNSET
    """Number of mentions"""

    positive_mention: Optional[int] = Field(default=UNSET, alias="positiveMention")
    """Number of positive mentions"""

    negative_mention: Optional[int] = Field(default=UNSET, alias="negativeMention")
    """Number of negative mentions"""

    positive_score: Optional[float] = Field(default=UNSET, alias="positiveScore")
    """Positive score. Range 0-1"""

    negative_score: Optional[float] = Field(default=UNSET, alias="negativeScore")
    """Negative score. Range 0-1"""

    score: Optional[float] = UNSET
    """Final score. Range: -1 to 1 with 1 is very positive and -1 is very negative"""

    at_time: Optional[str] = Field(default=UNSET, alias="atTime")
    """Period."""


class SentimentContentDict(TypedDict):
    mention: NotRequired[int]
    positive_mention: NotRequired[int]
    negative_mention: NotRequired[int]
    positive_score: NotRequired[float]
    negative_score: NotRequired[float]
    score: NotRequired[float]
    at_time: NotRequired[str]
