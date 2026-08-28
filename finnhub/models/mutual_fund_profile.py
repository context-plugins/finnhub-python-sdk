from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .mutual_fund_profile_data import MutualFundProfileData, MutualFundProfileDataDict


class MutualFundProfile(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol."""

    profile: Optional[MutualFundProfileData] = UNSET


class MutualFundProfileDict(TypedDict):
    symbol: NotRequired[str]
    profile: NotRequired[MutualFundProfileData | MutualFundProfileDataDict]
