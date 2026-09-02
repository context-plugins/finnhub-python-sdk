<!-- Generated file — do not edit; regenerated with the SDK. -->

# News — operations

Accessor: `client.news` · Source: `finnhub_api/apis/news.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.news.company_news

- **Route**: `GET /company-news`
- **Auth**: `api_key`
- **Signature**: `def company_news(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `from_`, `to`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `list[CompanyNews]`
- **Returns (raw)**: `ApiResult[list[CompanyNews], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CompanyNews` | `finnhub_api/models/company_news.py` |

### client.news.market_news

- **Route**: `GET /news`
- **Auth**: `api_key`
- **Signature**: `def market_news(category: str, *, min_id: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `category`
- **Params**: `category` — query · `min_id` — query `minId`
- **Returns (parsed)**: `list[MarketNews]`
- **Returns (raw)**: `ApiResult[list[MarketNews], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MarketNews` | `finnhub_api/models/market_news.py` |

### client.news.news_sentiment

- **Route**: `GET /news-sentiment`
- **Auth**: `api_key`
- **Signature**: `def news_sentiment(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `NewsSentiment`
- **Returns (raw)**: `ApiResult[NewsSentiment, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NewsSentiment` | `finnhub_api/models/news_sentiment.py` |

### client.news.press_releases

- **Route**: `GET /press-releases`
- **Auth**: `api_key`
- **Signature**: `def press_releases(symbol: str, *, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `PressRelease`
- **Returns (raw)**: `ApiResult[PressRelease, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PressRelease` | `finnhub_api/models/press_release.py` |

