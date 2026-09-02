<!-- Generated file — do not edit; regenerated with the SDK. -->

# Forex — operations

Accessor: `client.forex` · Source: `finnhub_api/apis/forex.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.forex.forex_candles

- **Route**: `GET /forex/candle`
- **Auth**: `api_key`
- **Signature**: `def forex_candles(symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `resolution`, `from_`, `to`
- **Params**: `symbol` — query · `resolution` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `ForexCandles`
- **Returns (raw)**: `ApiResult[ForexCandles, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ForexCandles` | `finnhub_api/models/forex_candles.py` |

### client.forex.forex_exchanges

- **Route**: `GET /forex/exchange`
- **Auth**: `api_key`
- **Signature**: `def forex_exchanges(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[str]`
- **Returns (raw)**: `ApiResult[list[str], RawError]`
- **Error**: `RawError` — **Case B**

### client.forex.forex_rates

- **Route**: `GET /forex/rates`
- **Auth**: `api_key`
- **Signature**: `def forex_rates(*, base: str | None = None, date: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `base` — query · `date` — query
- **Returns (parsed)**: `Forexrates`
- **Returns (raw)**: `ApiResult[Forexrates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Forexrates` | `finnhub_api/models/forexrates.py` |

### client.forex.forex_symbols

- **Route**: `GET /forex/symbol`
- **Auth**: `api_key`
- **Signature**: `def forex_symbols(exchange: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `exchange`
- **Params**: `exchange` — query
- **Returns (parsed)**: `list[ForexSymbol]`
- **Returns (raw)**: `ApiResult[list[ForexSymbol], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ForexSymbol` | `finnhub_api/models/forex_symbol.py` |

