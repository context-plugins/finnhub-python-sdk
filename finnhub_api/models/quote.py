from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Quote(SdkBaseModel):
    o: Optional[float] = UNSET
    """Open price of the day"""

    h: Optional[float] = UNSET
    """High price of the day"""

    l_: Optional[float] = Field(default=UNSET, alias="l")
    """Low price of the day"""

    c: Optional[float] = UNSET
    """Current price"""

    pc: Optional[float] = UNSET
    """Previous close price"""

    d: Optional[float] = UNSET
    """Change"""

    dp: Optional[float] = UNSET
    """Percent change"""


class QuoteDict(TypedDict):
    o: NotRequired[float]
    h: NotRequired[float]
    l_: NotRequired[float]
    c: NotRequired[float]
    pc: NotRequired[float]
    d: NotRequired[float]
    dp: NotRequired[float]
