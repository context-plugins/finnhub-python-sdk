from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LobbyingData(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol."""

    name: Optional[str] = UNSET
    """Company's name."""

    description: Optional[str] = UNSET
    """Description."""

    country: Optional[str] = UNSET
    """Country."""

    year: Optional[int] = UNSET
    """Year."""

    period: Optional[str] = UNSET
    """Period."""

    income: Optional[float] = UNSET
    """Income reported by lobbying firms."""

    expenses: Optional[float] = UNSET
    """Expenses reported by the company."""

    document_url: Optional[str] = Field(default=UNSET, alias="documentUrl")
    """Document's URL."""

    posted_name: Optional[str] = Field(default=UNSET, alias="postedName")
    """Posted name."""

    date: Optional[str] = UNSET
    """Date."""

    client_id: Optional[str] = Field(default=UNSET, alias="clientId")
    """Client ID."""

    registrant_id: Optional[str] = Field(default=UNSET, alias="registrantId")
    """Registrant ID."""

    senate_id: Optional[str] = Field(default=UNSET, alias="senateId")
    """Senate ID."""

    houseregistrant_id: Optional[str] = Field(default=UNSET, alias="houseregistrantId")
    """House registrant ID."""


class LobbyingDataDict(TypedDict):
    symbol: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str]
    country: NotRequired[str]
    year: NotRequired[int]
    period: NotRequired[str]
    income: NotRequired[float]
    expenses: NotRequired[float]
    document_url: NotRequired[str]
    posted_name: NotRequired[str]
    date: NotRequired[str]
    client_id: NotRequired[str]
    registrant_id: NotRequired[str]
    senate_id: NotRequired[str]
    houseregistrant_id: NotRequired[str]
