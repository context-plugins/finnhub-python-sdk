<!-- Generated file — do not edit; regenerated with the SDK. -->

# Economic — operations

Accessor: `client.economic` · Source: `finnhub_api/apis/economic.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.economic.economic_code

- **Route**: `GET /economic/code`
- **Auth**: `api_key`
- **Signature**: `def economic_code(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[EconomicCode]`
- **Returns (raw)**: `ApiResult[list[EconomicCode], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EconomicCode` | `finnhub_api/models/economic_code.py` |

### client.economic.economic_data

- **Route**: `GET /economic`
- **Auth**: `api_key`
- **Signature**: `def economic_data(code: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `code`
- **Params**: `code` — query
- **Returns (parsed)**: `EconomicData`
- **Returns (raw)**: `ApiResult[EconomicData, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EconomicData` | `finnhub_api/models/economic_data.py` |

