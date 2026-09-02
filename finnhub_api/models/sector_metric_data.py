from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SectorMetricData(SdkBaseModel):
    sector: Optional[str] = UNSET
    """Sector"""

    metrics: Optional[Any] = UNSET
    """Metrics data in key-value format. <code>a</code> and <code>m</code> fields are for average and median
    respectively."""


class SectorMetricDataDict(TypedDict):
    sector: NotRequired[str]
    metrics: NotRequired[Any]
