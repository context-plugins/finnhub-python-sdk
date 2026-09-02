from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CryptoProfile(SdkBaseModel):
    long_name: Optional[str] = Field(default=UNSET, alias="longName")
    """Long name."""

    name: Optional[str] = UNSET
    """Name."""

    description: Optional[str] = UNSET
    """Description."""

    website: Optional[str] = UNSET
    """Project's website."""

    market_cap: Optional[float] = Field(default=UNSET, alias="marketCap")
    """Market capitalization."""

    total_supply: Optional[float] = Field(default=UNSET, alias="totalSupply")
    """Total supply."""

    max_supply: Optional[float] = Field(default=UNSET, alias="maxSupply")
    """Max supply."""

    circulating_supply: Optional[float] = Field(default=UNSET, alias="circulatingSupply")
    """Circulating supply."""

    logo: Optional[str] = UNSET
    """Logo image."""

    launch_date: Optional[str] = Field(default=UNSET, alias="launchDate")
    """Launch date."""

    proof_type: Optional[str] = Field(default=UNSET, alias="proofType")
    """Proof type."""


class CryptoProfileDict(TypedDict):
    long_name: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str]
    website: NotRequired[str]
    market_cap: NotRequired[float]
    total_supply: NotRequired[float]
    max_supply: NotRequired[float]
    circulating_supply: NotRequired[float]
    logo: NotRequired[str]
    launch_date: NotRequired[str]
    proof_type: NotRequired[str]
