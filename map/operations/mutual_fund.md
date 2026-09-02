<!-- Generated file — do not edit; regenerated with the SDK. -->

# MutualFund — operations

Accessor: `client.mutual_fund` · Source: `finnhub_api/apis/mutual_fund.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.mutual_fund.mutual_fund_country_exposure

- **Route**: `GET /mutual-fund/country`
- **Auth**: `api_key`
- **Signature**: `def mutual_fund_country_exposure(*, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `isin` — query
- **Returns (parsed)**: `MutualFundCountryExposure`
- **Returns (raw)**: `ApiResult[MutualFundCountryExposure, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MutualFundCountryExposure` | `finnhub_api/models/mutual_fund_country_exposure.py` |

### client.mutual_fund.mutual_fund_eet

- **Route**: `GET /mutual-fund/eet`
- **Auth**: `api_key`
- **Signature**: `def mutual_fund_eet(isin: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `isin`
- **Params**: `isin` — query
- **Returns (parsed)**: `MutualFundEet`
- **Returns (raw)**: `ApiResult[MutualFundEet, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MutualFundEet` | `finnhub_api/models/mutual_fund_eet.py` |

### client.mutual_fund.mutual_fund_eet_pai

- **Route**: `GET /mutual-fund/eet-pai`
- **Auth**: `api_key`
- **Signature**: `def mutual_fund_eet_pai(isin: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `isin`
- **Params**: `isin` — query
- **Returns (parsed)**: `MutualFundEetPai`
- **Returns (raw)**: `ApiResult[MutualFundEetPai, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MutualFundEetPai` | `finnhub_api/models/mutual_fund_eet_pai.py` |

### client.mutual_fund.mutual_fund_holdings

- **Route**: `GET /mutual-fund/holdings`
- **Auth**: `api_key`
- **Signature**: `def mutual_fund_holdings(*, symbol: str | None = None, isin: str | None = None, skip: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `isin` — query · `skip` — query
- **Returns (parsed)**: `MutualFundHoldings`
- **Returns (raw)**: `ApiResult[MutualFundHoldings, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MutualFundHoldings` | `finnhub_api/models/mutual_fund_holdings.py` |

### client.mutual_fund.mutual_fund_profile

- **Route**: `GET /mutual-fund/profile`
- **Auth**: `api_key`
- **Signature**: `def mutual_fund_profile(*, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `isin` — query
- **Returns (parsed)**: `MutualFundProfile`
- **Returns (raw)**: `ApiResult[MutualFundProfile, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MutualFundProfile` | `finnhub_api/models/mutual_fund_profile.py` |

### client.mutual_fund.mutual_fund_sector_exposure

- **Route**: `GET /mutual-fund/sector`
- **Auth**: `api_key`
- **Signature**: `def mutual_fund_sector_exposure(*, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `isin` — query
- **Returns (parsed)**: `MutualFundSectorExposure`
- **Returns (raw)**: `ApiResult[MutualFundSectorExposure, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MutualFundSectorExposure` | `finnhub_api/models/mutual_fund_sector_exposure.py` |

