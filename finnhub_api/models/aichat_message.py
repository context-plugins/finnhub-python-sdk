from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AichatMessage(SdkBaseModel):
    role: Optional[str] = UNSET
    """Role system/user"""

    content: Optional[str] = UNSET
    """Content"""


class AichatMessageDict(TypedDict):
    role: NotRequired[str]
    content: NotRequired[str]
