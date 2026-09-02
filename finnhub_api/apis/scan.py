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
from ..models.aggregate_indicators import AggregateIndicators
from ..models.pattern_recognition import PatternRecognition
from ..models.support_resistance import SupportResistance
from ..server.server import Server


class Scan:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ScanWithRawResponse(client, server, auth)

    def aggregate_indicator(
        self, symbol: str, resolution: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AggregateIndicators:
        """Get aggregate signal of multiple technical indicators such as MACD, RSI, Moving Average v.v. A full list of
        indicators can be found <a
        href="https://docs.google.com/spreadsheets/d/1MWuy0WuT2yVlxr1KbPdggVygMZtJfunDnhe-C0GEXYM/edit?usp=sharing"
        target="_blank">here</a>.

        Args:
            symbol: symbol
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.aggregate_indicator(symbol, resolution, request_options=request_options).unwrap()

    def pattern_recognition(
        self, symbol: str, resolution: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PatternRecognition:
        """Run pattern recognition algorithm on a symbol. Support double top/bottom, triple top/bottom, head and
        shoulders, triangle, wedge, channel, flag, and candlestick patterns.

        Args:
            symbol: Symbol
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.pattern_recognition(symbol, resolution, request_options=request_options).unwrap()

    def support_resistance(
        self, symbol: str, resolution: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SupportResistance:
        """Get support and resistance levels for a symbol.

        Args:
            symbol: Symbol
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.support_resistance(symbol, resolution, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ScanWithRawResponse:
        return self._with_raw_response


class AsyncScan:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncScanWithRawResponse(client, server, auth)

    async def aggregate_indicator(
        self, symbol: str, resolution: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AggregateIndicators:
        """Get aggregate signal of multiple technical indicators such as MACD, RSI, Moving Average v.v. A full list of
        indicators can be found <a
        href="https://docs.google.com/spreadsheets/d/1MWuy0WuT2yVlxr1KbPdggVygMZtJfunDnhe-C0GEXYM/edit?usp=sharing"
        target="_blank">here</a>.

        Args:
            symbol: symbol
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.aggregate_indicator(symbol, resolution, request_options=request_options)
        ).unwrap()

    async def pattern_recognition(
        self, symbol: str, resolution: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PatternRecognition:
        """Run pattern recognition algorithm on a symbol. Support double top/bottom, triple top/bottom, head and
        shoulders, triangle, wedge, channel, flag, and candlestick patterns.

        Args:
            symbol: Symbol
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.pattern_recognition(symbol, resolution, request_options=request_options)
        ).unwrap()

    async def support_resistance(
        self, symbol: str, resolution: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SupportResistance:
        """Get support and resistance levels for a symbol.

        Args:
            symbol: Symbol
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.support_resistance(symbol, resolution, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncScanWithRawResponse:
        return self._with_raw_response


class ScanWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def aggregate_indicator(
        self, symbol: str, resolution: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AggregateIndicators, RawError]:
        """Get aggregate signal of multiple technical indicators such as MACD, RSI, Moving Average v.v. A full list of
        indicators can be found <a
        href="https://docs.google.com/spreadsheets/d/1MWuy0WuT2yVlxr1KbPdggVygMZtJfunDnhe-C0GEXYM/edit?usp=sharing"
        target="_blank">here</a>.

        Args:
            symbol: symbol
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/scan/technical-indicator"),
            query_params=[param[str]("symbol", symbol), param[str]("resolution", resolution)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[AggregateIndicators],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def pattern_recognition(
        self, symbol: str, resolution: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PatternRecognition, RawError]:
        """Run pattern recognition algorithm on a symbol. Support double top/bottom, triple top/bottom, head and
        shoulders, triangle, wedge, channel, flag, and candlestick patterns.

        Args:
            symbol: Symbol
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/scan/pattern"),
            query_params=[param[str]("symbol", symbol), param[str]("resolution", resolution)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[PatternRecognition],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def support_resistance(
        self, symbol: str, resolution: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SupportResistance, RawError]:
        """Get support and resistance levels for a symbol.

        Args:
            symbol: Symbol
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/scan/support-resistance"),
            query_params=[param[str]("symbol", symbol), param[str]("resolution", resolution)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[SupportResistance],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncScanWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def aggregate_indicator(
        self, symbol: str, resolution: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AggregateIndicators, RawError]:
        """Get aggregate signal of multiple technical indicators such as MACD, RSI, Moving Average v.v. A full list of
        indicators can be found <a
        href="https://docs.google.com/spreadsheets/d/1MWuy0WuT2yVlxr1KbPdggVygMZtJfunDnhe-C0GEXYM/edit?usp=sharing"
        target="_blank">here</a>.

        Args:
            symbol: symbol
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/scan/technical-indicator"),
            query_params=[param[str]("symbol", symbol), param[str]("resolution", resolution)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[AggregateIndicators],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def pattern_recognition(
        self, symbol: str, resolution: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PatternRecognition, RawError]:
        """Run pattern recognition algorithm on a symbol. Support double top/bottom, triple top/bottom, head and
        shoulders, triangle, wedge, channel, flag, and candlestick patterns.

        Args:
            symbol: Symbol
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/scan/pattern"),
            query_params=[param[str]("symbol", symbol), param[str]("resolution", resolution)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[PatternRecognition],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def support_resistance(
        self, symbol: str, resolution: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SupportResistance, RawError]:
        """Get support and resistance levels for a symbol.

        Args:
            symbol: Symbol
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/scan/support-resistance"),
            query_params=[param[str]("symbol", symbol), param[str]("resolution", resolution)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[SupportResistance],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
