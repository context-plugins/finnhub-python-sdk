<!-- Generated file — do not edit; regenerated with the SDK. -->

# Misc — operations

Accessor: `client.misc` · Source: `finnhub_api/apis/misc.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.misc.ai_chat

- **Route**: `POST /ai-chat`
- **Auth**: `api_key`
- **Signature**: `def ai_chat(*, search: AichatBody | AichatBodyDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `search` — JSON body
- **Returns (parsed)**: `AichatResponse`
- **Returns (raw)**: `ApiResult[AichatResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AichatBody` | `finnhub_api/models/aichat_body.py` |
| `AichatBodyDict` | `finnhub_api/models/aichat_body.py` |
| `AichatResponse` | `finnhub_api/models/aichat_response.py` |

### client.misc.airline_price_index

- **Route**: `GET /airline/price-index`
- **Auth**: `api_key`
- **Signature**: `def airline_price_index(airline: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `airline`, `from_`, `to`
- **Params**: `airline` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `AirlinePriceIndexData`
- **Returns (raw)**: `ApiResult[AirlinePriceIndexData, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AirlinePriceIndexData` | `finnhub_api/models/airline_price_index_data.py` |

### client.misc.bank_branch

- **Route**: `GET /bank-branch`
- **Auth**: `api_key`
- **Signature**: `def bank_branch(symbol: Any, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `BankBranchRes`
- **Returns (raw)**: `ApiResult[BankBranchRes, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BankBranchRes` | `finnhub_api/models/bank_branch_res.py` |

### client.misc.country

- **Route**: `GET /country`
- **Auth**: `api_key`
- **Signature**: `def country(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[CountryMetadata]`
- **Returns (raw)**: `ApiResult[list[CountryMetadata], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CountryMetadata` | `finnhub_api/models/country_metadata.py` |

### client.misc.covid_19

- **Route**: `GET /covid19/us`
- **Auth**: `api_key`
- **Signature**: `def covid_19(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[CovidInfo]`
- **Returns (raw)**: `ApiResult[list[CovidInfo], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CovidInfo` | `finnhub_api/models/covid_info.py` |

### client.misc.fda_committee_meeting_calendar

- **Route**: `GET /fda-advisory-committee-calendar`
- **Auth**: `api_key`
- **Signature**: `def fda_committee_meeting_calendar(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[FdacomitteeMeeting]`
- **Returns (raw)**: `ApiResult[list[FdacomitteeMeeting], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FdacomitteeMeeting` | `finnhub_api/models/fdacomittee_meeting.py` |

### client.misc.quote

- **Route**: `GET /quote`
- **Auth**: `api_key`
- **Signature**: `def quote(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `Quote`
- **Returns (raw)**: `ApiResult[Quote, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Quote` | `finnhub_api/models/quote.py` |

### client.misc.sector_metric

- **Route**: `GET /sector/metrics`
- **Auth**: `api_key`
- **Signature**: `def sector_metric(region: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `region`
- **Params**: `region` — query
- **Returns (parsed)**: `SectorMetric`
- **Returns (raw)**: `ApiResult[SectorMetric, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SectorMetric` | `finnhub_api/models/sector_metric.py` |

### client.misc.symbol_search

- **Route**: `GET /search`
- **Auth**: `api_key`
- **Signature**: `def symbol_search(q: str, *, exchange: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `q`
- **Params**: `q` — query · `exchange` — query
- **Returns (parsed)**: `SymbolLookup`
- **Returns (raw)**: `ApiResult[SymbolLookup, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SymbolLookup` | `finnhub_api/models/symbol_lookup.py` |

### client.misc.technical_indicator

- **Route**: `GET /indicator`
- **Auth**: `api_key`
- **Signature**: `def technical_indicator(symbol: str, resolution: str, from_: int, to: int, indicator: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `resolution`, `from_`, `to`, `indicator`
- **Params**: `symbol` — query · `resolution` — query · `from_` — query `from` · `to` — query · `indicator` — query
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, RawError]`
- **Error**: `RawError` — **Case B**

