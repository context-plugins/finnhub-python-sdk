from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UpgradeDowngrade(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Company symbol."""

    grade_time: Optional[int] = Field(default=UNSET, alias="gradeTime")
    """Upgrade/downgrade time in UNIX timestamp."""

    from_grade: Optional[str] = Field(default=UNSET, alias="fromGrade")
    """From grade."""

    to_grade: Optional[str] = Field(default=UNSET, alias="toGrade")
    """To grade."""

    company: Optional[str] = UNSET
    """Company/analyst who did the upgrade/downgrade."""

    action: Optional[str] = UNSET
    """Action can take any of the following values: <code>up(upgrade), down(downgrade), main(maintains), init(initiate),
    reit(reiterate)</code>."""


class UpgradeDowngradeDict(TypedDict):
    symbol: NotRequired[str]
    grade_time: NotRequired[int]
    from_grade: NotRequired[str]
    to_grade: NotRequired[str]
    company: NotRequired[str]
    action: NotRequired[str]
