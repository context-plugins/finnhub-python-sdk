from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ExcerptResponse(SdkBaseModel):
    content: Optional[str] = UNSET
    """Highlighted content"""

    snippet_id: Optional[str] = Field(default=UNSET, alias="snippetId")
    """Location of the content in the rendered document"""

    start_offset: Optional[str] = Field(default=UNSET, alias="startOffset")
    """Start offset of highlighted content"""

    end_offset: Optional[str] = Field(default=UNSET, alias="endOffset")
    """End offset of highlighted content"""


class ExcerptResponseDict(TypedDict):
    content: NotRequired[str]
    snippet_id: NotRequired[str]
    start_offset: NotRequired[str]
    end_offset: NotRequired[str]
