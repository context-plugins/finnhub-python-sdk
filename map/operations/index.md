<!-- Generated file — do not edit; regenerated with the SDK. -->

# Index — operations

Accessor: `client.index` · Source: `finnhub_api/apis/index.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.index.indices_constituents

- **Route**: `GET /index/constituents`
- **Auth**: `api_key`
- **Signature**: `def indices_constituents(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `IndicesConstituents`
- **Returns (raw)**: `ApiResult[IndicesConstituents, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IndicesConstituents` | `finnhub_api/models/indices_constituents.py` |

### client.index.indices_historical_constituents

- **Route**: `GET /index/historical-constituents`
- **Auth**: `api_key`
- **Signature**: `def indices_historical_constituents(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `IndicesHistoricalConstituents`
- **Returns (raw)**: `ApiResult[IndicesHistoricalConstituents, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IndicesHistoricalConstituents` | `finnhub_api/models/indices_historical_constituents.py` |

