from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class Dividends(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol."""

    date: Optional[Date] = UNSET
    """Ex-Dividend date."""

    amount: Optional[float] = UNSET
    """Amount in local currency."""

    adjusted_amount: Optional[float] = Field(default=UNSET, alias="adjustedAmount")
    """Adjusted dividend."""

    pay_date: Optional[Date] = Field(default=UNSET, alias="payDate")
    """Pay date."""

    record_date: Optional[Date] = Field(default=UNSET, alias="recordDate")
    """Record date."""

    declaration_date: Optional[Date] = Field(default=UNSET, alias="declarationDate")
    """Declaration date."""

    currency: Optional[str] = UNSET
    """Currency."""

    freq: Optional[str] = UNSET
    """<p>Dividend frequency. Can be 1 of the following values:</p><ul> <li><code>0: Annually</code></li> <li><code>1:
    Monthly</code></li> <li><code>2: Quarterly</code></li> <li><code>3: Semi-annually</code></li> <li><code>4:
    Other/Unknown</code></li> <li><code>5: Bimonthly</code></li> <li><code>6: Trimesterly</code></li> <li><code>7:
    Weekly</code></li> </ul>"""


class DividendsDict(TypedDict):
    symbol: NotRequired[str]
    date: NotRequired[Date]
    amount: NotRequired[float]
    adjusted_amount: NotRequired[float]
    pay_date: NotRequired[Date]
    record_date: NotRequired[Date]
    declaration_date: NotRequired[Date]
    currency: NotRequired[str]
    freq: NotRequired[str]
