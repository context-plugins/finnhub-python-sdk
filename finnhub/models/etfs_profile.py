from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .etfprofile_data import EtfprofileData, EtfprofileDataDict


class EtfsProfile(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol."""

    profile: Optional[EtfprofileData] = UNSET


class EtfsProfileDict(TypedDict):
    symbol: NotRequired[str]
    profile: NotRequired[EtfprofileData | EtfprofileDataDict]
