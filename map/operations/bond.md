<!-- Generated file — do not edit; regenerated with the SDK. -->

# Bond — operations

Accessor: `client.bond` · Source: `finnhub_api/apis/bond.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.bond.bond_price

- **Route**: `GET /bond/price`
- **Auth**: `api_key`
- **Signature**: `def bond_price(isin: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `isin`, `from_`, `to`
- **Params**: `isin` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `BondCandles`
- **Returns (raw)**: `ApiResult[BondCandles, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BondCandles` | `finnhub_api/models/bond_candles.py` |

### client.bond.bond_profile

- **Route**: `GET /bond/profile`
- **Auth**: `api_key`
- **Signature**: `def bond_profile(*, isin: str | None = None, cusip: str | None = None, figi: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `isin` — query · `cusip` — query · `figi` — query
- **Returns (parsed)**: `BondProfile`
- **Returns (raw)**: `ApiResult[BondProfile, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BondProfile` | `finnhub_api/models/bond_profile.py` |

### client.bond.bond_tick

- **Route**: `GET /bond/tick`
- **Auth**: `api_key`
- **Signature**: `def bond_tick(isin: str, date: Date, limit: int, skip: int, exchange: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `isin`, `date`, `limit`, `skip`, `exchange`
- **Params**: `isin` — query · `date` — query · `limit` — query · `skip` — query · `exchange` — query
- **Returns (parsed)**: `BondTickData`
- **Returns (raw)**: `ApiResult[BondTickData, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BondTickData` | `finnhub_api/models/bond_tick_data.py` |

### client.bond.bond_yield_curve

- **Route**: `GET /bond/yield-curve`
- **Auth**: `api_key`
- **Signature**: `def bond_yield_curve(code: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `code`
- **Params**: `code` — query
- **Returns (parsed)**: `BondYieldCurve`
- **Returns (raw)**: `ApiResult[BondYieldCurve, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BondYieldCurve` | `finnhub_api/models/bond_yield_curve.py` |

