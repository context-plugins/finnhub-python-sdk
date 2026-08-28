from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PatternRecognition(SdkBaseModel):
    points: Optional[list[Any]] = UNSET
    """Array of patterns."""


class PatternRecognitionDict(TypedDict):
    points: NotRequired[list[Any]]
