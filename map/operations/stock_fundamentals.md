<!-- Generated file — do not edit; regenerated with the SDK. -->

# StockFundamentals — operations

Accessor: `client.stock_fundamentals` · Source: `finnhub_api/apis/stock_fundamentals.py` · 18 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.stock_fundamentals.company_basic_financials

- **Route**: `GET /stock/metric`
- **Auth**: `api_key`
- **Signature**: `def company_basic_financials(symbol: str, metric: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `metric`
- **Params**: `symbol` — query · `metric` — query
- **Returns (parsed)**: `BasicFinancials`
- **Returns (raw)**: `ApiResult[BasicFinancials, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BasicFinancials` | `finnhub_api/models/basic_financials.py` |

### client.stock_fundamentals.company_esg_score

- **Route**: `GET /stock/esg`
- **Auth**: `api_key`
- **Signature**: `def company_esg_score(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `CompanyEsg`
- **Returns (raw)**: `ApiResult[CompanyEsg, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CompanyEsg` | `finnhub_api/models/company_esg.py` |

### client.stock_fundamentals.company_executive

- **Route**: `GET /stock/executive`
- **Auth**: `api_key`
- **Signature**: `def company_executive(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `CompanyExecutive`
- **Returns (raw)**: `ApiResult[CompanyExecutive, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CompanyExecutive` | `finnhub_api/models/company_executive.py` |

### client.stock_fundamentals.company_historical_esg_score

- **Route**: `GET /stock/historical-esg`
- **Auth**: `api_key`
- **Signature**: `def company_historical_esg_score(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `HistoricalCompanyEsg`
- **Returns (raw)**: `ApiResult[HistoricalCompanyEsg, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `HistoricalCompanyEsg` | `finnhub_api/models/historical_company_esg.py` |

### client.stock_fundamentals.company_profile

- **Route**: `GET /stock/profile`
- **Auth**: `api_key`
- **Signature**: `def company_profile(*, symbol: str | None = None, isin: str | None = None, cusip: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `isin` — query · `cusip` — query
- **Returns (parsed)**: `CompanyProfile`
- **Returns (raw)**: `ApiResult[CompanyProfile, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CompanyProfile` | `finnhub_api/models/company_profile.py` |

### client.stock_fundamentals.company_profile2

- **Route**: `GET /stock/profile2`
- **Auth**: `api_key`
- **Signature**: `def company_profile2(*, symbol: str | None = None, isin: str | None = None, cusip: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `isin` — query · `cusip` — query
- **Returns (parsed)**: `CompanyProfile2`
- **Returns (raw)**: `ApiResult[CompanyProfile2, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CompanyProfile2` | `finnhub_api/models/company_profile2.py` |

### client.stock_fundamentals.earnings_call_live

- **Route**: `GET /stock/earnings-call-live`
- **Auth**: `api_key`
- **Signature**: `def earnings_call_live(*, from_: Date | None = None, to: Date | None = None, symbol: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `from_` — query `from` · `to` — query · `symbol` — query
- **Returns (parsed)**: `EarningsCallLive`
- **Returns (raw)**: `ApiResult[EarningsCallLive, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EarningsCallLive` | `finnhub_api/models/earnings_call_live.py` |

### client.stock_fundamentals.filings

- **Route**: `GET /stock/filings`
- **Auth**: `api_key`
- **Signature**: `def filings(*, symbol: str | None = None, cik: str | None = None, access_number: str | None = None, form: str | None = None, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `cik` — query · `access_number` — query `accessNumber` · `form` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `list[Filing]`
- **Returns (raw)**: `ApiResult[list[Filing], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Filing` | `finnhub_api/models/filing.py` |

### client.stock_fundamentals.filings_sentiment

- **Route**: `GET /stock/filings-sentiment`
- **Auth**: `api_key`
- **Signature**: `def filings_sentiment(access_number: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `access_number`
- **Params**: `access_number` — query `accessNumber`
- **Returns (parsed)**: `SecsentimentAnalysis`
- **Returns (raw)**: `ApiResult[SecsentimentAnalysis, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SecsentimentAnalysis` | `finnhub_api/models/secsentiment_analysis.py` |

### client.stock_fundamentals.financials

- **Route**: `GET /stock/financials`
- **Auth**: `api_key`
- **Signature**: `def financials(symbol: str, statement: str, freq: str, *, preliminary: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `statement`, `freq`
- **Params**: `symbol` — query · `statement` — query · `freq` — query · `preliminary` — query
- **Returns (parsed)**: `FinancialStatements`
- **Returns (raw)**: `ApiResult[FinancialStatements, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FinancialStatements` | `finnhub_api/models/financial_statements.py` |

### client.stock_fundamentals.financials_reported

- **Route**: `GET /stock/financials-reported`
- **Auth**: `api_key`
- **Signature**: `def financials_reported(*, symbol: str | None = None, cik: str | None = None, access_number: str | None = None, freq: str | None = None, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `cik` — query · `access_number` — query `accessNumber` · `freq` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `FinancialsAsReported`
- **Returns (raw)**: `ApiResult[FinancialsAsReported, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FinancialsAsReported` | `finnhub_api/models/financials_as_reported.py` |

### client.stock_fundamentals.historical_employee_count

- **Route**: `GET /stock/historical-employee-count`
- **Auth**: `api_key`
- **Signature**: `def historical_employee_count(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `from_`, `to`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `HistoricalEmployeeCount`
- **Returns (raw)**: `ApiResult[HistoricalEmployeeCount, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `HistoricalEmployeeCount` | `finnhub_api/models/historical_employee_count.py` |

### client.stock_fundamentals.international_filings

- **Route**: `GET /stock/international-filings`
- **Auth**: `api_key`
- **Signature**: `def international_filings(*, symbol: str | None = None, country: str | None = None, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `country` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `list[InternationalFiling]`
- **Returns (raw)**: `ApiResult[list[InternationalFiling], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InternationalFiling` | `finnhub_api/models/international_filing.py` |

### client.stock_fundamentals.newsroom

- **Route**: `GET /stock/newsroom`
- **Auth**: `api_key`
- **Signature**: `def newsroom(symbol: str, *, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `Newsroom`
- **Returns (raw)**: `ApiResult[Newsroom, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Newsroom` | `finnhub_api/models/newsroom.py` |

### client.stock_fundamentals.similarity_index

- **Route**: `GET /stock/similarity-index`
- **Auth**: `api_key`
- **Signature**: `def similarity_index(*, symbol: str | None = None, cik: str | None = None, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `cik` — query · `freq` — query
- **Returns (parsed)**: `SimilarityIndex`
- **Returns (raw)**: `ApiResult[SimilarityIndex, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SimilarityIndex` | `finnhub_api/models/similarity_index.py` |

### client.stock_fundamentals.stock_presentation

- **Route**: `GET /stock/presentation`
- **Auth**: `api_key`
- **Signature**: `def stock_presentation(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `StockPresentation`
- **Returns (raw)**: `ApiResult[StockPresentation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StockPresentation` | `finnhub_api/models/stock_presentation.py` |

### client.stock_fundamentals.transcripts

- **Route**: `GET /stock/transcripts`
- **Auth**: `api_key`
- **Signature**: `def transcripts(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — query
- **Returns (parsed)**: `EarningsCallTranscripts`
- **Returns (raw)**: `ApiResult[EarningsCallTranscripts, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EarningsCallTranscripts` | `finnhub_api/models/earnings_call_transcripts.py` |

### client.stock_fundamentals.transcripts_list

- **Route**: `GET /stock/transcripts/list`
- **Auth**: `api_key`
- **Signature**: `def transcripts_list(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `EarningsCallTranscriptsList`
- **Returns (raw)**: `ApiResult[EarningsCallTranscriptsList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EarningsCallTranscriptsList` | `finnhub_api/models/earnings_call_transcripts_list.py` |

