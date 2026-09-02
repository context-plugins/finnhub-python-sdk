<!-- Generated file — do not edit; regenerated with the SDK. -->

# CorporateActions — operations

Accessor: `client.corporate_actions` · Source: `finnhub_api/apis/corporate_actions.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.corporate_actions.isin_change

- **Route**: `GET /ca/isin-change`
- **Auth**: `api_key`
- **Signature**: `def isin_change(from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `from_`, `to`
- **Params**: `from_` — query `from` · `to` — query
- **Returns (parsed)**: `IsinChange`
- **Returns (raw)**: `ApiResult[IsinChange, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IsinChange` | `finnhub_api/models/isin_change.py` |

### client.corporate_actions.symbol_change

- **Route**: `GET /ca/symbol-change`
- **Auth**: `api_key`
- **Signature**: `def symbol_change(from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `from_`, `to`
- **Params**: `from_` — query `from` · `to` — query
- **Returns (parsed)**: `SymbolChange`
- **Returns (raw)**: `ApiResult[SymbolChange, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SymbolChange` | `finnhub_api/models/symbol_change.py` |

