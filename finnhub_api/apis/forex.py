from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.forex_candles import ForexCandles
from ..models.forex_symbol import ForexSymbol
from ..models.forexrates import Forexrates
from ..server.server import Server


class Forex:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ForexWithRawResponse(client, server, auth)

    def forex_candles(
        self, symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ForexCandles:
        """Get candlestick data for forex symbols.

        Args:
            symbol: Use symbol returned in <code>/forex/symbol</code> endpoint for this field.
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            from_: UNIX timestamp. Interval initial value.
            to: UNIX timestamp. Interval end value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.forex_candles(
            symbol, resolution, from_, to, request_options=request_options
        ).unwrap()

    def forex_exchanges(self, *, request_options: RequestOptionsOrDict | None = None) -> list[str]:
        """List supported forex exchanges

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.forex_exchanges(request_options=request_options).unwrap()

    def forex_rates(
        self, *, base: str | None = None, date: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Forexrates:
        """Get rates for all forex pairs. Ideal for currency conversion

        Args:
            base: Base currency. Default to EUR.
            date: Date. Leave blank to get the latest data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.forex_rates(base=base, date=date, request_options=request_options).unwrap()

    def forex_symbols(self, exchange: str, *, request_options: RequestOptionsOrDict | None = None) -> list[ForexSymbol]:
        """List supported forex symbols.

        Args:
            exchange: Exchange you want to get the list of symbols from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.forex_symbols(exchange, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ForexWithRawResponse:
        return self._with_raw_response


class AsyncForex:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncForexWithRawResponse(client, server, auth)

    async def forex_candles(
        self, symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ForexCandles:
        """Get candlestick data for forex symbols.

        Args:
            symbol: Use symbol returned in <code>/forex/symbol</code> endpoint for this field.
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
            await self._with_raw_response.forex_candles(symbol, resolution, from_, to, request_options=request_options)
        ).unwrap()

    async def forex_exchanges(self, *, request_options: RequestOptionsOrDict | None = None) -> list[str]:
        """List supported forex exchanges

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.forex_exchanges(request_options=request_options)).unwrap()

    async def forex_rates(
        self, *, base: str | None = None, date: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Forexrates:
        """Get rates for all forex pairs. Ideal for currency conversion

        Args:
            base: Base currency. Default to EUR.
            date: Date. Leave blank to get the latest data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.forex_rates(base=base, date=date, request_options=request_options)
        ).unwrap()

    async def forex_symbols(
        self, exchange: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ForexSymbol]:
        """List supported forex symbols.

        Args:
            exchange: Exchange you want to get the list of symbols from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.forex_symbols(exchange, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncForexWithRawResponse:
        return self._with_raw_response


class ForexWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def forex_candles(
        self, symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ForexCandles, RawError]:
        """Get candlestick data for forex symbols.

        Args:
            symbol: Use symbol returned in <code>/forex/symbol</code> endpoint for this field.
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            from_: UNIX timestamp. Interval initial value.
            to: UNIX timestamp. Interval end value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/forex/candle"),
            query_params=[
                param[str]("symbol", symbol),
                param[str]("resolution", resolution),
                param[int]("from", from_),
                param[int]("to", to),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[ForexCandles],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def forex_exchanges(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[str], RawError]:
        """List supported forex exchanges

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/forex/exchange"),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[str]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def forex_rates(
        self, *, base: str | None = None, date: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Forexrates, RawError]:
        """Get rates for all forex pairs. Ideal for currency conversion

        Args:
            base: Base currency. Default to EUR.
            date: Date. Leave blank to get the latest data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/forex/rates"),
            query_params=[param[str | None]("base", base), param[str | None]("date", date)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[Forexrates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def forex_symbols(
        self, exchange: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ForexSymbol], RawError]:
        """List supported forex symbols.

        Args:
            exchange: Exchange you want to get the list of symbols from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/forex/symbol"),
            query_params=[param[str]("exchange", exchange)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[ForexSymbol]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncForexWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def forex_candles(
        self, symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ForexCandles, RawError]:
        """Get candlestick data for forex symbols.

        Args:
            symbol: Use symbol returned in <code>/forex/symbol</code> endpoint for this field.
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            from_: UNIX timestamp. Interval initial value.
            to: UNIX timestamp. Interval end value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/forex/candle"),
            query_params=[
                param[str]("symbol", symbol),
                param[str]("resolution", resolution),
                param[int]("from", from_),
                param[int]("to", to),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[ForexCandles],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def forex_exchanges(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[str], RawError]:
        """List supported forex exchanges

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/forex/exchange"),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[str]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def forex_rates(
        self, *, base: str | None = None, date: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Forexrates, RawError]:
        """Get rates for all forex pairs. Ideal for currency conversion

        Args:
            base: Base currency. Default to EUR.
            date: Date. Leave blank to get the latest data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/forex/rates"),
            query_params=[param[str | None]("base", base), param[str | None]("date", date)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[Forexrates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def forex_symbols(
        self, exchange: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ForexSymbol], RawError]:
        """List supported forex symbols.

        Args:
            exchange: Exchange you want to get the list of symbols from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/forex/symbol"),
            query_params=[param[str]("exchange", exchange)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[ForexSymbol]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
