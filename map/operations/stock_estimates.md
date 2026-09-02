<!-- Generated file — do not edit; regenerated with the SDK. -->

# StockEstimates — operations

Accessor: `client.stock_estimates` · Source: `finnhub_api/apis/stock_estimates.py` · 18 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.stock_estimates.company_capex_estimates

- **Route**: `GET /stock/capex-estimate`
- **Auth**: `api_key`
- **Signature**: `def company_capex_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `CapexEstimates`
- **Returns (raw)**: `ApiResult[CapexEstimates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CapexEstimates` | `finnhub_api/models/capex_estimates.py` |

### client.stock_estimates.company_dps_estimates

- **Route**: `GET /stock/dps-estimate`
- **Auth**: `api_key`
- **Signature**: `def company_dps_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `DpsEstimates`
- **Returns (raw)**: `ApiResult[DpsEstimates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DpsEstimates` | `finnhub_api/models/dps_estimates.py` |

### client.stock_estimates.company_earnings

- **Route**: `GET /stock/earnings`
- **Auth**: `api_key`
- **Signature**: `def company_earnings(symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `limit` — query
- **Returns (parsed)**: `list[EarningResult]`
- **Returns (raw)**: `ApiResult[list[EarningResult], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EarningResult` | `finnhub_api/models/earning_result.py` |

### client.stock_estimates.company_earnings_quality_score

- **Route**: `GET /stock/earnings-quality-score`
- **Auth**: `api_key`
- **Signature**: `def company_earnings_quality_score(symbol: str, freq: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `freq`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `CompanyEarningsQualityScore`
- **Returns (raw)**: `ApiResult[CompanyEarningsQualityScore, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CompanyEarningsQualityScore` | `finnhub_api/models/company_earnings_quality_score.py` |

### client.stock_estimates.company_ebit_estimates

- **Route**: `GET /stock/ebit-estimate`
- **Auth**: `api_key`
- **Signature**: `def company_ebit_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `EbitEstimates`
- **Returns (raw)**: `ApiResult[EbitEstimates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EbitEstimates` | `finnhub_api/models/ebit_estimates.py` |

### client.stock_estimates.company_ebitda_estimates

- **Route**: `GET /stock/ebitda-estimate`
- **Auth**: `api_key`
- **Signature**: `def company_ebitda_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `EbitdaEstimates`
- **Returns (raw)**: `ApiResult[EbitdaEstimates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EbitdaEstimates` | `finnhub_api/models/ebitda_estimates.py` |

### client.stock_estimates.company_eps_estimates

- **Route**: `GET /stock/eps-estimate`
- **Auth**: `api_key`
- **Signature**: `def company_eps_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `EarningsEstimates`
- **Returns (raw)**: `ApiResult[EarningsEstimates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EarningsEstimates` | `finnhub_api/models/earnings_estimates.py` |

### client.stock_estimates.company_fcf_estimates

- **Route**: `GET /stock/fcf-estimate`
- **Auth**: `api_key`
- **Signature**: `def company_fcf_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `FcfEstimates`
- **Returns (raw)**: `ApiResult[FcfEstimates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FcfEstimates` | `finnhub_api/models/fcf_estimates.py` |

### client.stock_estimates.company_gross_income_estimates

- **Route**: `GET /stock/gross-income-estimate`
- **Auth**: `api_key`
- **Signature**: `def company_gross_income_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `GrossIncomeEstimates`
- **Returns (raw)**: `ApiResult[GrossIncomeEstimates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GrossIncomeEstimates` | `finnhub_api/models/gross_income_estimates.py` |

### client.stock_estimates.company_net_income_estimates

- **Route**: `GET /stock/net-income-estimate`
- **Auth**: `api_key`
- **Signature**: `def company_net_income_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `NetIncomeEstimates`
- **Returns (raw)**: `ApiResult[NetIncomeEstimates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NetIncomeEstimates` | `finnhub_api/models/net_income_estimates.py` |

### client.stock_estimates.company_ocf_estimates

- **Route**: `GET /stock/ocf-estimate`
- **Auth**: `api_key`
- **Signature**: `def company_ocf_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `OcfEstimates`
- **Returns (raw)**: `ApiResult[OcfEstimates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `OcfEstimates` | `finnhub_api/models/ocf_estimates.py` |

### client.stock_estimates.company_pretax_income_estimates

- **Route**: `GET /stock/pretax-income-estimate`
- **Auth**: `api_key`
- **Signature**: `def company_pretax_income_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `PretaxIncomeEstimates`
- **Returns (raw)**: `ApiResult[PretaxIncomeEstimates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PretaxIncomeEstimates` | `finnhub_api/models/pretax_income_estimates.py` |

### client.stock_estimates.company_revenue_estimates

- **Route**: `GET /stock/revenue-estimate`
- **Auth**: `api_key`
- **Signature**: `def company_revenue_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `RevenueEstimates`
- **Returns (raw)**: `ApiResult[RevenueEstimates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RevenueEstimates` | `finnhub_api/models/revenue_estimates.py` |

### client.stock_estimates.price_target

- **Route**: `GET /stock/price-target`
- **Auth**: `api_key`
- **Signature**: `def price_target(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `PriceTarget`
- **Returns (raw)**: `ApiResult[PriceTarget, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PriceTarget` | `finnhub_api/models/price_target.py` |

### client.stock_estimates.recommendation_trends

- **Route**: `GET /stock/recommendation`
- **Auth**: `api_key`
- **Signature**: `def recommendation_trends(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `list[RecommendationTrend]`
- **Returns (raw)**: `ApiResult[list[RecommendationTrend], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RecommendationTrend` | `finnhub_api/models/recommendation_trend.py` |

### client.stock_estimates.revenue_breakdown

- **Route**: `GET /stock/revenue-breakdown`
- **Auth**: `api_key`
- **Signature**: `def revenue_breakdown(*, symbol: str | None = None, cik: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `cik` — query
- **Returns (parsed)**: `RevenueBreakdown`
- **Returns (raw)**: `ApiResult[RevenueBreakdown, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RevenueBreakdown` | `finnhub_api/models/revenue_breakdown.py` |

### client.stock_estimates.revenue_breakdown2

- **Route**: `GET /stock/revenue-breakdown2`
- **Auth**: `api_key`
- **Signature**: `def revenue_breakdown2(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `RevenueBreakdown2`
- **Returns (raw)**: `ApiResult[RevenueBreakdown2, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RevenueBreakdown2` | `finnhub_api/models/revenue_breakdown2.py` |

### client.stock_estimates.upgrade_downgrade

- **Route**: `GET /stock/upgrade-downgrade`
- **Auth**: `api_key`
- **Signature**: `def upgrade_downgrade(*, symbol: str | None = None, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `list[UpgradeDowngrade]`
- **Returns (raw)**: `ApiResult[list[UpgradeDowngrade], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpgradeDowngrade` | `finnhub_api/models/upgrade_downgrade.py` |

