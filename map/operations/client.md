<!-- Generated file — do not edit; regenerated with the SDK. -->

# Client — operations

Accessor: `client` · Source: `finnhub/client.py` · 117 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.aggregate_indicator

- **Route**: `GET /scan/technical-indicator`
- **Signature**: `def aggregate_indicator(symbol: str, resolution: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `resolution`
- **Params**: `symbol` — query · `resolution` — query
- **Returns (parsed)**: `AggregateIndicators`
- **Returns (raw)**: `ApiResult[AggregateIndicators, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AggregateIndicators` | `finnhub/models/aggregate_indicators.py` |

### client.ai_chat

- **Route**: `POST /ai-chat`
- **Signature**: `def ai_chat(*, search: AichatBody | AichatBodyDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `search` — JSON body
- **Returns (parsed)**: `AichatResponse`
- **Returns (raw)**: `ApiResult[AichatResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AichatBody` | `finnhub/models/aichat_body.py` |
| `AichatBodyDict` | `finnhub/models/aichat_body.py` |
| `AichatResponse` | `finnhub/models/aichat_response.py` |

### client.airline_price_index

- **Route**: `GET /airline/price-index`
- **Signature**: `def airline_price_index(airline: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `airline`, `from_`, `to`
- **Params**: `airline` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `AirlinePriceIndexData`
- **Returns (raw)**: `ApiResult[AirlinePriceIndexData, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AirlinePriceIndexData` | `finnhub/models/airline_price_index_data.py` |

### client.bank_branch

- **Route**: `GET /bank-branch`
- **Signature**: `def bank_branch(symbol: Any, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `BankBranchRes`
- **Returns (raw)**: `ApiResult[BankBranchRes, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BankBranchRes` | `finnhub/models/bank_branch_res.py` |

### client.bond_price

- **Route**: `GET /bond/price`
- **Signature**: `def bond_price(isin: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `isin`, `from_`, `to`
- **Params**: `isin` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `BondCandles`
- **Returns (raw)**: `ApiResult[BondCandles, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BondCandles` | `finnhub/models/bond_candles.py` |

### client.bond_profile

- **Route**: `GET /bond/profile`
- **Signature**: `def bond_profile(*, isin: str | None = None, cusip: str | None = None, figi: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `isin` — query · `cusip` — query · `figi` — query
- **Returns (parsed)**: `BondProfile`
- **Returns (raw)**: `ApiResult[BondProfile, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BondProfile` | `finnhub/models/bond_profile.py` |

### client.bond_tick

- **Route**: `GET /bond/tick`
- **Signature**: `def bond_tick(isin: str, date: Date, limit: int, skip: int, exchange: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `isin`, `date`, `limit`, `skip`, `exchange`
- **Params**: `isin` — query · `date` — query · `limit` — query · `skip` — query · `exchange` — query
- **Returns (parsed)**: `BondTickData`
- **Returns (raw)**: `ApiResult[BondTickData, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BondTickData` | `finnhub/models/bond_tick_data.py` |

### client.bond_yield_curve

- **Route**: `GET /bond/yield-curve`
- **Signature**: `def bond_yield_curve(code: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `code`
- **Params**: `code` — query
- **Returns (parsed)**: `BondYieldCurve`
- **Returns (raw)**: `ApiResult[BondYieldCurve, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BondYieldCurve` | `finnhub/models/bond_yield_curve.py` |

### client.company_basic_financials

- **Route**: `GET /stock/metric`
- **Signature**: `def company_basic_financials(symbol: str, metric: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `metric`
- **Params**: `symbol` — query · `metric` — query
- **Returns (parsed)**: `BasicFinancials`
- **Returns (raw)**: `ApiResult[BasicFinancials, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BasicFinancials` | `finnhub/models/basic_financials.py` |

### client.company_capex_estimates

- **Route**: `GET /stock/capex-estimate`
- **Signature**: `def company_capex_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `CapexEstimates`
- **Returns (raw)**: `ApiResult[CapexEstimates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CapexEstimates` | `finnhub/models/capex_estimates.py` |

### client.company_dps_estimates

- **Route**: `GET /stock/dps-estimate`
- **Signature**: `def company_dps_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `DpsEstimates`
- **Returns (raw)**: `ApiResult[DpsEstimates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DpsEstimates` | `finnhub/models/dps_estimates.py` |

### client.company_earnings

- **Route**: `GET /stock/earnings`
- **Signature**: `def company_earnings(symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `limit` — query
- **Returns (parsed)**: `list[EarningResult]`
- **Returns (raw)**: `ApiResult[list[EarningResult], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EarningResult` | `finnhub/models/earning_result.py` |

### client.company_earnings_quality_score

- **Route**: `GET /stock/earnings-quality-score`
- **Signature**: `def company_earnings_quality_score(symbol: str, freq: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `freq`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `CompanyEarningsQualityScore`
- **Returns (raw)**: `ApiResult[CompanyEarningsQualityScore, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CompanyEarningsQualityScore` | `finnhub/models/company_earnings_quality_score.py` |

### client.company_ebit_estimates

- **Route**: `GET /stock/ebit-estimate`
- **Signature**: `def company_ebit_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `EbitEstimates`
- **Returns (raw)**: `ApiResult[EbitEstimates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EbitEstimates` | `finnhub/models/ebit_estimates.py` |

### client.company_ebitda_estimates

- **Route**: `GET /stock/ebitda-estimate`
- **Signature**: `def company_ebitda_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `EbitdaEstimates`
- **Returns (raw)**: `ApiResult[EbitdaEstimates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EbitdaEstimates` | `finnhub/models/ebitda_estimates.py` |

### client.company_eps_estimates

- **Route**: `GET /stock/eps-estimate`
- **Signature**: `def company_eps_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `EarningsEstimates`
- **Returns (raw)**: `ApiResult[EarningsEstimates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EarningsEstimates` | `finnhub/models/earnings_estimates.py` |

### client.company_esg_score

- **Route**: `GET /stock/esg`
- **Signature**: `def company_esg_score(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `CompanyEsg`
- **Returns (raw)**: `ApiResult[CompanyEsg, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CompanyEsg` | `finnhub/models/company_esg.py` |

### client.company_executive

- **Route**: `GET /stock/executive`
- **Signature**: `def company_executive(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `CompanyExecutive`
- **Returns (raw)**: `ApiResult[CompanyExecutive, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CompanyExecutive` | `finnhub/models/company_executive.py` |

### client.company_fcf_estimates

- **Route**: `GET /stock/fcf-estimate`
- **Signature**: `def company_fcf_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `FcfEstimates`
- **Returns (raw)**: `ApiResult[FcfEstimates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FcfEstimates` | `finnhub/models/fcf_estimates.py` |

### client.company_gross_income_estimates

- **Route**: `GET /stock/gross-income-estimate`
- **Signature**: `def company_gross_income_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `GrossIncomeEstimates`
- **Returns (raw)**: `ApiResult[GrossIncomeEstimates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GrossIncomeEstimates` | `finnhub/models/gross_income_estimates.py` |

### client.company_historical_esg_score

- **Route**: `GET /stock/historical-esg`
- **Signature**: `def company_historical_esg_score(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `HistoricalCompanyEsg`
- **Returns (raw)**: `ApiResult[HistoricalCompanyEsg, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `HistoricalCompanyEsg` | `finnhub/models/historical_company_esg.py` |

### client.company_net_income_estimates

- **Route**: `GET /stock/net-income-estimate`
- **Signature**: `def company_net_income_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `NetIncomeEstimates`
- **Returns (raw)**: `ApiResult[NetIncomeEstimates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NetIncomeEstimates` | `finnhub/models/net_income_estimates.py` |

### client.company_news

- **Route**: `GET /company-news`
- **Signature**: `def company_news(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `from_`, `to`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `list[CompanyNews]`
- **Returns (raw)**: `ApiResult[list[CompanyNews], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CompanyNews` | `finnhub/models/company_news.py` |

### client.company_ocf_estimates

- **Route**: `GET /stock/ocf-estimate`
- **Signature**: `def company_ocf_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `OcfEstimates`
- **Returns (raw)**: `ApiResult[OcfEstimates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `OcfEstimates` | `finnhub/models/ocf_estimates.py` |

### client.company_peers

- **Route**: `GET /stock/peers`
- **Signature**: `def company_peers(symbol: str, *, grouping: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `grouping` — query
- **Returns (parsed)**: `list[str]`
- **Returns (raw)**: `ApiResult[list[str], RawError]`
- **Error**: `RawError` — **Case B**

### client.company_pretax_income_estimates

- **Route**: `GET /stock/pretax-income-estimate`
- **Signature**: `def company_pretax_income_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `PretaxIncomeEstimates`
- **Returns (raw)**: `ApiResult[PretaxIncomeEstimates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PretaxIncomeEstimates` | `finnhub/models/pretax_income_estimates.py` |

### client.company_profile

- **Route**: `GET /stock/profile`
- **Signature**: `def company_profile(*, symbol: str | None = None, isin: str | None = None, cusip: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `isin` — query · `cusip` — query
- **Returns (parsed)**: `CompanyProfile`
- **Returns (raw)**: `ApiResult[CompanyProfile, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CompanyProfile` | `finnhub/models/company_profile.py` |

### client.company_profile2

- **Route**: `GET /stock/profile2`
- **Signature**: `def company_profile2(*, symbol: str | None = None, isin: str | None = None, cusip: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `isin` — query · `cusip` — query
- **Returns (parsed)**: `CompanyProfile2`
- **Returns (raw)**: `ApiResult[CompanyProfile2, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CompanyProfile2` | `finnhub/models/company_profile2.py` |

### client.company_revenue_estimates

- **Route**: `GET /stock/revenue-estimate`
- **Signature**: `def company_revenue_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `freq` — query
- **Returns (parsed)**: `RevenueEstimates`
- **Returns (raw)**: `ApiResult[RevenueEstimates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RevenueEstimates` | `finnhub/models/revenue_estimates.py` |

### client.congressional_trading

- **Route**: `GET /stock/congressional-trading`
- **Signature**: `def congressional_trading(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `from_`, `to`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `CongressionalTrading`
- **Returns (raw)**: `ApiResult[CongressionalTrading, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CongressionalTrading` | `finnhub/models/congressional_trading.py` |

### client.country

- **Route**: `GET /country`
- **Signature**: `def country(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[CountryMetadata]`
- **Returns (raw)**: `ApiResult[list[CountryMetadata], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CountryMetadata` | `finnhub/models/country_metadata.py` |

### client.covid_19

- **Route**: `GET /covid19/us`
- **Signature**: `def covid_19(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[CovidInfo]`
- **Returns (raw)**: `ApiResult[list[CovidInfo], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CovidInfo` | `finnhub/models/covid_info.py` |

### client.crypto_candles

- **Route**: `GET /crypto/candle`
- **Signature**: `def crypto_candles(symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `resolution`, `from_`, `to`
- **Params**: `symbol` — query · `resolution` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `CryptoCandles`
- **Returns (raw)**: `ApiResult[CryptoCandles, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CryptoCandles` | `finnhub/models/crypto_candles.py` |

### client.crypto_exchanges

- **Route**: `GET /crypto/exchange`
- **Signature**: `def crypto_exchanges(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[str]`
- **Returns (raw)**: `ApiResult[list[str], RawError]`
- **Error**: `RawError` — **Case B**

### client.crypto_profile

- **Route**: `GET /crypto/profile`
- **Signature**: `def crypto_profile(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `CryptoProfile`
- **Returns (raw)**: `ApiResult[CryptoProfile, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CryptoProfile` | `finnhub/models/crypto_profile.py` |

### client.crypto_symbols

- **Route**: `GET /crypto/symbol`
- **Signature**: `def crypto_symbols(exchange: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `exchange`
- **Params**: `exchange` — query
- **Returns (parsed)**: `list[CryptoSymbol]`
- **Returns (raw)**: `ApiResult[list[CryptoSymbol], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CryptoSymbol` | `finnhub/models/crypto_symbol.py` |

### client.earnings_calendar

- **Route**: `GET /calendar/earnings`
- **Signature**: `def earnings_calendar(*, from_: Date | None = None, to: Date | None = None, symbol: str | None = None, international: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `from_` — query `from` · `to` — query · `symbol` — query · `international` — query
- **Returns (parsed)**: `EarningsCalendar`
- **Returns (raw)**: `ApiResult[EarningsCalendar, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EarningsCalendar` | `finnhub/models/earnings_calendar.py` |

### client.earnings_call_live

- **Route**: `GET /stock/earnings-call-live`
- **Signature**: `def earnings_call_live(*, from_: Date | None = None, to: Date | None = None, symbol: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `from_` — query `from` · `to` — query · `symbol` — query
- **Returns (parsed)**: `EarningsCallLive`
- **Returns (raw)**: `ApiResult[EarningsCallLive, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EarningsCallLive` | `finnhub/models/earnings_call_live.py` |

### client.economic_calendar

- **Route**: `GET /calendar/economic`
- **Signature**: `def economic_calendar(*, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `from_` — query `from` · `to` — query
- **Returns (parsed)**: `EconomicCalendar`
- **Returns (raw)**: `ApiResult[EconomicCalendar, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EconomicCalendar` | `finnhub/models/economic_calendar.py` |

### client.economic_code

- **Route**: `GET /economic/code`
- **Signature**: `def economic_code(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[EconomicCode]`
- **Returns (raw)**: `ApiResult[list[EconomicCode], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EconomicCode` | `finnhub/models/economic_code.py` |

### client.economic_data

- **Route**: `GET /economic`
- **Signature**: `def economic_data(code: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `code`
- **Params**: `code` — query
- **Returns (parsed)**: `EconomicData`
- **Returns (raw)**: `ApiResult[EconomicData, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EconomicData` | `finnhub/models/economic_data.py` |

### client.etfs_allocation

- **Route**: `GET /etf/allocation`
- **Signature**: `def etfs_allocation(*, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `isin` — query
- **Returns (parsed)**: `EtfsAllocation`
- **Returns (raw)**: `ApiResult[EtfsAllocation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EtfsAllocation` | `finnhub/models/etfs_allocation.py` |

### client.etfs_country_exposure

- **Route**: `GET /etf/country`
- **Signature**: `def etfs_country_exposure(*, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `isin` — query
- **Returns (parsed)**: `EtfsCountryExposure`
- **Returns (raw)**: `ApiResult[EtfsCountryExposure, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EtfsCountryExposure` | `finnhub/models/etfs_country_exposure.py` |

### client.etfs_holdings

- **Route**: `GET /etf/holdings`
- **Signature**: `def etfs_holdings(*, symbol: str | None = None, isin: str | None = None, skip: int | None = None, date: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `isin` — query · `skip` — query · `date` — query
- **Returns (parsed)**: `EtfsHoldings`
- **Returns (raw)**: `ApiResult[EtfsHoldings, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EtfsHoldings` | `finnhub/models/etfs_holdings.py` |

### client.etfs_profile

- **Route**: `GET /etf/profile`
- **Signature**: `def etfs_profile(*, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `isin` — query
- **Returns (parsed)**: `EtfsProfile`
- **Returns (raw)**: `ApiResult[EtfsProfile, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EtfsProfile` | `finnhub/models/etfs_profile.py` |

### client.etfs_sector_exposure

- **Route**: `GET /etf/sector`
- **Signature**: `def etfs_sector_exposure(*, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `isin` — query
- **Returns (parsed)**: `EtfsSectorExposure`
- **Returns (raw)**: `ApiResult[EtfsSectorExposure, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EtfsSectorExposure` | `finnhub/models/etfs_sector_exposure.py` |

### client.fda_committee_meeting_calendar

- **Route**: `GET /fda-advisory-committee-calendar`
- **Signature**: `def fda_committee_meeting_calendar(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[FdacomitteeMeeting]`
- **Returns (raw)**: `ApiResult[list[FdacomitteeMeeting], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FdacomitteeMeeting` | `finnhub/models/fdacomittee_meeting.py` |

### client.filings

- **Route**: `GET /stock/filings`
- **Signature**: `def filings(*, symbol: str | None = None, cik: str | None = None, access_number: str | None = None, form: str | None = None, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `cik` — query · `access_number` — query `accessNumber` · `form` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `list[Filing]`
- **Returns (raw)**: `ApiResult[list[Filing], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Filing` | `finnhub/models/filing.py` |

### client.filings_sentiment

- **Route**: `GET /stock/filings-sentiment`
- **Signature**: `def filings_sentiment(access_number: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `access_number`
- **Params**: `access_number` — query `accessNumber`
- **Returns (parsed)**: `SecsentimentAnalysis`
- **Returns (raw)**: `ApiResult[SecsentimentAnalysis, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SecsentimentAnalysis` | `finnhub/models/secsentiment_analysis.py` |

### client.financials

- **Route**: `GET /stock/financials`
- **Signature**: `def financials(symbol: str, statement: str, freq: str, *, preliminary: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `statement`, `freq`
- **Params**: `symbol` — query · `statement` — query · `freq` — query · `preliminary` — query
- **Returns (parsed)**: `FinancialStatements`
- **Returns (raw)**: `ApiResult[FinancialStatements, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FinancialStatements` | `finnhub/models/financial_statements.py` |

### client.financials_reported

- **Route**: `GET /stock/financials-reported`
- **Signature**: `def financials_reported(*, symbol: str | None = None, cik: str | None = None, access_number: str | None = None, freq: str | None = None, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `cik` — query · `access_number` — query `accessNumber` · `freq` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `FinancialsAsReported`
- **Returns (raw)**: `ApiResult[FinancialsAsReported, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FinancialsAsReported` | `finnhub/models/financials_as_reported.py` |

### client.forex_candles

- **Route**: `GET /forex/candle`
- **Signature**: `def forex_candles(symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `resolution`, `from_`, `to`
- **Params**: `symbol` — query · `resolution` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `ForexCandles`
- **Returns (raw)**: `ApiResult[ForexCandles, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ForexCandles` | `finnhub/models/forex_candles.py` |

### client.forex_exchanges

- **Route**: `GET /forex/exchange`
- **Signature**: `def forex_exchanges(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[str]`
- **Returns (raw)**: `ApiResult[list[str], RawError]`
- **Error**: `RawError` — **Case B**

### client.forex_rates

- **Route**: `GET /forex/rates`
- **Signature**: `def forex_rates(*, base: str | None = None, date: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `base` — query · `date` — query
- **Returns (parsed)**: `Forexrates`
- **Returns (raw)**: `ApiResult[Forexrates, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Forexrates` | `finnhub/models/forexrates.py` |

### client.forex_symbols

- **Route**: `GET /forex/symbol`
- **Signature**: `def forex_symbols(exchange: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `exchange`
- **Params**: `exchange` — query
- **Returns (parsed)**: `list[ForexSymbol]`
- **Returns (raw)**: `ApiResult[list[ForexSymbol], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ForexSymbol` | `finnhub/models/forex_symbol.py` |

### client.fund_ownership

- **Route**: `GET /stock/fund-ownership`
- **Signature**: `def fund_ownership(symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `limit` — query
- **Returns (parsed)**: `FundOwnership`
- **Returns (raw)**: `ApiResult[FundOwnership, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FundOwnership` | `finnhub/models/fund_ownership.py` |

### client.global_filings_download

- **Route**: `GET /global-filings/download`
- **Signature**: `def global_filings_download(document_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `document_id`
- **Params**: `document_id` — query `documentId`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.global_filings_search

- **Route**: `POST /global-filings/search`
- **Signature**: `def global_filings_search(*, search: SearchBody | SearchBodyDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `search` — JSON body
- **Returns (parsed)**: `SearchResponse`
- **Returns (raw)**: `ApiResult[SearchResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchBody` | `finnhub/models/search_body.py` |
| `SearchBodyDict` | `finnhub/models/search_body.py` |
| `SearchResponse` | `finnhub/models/search_response.py` |

### client.global_filings_search_filter

- **Route**: `GET /global-filings/filter`
- **Signature**: `def global_filings_search_filter(field: str, *, source: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `field`
- **Params**: `field` — query · `source` — query
- **Returns (parsed)**: `SearchFilter`
- **Returns (raw)**: `ApiResult[SearchFilter, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchFilter` | `finnhub/models/search_filter.py` |

### client.historical_employee_count

- **Route**: `GET /stock/historical-employee-count`
- **Signature**: `def historical_employee_count(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `from_`, `to`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `HistoricalEmployeeCount`
- **Returns (raw)**: `ApiResult[HistoricalEmployeeCount, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `HistoricalEmployeeCount` | `finnhub/models/historical_employee_count.py` |

### client.historical_market_cap

- **Route**: `GET /stock/historical-market-cap`
- **Signature**: `def historical_market_cap(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `from_`, `to`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `HistoricalMarketCapData`
- **Returns (raw)**: `ApiResult[HistoricalMarketCapData, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `HistoricalMarketCapData` | `finnhub/models/historical_market_cap_data.py` |

### client.indices_constituents

- **Route**: `GET /index/constituents`
- **Signature**: `def indices_constituents(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `IndicesConstituents`
- **Returns (raw)**: `ApiResult[IndicesConstituents, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IndicesConstituents` | `finnhub/models/indices_constituents.py` |

### client.indices_historical_constituents

- **Route**: `GET /index/historical-constituents`
- **Signature**: `def indices_historical_constituents(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `IndicesHistoricalConstituents`
- **Returns (raw)**: `ApiResult[IndicesHistoricalConstituents, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IndicesHistoricalConstituents` | `finnhub/models/indices_historical_constituents.py` |

### client.insider_sentiment

- **Route**: `GET /stock/insider-sentiment`
- **Signature**: `def insider_sentiment(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `from_`, `to`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `InsiderSentiments`
- **Returns (raw)**: `ApiResult[InsiderSentiments, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InsiderSentiments` | `finnhub/models/insider_sentiments.py` |

### client.insider_transactions

- **Route**: `GET /stock/insider-transactions`
- **Signature**: `def insider_transactions(symbol: str, *, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `InsiderTransactions`
- **Returns (raw)**: `ApiResult[InsiderTransactions, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InsiderTransactions` | `finnhub/models/insider_transactions.py` |

### client.institutional_ownership

- **Route**: `GET /institutional/ownership`
- **Signature**: `def institutional_ownership(symbol: str, cusip: str, from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `cusip`, `from_`, `to`
- **Params**: `symbol` — query · `cusip` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `InstitutionalOwnership`
- **Returns (raw)**: `ApiResult[InstitutionalOwnership, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InstitutionalOwnership` | `finnhub/models/institutional_ownership.py` |

### client.institutional_portfolio

- **Route**: `GET /institutional/portfolio`
- **Signature**: `def institutional_portfolio(cik: str, from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `cik`, `from_`, `to`
- **Params**: `cik` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `InstitutionalPortfolio`
- **Returns (raw)**: `ApiResult[InstitutionalPortfolio, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InstitutionalPortfolio` | `finnhub/models/institutional_portfolio.py` |

### client.institutional_profile

- **Route**: `GET /institutional/profile`
- **Signature**: `def institutional_profile(*, cik: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `cik` — query
- **Returns (parsed)**: `InstitutionalProfile`
- **Returns (raw)**: `ApiResult[InstitutionalProfile, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InstitutionalProfile` | `finnhub/models/institutional_profile.py` |

### client.international_filings

- **Route**: `GET /stock/international-filings`
- **Signature**: `def international_filings(*, symbol: str | None = None, country: str | None = None, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `country` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `list[InternationalFiling]`
- **Returns (raw)**: `ApiResult[list[InternationalFiling], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InternationalFiling` | `finnhub/models/international_filing.py` |

### client.investment_themes

- **Route**: `GET /stock/investment-theme`
- **Signature**: `def investment_themes(theme: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `theme`
- **Params**: `theme` — query
- **Returns (parsed)**: `InvestmentThemes`
- **Returns (raw)**: `ApiResult[InvestmentThemes, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InvestmentThemes` | `finnhub/models/investment_themes.py` |

### client.ipo_calendar

- **Route**: `GET /calendar/ipo`
- **Signature**: `def ipo_calendar(from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `from_`, `to`
- **Params**: `from_` — query `from` · `to` — query
- **Returns (parsed)**: `Ipocalendar`
- **Returns (raw)**: `ApiResult[Ipocalendar, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Ipocalendar` | `finnhub/models/ipocalendar.py` |

### client.isin_change

- **Route**: `GET /ca/isin-change`
- **Signature**: `def isin_change(from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `from_`, `to`
- **Params**: `from_` — query `from` · `to` — query
- **Returns (parsed)**: `IsinChange`
- **Returns (raw)**: `ApiResult[IsinChange, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IsinChange` | `finnhub/models/isin_change.py` |

### client.market_holiday

- **Route**: `GET /stock/market-holiday`
- **Signature**: `def market_holiday(exchange: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `exchange`
- **Params**: `exchange` — query
- **Returns (parsed)**: `MarketHoliday`
- **Returns (raw)**: `ApiResult[MarketHoliday, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MarketHoliday` | `finnhub/models/market_holiday.py` |

### client.market_news

- **Route**: `GET /news`
- **Signature**: `def market_news(category: str, *, min_id: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `category`
- **Params**: `category` — query · `min_id` — query `minId`
- **Returns (parsed)**: `list[MarketNews]`
- **Returns (raw)**: `ApiResult[list[MarketNews], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MarketNews` | `finnhub/models/market_news.py` |

### client.market_status

- **Route**: `GET /stock/market-status`
- **Signature**: `def market_status(exchange: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `exchange`
- **Params**: `exchange` — query
- **Returns (parsed)**: `MarketStatus`
- **Returns (raw)**: `ApiResult[MarketStatus, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MarketStatus` | `finnhub/models/market_status.py` |

### client.mutual_fund_country_exposure

- **Route**: `GET /mutual-fund/country`
- **Signature**: `def mutual_fund_country_exposure(*, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `isin` — query
- **Returns (parsed)**: `MutualFundCountryExposure`
- **Returns (raw)**: `ApiResult[MutualFundCountryExposure, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MutualFundCountryExposure` | `finnhub/models/mutual_fund_country_exposure.py` |

### client.mutual_fund_eet

- **Route**: `GET /mutual-fund/eet`
- **Signature**: `def mutual_fund_eet(isin: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `isin`
- **Params**: `isin` — query
- **Returns (parsed)**: `MutualFundEet`
- **Returns (raw)**: `ApiResult[MutualFundEet, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MutualFundEet` | `finnhub/models/mutual_fund_eet.py` |

### client.mutual_fund_eet_pai

- **Route**: `GET /mutual-fund/eet-pai`
- **Signature**: `def mutual_fund_eet_pai(isin: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `isin`
- **Params**: `isin` — query
- **Returns (parsed)**: `MutualFundEetPai`
- **Returns (raw)**: `ApiResult[MutualFundEetPai, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MutualFundEetPai` | `finnhub/models/mutual_fund_eet_pai.py` |

### client.mutual_fund_holdings

- **Route**: `GET /mutual-fund/holdings`
- **Signature**: `def mutual_fund_holdings(*, symbol: str | None = None, isin: str | None = None, skip: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `isin` — query · `skip` — query
- **Returns (parsed)**: `MutualFundHoldings`
- **Returns (raw)**: `ApiResult[MutualFundHoldings, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MutualFundHoldings` | `finnhub/models/mutual_fund_holdings.py` |

### client.mutual_fund_profile

- **Route**: `GET /mutual-fund/profile`
- **Signature**: `def mutual_fund_profile(*, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `isin` — query
- **Returns (parsed)**: `MutualFundProfile`
- **Returns (raw)**: `ApiResult[MutualFundProfile, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MutualFundProfile` | `finnhub/models/mutual_fund_profile.py` |

### client.mutual_fund_sector_exposure

- **Route**: `GET /mutual-fund/sector`
- **Signature**: `def mutual_fund_sector_exposure(*, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `isin` — query
- **Returns (parsed)**: `MutualFundSectorExposure`
- **Returns (raw)**: `ApiResult[MutualFundSectorExposure, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MutualFundSectorExposure` | `finnhub/models/mutual_fund_sector_exposure.py` |

### client.news_sentiment

- **Route**: `GET /news-sentiment`
- **Signature**: `def news_sentiment(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `NewsSentiment`
- **Returns (raw)**: `ApiResult[NewsSentiment, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NewsSentiment` | `finnhub/models/news_sentiment.py` |

### client.newsroom

- **Route**: `GET /stock/newsroom`
- **Signature**: `def newsroom(symbol: str, *, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `Newsroom`
- **Returns (raw)**: `ApiResult[Newsroom, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Newsroom` | `finnhub/models/newsroom.py` |

### client.ownership

- **Route**: `GET /stock/ownership`
- **Signature**: `def ownership(symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `limit` — query
- **Returns (parsed)**: `Ownership`
- **Returns (raw)**: `ApiResult[Ownership, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Ownership` | `finnhub/models/ownership.py` |

### client.pattern_recognition

- **Route**: `GET /scan/pattern`
- **Signature**: `def pattern_recognition(symbol: str, resolution: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `resolution`
- **Params**: `symbol` — query · `resolution` — query
- **Returns (parsed)**: `PatternRecognition`
- **Returns (raw)**: `ApiResult[PatternRecognition, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PatternRecognition` | `finnhub/models/pattern_recognition.py` |

### client.press_releases

- **Route**: `GET /press-releases`
- **Signature**: `def press_releases(symbol: str, *, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `PressRelease`
- **Returns (raw)**: `ApiResult[PressRelease, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PressRelease` | `finnhub/models/press_release.py` |

### client.price_metrics

- **Route**: `GET /stock/price-metric`
- **Signature**: `def price_metrics(symbol: str, *, date: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `date` — query
- **Returns (parsed)**: `PriceMetrics`
- **Returns (raw)**: `ApiResult[PriceMetrics, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PriceMetrics` | `finnhub/models/price_metrics.py` |

### client.price_target

- **Route**: `GET /stock/price-target`
- **Signature**: `def price_target(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `PriceTarget`
- **Returns (raw)**: `ApiResult[PriceTarget, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PriceTarget` | `finnhub/models/price_target.py` |

### client.quote

- **Route**: `GET /quote`
- **Signature**: `def quote(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `Quote`
- **Returns (raw)**: `ApiResult[Quote, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Quote` | `finnhub/models/quote.py` |

### client.recommendation_trends

- **Route**: `GET /stock/recommendation`
- **Signature**: `def recommendation_trends(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `list[RecommendationTrend]`
- **Returns (raw)**: `ApiResult[list[RecommendationTrend], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RecommendationTrend` | `finnhub/models/recommendation_trend.py` |

### client.revenue_breakdown

- **Route**: `GET /stock/revenue-breakdown`
- **Signature**: `def revenue_breakdown(*, symbol: str | None = None, cik: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `cik` — query
- **Returns (parsed)**: `RevenueBreakdown`
- **Returns (raw)**: `ApiResult[RevenueBreakdown, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RevenueBreakdown` | `finnhub/models/revenue_breakdown.py` |

### client.revenue_breakdown2

- **Route**: `GET /stock/revenue-breakdown2`
- **Signature**: `def revenue_breakdown2(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `RevenueBreakdown2`
- **Returns (raw)**: `ApiResult[RevenueBreakdown2, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RevenueBreakdown2` | `finnhub/models/revenue_breakdown2.py` |

### client.search_in_filing

- **Route**: `POST /global-filings/search-in-filing`
- **Signature**: `def search_in_filing(*, search: InFilingSearchBody | InFilingSearchBodyDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `search` — JSON body
- **Returns (parsed)**: `InFilingResponse`
- **Returns (raw)**: `ApiResult[InFilingResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InFilingSearchBody` | `finnhub/models/in_filing_search_body.py` |
| `InFilingSearchBodyDict` | `finnhub/models/in_filing_search_body.py` |
| `InFilingResponse` | `finnhub/models/in_filing_response.py` |

### client.sector_metric

- **Route**: `GET /sector/metrics`
- **Signature**: `def sector_metric(region: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `region`
- **Params**: `region` — query
- **Returns (parsed)**: `SectorMetric`
- **Returns (raw)**: `ApiResult[SectorMetric, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SectorMetric` | `finnhub/models/sector_metric.py` |

### client.similarity_index

- **Route**: `GET /stock/similarity-index`
- **Signature**: `def similarity_index(*, symbol: str | None = None, cik: str | None = None, freq: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `cik` — query · `freq` — query
- **Returns (parsed)**: `SimilarityIndex`
- **Returns (raw)**: `ApiResult[SimilarityIndex, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SimilarityIndex` | `finnhub/models/similarity_index.py` |

### client.social_sentiment

- **Route**: `GET /stock/social-sentiment`
- **Signature**: `def social_sentiment(symbol: str, *, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `SocialSentiment`
- **Returns (raw)**: `ApiResult[SocialSentiment, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SocialSentiment` | `finnhub/models/social_sentiment.py` |

### client.stock_basic_dividends

- **Route**: `GET /stock/dividend2`
- **Signature**: `def stock_basic_dividends(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `Dividends2`
- **Returns (raw)**: `ApiResult[Dividends2, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Dividends2` | `finnhub/models/dividends2.py` |

### client.stock_bidask

- **Route**: `GET /stock/bidask`
- **Signature**: `def stock_bidask(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `LastBidAsk`
- **Returns (raw)**: `ApiResult[LastBidAsk, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LastBidAsk` | `finnhub/models/last_bid_ask.py` |

### client.stock_candles

- **Route**: `GET /stock/candle`
- **Signature**: `def stock_candles(symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `resolution`, `from_`, `to`
- **Params**: `symbol` — query · `resolution` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `StockCandles`
- **Returns (raw)**: `ApiResult[StockCandles, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StockCandles` | `finnhub/models/stock_candles.py` |

### client.stock_dividends

- **Route**: `GET /stock/dividend`
- **Signature**: `def stock_dividends(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `from_`, `to`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `list[Dividends]`
- **Returns (raw)**: `ApiResult[list[Dividends], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Dividends` | `finnhub/models/dividends.py` |

### client.stock_lobbying

- **Route**: `GET /stock/lobbying`
- **Signature**: `def stock_lobbying(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `from_`, `to`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `LobbyingResult`
- **Returns (raw)**: `ApiResult[LobbyingResult, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LobbyingResult` | `finnhub/models/lobbying_result.py` |

### client.stock_nbbo

- **Route**: `GET /stock/bbo`
- **Signature**: `def stock_nbbo(symbol: str, date: Date, limit: int, skip: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `date`, `limit`, `skip`
- **Params**: `symbol` — query · `date` — query · `limit` — query · `skip` — query
- **Returns (parsed)**: `HistoricalNbbo`
- **Returns (raw)**: `ApiResult[HistoricalNbbo, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `HistoricalNbbo` | `finnhub/models/historical_nbbo.py` |

### client.stock_presentation

- **Route**: `GET /stock/presentation`
- **Signature**: `def stock_presentation(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `StockPresentation`
- **Returns (raw)**: `ApiResult[StockPresentation, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StockPresentation` | `finnhub/models/stock_presentation.py` |

### client.stock_splits

- **Route**: `GET /stock/split`
- **Signature**: `def stock_splits(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `from_`, `to`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `list[Split]`
- **Returns (raw)**: `ApiResult[list[Split], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Split` | `finnhub/models/split.py` |

### client.stock_symbols

- **Route**: `GET /stock/symbol`
- **Signature**: `def stock_symbols(exchange: str, *, mic: str | None = None, security_type: str | None = None, currency: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `exchange`
- **Params**: `exchange` — query · `mic` — query · `security_type` — query `securityType` · `currency` — query
- **Returns (parsed)**: `list[StockSymbol]`
- **Returns (raw)**: `ApiResult[list[StockSymbol], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StockSymbol` | `finnhub/models/stock_symbol.py` |

### client.stock_tick

- **Route**: `GET /stock/tick`
- **Signature**: `def stock_tick(symbol: str, date: Date, limit: int, skip: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `date`, `limit`, `skip`
- **Params**: `symbol` — query · `date` — query · `limit` — query · `skip` — query
- **Returns (parsed)**: `TickData`
- **Returns (raw)**: `ApiResult[TickData, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TickData` | `finnhub/models/tick_data.py` |

### client.stock_usa_spending

- **Route**: `GET /stock/usa-spending`
- **Signature**: `def stock_usa_spending(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `from_`, `to`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `UsaSpendingResult`
- **Returns (raw)**: `ApiResult[UsaSpendingResult, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UsaSpendingResult` | `finnhub/models/usa_spending_result.py` |

### client.stock_uspto_patent

- **Route**: `GET /stock/uspto-patent`
- **Signature**: `def stock_uspto_patent(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `from_`, `to`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `UsptoPatentResult`
- **Returns (raw)**: `ApiResult[UsptoPatentResult, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UsptoPatentResult` | `finnhub/models/uspto_patent_result.py` |

### client.stock_visa_application

- **Route**: `GET /stock/visa-application`
- **Signature**: `def stock_visa_application(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `from_`, `to`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `VisaApplicationResult`
- **Returns (raw)**: `ApiResult[VisaApplicationResult, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VisaApplicationResult` | `finnhub/models/visa_application_result.py` |

### client.supply_chain_relationships

- **Route**: `GET /stock/supply-chain`
- **Signature**: `def supply_chain_relationships(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `SupplyChainRelationships`
- **Returns (raw)**: `ApiResult[SupplyChainRelationships, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SupplyChainRelationships` | `finnhub/models/supply_chain_relationships.py` |

### client.support_resistance

- **Route**: `GET /scan/support-resistance`
- **Signature**: `def support_resistance(symbol: str, resolution: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `resolution`
- **Params**: `symbol` — query · `resolution` — query
- **Returns (parsed)**: `SupportResistance`
- **Returns (raw)**: `ApiResult[SupportResistance, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SupportResistance` | `finnhub/models/support_resistance.py` |

### client.symbol_change

- **Route**: `GET /ca/symbol-change`
- **Signature**: `def symbol_change(from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `from_`, `to`
- **Params**: `from_` — query `from` · `to` — query
- **Returns (parsed)**: `SymbolChange`
- **Returns (raw)**: `ApiResult[SymbolChange, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SymbolChange` | `finnhub/models/symbol_change.py` |

### client.symbol_search

- **Route**: `GET /search`
- **Signature**: `def symbol_search(q: str, *, exchange: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `q`
- **Params**: `q` — query · `exchange` — query
- **Returns (parsed)**: `SymbolLookup`
- **Returns (raw)**: `ApiResult[SymbolLookup, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SymbolLookup` | `finnhub/models/symbol_lookup.py` |

### client.technical_indicator

- **Route**: `GET /indicator`
- **Signature**: `def technical_indicator(symbol: str, resolution: str, from_: int, to: int, indicator: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `resolution`, `from_`, `to`, `indicator`
- **Params**: `symbol` — query · `resolution` — query · `from_` — query `from` · `to` — query · `indicator` — query
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, RawError]`
- **Error**: `RawError` — **Case B**

### client.transcripts

- **Route**: `GET /stock/transcripts`
- **Signature**: `def transcripts(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — query
- **Returns (parsed)**: `EarningsCallTranscripts`
- **Returns (raw)**: `ApiResult[EarningsCallTranscripts, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EarningsCallTranscripts` | `finnhub/models/earnings_call_transcripts.py` |

### client.transcripts_list

- **Route**: `GET /stock/transcripts/list`
- **Signature**: `def transcripts_list(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `EarningsCallTranscriptsList`
- **Returns (raw)**: `ApiResult[EarningsCallTranscriptsList, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EarningsCallTranscriptsList` | `finnhub/models/earnings_call_transcripts_list.py` |

### client.upgrade_downgrade

- **Route**: `GET /stock/upgrade-downgrade`
- **Signature**: `def upgrade_downgrade(*, symbol: str | None = None, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `list[UpgradeDowngrade]`
- **Returns (raw)**: `ApiResult[list[UpgradeDowngrade], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpgradeDowngrade` | `finnhub/models/upgrade_downgrade.py` |

