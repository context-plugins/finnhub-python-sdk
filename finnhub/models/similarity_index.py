from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .similarity_index_info import SimilarityIndexInfo, SimilarityIndexInfoDict


class SimilarityIndex(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """Symbol."""

    cik: Optional[str] = UNSET
    """CIK."""

    similarity: Optional[list[SimilarityIndexInfo]] = UNSET
    """Array of filings with its cosine similarity compared to the same report of the previous year."""


class SimilarityIndexDict(TypedDict):
    symbol: NotRequired[str]
    cik: NotRequired[str]
    similarity: NotRequired[list[SimilarityIndexInfo | SimilarityIndexInfoDict]]
