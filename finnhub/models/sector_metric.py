from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sector_metric_data import SectorMetricData, SectorMetricDataDict


class SectorMetric(SdkBaseModel):
    region: Optional[str] = UNSET
    """Region."""

    data: Optional[list[SectorMetricData]] = UNSET
    """Metrics for each sector."""


class SectorMetricDict(TypedDict):
    region: NotRequired[str]
    data: NotRequired[list[SectorMetricData | SectorMetricDataDict]]
