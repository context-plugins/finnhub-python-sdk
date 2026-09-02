from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    Date,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.dividends import Dividends
from ..models.dividends2 import Dividends2
from ..models.historical_market_cap_data import HistoricalMarketCapData
from ..models.historical_nbbo import HistoricalNbbo
from ..models.last_bid_ask import LastBidAsk
from ..models.market_holiday import MarketHoliday
from ..models.market_status import MarketStatus
from ..models.price_metrics import PriceMetrics
from ..models.split import Split
from ..models.stock_candles import StockCandles
from ..models.stock_symbol import StockSymbol
from ..models.tick_data import TickData
from ..server.server import Server


class StockPrices:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = StockPricesWithRawResponse(client, server, auth)

    def company_peers(
        self, symbol: str, *, grouping: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[str]:
        """Get company peers. Return a list of peers operating in the same country and sector/industry.

        Args:
            symbol: Symbol of the company: AAPL.
            grouping: Specify the grouping criteria for choosing peers.Supporter values: <code>sector</code>,
                <code>industry</code>, <code>subIndustry</code>. Default to <code>subIndustry</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.company_peers(
            symbol, grouping=grouping, request_options=request_options
        ).unwrap()

    def historical_market_cap(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> HistoricalMarketCapData:
        """Get historical market cap data for global companies.

        Args:
            symbol: Company symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.historical_market_cap(
            symbol, from_, to, request_options=request_options
        ).unwrap()

    def market_holiday(self, exchange: str, *, request_options: RequestOptionsOrDict | None = None) -> MarketHoliday:
        """Get a list of holidays for global exchanges.

        Args:
            exchange: Exchange code.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.market_holiday(exchange, request_options=request_options).unwrap()

    def market_status(self, exchange: str, *, request_options: RequestOptionsOrDict | None = None) -> MarketStatus:
        """Get current market status for global exchanges (whether exchanges are open or close).

        Args:
            exchange: Exchange code.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.market_status(exchange, request_options=request_options).unwrap()

    def price_metrics(
        self, symbol: str, *, date: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> PriceMetrics:
        """Get company price performance statistics such as 52-week high/low, YTD return and much more.

        Args:
            symbol: Symbol of the company: AAPL.
            date: Get data on a specific date in the past. The data is available weekly so your date will be
                automatically adjusted to the last day of that week.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.price_metrics(symbol, date=date, request_options=request_options).unwrap()

    def stock_basic_dividends(self, symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> Dividends2:
        """Get global dividends data.

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.stock_basic_dividends(symbol, request_options=request_options).unwrap()

    def stock_bidask(self, symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> LastBidAsk:
        """Get last bid/ask data for US stocks.

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.stock_bidask(symbol, request_options=request_options).unwrap()

    def stock_candles(
        self, symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> StockCandles:
        """<p>Get candlestick data (OHLCV) for stocks.</p><p>Daily data will be adjusted for Splits. Intraday data will
        remain unadjusted. Only 1 month of intraday will be returned at a time. If you need more historical intraday
        data, please use the from and to params iteratively to request more data.</p>

        Args:
            symbol: Symbol.
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            from_: UNIX timestamp. Interval initial value.
            to: UNIX timestamp. Interval end value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.stock_candles(
            symbol, resolution, from_, to, request_options=request_options
        ).unwrap()

    def stock_dividends(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Dividends]:
        """Get dividends data for common stocks going back 30 years.

        Args:
            symbol: Symbol.
            from_: YYYY-MM-DD.
            to: YYYY-MM-DD.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.stock_dividends(symbol, from_, to, request_options=request_options).unwrap()

    def stock_nbbo(
        self, symbol: str, date: Date, limit: int, skip: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> HistoricalNbbo:
        """<p>Get historical best bid and offer for US stocks, LSE, TSX, Euronext and Deutsche Borse.</p><p>For US
        market, this endpoint only serves historical NBBO from the beginning of 2023. To download more historical data,
        please visit our bulk download page in the Dashboard <a target="_blank"
        href="/dashboard/download",>here</a>.</p>

        Args:
            symbol: Symbol.
            date: Date: 2020-04-02.
            limit: Limit number of ticks returned. Maximum value: <code>25000</code>
            skip: Number of ticks to skip. Use this parameter to loop through the entire data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.stock_nbbo(symbol, date, limit, skip, request_options=request_options).unwrap()

    def stock_splits(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Split]:
        """Get splits data for stocks.

        Args:
            symbol: Symbol.
            from_: YYYY-MM-DD.
            to: YYYY-MM-DD.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.stock_splits(symbol, from_, to, request_options=request_options).unwrap()

    def stock_symbols(
        self,
        exchange: str,
        *,
        mic: str | None = None,
        security_type: str | None = None,
        currency: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[StockSymbol]:
        """List supported stocks. We use the following symbology to identify stocks on Finnhub
        <code>Exchange_Ticker.Exchange_Code</code>. A list of supported exchange codes can be found <a
        href="https://docs.google.com/spreadsheets/d/1I3pBxjfXB056-g_JYf_6o3Rns3BV2kMGG1nCatb91ls/edit?usp=sharing"
        target="_blank">here</a>.

        Args:
            exchange: Exchange you want to get the list of symbols from. List of exchange codes can be found <a
                href="https://docs.google.com/spreadsheets/d/1I3pBxjfXB056-g_JYf_6o3Rns3BV2kMGG1nCatb91ls/edit?usp=sharing"
                target="_blank">here</a>.
            mic: Filter by MIC code.
            security_type: Filter by security type used by OpenFigi standard.
            currency: Filter by currency.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.stock_symbols(
            exchange, mic=mic, security_type=security_type, currency=currency, request_options=request_options
        ).unwrap()

    def stock_tick(
        self, symbol: str, date: Date, limit: int, skip: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> TickData:
        """<p>Get historical tick data for global exchanges.</p><p>For more historical tick data, you can visit our bulk
        download page in the Dashboard <a target="_blank" href="/dashboard/download",>here</a> to speed up the download
        process.</p><table class="table table-hover">
          <thead>
            <tr>
              <th>Exchange</th>
              <th>Segment</th>
              <th>Delay</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-blue">US CTA/UTP</th>
              <td>Full SIP</td>
              <td>End-of-day</td>
            </tr>
            <tr>
              <td class="text-blue">TSX</th>
              <td><ul><li>TSX</li><li>TSX Venture</li><li>Index</li></ul></td>
              <td>End-of-day</td>
            </tr>
            <tr>
              <td class="text-blue">LSE</th>
              <td><ul><li>London Stock Exchange (L)</li><li>LSE International (L)</li><li>LSE European
                (L)</li></ul></td>
              <td>15 minute</td>
            </tr>
            <tr>
              <td class="text-blue">Euronext</th>
              <td><ul> <li>Euronext Paris (PA)</li> <li>Euronext Amsterdam (AS)</li> <li>Euronext Lisbon (LS)</li>
                <li>Euronext Brussels (BR)</li> <li>Euronext Oslo (OL)</li> <li>Euronext London (LN)</li> <li>Euronext
                Dublin (IR)</li> <li>Index</li> <li>Warrant</li></ul></td>
              <td>End-of-day</td>
            </tr>
            <tr>
              <td class="text-blue">Deutsche Börse</th>
              <td><ul> <li>Frankfurt (F)</li> <li>Xetra (DE)</li> <li>Duesseldorf (DU)</li> <li>Hamburg (HM)</li>
                <li>Berlin (BE)</li> <li>Hanover (HA)</li> <li>Stoxx (SX)</li> <li>TradeGate (TG)</li> <li>Zertifikate
                (SC)</li> <li>Index</li> <li>Warrant</li></ul></td>
              <td>End-of-day</td>
            </tr>
          </tbody>
        </table>

        Args:
            symbol: Symbol.
            date: Date: 2020-04-02.
            limit: Limit number of ticks returned. Maximum value: <code>25000</code>
            skip: Number of ticks to skip. Use this parameter to loop through the entire data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.stock_tick(symbol, date, limit, skip, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> StockPricesWithRawResponse:
        return self._with_raw_response


class AsyncStockPrices:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncStockPricesWithRawResponse(client, server, auth)

    async def company_peers(
        self, symbol: str, *, grouping: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[str]:
        """Get company peers. Return a list of peers operating in the same country and sector/industry.

        Args:
            symbol: Symbol of the company: AAPL.
            grouping: Specify the grouping criteria for choosing peers.Supporter values: <code>sector</code>,
                <code>industry</code>, <code>subIndustry</code>. Default to <code>subIndustry</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.company_peers(symbol, grouping=grouping, request_options=request_options)
        ).unwrap()

    async def historical_market_cap(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> HistoricalMarketCapData:
        """Get historical market cap data for global companies.

        Args:
            symbol: Company symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.historical_market_cap(symbol, from_, to, request_options=request_options)
        ).unwrap()

    async def market_holiday(
        self, exchange: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MarketHoliday:
        """Get a list of holidays for global exchanges.

        Args:
            exchange: Exchange code.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.market_holiday(exchange, request_options=request_options)).unwrap()

    async def market_status(
        self, exchange: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MarketStatus:
        """Get current market status for global exchanges (whether exchanges are open or close).

        Args:
            exchange: Exchange code.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.market_status(exchange, request_options=request_options)).unwrap()

    async def price_metrics(
        self, symbol: str, *, date: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> PriceMetrics:
        """Get company price performance statistics such as 52-week high/low, YTD return and much more.

        Args:
            symbol: Symbol of the company: AAPL.
            date: Get data on a specific date in the past. The data is available weekly so your date will be
                automatically adjusted to the last day of that week.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.price_metrics(symbol, date=date, request_options=request_options)
        ).unwrap()

    async def stock_basic_dividends(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Dividends2:
        """Get global dividends data.

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.stock_basic_dividends(symbol, request_options=request_options)).unwrap()

    async def stock_bidask(self, symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> LastBidAsk:
        """Get last bid/ask data for US stocks.

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.stock_bidask(symbol, request_options=request_options)).unwrap()

    async def stock_candles(
        self, symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> StockCandles:
        """<p>Get candlestick data (OHLCV) for stocks.</p><p>Daily data will be adjusted for Splits. Intraday data will
        remain unadjusted. Only 1 month of intraday will be returned at a time. If you need more historical intraday
        data, please use the from and to params iteratively to request more data.</p>

        Args:
            symbol: Symbol.
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            from_: UNIX timestamp. Interval initial value.
            to: UNIX timestamp. Interval end value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.stock_candles(symbol, resolution, from_, to, request_options=request_options)
        ).unwrap()

    async def stock_dividends(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Dividends]:
        """Get dividends data for common stocks going back 30 years.

        Args:
            symbol: Symbol.
            from_: YYYY-MM-DD.
            to: YYYY-MM-DD.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.stock_dividends(symbol, from_, to, request_options=request_options)
        ).unwrap()

    async def stock_nbbo(
        self, symbol: str, date: Date, limit: int, skip: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> HistoricalNbbo:
        """<p>Get historical best bid and offer for US stocks, LSE, TSX, Euronext and Deutsche Borse.</p><p>For US
        market, this endpoint only serves historical NBBO from the beginning of 2023. To download more historical data,
        please visit our bulk download page in the Dashboard <a target="_blank"
        href="/dashboard/download",>here</a>.</p>

        Args:
            symbol: Symbol.
            date: Date: 2020-04-02.
            limit: Limit number of ticks returned. Maximum value: <code>25000</code>
            skip: Number of ticks to skip. Use this parameter to loop through the entire data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.stock_nbbo(symbol, date, limit, skip, request_options=request_options)
        ).unwrap()

    async def stock_splits(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Split]:
        """Get splits data for stocks.

        Args:
            symbol: Symbol.
            from_: YYYY-MM-DD.
            to: YYYY-MM-DD.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.stock_splits(symbol, from_, to, request_options=request_options)).unwrap()

    async def stock_symbols(
        self,
        exchange: str,
        *,
        mic: str | None = None,
        security_type: str | None = None,
        currency: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[StockSymbol]:
        """List supported stocks. We use the following symbology to identify stocks on Finnhub
        <code>Exchange_Ticker.Exchange_Code</code>. A list of supported exchange codes can be found <a
        href="https://docs.google.com/spreadsheets/d/1I3pBxjfXB056-g_JYf_6o3Rns3BV2kMGG1nCatb91ls/edit?usp=sharing"
        target="_blank">here</a>.

        Args:
            exchange: Exchange you want to get the list of symbols from. List of exchange codes can be found <a
                href="https://docs.google.com/spreadsheets/d/1I3pBxjfXB056-g_JYf_6o3Rns3BV2kMGG1nCatb91ls/edit?usp=sharing"
                target="_blank">here</a>.
            mic: Filter by MIC code.
            security_type: Filter by security type used by OpenFigi standard.
            currency: Filter by currency.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.stock_symbols(
                exchange, mic=mic, security_type=security_type, currency=currency, request_options=request_options
            )
        ).unwrap()

    async def stock_tick(
        self, symbol: str, date: Date, limit: int, skip: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> TickData:
        """<p>Get historical tick data for global exchanges.</p><p>For more historical tick data, you can visit our bulk
        download page in the Dashboard <a target="_blank" href="/dashboard/download",>here</a> to speed up the download
        process.</p><table class="table table-hover">
          <thead>
            <tr>
              <th>Exchange</th>
              <th>Segment</th>
              <th>Delay</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-blue">US CTA/UTP</th>
              <td>Full SIP</td>
              <td>End-of-day</td>
            </tr>
            <tr>
              <td class="text-blue">TSX</th>
              <td><ul><li>TSX</li><li>TSX Venture</li><li>Index</li></ul></td>
              <td>End-of-day</td>
            </tr>
            <tr>
              <td class="text-blue">LSE</th>
              <td><ul><li>London Stock Exchange (L)</li><li>LSE International (L)</li><li>LSE European
                (L)</li></ul></td>
              <td>15 minute</td>
            </tr>
            <tr>
              <td class="text-blue">Euronext</th>
              <td><ul> <li>Euronext Paris (PA)</li> <li>Euronext Amsterdam (AS)</li> <li>Euronext Lisbon (LS)</li>
                <li>Euronext Brussels (BR)</li> <li>Euronext Oslo (OL)</li> <li>Euronext London (LN)</li> <li>Euronext
                Dublin (IR)</li> <li>Index</li> <li>Warrant</li></ul></td>
              <td>End-of-day</td>
            </tr>
            <tr>
              <td class="text-blue">Deutsche Börse</th>
              <td><ul> <li>Frankfurt (F)</li> <li>Xetra (DE)</li> <li>Duesseldorf (DU)</li> <li>Hamburg (HM)</li>
                <li>Berlin (BE)</li> <li>Hanover (HA)</li> <li>Stoxx (SX)</li> <li>TradeGate (TG)</li> <li>Zertifikate
                (SC)</li> <li>Index</li> <li>Warrant</li></ul></td>
              <td>End-of-day</td>
            </tr>
          </tbody>
        </table>

        Args:
            symbol: Symbol.
            date: Date: 2020-04-02.
            limit: Limit number of ticks returned. Maximum value: <code>25000</code>
            skip: Number of ticks to skip. Use this parameter to loop through the entire data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.stock_tick(symbol, date, limit, skip, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncStockPricesWithRawResponse:
        return self._with_raw_response


class StockPricesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def company_peers(
        self, symbol: str, *, grouping: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[str], RawError]:
        """Get company peers. Return a list of peers operating in the same country and sector/industry.

        Args:
            symbol: Symbol of the company: AAPL.
            grouping: Specify the grouping criteria for choosing peers.Supporter values: <code>sector</code>,
                <code>industry</code>, <code>subIndustry</code>. Default to <code>subIndustry</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/peers"),
            query_params=[param[str]("symbol", symbol), param[str | None]("grouping", grouping)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[str]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def historical_market_cap(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[HistoricalMarketCapData, RawError]:
        """Get historical market cap data for global companies.

        Args:
            symbol: Company symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/historical-market-cap"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[HistoricalMarketCapData],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def market_holiday(
        self, exchange: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MarketHoliday, RawError]:
        """Get a list of holidays for global exchanges.

        Args:
            exchange: Exchange code.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/market-holiday"),
            query_params=[param[str]("exchange", exchange)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[MarketHoliday],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def market_status(
        self, exchange: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MarketStatus, RawError]:
        """Get current market status for global exchanges (whether exchanges are open or close).

        Args:
            exchange: Exchange code.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/market-status"),
            query_params=[param[str]("exchange", exchange)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[MarketStatus],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def price_metrics(
        self, symbol: str, *, date: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PriceMetrics, RawError]:
        """Get company price performance statistics such as 52-week high/low, YTD return and much more.

        Args:
            symbol: Symbol of the company: AAPL.
            date: Get data on a specific date in the past. The data is available weekly so your date will be
                automatically adjusted to the last day of that week.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/price-metric"),
            query_params=[param[str]("symbol", symbol), param[str | None]("date", date)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[PriceMetrics],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stock_basic_dividends(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Dividends2, RawError]:
        """Get global dividends data.

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/dividend2"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[Dividends2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stock_bidask(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LastBidAsk, RawError]:
        """Get last bid/ask data for US stocks.

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/bidask"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[LastBidAsk],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stock_candles(
        self, symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StockCandles, RawError]:
        """<p>Get candlestick data (OHLCV) for stocks.</p><p>Daily data will be adjusted for Splits. Intraday data will
        remain unadjusted. Only 1 month of intraday will be returned at a time. If you need more historical intraday
        data, please use the from and to params iteratively to request more data.</p>

        Args:
            symbol: Symbol.
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            from_: UNIX timestamp. Interval initial value.
            to: UNIX timestamp. Interval end value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/candle"),
            query_params=[
                param[str]("symbol", symbol),
                param[str]("resolution", resolution),
                param[int]("from", from_),
                param[int]("to", to),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[StockCandles],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stock_dividends(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Dividends], RawError]:
        """Get dividends data for common stocks going back 30 years.

        Args:
            symbol: Symbol.
            from_: YYYY-MM-DD.
            to: YYYY-MM-DD.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/dividend"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[Dividends]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stock_nbbo(
        self, symbol: str, date: Date, limit: int, skip: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[HistoricalNbbo, RawError]:
        """<p>Get historical best bid and offer for US stocks, LSE, TSX, Euronext and Deutsche Borse.</p><p>For US
        market, this endpoint only serves historical NBBO from the beginning of 2023. To download more historical data,
        please visit our bulk download page in the Dashboard <a target="_blank"
        href="/dashboard/download",>here</a>.</p>

        Args:
            symbol: Symbol.
            date: Date: 2020-04-02.
            limit: Limit number of ticks returned. Maximum value: <code>25000</code>
            skip: Number of ticks to skip. Use this parameter to loop through the entire data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/bbo"),
            query_params=[
                param[str]("symbol", symbol),
                param[Date]("date", date),
                param[int]("limit", limit),
                param[int]("skip", skip),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[HistoricalNbbo],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stock_splits(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Split], RawError]:
        """Get splits data for stocks.

        Args:
            symbol: Symbol.
            from_: YYYY-MM-DD.
            to: YYYY-MM-DD.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/split"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[Split]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stock_symbols(
        self,
        exchange: str,
        *,
        mic: str | None = None,
        security_type: str | None = None,
        currency: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[StockSymbol], RawError]:
        """List supported stocks. We use the following symbology to identify stocks on Finnhub
        <code>Exchange_Ticker.Exchange_Code</code>. A list of supported exchange codes can be found <a
        href="https://docs.google.com/spreadsheets/d/1I3pBxjfXB056-g_JYf_6o3Rns3BV2kMGG1nCatb91ls/edit?usp=sharing"
        target="_blank">here</a>.

        Args:
            exchange: Exchange you want to get the list of symbols from. List of exchange codes can be found <a
                href="https://docs.google.com/spreadsheets/d/1I3pBxjfXB056-g_JYf_6o3Rns3BV2kMGG1nCatb91ls/edit?usp=sharing"
                target="_blank">here</a>.
            mic: Filter by MIC code.
            security_type: Filter by security type used by OpenFigi standard.
            currency: Filter by currency.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/symbol"),
            query_params=[
                param[str]("exchange", exchange),
                param[str | None]("mic", mic),
                param[str | None]("securityType", security_type),
                param[str | None]("currency", currency),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[StockSymbol]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stock_tick(
        self, symbol: str, date: Date, limit: int, skip: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TickData, RawError]:
        """<p>Get historical tick data for global exchanges.</p><p>For more historical tick data, you can visit our bulk
        download page in the Dashboard <a target="_blank" href="/dashboard/download",>here</a> to speed up the download
        process.</p><table class="table table-hover">
          <thead>
            <tr>
              <th>Exchange</th>
              <th>Segment</th>
              <th>Delay</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-blue">US CTA/UTP</th>
              <td>Full SIP</td>
              <td>End-of-day</td>
            </tr>
            <tr>
              <td class="text-blue">TSX</th>
              <td><ul><li>TSX</li><li>TSX Venture</li><li>Index</li></ul></td>
              <td>End-of-day</td>
            </tr>
            <tr>
              <td class="text-blue">LSE</th>
              <td><ul><li>London Stock Exchange (L)</li><li>LSE International (L)</li><li>LSE European
                (L)</li></ul></td>
              <td>15 minute</td>
            </tr>
            <tr>
              <td class="text-blue">Euronext</th>
              <td><ul> <li>Euronext Paris (PA)</li> <li>Euronext Amsterdam (AS)</li> <li>Euronext Lisbon (LS)</li>
                <li>Euronext Brussels (BR)</li> <li>Euronext Oslo (OL)</li> <li>Euronext London (LN)</li> <li>Euronext
                Dublin (IR)</li> <li>Index</li> <li>Warrant</li></ul></td>
              <td>End-of-day</td>
            </tr>
            <tr>
              <td class="text-blue">Deutsche Börse</th>
              <td><ul> <li>Frankfurt (F)</li> <li>Xetra (DE)</li> <li>Duesseldorf (DU)</li> <li>Hamburg (HM)</li>
                <li>Berlin (BE)</li> <li>Hanover (HA)</li> <li>Stoxx (SX)</li> <li>TradeGate (TG)</li> <li>Zertifikate
                (SC)</li> <li>Index</li> <li>Warrant</li></ul></td>
              <td>End-of-day</td>
            </tr>
          </tbody>
        </table>

        Args:
            symbol: Symbol.
            date: Date: 2020-04-02.
            limit: Limit number of ticks returned. Maximum value: <code>25000</code>
            skip: Number of ticks to skip. Use this parameter to loop through the entire data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/tick"),
            query_params=[
                param[str]("symbol", symbol),
                param[Date]("date", date),
                param[int]("limit", limit),
                param[int]("skip", skip),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[TickData],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncStockPricesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def company_peers(
        self, symbol: str, *, grouping: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[str], RawError]:
        """Get company peers. Return a list of peers operating in the same country and sector/industry.

        Args:
            symbol: Symbol of the company: AAPL.
            grouping: Specify the grouping criteria for choosing peers.Supporter values: <code>sector</code>,
                <code>industry</code>, <code>subIndustry</code>. Default to <code>subIndustry</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/peers"),
            query_params=[param[str]("symbol", symbol), param[str | None]("grouping", grouping)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[str]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def historical_market_cap(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[HistoricalMarketCapData, RawError]:
        """Get historical market cap data for global companies.

        Args:
            symbol: Company symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/historical-market-cap"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[HistoricalMarketCapData],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def market_holiday(
        self, exchange: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MarketHoliday, RawError]:
        """Get a list of holidays for global exchanges.

        Args:
            exchange: Exchange code.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/market-holiday"),
            query_params=[param[str]("exchange", exchange)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[MarketHoliday],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def market_status(
        self, exchange: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MarketStatus, RawError]:
        """Get current market status for global exchanges (whether exchanges are open or close).

        Args:
            exchange: Exchange code.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/market-status"),
            query_params=[param[str]("exchange", exchange)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[MarketStatus],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def price_metrics(
        self, symbol: str, *, date: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PriceMetrics, RawError]:
        """Get company price performance statistics such as 52-week high/low, YTD return and much more.

        Args:
            symbol: Symbol of the company: AAPL.
            date: Get data on a specific date in the past. The data is available weekly so your date will be
                automatically adjusted to the last day of that week.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/price-metric"),
            query_params=[param[str]("symbol", symbol), param[str | None]("date", date)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[PriceMetrics],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def stock_basic_dividends(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Dividends2, RawError]:
        """Get global dividends data.

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/dividend2"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[Dividends2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def stock_bidask(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LastBidAsk, RawError]:
        """Get last bid/ask data for US stocks.

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/bidask"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[LastBidAsk],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def stock_candles(
        self, symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StockCandles, RawError]:
        """<p>Get candlestick data (OHLCV) for stocks.</p><p>Daily data will be adjusted for Splits. Intraday data will
        remain unadjusted. Only 1 month of intraday will be returned at a time. If you need more historical intraday
        data, please use the from and to params iteratively to request more data.</p>

        Args:
            symbol: Symbol.
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            from_: UNIX timestamp. Interval initial value.
            to: UNIX timestamp. Interval end value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/candle"),
            query_params=[
                param[str]("symbol", symbol),
                param[str]("resolution", resolution),
                param[int]("from", from_),
                param[int]("to", to),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[StockCandles],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def stock_dividends(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Dividends], RawError]:
        """Get dividends data for common stocks going back 30 years.

        Args:
            symbol: Symbol.
            from_: YYYY-MM-DD.
            to: YYYY-MM-DD.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/dividend"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[Dividends]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def stock_nbbo(
        self, symbol: str, date: Date, limit: int, skip: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[HistoricalNbbo, RawError]:
        """<p>Get historical best bid and offer for US stocks, LSE, TSX, Euronext and Deutsche Borse.</p><p>For US
        market, this endpoint only serves historical NBBO from the beginning of 2023. To download more historical data,
        please visit our bulk download page in the Dashboard <a target="_blank"
        href="/dashboard/download",>here</a>.</p>

        Args:
            symbol: Symbol.
            date: Date: 2020-04-02.
            limit: Limit number of ticks returned. Maximum value: <code>25000</code>
            skip: Number of ticks to skip. Use this parameter to loop through the entire data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/bbo"),
            query_params=[
                param[str]("symbol", symbol),
                param[Date]("date", date),
                param[int]("limit", limit),
                param[int]("skip", skip),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[HistoricalNbbo],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def stock_splits(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Split], RawError]:
        """Get splits data for stocks.

        Args:
            symbol: Symbol.
            from_: YYYY-MM-DD.
            to: YYYY-MM-DD.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/split"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[Split]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def stock_symbols(
        self,
        exchange: str,
        *,
        mic: str | None = None,
        security_type: str | None = None,
        currency: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[StockSymbol], RawError]:
        """List supported stocks. We use the following symbology to identify stocks on Finnhub
        <code>Exchange_Ticker.Exchange_Code</code>. A list of supported exchange codes can be found <a
        href="https://docs.google.com/spreadsheets/d/1I3pBxjfXB056-g_JYf_6o3Rns3BV2kMGG1nCatb91ls/edit?usp=sharing"
        target="_blank">here</a>.

        Args:
            exchange: Exchange you want to get the list of symbols from. List of exchange codes can be found <a
                href="https://docs.google.com/spreadsheets/d/1I3pBxjfXB056-g_JYf_6o3Rns3BV2kMGG1nCatb91ls/edit?usp=sharing"
                target="_blank">here</a>.
            mic: Filter by MIC code.
            security_type: Filter by security type used by OpenFigi standard.
            currency: Filter by currency.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/symbol"),
            query_params=[
                param[str]("exchange", exchange),
                param[str | None]("mic", mic),
                param[str | None]("securityType", security_type),
                param[str | None]("currency", currency),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[StockSymbol]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def stock_tick(
        self, symbol: str, date: Date, limit: int, skip: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TickData, RawError]:
        """<p>Get historical tick data for global exchanges.</p><p>For more historical tick data, you can visit our bulk
        download page in the Dashboard <a target="_blank" href="/dashboard/download",>here</a> to speed up the download
        process.</p><table class="table table-hover">
          <thead>
            <tr>
              <th>Exchange</th>
              <th>Segment</th>
              <th>Delay</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-blue">US CTA/UTP</th>
              <td>Full SIP</td>
              <td>End-of-day</td>
            </tr>
            <tr>
              <td class="text-blue">TSX</th>
              <td><ul><li>TSX</li><li>TSX Venture</li><li>Index</li></ul></td>
              <td>End-of-day</td>
            </tr>
            <tr>
              <td class="text-blue">LSE</th>
              <td><ul><li>London Stock Exchange (L)</li><li>LSE International (L)</li><li>LSE European
                (L)</li></ul></td>
              <td>15 minute</td>
            </tr>
            <tr>
              <td class="text-blue">Euronext</th>
              <td><ul> <li>Euronext Paris (PA)</li> <li>Euronext Amsterdam (AS)</li> <li>Euronext Lisbon (LS)</li>
                <li>Euronext Brussels (BR)</li> <li>Euronext Oslo (OL)</li> <li>Euronext London (LN)</li> <li>Euronext
                Dublin (IR)</li> <li>Index</li> <li>Warrant</li></ul></td>
              <td>End-of-day</td>
            </tr>
            <tr>
              <td class="text-blue">Deutsche Börse</th>
              <td><ul> <li>Frankfurt (F)</li> <li>Xetra (DE)</li> <li>Duesseldorf (DU)</li> <li>Hamburg (HM)</li>
                <li>Berlin (BE)</li> <li>Hanover (HA)</li> <li>Stoxx (SX)</li> <li>TradeGate (TG)</li> <li>Zertifikate
                (SC)</li> <li>Index</li> <li>Warrant</li></ul></td>
              <td>End-of-day</td>
            </tr>
          </tbody>
        </table>

        Args:
            symbol: Symbol.
            date: Date: 2020-04-02.
            limit: Limit number of ticks returned. Maximum value: <code>25000</code>
            skip: Number of ticks to skip. Use this parameter to loop through the entire data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/tick"),
            query_params=[
                param[str]("symbol", symbol),
                param[Date]("date", date),
                param[int]("limit", limit),
                param[int]("skip", skip),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[TickData],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
