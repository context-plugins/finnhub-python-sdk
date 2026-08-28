from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Company(SdkBaseModel):
    name: Optional[str] = UNSET
    """Executive name"""

    age: Optional[int] = UNSET
    """Age"""

    title: Optional[str] = UNSET
    """Title"""

    since: Optional[str] = UNSET
    """Year first appointed as executive/director of the company"""

    sex: Optional[str] = UNSET
    """Sex"""

    compensation: Optional[int] = UNSET
    """Total compensation"""

    currency: Optional[str] = UNSET
    """Compensation currency"""


class CompanyDict(TypedDict):
    name: NotRequired[str]
    age: NotRequired[int]
    title: NotRequired[str]
    since: NotRequired[str]
    sex: NotRequired[str]
    compensation: NotRequired[int]
    currency: NotRequired[str]
