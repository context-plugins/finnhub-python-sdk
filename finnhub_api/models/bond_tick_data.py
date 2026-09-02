from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BondTickData(SdkBaseModel):
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

    y: Optional[list[float]] = UNSET
    """List of yield data."""

    t: Optional[list[int]] = UNSET
    """List of timestamp in UNIX ms."""

    si: Optional[list[str]] = UNSET
    """List of values showing the side (Buy/sell) of each trade. List of supported values: <a target="_blank"
    href="https://docs.google.com/spreadsheets/d/1O3aueXSPOqo7Iuyz4PqDG6yZunHsX8BTefZ2kFk5pz4/edit?usp=sharing",>here</a>"""

    cp: Optional[list[str]] = UNSET
    """List of values showing the counterparty of each trade. List of supported values: <a target="_blank"
    href="https://docs.google.com/spreadsheets/d/1O3aueXSPOqo7Iuyz4PqDG6yZunHsX8BTefZ2kFk5pz4/edit?usp=sharing",>here</a>"""

    rp: Optional[list[str]] = UNSET
    """List of values showing the reporting party of each trade. List of supported values: <a target="_blank"
    href="https://docs.google.com/spreadsheets/d/1O3aueXSPOqo7Iuyz4PqDG6yZunHsX8BTefZ2kFk5pz4/edit?usp=sharing",>here</a>"""

    ats: Optional[list[str]] = UNSET
    """ATS flag. Y or empty"""

    c: Optional[list[list[str]]] = UNSET
    """List of trade conditions. A comprehensive list of trade conditions code can be found <a target="_blank"
    href="https://docs.google.com/spreadsheets/d/1O3aueXSPOqo7Iuyz4PqDG6yZunHsX8BTefZ2kFk5pz4/edit?usp=sharing">here</a>"""


class BondTickDataDict(TypedDict):
    skip: NotRequired[int]
    count: NotRequired[int]
    total: NotRequired[int]
    v: NotRequired[list[float]]
    p: NotRequired[list[float]]
    y: NotRequired[list[float]]
    t: NotRequired[list[int]]
    si: NotRequired[list[str]]
    cp: NotRequired[list[str]]
    rp: NotRequired[list[str]]
    ats: NotRequired[list[str]]
    c: NotRequired[list[list[str]]]
