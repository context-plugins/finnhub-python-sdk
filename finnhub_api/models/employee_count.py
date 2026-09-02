from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EmployeeCount(SdkBaseModel):
    at_date: Optional[str] = Field(default=UNSET, alias="atDate")
    """Date of the reading"""

    employee: Optional[float] = UNSET
    """Value"""


class EmployeeCountDict(TypedDict):
    at_date: NotRequired[str]
    employee: NotRequired[float]
