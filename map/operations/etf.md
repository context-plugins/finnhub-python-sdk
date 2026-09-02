<!-- Generated file — do not edit; regenerated with the SDK. -->

# Etf — operations

Accessor: `client.etf` · Source: `finnhub_api/apis/etf.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.etf.etfs_allocation

- **Route**: `GET /etf/allocation`
- **Auth**: `api_key`
- **Signature**: `def etfs_allocation(*, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `isin` — query
- **Returns (parsed)**: `EtfsAllocation`
- **Returns (raw)**: `ApiResult[EtfsAllocation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EtfsAllocation` | `finnhub_api/models/etfs_allocation.py` |

### client.etf.etfs_country_exposure

- **Route**: `GET /etf/country`
- **Auth**: `api_key`
- **Signature**: `def etfs_country_exposure(*, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `isin` — query
- **Returns (parsed)**: `EtfsCountryExposure`
- **Returns (raw)**: `ApiResult[EtfsCountryExposure, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EtfsCountryExposure` | `finnhub_api/models/etfs_country_exposure.py` |

### client.etf.etfs_holdings

- **Route**: `GET /etf/holdings`
- **Auth**: `api_key`
- **Signature**: `def etfs_holdings(*, symbol: str | None = None, isin: str | None = None, skip: int | None = None, date: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `isin` — query · `skip` — query · `date` — query
- **Returns (parsed)**: `EtfsHoldings`
- **Returns (raw)**: `ApiResult[EtfsHoldings, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EtfsHoldings` | `finnhub_api/models/etfs_holdings.py` |

### client.etf.etfs_profile

- **Route**: `GET /etf/profile`
- **Auth**: `api_key`
- **Signature**: `def etfs_profile(*, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `isin` — query
- **Returns (parsed)**: `EtfsProfile`
- **Returns (raw)**: `ApiResult[EtfsProfile, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EtfsProfile` | `finnhub_api/models/etfs_profile.py` |

### client.etf.etfs_sector_exposure

- **Route**: `GET /etf/sector`
- **Auth**: `api_key`
- **Signature**: `def etfs_sector_exposure(*, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `isin` — query
- **Returns (parsed)**: `EtfsSectorExposure`
- **Returns (raw)**: `ApiResult[EtfsSectorExposure, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EtfsSectorExposure` | `finnhub_api/models/etfs_sector_exposure.py` |

