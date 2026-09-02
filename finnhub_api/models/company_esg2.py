from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CompanyEsg2(SdkBaseModel):
    total_esg_score: Optional[float] = Field(default=UNSET, alias="totalESGScore")
    """Total ESG Score"""

    environment_score: Optional[float] = Field(default=UNSET, alias="environmentScore")
    """Environment Score"""

    governance_score: Optional[float] = Field(default=UNSET, alias="governanceScore")
    """Governance Score"""

    social_score: Optional[float] = Field(default=UNSET, alias="socialScore")
    """Social Score"""

    data: Optional[Any] = UNSET
    period: Optional[str] = UNSET
    """Period"""


class CompanyEsg2Dict(TypedDict):
    total_esg_score: NotRequired[float]
    environment_score: NotRequired[float]
    governance_score: NotRequired[float]
    social_score: NotRequired[float]
    data: NotRequired[Any]
    period: NotRequired[str]
