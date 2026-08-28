from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class KeyCustomersSuppliers(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol"""

    name: Optional[str] = UNSET
    """Name"""

    country: Optional[str] = UNSET
    """Country"""

    industry: Optional[str] = UNSET
    """Industry"""

    customer: Optional[bool] = UNSET
    """Whether the company is a customer."""

    supplier: Optional[bool] = UNSET
    """Whether the company is a supplier"""

    one_month_correlation: Optional[float] = Field(default=UNSET, alias="oneMonthCorrelation")
    """1-month price correlation"""

    one_year_correlation: Optional[float] = Field(default=UNSET, alias="oneYearCorrelation")
    """1-year price correlation"""

    six_month_correlation: Optional[float] = Field(default=UNSET, alias="sixMonthCorrelation")
    """6-month price correlation"""

    three_month_correlation: Optional[float] = Field(default=UNSET, alias="threeMonthCorrelation")
    """3-month price correlation"""

    two_week_correlation: Optional[float] = Field(default=UNSET, alias="twoWeekCorrelation")
    """2-week price correlation"""

    two_year_correlation: Optional[float] = Field(default=UNSET, alias="twoYearCorrelation")
    """2-year price correlation"""


class KeyCustomersSuppliersDict(TypedDict):
    symbol: NotRequired[str]
    name: NotRequired[str]
    country: NotRequired[str]
    industry: NotRequired[str]
    customer: NotRequired[bool]
    supplier: NotRequired[bool]
    one_month_correlation: NotRequired[float]
    one_year_correlation: NotRequired[float]
    six_month_correlation: NotRequired[float]
    three_month_correlation: NotRequired[float]
    two_week_correlation: NotRequired[float]
    two_year_correlation: NotRequired[float]
