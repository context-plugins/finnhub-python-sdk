<!-- Generated file — do not edit; regenerated with the SDK. -->

# StockOwnership — operations

Accessor: `client.stock_ownership` · Source: `finnhub_api/apis/stock_ownership.py` · 12 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.stock_ownership.congressional_trading

- **Route**: `GET /stock/congressional-trading`
- **Auth**: `api_key`
- **Signature**: `def congressional_trading(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `from_`, `to`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `CongressionalTrading`
- **Returns (raw)**: `ApiResult[CongressionalTrading, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CongressionalTrading` | `finnhub_api/models/congressional_trading.py` |

### client.stock_ownership.fund_ownership

- **Route**: `GET /stock/fund-ownership`
- **Auth**: `api_key`
- **Signature**: `def fund_ownership(symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `limit` — query
- **Returns (parsed)**: `FundOwnership`
- **Returns (raw)**: `ApiResult[FundOwnership, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FundOwnership` | `finnhub_api/models/fund_ownership.py` |

### client.stock_ownership.insider_sentiment

- **Route**: `GET /stock/insider-sentiment`
- **Auth**: `api_key`
- **Signature**: `def insider_sentiment(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `from_`, `to`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `InsiderSentiments`
- **Returns (raw)**: `ApiResult[InsiderSentiments, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InsiderSentiments` | `finnhub_api/models/insider_sentiments.py` |

### client.stock_ownership.insider_transactions

- **Route**: `GET /stock/insider-transactions`
- **Auth**: `api_key`
- **Signature**: `def insider_transactions(symbol: str, *, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `InsiderTransactions`
- **Returns (raw)**: `ApiResult[InsiderTransactions, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InsiderTransactions` | `finnhub_api/models/insider_transactions.py` |

### client.stock_ownership.investment_themes

- **Route**: `GET /stock/investment-theme`
- **Auth**: `api_key`
- **Signature**: `def investment_themes(theme: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `theme`
- **Params**: `theme` — query
- **Returns (parsed)**: `InvestmentThemes`
- **Returns (raw)**: `ApiResult[InvestmentThemes, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InvestmentThemes` | `finnhub_api/models/investment_themes.py` |

### client.stock_ownership.ownership

- **Route**: `GET /stock/ownership`
- **Auth**: `api_key`
- **Signature**: `def ownership(symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `limit` — query
- **Returns (parsed)**: `Ownership`
- **Returns (raw)**: `ApiResult[Ownership, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Ownership` | `finnhub_api/models/ownership.py` |

### client.stock_ownership.social_sentiment

- **Route**: `GET /stock/social-sentiment`
- **Auth**: `api_key`
- **Signature**: `def social_sentiment(symbol: str, *, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `SocialSentiment`
- **Returns (raw)**: `ApiResult[SocialSentiment, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SocialSentiment` | `finnhub_api/models/social_sentiment.py` |

### client.stock_ownership.stock_lobbying

- **Route**: `GET /stock/lobbying`
- **Auth**: `api_key`
- **Signature**: `def stock_lobbying(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `from_`, `to`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `LobbyingResult`
- **Returns (raw)**: `ApiResult[LobbyingResult, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LobbyingResult` | `finnhub_api/models/lobbying_result.py` |

### client.stock_ownership.stock_usa_spending

- **Route**: `GET /stock/usa-spending`
- **Auth**: `api_key`
- **Signature**: `def stock_usa_spending(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `from_`, `to`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `UsaSpendingResult`
- **Returns (raw)**: `ApiResult[UsaSpendingResult, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UsaSpendingResult` | `finnhub_api/models/usa_spending_result.py` |

### client.stock_ownership.stock_uspto_patent

- **Route**: `GET /stock/uspto-patent`
- **Auth**: `api_key`
- **Signature**: `def stock_uspto_patent(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `from_`, `to`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `UsptoPatentResult`
- **Returns (raw)**: `ApiResult[UsptoPatentResult, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UsptoPatentResult` | `finnhub_api/models/uspto_patent_result.py` |

### client.stock_ownership.stock_visa_application

- **Route**: `GET /stock/visa-application`
- **Auth**: `api_key`
- **Signature**: `def stock_visa_application(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `from_`, `to`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `VisaApplicationResult`
- **Returns (raw)**: `ApiResult[VisaApplicationResult, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VisaApplicationResult` | `finnhub_api/models/visa_application_result.py` |

### client.stock_ownership.supply_chain_relationships

- **Route**: `GET /stock/supply-chain`
- **Auth**: `api_key`
- **Signature**: `def supply_chain_relationships(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `SupplyChainRelationships`
- **Returns (raw)**: `ApiResult[SupplyChainRelationships, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SupplyChainRelationships` | `finnhub_api/models/supply_chain_relationships.py` |

