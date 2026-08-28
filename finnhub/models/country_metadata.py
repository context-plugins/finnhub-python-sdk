from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CountryMetadata(SdkBaseModel):
    country: Optional[str] = UNSET
    """Country name"""

    code2: Optional[str] = UNSET
    """Alpha 2 code"""

    code3: Optional[str] = UNSET
    """Alpha 3 code"""

    code_no: Optional[str] = Field(default=UNSET, alias="codeNo")
    """UN code"""

    currency: Optional[str] = UNSET
    """Currency name"""

    currency_code: Optional[str] = Field(default=UNSET, alias="currencyCode")
    """Currency code"""

    region: Optional[str] = UNSET
    """Region"""

    sub_region: Optional[str] = Field(default=UNSET, alias="subRegion")
    """Sub-Region"""

    rating: Optional[str] = UNSET
    """Moody's credit risk rating."""

    default_spread: Optional[float] = Field(default=UNSET, alias="defaultSpread")
    """Default spread"""

    country_risk_premium: Optional[float] = Field(default=UNSET, alias="countryRiskPremium")
    """Country risk premium"""

    equity_risk_premium: Optional[float] = Field(default=UNSET, alias="equityRiskPremium")
    """Equity risk premium"""

    logo: Optional[str] = UNSET
    """Flag image"""


class CountryMetadataDict(TypedDict):
    country: NotRequired[str]
    code2: NotRequired[str]
    code3: NotRequired[str]
    code_no: NotRequired[str]
    currency: NotRequired[str]
    currency_code: NotRequired[str]
    region: NotRequired[str]
    sub_region: NotRequired[str]
    rating: NotRequired[str]
    default_spread: NotRequired[float]
    country_risk_premium: NotRequired[float]
    equity_risk_premium: NotRequired[float]
    logo: NotRequired[str]
