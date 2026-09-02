<!-- Generated file — do not edit; regenerated with the SDK. -->

# Crypto — operations

Accessor: `client.crypto` · Source: `finnhub_api/apis/crypto.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.crypto.crypto_candles

- **Route**: `GET /crypto/candle`
- **Auth**: `api_key`
- **Signature**: `def crypto_candles(symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `resolution`, `from_`, `to`
- **Params**: `symbol` — query · `resolution` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `CryptoCandles`
- **Returns (raw)**: `ApiResult[CryptoCandles, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CryptoCandles` | `finnhub_api/models/crypto_candles.py` |

### client.crypto.crypto_exchanges

- **Route**: `GET /crypto/exchange`
- **Auth**: `api_key`
- **Signature**: `def crypto_exchanges(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[str]`
- **Returns (raw)**: `ApiResult[list[str], RawError]`
- **Error**: `RawError` — **Case B**

### client.crypto.crypto_profile

- **Route**: `GET /crypto/profile`
- **Auth**: `api_key`
- **Signature**: `def crypto_profile(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `CryptoProfile`
- **Returns (raw)**: `ApiResult[CryptoProfile, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CryptoProfile` | `finnhub_api/models/crypto_profile.py` |

### client.crypto.crypto_symbols

- **Route**: `GET /crypto/symbol`
- **Auth**: `api_key`
- **Signature**: `def crypto_symbols(exchange: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `exchange`
- **Params**: `exchange` — query
- **Returns (parsed)**: `list[CryptoSymbol]`
- **Returns (raw)**: `ApiResult[list[CryptoSymbol], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CryptoSymbol` | `finnhub_api/models/crypto_symbol.py` |

