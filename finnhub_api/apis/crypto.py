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
from ..models.crypto_candles import CryptoCandles
from ..models.crypto_profile import CryptoProfile
from ..models.crypto_symbol import CryptoSymbol
from ..server.server import Server


class Crypto:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CryptoWithRawResponse(client, server, auth)

    def crypto_candles(
        self, symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> CryptoCandles:
        """Get candlestick data for crypto symbols.

        Args:
            symbol: Use symbol returned in <code>/crypto/symbol</code> endpoint for this field.
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            from_: UNIX timestamp. Interval initial value.
            to: UNIX timestamp. Interval end value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.crypto_candles(
            symbol, resolution, from_, to, request_options=request_options
        ).unwrap()

    def crypto_exchanges(self, *, request_options: RequestOptionsOrDict | None = None) -> list[str]:
        """List supported crypto exchanges

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.crypto_exchanges(request_options=request_options).unwrap()

    def crypto_profile(self, symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> CryptoProfile:
        """Get crypto's profile.

        Args:
            symbol: Crypto symbol such as BTC or ETH.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.crypto_profile(symbol, request_options=request_options).unwrap()

    def crypto_symbols(
        self, exchange: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[CryptoSymbol]:
        """List supported crypto symbols by exchange

        Args:
            exchange: Exchange you want to get the list of symbols from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.crypto_symbols(exchange, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> CryptoWithRawResponse:
        return self._with_raw_response


class AsyncCrypto:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCryptoWithRawResponse(client, server, auth)

    async def crypto_candles(
        self, symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> CryptoCandles:
        """Get candlestick data for crypto symbols.

        Args:
            symbol: Use symbol returned in <code>/crypto/symbol</code> endpoint for this field.
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
            await self._with_raw_response.crypto_candles(symbol, resolution, from_, to, request_options=request_options)
        ).unwrap()

    async def crypto_exchanges(self, *, request_options: RequestOptionsOrDict | None = None) -> list[str]:
        """List supported crypto exchanges

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.crypto_exchanges(request_options=request_options)).unwrap()

    async def crypto_profile(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CryptoProfile:
        """Get crypto's profile.

        Args:
            symbol: Crypto symbol such as BTC or ETH.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.crypto_profile(symbol, request_options=request_options)).unwrap()

    async def crypto_symbols(
        self, exchange: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[CryptoSymbol]:
        """List supported crypto symbols by exchange

        Args:
            exchange: Exchange you want to get the list of symbols from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.crypto_symbols(exchange, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncCryptoWithRawResponse:
        return self._with_raw_response


class CryptoWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def crypto_candles(
        self, symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CryptoCandles, RawError]:
        """Get candlestick data for crypto symbols.

        Args:
            symbol: Use symbol returned in <code>/crypto/symbol</code> endpoint for this field.
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            from_: UNIX timestamp. Interval initial value.
            to: UNIX timestamp. Interval end value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/crypto/candle"),
            query_params=[
                param[str]("symbol", symbol),
                param[str]("resolution", resolution),
                param[int]("from", from_),
                param[int]("to", to),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[CryptoCandles],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def crypto_exchanges(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[str], RawError]:
        """List supported crypto exchanges

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/crypto/exchange"),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[str]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def crypto_profile(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CryptoProfile, RawError]:
        """Get crypto's profile.

        Args:
            symbol: Crypto symbol such as BTC or ETH.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/crypto/profile"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[CryptoProfile],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def crypto_symbols(
        self, exchange: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[CryptoSymbol], RawError]:
        """List supported crypto symbols by exchange

        Args:
            exchange: Exchange you want to get the list of symbols from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/crypto/symbol"),
            query_params=[param[str]("exchange", exchange)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[CryptoSymbol]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncCryptoWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def crypto_candles(
        self, symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CryptoCandles, RawError]:
        """Get candlestick data for crypto symbols.

        Args:
            symbol: Use symbol returned in <code>/crypto/symbol</code> endpoint for this field.
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            from_: UNIX timestamp. Interval initial value.
            to: UNIX timestamp. Interval end value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/crypto/candle"),
            query_params=[
                param[str]("symbol", symbol),
                param[str]("resolution", resolution),
                param[int]("from", from_),
                param[int]("to", to),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[CryptoCandles],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def crypto_exchanges(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[str], RawError]:
        """List supported crypto exchanges

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/crypto/exchange"),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[str]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def crypto_profile(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CryptoProfile, RawError]:
        """Get crypto's profile.

        Args:
            symbol: Crypto symbol such as BTC or ETH.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/crypto/profile"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[CryptoProfile],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def crypto_symbols(
        self, exchange: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[CryptoSymbol], RawError]:
        """List supported crypto symbols by exchange

        Args:
            exchange: Exchange you want to get the list of symbols from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/crypto/symbol"),
            query_params=[param[str]("exchange", exchange)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[CryptoSymbol]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
