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
from ..models.indices_constituents import IndicesConstituents
from ..models.indices_historical_constituents import IndicesHistoricalConstituents
from ..server.server import Server


class Index:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = IndexWithRawResponse(client, server, auth)

    def indices_constituents(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> IndicesConstituents:
        """Get a list of index's constituents. A list of supported indices for this endpoint can be found <a
        href="/api/v1/index/list?token=" target="_blank">here</a>.

        Args:
            symbol: symbol
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.indices_constituents(symbol, request_options=request_options).unwrap()

    def indices_historical_constituents(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> IndicesHistoricalConstituents:
        """Get full history of index's constituents including symbols and dates of joining and leaving the Index. A list
        of supported indices for this endpoint can be found <a href="/api/v1/index/historical-list?token="
        target="_blank">here</a>.

        Args:
            symbol: symbol
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.indices_historical_constituents(symbol, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> IndexWithRawResponse:
        return self._with_raw_response


class AsyncIndex:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncIndexWithRawResponse(client, server, auth)

    async def indices_constituents(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> IndicesConstituents:
        """Get a list of index's constituents. A list of supported indices for this endpoint can be found <a
        href="/api/v1/index/list?token=" target="_blank">here</a>.

        Args:
            symbol: symbol
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.indices_constituents(symbol, request_options=request_options)).unwrap()

    async def indices_historical_constituents(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> IndicesHistoricalConstituents:
        """Get full history of index's constituents including symbols and dates of joining and leaving the Index. A list
        of supported indices for this endpoint can be found <a href="/api/v1/index/historical-list?token="
        target="_blank">here</a>.

        Args:
            symbol: symbol
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.indices_historical_constituents(symbol, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncIndexWithRawResponse:
        return self._with_raw_response


class IndexWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def indices_constituents(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[IndicesConstituents, RawError]:
        """Get a list of index's constituents. A list of supported indices for this endpoint can be found <a
        href="/api/v1/index/list?token=" target="_blank">here</a>.

        Args:
            symbol: symbol
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/index/constituents"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[IndicesConstituents],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def indices_historical_constituents(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[IndicesHistoricalConstituents, RawError]:
        """Get full history of index's constituents including symbols and dates of joining and leaving the Index. A list
        of supported indices for this endpoint can be found <a href="/api/v1/index/historical-list?token="
        target="_blank">here</a>.

        Args:
            symbol: symbol
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/index/historical-constituents"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[IndicesHistoricalConstituents],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncIndexWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def indices_constituents(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[IndicesConstituents, RawError]:
        """Get a list of index's constituents. A list of supported indices for this endpoint can be found <a
        href="/api/v1/index/list?token=" target="_blank">here</a>.

        Args:
            symbol: symbol
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/index/constituents"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[IndicesConstituents],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def indices_historical_constituents(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[IndicesHistoricalConstituents, RawError]:
        """Get full history of index's constituents including symbols and dates of joining and leaving the Index. A list
        of supported indices for this endpoint can be found <a href="/api/v1/index/historical-list?token="
        target="_blank">here</a>.

        Args:
            symbol: symbol
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/index/historical-constituents"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[IndicesHistoricalConstituents],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
