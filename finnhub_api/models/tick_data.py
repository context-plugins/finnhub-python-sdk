from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TickData(SdkBaseModel):
    s: Optional[str] = UNSET
    """Symbol."""

    skip: Optional[int] = UNSET
    """Number of ticks skipped."""

    count: Optional[int] = UNSET
    """Number of ticks returned. If <code>count</code> < <code>limit</code>, all data for that date has been
    returned."""

    total: Optional[int] = UNSET
    """Total number of ticks for that date."""

    v: Optional[list[float]] = UNSET
    """List of volume data."""

    p: Optional[list[float]] = UNSET
    """List of price data."""

    t: Optional[list[int]] = UNSET
    """List of timestamp in UNIX ms."""

    x: Optional[list[str]] = UNSET
    """List of venues/exchanges. A list of exchange codes can be found <a target="_blank"
    href="https://docs.google.com/spreadsheets/d/1Tj53M1svmr-hfEtbk6_NpVR1yAyGLMaH6ByYU6CG0ZY/edit?usp=sharing",>here</a>"""

    c: Optional[list[list[str]]] = UNSET
    """List of trade conditions. A comprehensive list of trade conditions code can be found <a target="_blank"
    href="https://docs.google.com/spreadsheets/d/1PUxiSWPHSODbaTaoL2Vef6DgU-yFtlRGZf19oBb9Hp0/edit?usp=sharing">here</a>"""


class TickDataDict(TypedDict):
    s: NotRequired[str]
    skip: NotRequired[int]
    count: NotRequired[int]
    total: NotRequired[int]
    v: NotRequired[list[float]]
    p: NotRequired[list[float]]
    t: NotRequired[list[int]]
    x: NotRequired[list[str]]
    c: NotRequired[list[list[str]]]
