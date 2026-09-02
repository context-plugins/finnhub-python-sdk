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
from ..models.earnings_calendar import EarningsCalendar
from ..models.economic_calendar import EconomicCalendar
from ..models.ipocalendar import Ipocalendar
from ..server.server import Server


class Calendar:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CalendarWithRawResponse(client, server, auth)

    def earnings_calendar(
        self,
        *,
        from_: Date | None = None,
        to: Date | None = None,
        symbol: str | None = None,
        international: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EarningsCalendar:
        """Get historical and coming earnings release. EPS and Revenue in this endpoint are non-GAAP, which means they
        are adjusted to exclude some one-time or unusual items. This is the same data investors usually react to and
        talked about on the media. Estimates are sourced from both sell-side and buy-side analysts.

        Args:
            from_: From date: 2020-03-15.
            to: To date: 2020-03-16.
            symbol: Filter by symbol: AAPL.
            international: Set to <code>true</code> to include international markets. Default value is
                <code>false</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.earnings_calendar(
            from_=from_, to=to, symbol=symbol, international=international, request_options=request_options
        ).unwrap()

    def economic_calendar(
        self, *, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> EconomicCalendar:
        """<p>Get recent and upcoming economic releases.</p><p>Historical events and surprises are available for
        Enterprise clients.</p>

        Args:
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.economic_calendar(from_=from_, to=to, request_options=request_options).unwrap()

    def ipo_calendar(
        self, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> Ipocalendar:
        """Get recent and upcoming IPO.

        Args:
            from_: From date: 2020-03-15.
            to: To date: 2020-03-16.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.ipo_calendar(from_, to, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> CalendarWithRawResponse:
        return self._with_raw_response


class AsyncCalendar:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCalendarWithRawResponse(client, server, auth)

    async def earnings_calendar(
        self,
        *,
        from_: Date | None = None,
        to: Date | None = None,
        symbol: str | None = None,
        international: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EarningsCalendar:
        """Get historical and coming earnings release. EPS and Revenue in this endpoint are non-GAAP, which means they
        are adjusted to exclude some one-time or unusual items. This is the same data investors usually react to and
        talked about on the media. Estimates are sourced from both sell-side and buy-side analysts.

        Args:
            from_: From date: 2020-03-15.
            to: To date: 2020-03-16.
            symbol: Filter by symbol: AAPL.
            international: Set to <code>true</code> to include international markets. Default value is
                <code>false</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.earnings_calendar(
                from_=from_, to=to, symbol=symbol, international=international, request_options=request_options
            )
        ).unwrap()

    async def economic_calendar(
        self, *, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> EconomicCalendar:
        """<p>Get recent and upcoming economic releases.</p><p>Historical events and surprises are available for
        Enterprise clients.</p>

        Args:
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.economic_calendar(from_=from_, to=to, request_options=request_options)
        ).unwrap()

    async def ipo_calendar(
        self, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> Ipocalendar:
        """Get recent and upcoming IPO.

        Args:
            from_: From date: 2020-03-15.
            to: To date: 2020-03-16.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.ipo_calendar(from_, to, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncCalendarWithRawResponse:
        return self._with_raw_response


class CalendarWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def earnings_calendar(
        self,
        *,
        from_: Date | None = None,
        to: Date | None = None,
        symbol: str | None = None,
        international: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EarningsCalendar, RawError]:
        """Get historical and coming earnings release. EPS and Revenue in this endpoint are non-GAAP, which means they
        are adjusted to exclude some one-time or unusual items. This is the same data investors usually react to and
        talked about on the media. Estimates are sourced from both sell-side and buy-side analysts.

        Args:
            from_: From date: 2020-03-15.
            to: To date: 2020-03-16.
            symbol: Filter by symbol: AAPL.
            international: Set to <code>true</code> to include international markets. Default value is
                <code>false</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/calendar/earnings"),
            query_params=[
                param[Date | None]("from", from_),
                param[Date | None]("to", to),
                param[str | None]("symbol", symbol),
                param[bool | None]("international", international),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EarningsCalendar],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def economic_calendar(
        self, *, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EconomicCalendar, RawError]:
        """<p>Get recent and upcoming economic releases.</p><p>Historical events and surprises are available for
        Enterprise clients.</p>

        Args:
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/calendar/economic"),
            query_params=[param[Date | None]("from", from_), param[Date | None]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EconomicCalendar],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def ipo_calendar(
        self, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Ipocalendar, RawError]:
        """Get recent and upcoming IPO.

        Args:
            from_: From date: 2020-03-15.
            to: To date: 2020-03-16.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/calendar/ipo"),
            query_params=[param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[Ipocalendar],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncCalendarWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def earnings_calendar(
        self,
        *,
        from_: Date | None = None,
        to: Date | None = None,
        symbol: str | None = None,
        international: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EarningsCalendar, RawError]:
        """Get historical and coming earnings release. EPS and Revenue in this endpoint are non-GAAP, which means they
        are adjusted to exclude some one-time or unusual items. This is the same data investors usually react to and
        talked about on the media. Estimates are sourced from both sell-side and buy-side analysts.

        Args:
            from_: From date: 2020-03-15.
            to: To date: 2020-03-16.
            symbol: Filter by symbol: AAPL.
            international: Set to <code>true</code> to include international markets. Default value is
                <code>false</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/calendar/earnings"),
            query_params=[
                param[Date | None]("from", from_),
                param[Date | None]("to", to),
                param[str | None]("symbol", symbol),
                param[bool | None]("international", international),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EarningsCalendar],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def economic_calendar(
        self, *, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EconomicCalendar, RawError]:
        """<p>Get recent and upcoming economic releases.</p><p>Historical events and surprises are available for
        Enterprise clients.</p>

        Args:
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/calendar/economic"),
            query_params=[param[Date | None]("from", from_), param[Date | None]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EconomicCalendar],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def ipo_calendar(
        self, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Ipocalendar, RawError]:
        """Get recent and upcoming IPO.

        Args:
            from_: From date: 2020-03-15.
            to: To date: 2020-03-16.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/calendar/ipo"),
            query_params=[param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[Ipocalendar],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
