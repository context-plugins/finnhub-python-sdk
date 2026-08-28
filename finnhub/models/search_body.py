from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SearchBody(SdkBaseModel):
    query: str
    """Search query"""

    isins: Optional[str] = UNSET
    """List of isin to search, comma separated (Max: 50)."""

    cusips: Optional[str] = UNSET
    """List of cusip to search, comma separated (Max: 50)."""

    ciks: Optional[str] = UNSET
    """List of SEC Center Index Key to search, comma separated (Max: 50)."""

    sedar_ids: Optional[str] = Field(default=UNSET, alias="sedarIds")
    """List of SEDAR issuer number to search, comma separated (Max: 50)."""

    ch_ids: Optional[str] = Field(default=UNSET, alias="chIds")
    """List of Companies House number to search, comma separated (Max: 50)."""

    symbols: Optional[str] = UNSET
    """List of symbols to search, comma separated (Max: 50)."""

    sedols: Optional[str] = UNSET
    """List of sedols to search, comma separated (Max: 50)."""

    sources: Optional[str] = UNSET
    """List of sources to search, comma separated (Max: 50). Look at <code>/filter</code> endpoint to see all available
    values."""

    forms: Optional[str] = UNSET
    """List of forms to search, comma separated (Max: 50). Look at <code>/filter</code> endpoint to see all available
    values."""

    gics: Optional[str] = UNSET
    """List of gics to search, comma separated (Max: 50). Look at <code>/filter</code> endpoint to see all available
    values."""

    naics: Optional[str] = UNSET
    """List of sources to search, comma separated (Max: 50). Look at <code>/filter</code> endpoint to see all available
    values."""

    exhibits: Optional[str] = UNSET
    """List of exhibits to search, comma separated (Max: 50). Look at <code>/filter</code> endpoint to see all available
    values."""

    exchanges: Optional[str] = UNSET
    """List of exchanges to search, comma separated (Max: 50). Look at <code>/filter</code> endpoint to see all
    available values."""

    countries: Optional[str] = UNSET
    """List of sources to search, comma separated (Max: 50). Look at <code>/filter</code> endpoint to see all available
    values."""

    acts: Optional[str] = UNSET
    """List of SEC's exchanges act to search, comma separated. Look at <code>/filter</code> endpoint to see all
    available values."""

    caps: Optional[str] = UNSET
    """List of market capitalization to search, comma separated. Look at <code>/filter</code> endpoint to see all
    available values."""

    from_date: Optional[str] = Field(default=UNSET, alias="fromDate")
    """Search from date in format: YYYY-MM-DD, default from the last 2 years"""

    to_date: Optional[str] = Field(default=UNSET, alias="toDate")
    """Search to date in format: YYYY-MM-DD, default to today"""

    page: Optional[str] = UNSET
    """Use for pagination, default to page 1"""

    sort: Optional[str] = UNSET
    """Sort result by, default: sortMostRecent. Look at <code>/filter</code> endpoint to see all available values."""

    highlighted: Optional[bool] = UNSET
    """Enable highlight in returned filings. If enabled, only return 10 results each time"""


class SearchBodyDict(TypedDict):
    query: str
    isins: NotRequired[str]
    cusips: NotRequired[str]
    ciks: NotRequired[str]
    sedar_ids: NotRequired[str]
    ch_ids: NotRequired[str]
    symbols: NotRequired[str]
    sedols: NotRequired[str]
    sources: NotRequired[str]
    forms: NotRequired[str]
    gics: NotRequired[str]
    naics: NotRequired[str]
    exhibits: NotRequired[str]
    exchanges: NotRequired[str]
    countries: NotRequired[str]
    acts: NotRequired[str]
    caps: NotRequired[str]
    from_date: NotRequired[str]
    to_date: NotRequired[str]
    page: NotRequired[str]
    sort: NotRequired[str]
    highlighted: NotRequired[bool]
