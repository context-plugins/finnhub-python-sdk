<!-- Generated file — do not edit; regenerated with the SDK. -->

# StockPrices — operations

Accessor: `client.stock_prices` · Source: `finnhub_api/apis/stock_prices.py` · 13 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.stock_prices.company_peers

- **Route**: `GET /stock/peers`
- **Auth**: `api_key`
- **Signature**: `def company_peers(symbol: str, *, grouping: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `grouping` — query
- **Returns (parsed)**: `list[str]`
- **Returns (raw)**: `ApiResult[list[str], RawError]`
- **Error**: `RawError` — **Case B**

### client.stock_prices.historical_market_cap

- **Route**: `GET /stock/historical-market-cap`
- **Auth**: `api_key`
- **Signature**: `def historical_market_cap(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `from_`, `to`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `HistoricalMarketCapData`
- **Returns (raw)**: `ApiResult[HistoricalMarketCapData, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `HistoricalMarketCapData` | `finnhub_api/models/historical_market_cap_data.py` |

### client.stock_prices.market_holiday

- **Route**: `GET /stock/market-holiday`
- **Auth**: `api_key`
- **Signature**: `def market_holiday(exchange: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `exchange`
- **Params**: `exchange` — query
- **Returns (parsed)**: `MarketHoliday`
- **Returns (raw)**: `ApiResult[MarketHoliday, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MarketHoliday` | `finnhub_api/models/market_holiday.py` |

### client.stock_prices.market_status

- **Route**: `GET /stock/market-status`
- **Auth**: `api_key`
- **Signature**: `def market_status(exchange: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `exchange`
- **Params**: `exchange` — query
- **Returns (parsed)**: `MarketStatus`
- **Returns (raw)**: `ApiResult[MarketStatus, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MarketStatus` | `finnhub_api/models/market_status.py` |

### client.stock_prices.price_metrics

- **Route**: `GET /stock/price-metric`
- **Auth**: `api_key`
- **Signature**: `def price_metrics(symbol: str, *, date: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query · `date` — query
- **Returns (parsed)**: `PriceMetrics`
- **Returns (raw)**: `ApiResult[PriceMetrics, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PriceMetrics` | `finnhub_api/models/price_metrics.py` |

### client.stock_prices.stock_basic_dividends

- **Route**: `GET /stock/dividend2`
- **Auth**: `api_key`
- **Signature**: `def stock_basic_dividends(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `Dividends2`
- **Returns (raw)**: `ApiResult[Dividends2, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Dividends2` | `finnhub_api/models/dividends2.py` |

### client.stock_prices.stock_bidask

- **Route**: `GET /stock/bidask`
- **Auth**: `api_key`
- **Signature**: `def stock_bidask(symbol: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`
- **Params**: `symbol` — query
- **Returns (parsed)**: `LastBidAsk`
- **Returns (raw)**: `ApiResult[LastBidAsk, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LastBidAsk` | `finnhub_api/models/last_bid_ask.py` |

### client.stock_prices.stock_candles

- **Route**: `GET /stock/candle`
- **Auth**: `api_key`
- **Signature**: `def stock_candles(symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `resolution`, `from_`, `to`
- **Params**: `symbol` — query · `resolution` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `StockCandles`
- **Returns (raw)**: `ApiResult[StockCandles, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StockCandles` | `finnhub_api/models/stock_candles.py` |

### client.stock_prices.stock_dividends

- **Route**: `GET /stock/dividend`
- **Auth**: `api_key`
- **Signature**: `def stock_dividends(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `from_`, `to`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `list[Dividends]`
- **Returns (raw)**: `ApiResult[list[Dividends], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Dividends` | `finnhub_api/models/dividends.py` |

### client.stock_prices.stock_nbbo

- **Route**: `GET /stock/bbo`
- **Auth**: `api_key`
- **Signature**: `def stock_nbbo(symbol: str, date: Date, limit: int, skip: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `date`, `limit`, `skip`
- **Params**: `symbol` — query · `date` — query · `limit` — query · `skip` — query
- **Returns (parsed)**: `HistoricalNbbo`
- **Returns (raw)**: `ApiResult[HistoricalNbbo, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `HistoricalNbbo` | `finnhub_api/models/historical_nbbo.py` |

### client.stock_prices.stock_splits

- **Route**: `GET /stock/split`
- **Auth**: `api_key`
- **Signature**: `def stock_splits(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `from_`, `to`
- **Params**: `symbol` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `list[Split]`
- **Returns (raw)**: `ApiResult[list[Split], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Split` | `finnhub_api/models/split.py` |

### client.stock_prices.stock_symbols

- **Route**: `GET /stock/symbol`
- **Auth**: `api_key`
- **Signature**: `def stock_symbols(exchange: str, *, mic: str | None = None, security_type: str | None = None, currency: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `exchange`
- **Params**: `exchange` — query · `mic` — query · `security_type` — query `securityType` · `currency` — query
- **Returns (parsed)**: `list[StockSymbol]`
- **Returns (raw)**: `ApiResult[list[StockSymbol], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StockSymbol` | `finnhub_api/models/stock_symbol.py` |

### client.stock_prices.stock_tick

- **Route**: `GET /stock/tick`
- **Auth**: `api_key`
- **Signature**: `def stock_tick(symbol: str, date: Date, limit: int, skip: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `symbol`, `date`, `limit`, `skip`
- **Params**: `symbol` — query · `date` — query · `limit` — query · `skip` — query
- **Returns (parsed)**: `TickData`
- **Returns (raw)**: `ApiResult[TickData, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TickData` | `finnhub_api/models/tick_data.py` |

