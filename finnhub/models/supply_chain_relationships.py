from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .key_customers_suppliers import KeyCustomersSuppliers, KeyCustomersSuppliersDict


class SupplyChainRelationships(SdkBaseModel):
    symbol: Optional[str] = UNSET
    """symbol"""

    data: Optional[list[KeyCustomersSuppliers]] = UNSET
    """Key customers and suppliers."""


class SupplyChainRelationshipsDict(TypedDict):
    symbol: NotRequired[str]
    data: NotRequired[list[KeyCustomersSuppliers | KeyCustomersSuppliersDict]]
