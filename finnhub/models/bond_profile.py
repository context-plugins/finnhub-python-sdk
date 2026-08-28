from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BondProfile(SdkBaseModel):
    isin: Optional[str] = UNSET
    """ISIN."""

    cusip: Optional[str] = UNSET
    """Cusip."""

    figi: Optional[str] = UNSET
    """FIGI."""

    coupon: Optional[float] = UNSET
    """Coupon."""

    maturity_date: Optional[str] = Field(default=UNSET, alias="maturityDate")
    """Period."""

    offering_price: Optional[float] = Field(default=UNSET, alias="offeringPrice")
    """Offering price."""

    issue_date: Optional[str] = Field(default=UNSET, alias="issueDate")
    """Issue date."""

    bond_type: Optional[str] = Field(default=UNSET, alias="bondType")
    """Bond type."""

    debt_type: Optional[str] = Field(default=UNSET, alias="debtType")
    """Bond type."""

    industry_group: Optional[str] = Field(default=UNSET, alias="industryGroup")
    """Industry."""

    industry_sub_group: Optional[str] = Field(default=UNSET, alias="industrySubGroup")
    """Sub-Industry."""

    asset: Optional[str] = UNSET
    """Asset."""

    asset_type: Optional[str] = Field(default=UNSET, alias="assetType")
    """Asset."""

    dated_date: Optional[str] = Field(default=UNSET, alias="datedDate")
    """Dated date."""

    first_coupon_date: Optional[str] = Field(default=UNSET, alias="firstCouponDate")
    """First coupon date."""

    original_offering: Optional[float] = Field(default=UNSET, alias="originalOffering")
    """Offering amount."""

    amount_outstanding: Optional[float] = Field(default=UNSET, alias="amountOutstanding")
    """Outstanding amount."""

    payment_frequency: Optional[str] = Field(default=UNSET, alias="paymentFrequency")
    """Payment frequency."""

    security_level: Optional[str] = Field(default=UNSET, alias="securityLevel")
    """Security level."""

    callable: Optional[bool] = UNSET
    """Callable."""

    coupon_type: Optional[str] = Field(default=UNSET, alias="couponType")
    """Coupon type."""


class BondProfileDict(TypedDict):
    isin: NotRequired[str]
    cusip: NotRequired[str]
    figi: NotRequired[str]
    coupon: NotRequired[float]
    maturity_date: NotRequired[str]
    offering_price: NotRequired[float]
    issue_date: NotRequired[str]
    bond_type: NotRequired[str]
    debt_type: NotRequired[str]
    industry_group: NotRequired[str]
    industry_sub_group: NotRequired[str]
    asset: NotRequired[str]
    asset_type: NotRequired[str]
    dated_date: NotRequired[str]
    first_coupon_date: NotRequired[str]
    original_offering: NotRequired[float]
    amount_outstanding: NotRequired[float]
    payment_frequency: NotRequired[str]
    security_level: NotRequired[str]
    callable: NotRequired[bool]
    coupon_type: NotRequired[str]
