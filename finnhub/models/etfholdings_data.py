from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EtfholdingsData(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol description"""

    name: Optional[str] = UNSET
    """Security name"""

    isin: Optional[str] = UNSET
    """ISIN."""

    cusip: Optional[str] = UNSET
    """CUSIP."""

    share: Optional[float] = UNSET
    """Number of shares owned by the ETF."""

    percent: Optional[float] = UNSET
    """Portfolio's percent"""

    value: Optional[float] = UNSET
    """Market value"""

    asset_type: Optional[str] = Field(default=UNSET, alias="assetType")
    """Asset type. Can be 1 of the following values: <code>Equity</code>, <code>ETP</code>, <code>Fund</code>,
    <code>Bond</code>, <code>Other</code> or empty."""


class EtfholdingsDataDict(TypedDict):
    symbol: NotRequired[str]
    name: NotRequired[str]
    isin: NotRequired[str]
    cusip: NotRequired[str]
    share: NotRequired[float]
    percent: NotRequired[float]
    value: NotRequired[float]
    asset_type: NotRequired[str]
