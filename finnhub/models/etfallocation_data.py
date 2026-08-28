from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EtfallocationData(SdkBaseModel):
    large_blend: Optional[float] = Field(default=UNSET, alias="largeBlend")
    """Percentage of stocks classified as Large Blend."""

    large_growth: Optional[float] = Field(default=UNSET, alias="largeGrowth")
    """Percentage of stocks classified as Large Growth."""

    large_value: Optional[float] = Field(default=UNSET, alias="largeValue")
    """Percentage of stocks classified as Large Value."""

    mid_blend: Optional[float] = Field(default=UNSET, alias="midBlend")
    """Percentage of stocks classified as Mid-cap Blend."""

    mid_growth: Optional[float] = Field(default=UNSET, alias="midGrowth")
    """Percentage of stocks classified as Mid-cap Growth."""

    mid_value: Optional[float] = Field(default=UNSET, alias="midValue")
    """Percentage of stocks classified as Mid-cap Value."""

    small_blend: Optional[float] = Field(default=UNSET, alias="smallBlend")
    """Percentage of stocks classified as Small-cap Blend."""

    small_growth: Optional[float] = Field(default=UNSET, alias="smallGrowth")
    """Percentage of stocks classified as Small-cap Growth."""

    small_value: Optional[float] = Field(default=UNSET, alias="smallValue")
    """Percentage of stocks classified as Small-cap Value."""


class EtfallocationDataDict(TypedDict):
    large_blend: NotRequired[float]
    large_growth: NotRequired[float]
    large_value: NotRequired[float]
    mid_blend: NotRequired[float]
    mid_growth: NotRequired[float]
    mid_value: NotRequired[float]
    small_blend: NotRequired[float]
    small_growth: NotRequired[float]
    small_value: NotRequired[float]
