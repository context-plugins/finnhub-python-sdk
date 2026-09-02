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
from ..models.economic_code import EconomicCode
from ..models.economic_data import EconomicData
from ..server.server import Server


class Economic:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EconomicWithRawResponse(client, server, auth)

    def economic_code(self, *, request_options: RequestOptionsOrDict | None = None) -> list[EconomicCode]:
        """List codes of supported economic data.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.economic_code(request_options=request_options).unwrap()

    def economic_data(self, code: str, *, request_options: RequestOptionsOrDict | None = None) -> EconomicData:
        """Get economic data.

        Args:
            code: Economic code.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.economic_data(code, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> EconomicWithRawResponse:
        return self._with_raw_response


class AsyncEconomic:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEconomicWithRawResponse(client, server, auth)

    async def economic_code(self, *, request_options: RequestOptionsOrDict | None = None) -> list[EconomicCode]:
        """List codes of supported economic data.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.economic_code(request_options=request_options)).unwrap()

    async def economic_data(self, code: str, *, request_options: RequestOptionsOrDict | None = None) -> EconomicData:
        """Get economic data.

        Args:
            code: Economic code.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.economic_data(code, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncEconomicWithRawResponse:
        return self._with_raw_response


class EconomicWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def economic_code(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[EconomicCode], RawError]:
        """List codes of supported economic data.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/economic/code"),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[EconomicCode]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def economic_data(
        self, code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EconomicData, RawError]:
        """Get economic data.

        Args:
            code: Economic code.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/economic"),
            query_params=[param[str]("code", code)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EconomicData],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncEconomicWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def economic_code(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[EconomicCode], RawError]:
        """List codes of supported economic data.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/economic/code"),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[EconomicCode]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def economic_data(
        self, code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EconomicData, RawError]:
        """Get economic data.

        Args:
            code: Economic code.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/economic"),
            query_params=[param[str]("code", code)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EconomicData],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
