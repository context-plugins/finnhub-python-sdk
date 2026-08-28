from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FilingSentiment(SdkBaseModel):
    negative: Optional[float] = UNSET
    """% of negative words in the filing."""

    positive: Optional[float] = UNSET
    """% of positive words in the filing."""

    polarity: Optional[float] = UNSET
    """% of polarity words in the filing."""

    litigious: Optional[float] = UNSET
    """% of litigious words in the filing."""

    uncertainty: Optional[float] = UNSET
    """% of uncertainty words in the filing."""

    constraining: Optional[float] = UNSET
    """% of constraining words in the filing."""

    modal_weak: Optional[float] = Field(default=UNSET, alias="modal-weak")
    """% of modal-weak words in the filing."""

    modal_strong: Optional[float] = Field(default=UNSET, alias="modal-strong")
    """% of modal-strong words in the filing."""

    modal_moderate: Optional[float] = Field(default=UNSET, alias="modal-moderate")
    """% of modal-moderate words in the filing."""


class FilingSentimentDict(TypedDict):
    negative: NotRequired[float]
    positive: NotRequired[float]
    polarity: NotRequired[float]
    litigious: NotRequired[float]
    uncertainty: NotRequired[float]
    constraining: NotRequired[float]
    modal_weak: NotRequired[float]
    modal_strong: NotRequired[float]
    modal_moderate: NotRequired[float]
