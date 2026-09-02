<!-- Generated file — do not edit; regenerated with the SDK. -->

# GlobalFilings — operations

Accessor: `client.global_filings` · Source: `finnhub_api/apis/global_filings.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.global_filings.global_filings_download

- **Route**: `GET /global-filings/download`
- **Auth**: `api_key`
- **Signature**: `def global_filings_download(document_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `document_id`
- **Params**: `document_id` — query `documentId`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.global_filings.global_filings_search

- **Route**: `POST /global-filings/search`
- **Auth**: `api_key`
- **Signature**: `def global_filings_search(*, search: SearchBody | SearchBodyDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `search` — JSON body
- **Returns (parsed)**: `SearchResponse`
- **Returns (raw)**: `ApiResult[SearchResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchBody` | `finnhub_api/models/search_body.py` |
| `SearchBodyDict` | `finnhub_api/models/search_body.py` |
| `SearchResponse` | `finnhub_api/models/search_response.py` |

### client.global_filings.global_filings_search_filter

- **Route**: `GET /global-filings/filter`
- **Auth**: `api_key`
- **Signature**: `def global_filings_search_filter(field: str, *, source: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `field`
- **Params**: `field` — query · `source` — query
- **Returns (parsed)**: `SearchFilter`
- **Returns (raw)**: `ApiResult[SearchFilter, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchFilter` | `finnhub_api/models/search_filter.py` |

### client.global_filings.search_in_filing

- **Route**: `POST /global-filings/search-in-filing`
- **Auth**: `api_key`
- **Signature**: `def search_in_filing(*, search: InFilingSearchBody | InFilingSearchBodyDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `search` — JSON body
- **Returns (parsed)**: `InFilingResponse`
- **Returns (raw)**: `ApiResult[InFilingResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InFilingSearchBody` | `finnhub_api/models/in_filing_search_body.py` |
| `InFilingSearchBodyDict` | `finnhub_api/models/in_filing_search_body.py` |
| `InFilingResponse` | `finnhub_api/models/in_filing_response.py` |

