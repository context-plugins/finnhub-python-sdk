from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .visa_application import VisaApplication, VisaApplicationDict


class VisaApplicationResult(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol."""

    data: Optional[list[VisaApplication]] = UNSET
    """Array of H1b and Permanent visa applications."""


class VisaApplicationResultDict(TypedDict):
    symbol: NotRequired[str]
    data: NotRequired[list[VisaApplication | VisaApplicationDict]]
