from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .filing_sentiment import FilingSentiment, FilingSentimentDict


class SecsentimentAnalysis(SdkBaseModel):
    access_number: Optional[str] = Field(default=UNSET, alias="accessNumber")
    """Access number."""

    symbol: Optional[str] = UNSET
    """Symbol."""

    cik: Optional[str] = UNSET
    """CIK."""

    sentiment: Optional[FilingSentiment] = UNSET


class SecsentimentAnalysisDict(TypedDict):
    access_number: NotRequired[str]
    symbol: NotRequired[str]
    cik: NotRequired[str]
    sentiment: NotRequired[FilingSentiment | FilingSentimentDict]
