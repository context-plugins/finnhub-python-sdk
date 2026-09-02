from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PresentationData(SdkBaseModel):
    quarter: Optional[int] = UNSET
    """Quarter"""

    year: Optional[int] = UNSET
    """Year"""

    url: Optional[str] = UNSET
    """Presentation url"""

    title: Optional[str] = UNSET
    """Title"""

    at_time: Optional[str] = Field(default=UNSET, alias="atTime")
    """At Time."""


class PresentationDataDict(TypedDict):
    quarter: NotRequired[int]
    year: NotRequired[int]
    url: NotRequired[str]
    title: NotRequired[str]
    at_time: NotRequired[str]
