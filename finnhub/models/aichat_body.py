from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .aichat_message import AichatMessage, AichatMessageDict


class AichatBody(SdkBaseModel):
    messages: list[AichatMessage]
    """Messages"""

    stream: Optional[bool] = UNSET
    """Stream responses"""


class AichatBodyDict(TypedDict):
    messages: list[AichatMessage | AichatMessageDict]
    stream: NotRequired[bool]
