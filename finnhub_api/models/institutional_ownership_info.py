from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InstitutionalOwnershipInfo(SdkBaseModel):
    cik: Optional[str] = UNSET
    """Investor's company CIK."""

    name: Optional[str] = UNSET
    """Firm's name."""

    put_call: Optional[str] = Field(default=UNSET, alias="putCall")
    """<code>put</code> or <code>call</code> for options."""

    change: Optional[float] = UNSET
    """Number of shares change."""

    no_voting: Optional[float] = Field(default=UNSET, alias="noVoting")
    """Number of shares with no voting rights."""

    percentage: Optional[float] = UNSET
    """Percentage of portfolio."""

    share: Optional[float] = UNSET
    """News score."""

    shared_voting: Optional[float] = Field(default=UNSET, alias="sharedVoting")
    """Number of shares with shared voting rights."""

    sole_voting: Optional[float] = Field(default=UNSET, alias="soleVoting")
    """Number of shares with sole voting rights."""

    value: Optional[float] = UNSET
    """Position value."""


class InstitutionalOwnershipInfoDict(TypedDict):
    cik: NotRequired[str]
    name: NotRequired[str]
    put_call: NotRequired[str]
    change: NotRequired[float]
    no_voting: NotRequired[float]
    percentage: NotRequired[float]
    share: NotRequired[float]
    shared_voting: NotRequired[float]
    sole_voting: NotRequired[float]
    value: NotRequired[float]
