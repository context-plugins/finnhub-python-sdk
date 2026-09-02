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
from ..models.institutional_ownership import InstitutionalOwnership
from ..models.institutional_portfolio import InstitutionalPortfolio
from ..models.institutional_profile import InstitutionalProfile
from ..server.server import Server


class Institutional:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InstitutionalWithRawResponse(client, server, auth)

    def institutional_ownership(
        self, symbol: str, cusip: str, from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> InstitutionalOwnership:
        """Get a list institutional investors' positions for a particular stock overtime. Data from 13-F filings. Limit
        to 1 year of data at a time.

        Args:
            symbol: Filter by symbol.
            cusip: Filter by CUSIP.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.institutional_ownership(
            symbol, cusip, from_, to, request_options=request_options
        ).unwrap()

    def institutional_portfolio(
        self, cik: str, from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> InstitutionalPortfolio:
        """Get the holdings/portfolio data of institutional investors from 13-F filings. Limit to 1 year of data at a
        time. You can get a list of supported CIK <a href="/api/v1/institutional/list?token=" target="_blank">here</a>.

        Args:
            cik: Fund's CIK.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.institutional_portfolio(cik, from_, to, request_options=request_options).unwrap()

    def institutional_profile(
        self, *, cik: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> InstitutionalProfile:
        """Get a list of well-known institutional investors. Currently support 60+ profiles.

        Args:
            cik: Filter by CIK. Leave blank to get the full list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.institutional_profile(cik=cik, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> InstitutionalWithRawResponse:
        return self._with_raw_response


class AsyncInstitutional:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInstitutionalWithRawResponse(client, server, auth)

    async def institutional_ownership(
        self, symbol: str, cusip: str, from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> InstitutionalOwnership:
        """Get a list institutional investors' positions for a particular stock overtime. Data from 13-F filings. Limit
        to 1 year of data at a time.

        Args:
            symbol: Filter by symbol.
            cusip: Filter by CUSIP.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.institutional_ownership(
                symbol, cusip, from_, to, request_options=request_options
            )
        ).unwrap()

    async def institutional_portfolio(
        self, cik: str, from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> InstitutionalPortfolio:
        """Get the holdings/portfolio data of institutional investors from 13-F filings. Limit to 1 year of data at a
        time. You can get a list of supported CIK <a href="/api/v1/institutional/list?token=" target="_blank">here</a>.

        Args:
            cik: Fund's CIK.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.institutional_portfolio(cik, from_, to, request_options=request_options)
        ).unwrap()

    async def institutional_profile(
        self, *, cik: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> InstitutionalProfile:
        """Get a list of well-known institutional investors. Currently support 60+ profiles.

        Args:
            cik: Filter by CIK. Leave blank to get the full list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.institutional_profile(cik=cik, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncInstitutionalWithRawResponse:
        return self._with_raw_response


class InstitutionalWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def institutional_ownership(
        self, symbol: str, cusip: str, from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InstitutionalOwnership, RawError]:
        """Get a list institutional investors' positions for a particular stock overtime. Data from 13-F filings. Limit
        to 1 year of data at a time.

        Args:
            symbol: Filter by symbol.
            cusip: Filter by CUSIP.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/institutional/ownership"),
            query_params=[
                param[str]("symbol", symbol),
                param[str]("cusip", cusip),
                param[str]("from", from_),
                param[str]("to", to),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[InstitutionalOwnership],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def institutional_portfolio(
        self, cik: str, from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InstitutionalPortfolio, RawError]:
        """Get the holdings/portfolio data of institutional investors from 13-F filings. Limit to 1 year of data at a
        time. You can get a list of supported CIK <a href="/api/v1/institutional/list?token=" target="_blank">here</a>.

        Args:
            cik: Fund's CIK.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/institutional/portfolio"),
            query_params=[param[str]("cik", cik), param[str]("from", from_), param[str]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[InstitutionalPortfolio],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def institutional_profile(
        self, *, cik: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InstitutionalProfile, RawError]:
        """Get a list of well-known institutional investors. Currently support 60+ profiles.

        Args:
            cik: Filter by CIK. Leave blank to get the full list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/institutional/profile"),
            query_params=[param[str | None]("cik", cik)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[InstitutionalProfile],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncInstitutionalWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def institutional_ownership(
        self, symbol: str, cusip: str, from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InstitutionalOwnership, RawError]:
        """Get a list institutional investors' positions for a particular stock overtime. Data from 13-F filings. Limit
        to 1 year of data at a time.

        Args:
            symbol: Filter by symbol.
            cusip: Filter by CUSIP.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/institutional/ownership"),
            query_params=[
                param[str]("symbol", symbol),
                param[str]("cusip", cusip),
                param[str]("from", from_),
                param[str]("to", to),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[InstitutionalOwnership],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def institutional_portfolio(
        self, cik: str, from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InstitutionalPortfolio, RawError]:
        """Get the holdings/portfolio data of institutional investors from 13-F filings. Limit to 1 year of data at a
        time. You can get a list of supported CIK <a href="/api/v1/institutional/list?token=" target="_blank">here</a>.

        Args:
            cik: Fund's CIK.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/institutional/portfolio"),
            query_params=[param[str]("cik", cik), param[str]("from", from_), param[str]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[InstitutionalPortfolio],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def institutional_profile(
        self, *, cik: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InstitutionalProfile, RawError]:
        """Get a list of well-known institutional investors. Currently support 60+ profiles.

        Args:
            cik: Filter by CIK. Leave blank to get the full list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/institutional/profile"),
            query_params=[param[str | None]("cik", cik)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[InstitutionalProfile],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
