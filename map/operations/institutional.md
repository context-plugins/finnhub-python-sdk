<!-- Generated file — do not edit; regenerated with the SDK. -->

# Institutional — operations

Accessor: `client.institutional` · Source: `finnhub_api/apis/institutional.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.institutional.institutional_ownership

- **Route**: `GET /institutional/ownership`
- **Auth**: `api_key`
- **Signature**: `def institutional_ownership(symbol: str, cusip: str, from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `cusip`, `from_`, `to`
- **Params**: `symbol` — query · `cusip` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `InstitutionalOwnership`
- **Returns (raw)**: `ApiResult[InstitutionalOwnership, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InstitutionalOwnership` | `finnhub_api/models/institutional_ownership.py` |

### client.institutional.institutional_portfolio

- **Route**: `GET /institutional/portfolio`
- **Auth**: `api_key`
- **Signature**: `def institutional_portfolio(cik: str, from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `cik`, `from_`, `to`
- **Params**: `cik` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `InstitutionalPortfolio`
- **Returns (raw)**: `ApiResult[InstitutionalPortfolio, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InstitutionalPortfolio` | `finnhub_api/models/institutional_portfolio.py` |

### client.institutional.institutional_profile

- **Route**: `GET /institutional/profile`
- **Auth**: `api_key`
- **Signature**: `def institutional_profile(*, cik: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `cik` — query
- **Returns (parsed)**: `InstitutionalProfile`
- **Returns (raw)**: `ApiResult[InstitutionalProfile, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InstitutionalProfile` | `finnhub_api/models/institutional_profile.py` |

