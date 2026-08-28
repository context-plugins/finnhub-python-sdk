from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class HistoricalNbbo(SdkBaseModel):
    s: Optional[str] = UNSET
    """Symbol."""

    skip: Optional[int] = UNSET
    """Number of ticks skipped."""

    count: Optional[int] = UNSET
    """Number of ticks returned. If <code>count</code> < <code>limit</code>, all data for that date has been
    returned."""

    total: Optional[int] = UNSET
    """Total number of ticks for that date."""

    av: Optional[list[float]] = UNSET
    """List of Ask volume data."""

    a: Optional[list[float]] = UNSET
    """List of Ask price data."""

    ax: Optional[list[str]] = UNSET
    """List of venues/exchanges - Ask price. A list of exchange codes can be found <a target="_blank"
    href="https://docs.google.com/spreadsheets/d/1Tj53M1svmr-hfEtbk6_NpVR1yAyGLMaH6ByYU6CG0ZY/edit?usp=sharing",>here</a>"""

    bv: Optional[list[float]] = UNSET
    """List of Bid volume data."""

    b: Optional[list[float]] = UNSET
    """List of Bid price data."""

    bx: Optional[list[str]] = UNSET
    """List of venues/exchanges - Bid price. A list of exchange codes can be found <a target="_blank"
    href="https://docs.google.com/spreadsheets/d/1Tj53M1svmr-hfEtbk6_NpVR1yAyGLMaH6ByYU6CG0ZY/edit?usp=sharing",>here</a>"""

    t: Optional[list[int]] = UNSET
    """List of timestamp in UNIX ms."""

    c: Optional[list[list[str]]] = UNSET
    """List of quote conditions. A comprehensive list of quote conditions code can be found <a target="_blank"
    href="https://docs.google.com/spreadsheets/d/1iiA6e7Osdtai0oPMOUzgAIKXCsay89dFDmsegz6OpEg/edit?usp=sharing">here</a>"""


class HistoricalNbboDict(TypedDict):
    s: NotRequired[str]
    skip: NotRequired[int]
    count: NotRequired[int]
    total: NotRequired[int]
    av: NotRequired[list[float]]
    a: NotRequired[list[float]]
    ax: NotRequired[list[str]]
    bv: NotRequired[list[float]]
    b: NotRequired[list[float]]
    bx: NotRequired[list[str]]
    t: NotRequired[list[int]]
    c: NotRequired[list[list[str]]]
