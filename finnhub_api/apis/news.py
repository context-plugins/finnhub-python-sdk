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
from ..models.company_news import CompanyNews
from ..models.market_news import MarketNews
from ..models.news_sentiment import NewsSentiment
from ..models.press_release import PressRelease
from ..server.server import Server


class News:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NewsWithRawResponse(client, server, auth)

    def company_news(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[CompanyNews]:
        """List latest company news by symbol. This endpoint is only available for North American companies.

        Args:
            symbol: Company symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.company_news(symbol, from_, to, request_options=request_options).unwrap()

    def market_news(
        self, category: str, *, min_id: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[MarketNews]:
        """Get latest market news.

        Args:
            category: This parameter can be 1 of the following values <code>general, forex, crypto, merger</code>.
            min_id: Use this field to get only news after this ID. Default to 0
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.market_news(category, min_id=min_id, request_options=request_options).unwrap()

    def news_sentiment(self, symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> NewsSentiment:
        """Get company's news sentiment and statistics. This endpoint is only available for US companies.

        Args:
            symbol: Company symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.news_sentiment(symbol, request_options=request_options).unwrap()

    def press_releases(
        self,
        symbol: str,
        *,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PressRelease:
        """<p>Get latest major press releases of a company. This data can be used to highlight the most significant
        events comprised of mostly press releases sourced from the exchanges, BusinessWire, AccessWire, GlobeNewswire,
        Newsfile, and PRNewswire.</p><p>Full-text press releases data is available for Enterprise clients. <a
        href="mailto:support@finnhub.io">Contact Us</a> to learn more.</p>

        Args:
            symbol: Company symbol.
            from_: From time: 2020-01-01.
            to: To time: 2020-01-05.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.press_releases(
            symbol, from_=from_, to=to, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> NewsWithRawResponse:
        return self._with_raw_response


class AsyncNews:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNewsWithRawResponse(client, server, auth)

    async def company_news(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[CompanyNews]:
        """List latest company news by symbol. This endpoint is only available for North American companies.

        Args:
            symbol: Company symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.company_news(symbol, from_, to, request_options=request_options)).unwrap()

    async def market_news(
        self, category: str, *, min_id: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[MarketNews]:
        """Get latest market news.

        Args:
            category: This parameter can be 1 of the following values <code>general, forex, crypto, merger</code>.
            min_id: Use this field to get only news after this ID. Default to 0
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.market_news(category, min_id=min_id, request_options=request_options)
        ).unwrap()

    async def news_sentiment(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NewsSentiment:
        """Get company's news sentiment and statistics. This endpoint is only available for US companies.

        Args:
            symbol: Company symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.news_sentiment(symbol, request_options=request_options)).unwrap()

    async def press_releases(
        self,
        symbol: str,
        *,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PressRelease:
        """<p>Get latest major press releases of a company. This data can be used to highlight the most significant
        events comprised of mostly press releases sourced from the exchanges, BusinessWire, AccessWire, GlobeNewswire,
        Newsfile, and PRNewswire.</p><p>Full-text press releases data is available for Enterprise clients. <a
        href="mailto:support@finnhub.io">Contact Us</a> to learn more.</p>

        Args:
            symbol: Company symbol.
            from_: From time: 2020-01-01.
            to: To time: 2020-01-05.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.press_releases(symbol, from_=from_, to=to, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNewsWithRawResponse:
        return self._with_raw_response


class NewsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def company_news(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[CompanyNews], RawError]:
        """List latest company news by symbol. This endpoint is only available for North American companies.

        Args:
            symbol: Company symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/company-news"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[CompanyNews]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def market_news(
        self, category: str, *, min_id: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[MarketNews], RawError]:
        """Get latest market news.

        Args:
            category: This parameter can be 1 of the following values <code>general, forex, crypto, merger</code>.
            min_id: Use this field to get only news after this ID. Default to 0
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/news"),
            query_params=[param[str]("category", category), param[int | None]("minId", min_id)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[MarketNews]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def news_sentiment(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NewsSentiment, RawError]:
        """Get company's news sentiment and statistics. This endpoint is only available for US companies.

        Args:
            symbol: Company symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/news-sentiment"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[NewsSentiment],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def press_releases(
        self,
        symbol: str,
        *,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PressRelease, RawError]:
        """<p>Get latest major press releases of a company. This data can be used to highlight the most significant
        events comprised of mostly press releases sourced from the exchanges, BusinessWire, AccessWire, GlobeNewswire,
        Newsfile, and PRNewswire.</p><p>Full-text press releases data is available for Enterprise clients. <a
        href="mailto:support@finnhub.io">Contact Us</a> to learn more.</p>

        Args:
            symbol: Company symbol.
            from_: From time: 2020-01-01.
            to: To time: 2020-01-05.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/press-releases"),
            query_params=[
                param[str]("symbol", symbol), param[Date | None]("from", from_), param[Date | None]("to", to)
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[PressRelease],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNewsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def company_news(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[CompanyNews], RawError]:
        """List latest company news by symbol. This endpoint is only available for North American companies.

        Args:
            symbol: Company symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/company-news"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[CompanyNews]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def market_news(
        self, category: str, *, min_id: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[MarketNews], RawError]:
        """Get latest market news.

        Args:
            category: This parameter can be 1 of the following values <code>general, forex, crypto, merger</code>.
            min_id: Use this field to get only news after this ID. Default to 0
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/news"),
            query_params=[param[str]("category", category), param[int | None]("minId", min_id)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[MarketNews]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def news_sentiment(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NewsSentiment, RawError]:
        """Get company's news sentiment and statistics. This endpoint is only available for US companies.

        Args:
            symbol: Company symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/news-sentiment"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[NewsSentiment],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def press_releases(
        self,
        symbol: str,
        *,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PressRelease, RawError]:
        """<p>Get latest major press releases of a company. This data can be used to highlight the most significant
        events comprised of mostly press releases sourced from the exchanges, BusinessWire, AccessWire, GlobeNewswire,
        Newsfile, and PRNewswire.</p><p>Full-text press releases data is available for Enterprise clients. <a
        href="mailto:support@finnhub.io">Contact Us</a> to learn more.</p>

        Args:
            symbol: Company symbol.
            from_: From time: 2020-01-01.
            to: To time: 2020-01-05.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/press-releases"),
            query_params=[
                param[str]("symbol", symbol), param[Date | None]("from", from_), param[Date | None]("to", to)
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[PressRelease],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
