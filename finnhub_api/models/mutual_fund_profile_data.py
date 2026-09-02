from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class MutualFundProfileData(SdkBaseModel):
    name: Optional[str] = UNSET
    """Name"""

    category: Optional[str] = UNSET
    """Fund's category."""

    investment_segment: Optional[str] = Field(default=UNSET, alias="investmentSegment")
    """Investment Segment."""

    total_nav: Optional[float] = Field(default=UNSET, alias="totalNav")
    """NAV."""

    expense_ratio: Optional[float] = Field(default=UNSET, alias="expenseRatio")
    """Expense ratio."""

    benchmark: Optional[str] = UNSET
    """Index benchmark."""

    inception_date: Optional[Date] = Field(default=UNSET, alias="inceptionDate")
    """Inception date."""

    description: Optional[str] = UNSET
    """Fund's description."""

    fund_family: Optional[str] = Field(default=UNSET, alias="fundFamily")
    """Fund Family."""

    fund_company: Optional[str] = Field(default=UNSET, alias="fundCompany")
    """Fund Company."""

    manager: Optional[str] = UNSET
    """Fund's managers."""

    status: Optional[str] = UNSET
    """Status."""

    beta: Optional[float] = UNSET
    """Beta."""

    deferred_load: Optional[float] = Field(default=UNSET, alias="deferredLoad")
    """Deferred load."""

    fee12b1: Optional[float] = UNSET
    """12B-1 fee."""

    front_load: Optional[float] = Field(default=UNSET, alias="frontLoad")
    """Front Load."""

    ira_min_investment: Optional[float] = Field(default=UNSET, alias="iraMinInvestment")
    """IRA minimum investment."""

    isin: Optional[str] = UNSET
    """ISIN."""

    cusip: Optional[str] = UNSET
    """CUSIP."""

    max_redemption_fee: Optional[float] = Field(default=UNSET, alias="maxRedemptionFee")
    """Max redemption fee."""

    standard_min_investment: Optional[float] = Field(default=UNSET, alias="standardMinInvestment")
    """Minimum investment for standard accounts."""

    turnover: Optional[float] = UNSET
    """Turnover."""

    series_id: Optional[str] = Field(default=UNSET, alias="seriesId")
    """Fund's series ID. This field can be used to group multiple share classes into 1 unique fund."""

    series_name: Optional[str] = Field(default=UNSET, alias="seriesName")
    """Fund's series name."""

    class_id: Optional[str] = Field(default=UNSET, alias="classId")
    """Class ID."""

    class_name: Optional[str] = Field(default=UNSET, alias="className")
    """Class name."""

    sfdr_classification: Optional[str] = Field(default=UNSET, alias="sfdrClassification")
    """SFDR classification for EU funds. Under the new classifications, a fund's strategy will labeled under either
    Article 6, 8 or 9. Article 6 covers funds which do not integrate any kind of sustainability into the investment
    process. Article 8, also known as ‘environmental and socially promoting’, applies “… where a financial product
    promotes, among other characteristics, environmental or social characteristics, or a combination of those
    characteristics, provided that the companies in which the investments are made follow good governance practices.”.
    Article 9, also known as ‘products targeting sustainable investments’, covers products targeting bespoke sustainable
    investments and applies “… where a financial product has sustainable investment as its objective and an index has
    been designated as a reference benchmark.”"""

    currency: Optional[str] = UNSET
    """Fund's currency"""


class MutualFundProfileDataDict(TypedDict):
    name: NotRequired[str]
    category: NotRequired[str]
    investment_segment: NotRequired[str]
    total_nav: NotRequired[float]
    expense_ratio: NotRequired[float]
    benchmark: NotRequired[str]
    inception_date: NotRequired[Date]
    description: NotRequired[str]
    fund_family: NotRequired[str]
    fund_company: NotRequired[str]
    manager: NotRequired[str]
    status: NotRequired[str]
    beta: NotRequired[float]
    deferred_load: NotRequired[float]
    fee12b1: NotRequired[float]
    front_load: NotRequired[float]
    ira_min_investment: NotRequired[float]
    isin: NotRequired[str]
    cusip: NotRequired[str]
    max_redemption_fee: NotRequired[float]
    standard_min_investment: NotRequired[float]
    turnover: NotRequired[float]
    series_id: NotRequired[str]
    series_name: NotRequired[str]
    class_id: NotRequired[str]
    class_name: NotRequired[str]
    sfdr_classification: NotRequired[str]
    currency: NotRequired[str]
