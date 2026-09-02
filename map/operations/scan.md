<!-- Generated file — do not edit; regenerated with the SDK. -->

# Scan — operations

Accessor: `client.scan` · Source: `finnhub_api/apis/scan.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.scan.aggregate_indicator

- **Route**: `GET /scan/technical-indicator`
- **Auth**: `api_key`
- **Signature**: `def aggregate_indicator(symbol: str, resolution: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `resolution`
- **Params**: `symbol` — query · `resolution` — query
- **Returns (parsed)**: `AggregateIndicators`
- **Returns (raw)**: `ApiResult[AggregateIndicators, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AggregateIndicators` | `finnhub_api/models/aggregate_indicators.py` |

### client.scan.pattern_recognition

- **Route**: `GET /scan/pattern`
- **Auth**: `api_key`
- **Signature**: `def pattern_recognition(symbol: str, resolution: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `resolution`
- **Params**: `symbol` — query · `resolution` — query
- **Returns (parsed)**: `PatternRecognition`
- **Returns (raw)**: `ApiResult[PatternRecognition, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PatternRecognition` | `finnhub_api/models/pattern_recognition.py` |

### client.scan.support_resistance

- **Route**: `GET /scan/support-resistance`
- **Auth**: `api_key`
- **Signature**: `def support_resistance(symbol: str, resolution: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `resolution`
- **Params**: `symbol` — query · `resolution` — query
- **Returns (parsed)**: `SupportResistance`
- **Returns (raw)**: `ApiResult[SupportResistance, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SupportResistance` | `finnhub_api/models/support_resistance.py` |

