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
from ..models.isin_change import IsinChange
from ..models.symbol_change import SymbolChange
from ..server.server import Server


class CorporateActions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CorporateActionsWithRawResponse(client, server, auth)

    def isin_change(self, from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None) -> IsinChange:
        """Get a list of ISIN changes for EU-listed securities. Limit to 2000 events at a time.

        Args:
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.isin_change(from_, to, request_options=request_options).unwrap()

    def symbol_change(
        self, from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SymbolChange:
        """Get a list of symbol changes for US-listed, EU-listed, NSE and ASX securities. Limit to 2000 events at a
        time.

        Args:
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.symbol_change(from_, to, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> CorporateActionsWithRawResponse:
        return self._with_raw_response


class AsyncCorporateActions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCorporateActionsWithRawResponse(client, server, auth)

    async def isin_change(
        self, from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> IsinChange:
        """Get a list of ISIN changes for EU-listed securities. Limit to 2000 events at a time.

        Args:
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.isin_change(from_, to, request_options=request_options)).unwrap()

    async def symbol_change(
        self, from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SymbolChange:
        """Get a list of symbol changes for US-listed, EU-listed, NSE and ASX securities. Limit to 2000 events at a
        time.

        Args:
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.symbol_change(from_, to, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncCorporateActionsWithRawResponse:
        return self._with_raw_response


class CorporateActionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def isin_change(
        self, from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[IsinChange, RawError]:
        """Get a list of ISIN changes for EU-listed securities. Limit to 2000 events at a time.

        Args:
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ca/isin-change"),
            query_params=[param[str]("from", from_), param[str]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[IsinChange],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def symbol_change(
        self, from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SymbolChange, RawError]:
        """Get a list of symbol changes for US-listed, EU-listed, NSE and ASX securities. Limit to 2000 events at a
        time.

        Args:
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ca/symbol-change"),
            query_params=[param[str]("from", from_), param[str]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[SymbolChange],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncCorporateActionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def isin_change(
        self, from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[IsinChange, RawError]:
        """Get a list of ISIN changes for EU-listed securities. Limit to 2000 events at a time.

        Args:
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ca/isin-change"),
            query_params=[param[str]("from", from_), param[str]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[IsinChange],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def symbol_change(
        self, from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SymbolChange, RawError]:
        """Get a list of symbol changes for US-listed, EU-listed, NSE and ASX securities. Limit to 2000 events at a
        time.

        Args:
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/ca/symbol-change"),
            query_params=[param[str]("from", from_), param[str]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[SymbolChange],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
