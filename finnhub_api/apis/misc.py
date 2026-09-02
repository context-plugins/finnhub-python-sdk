from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    Date,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.aichat_body import AichatBody, AichatBodyDict
from ..models.aichat_response import AichatResponse
from ..models.airline_price_index_data import AirlinePriceIndexData
from ..models.bank_branch_res import BankBranchRes
from ..models.country_metadata import CountryMetadata
from ..models.covid_info import CovidInfo
from ..models.fdacomittee_meeting import FdacomitteeMeeting
from ..models.quote import Quote
from ..models.sector_metric import SectorMetric
from ..models.symbol_lookup import SymbolLookup
from ..server.server import Server


class Misc:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MiscWithRawResponse(client, server, auth)

    def ai_chat(
        self, *, search: AichatBody | AichatBodyDict | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> AichatResponse:
        """<p>Chat with our AI copilot trained on the extensive Finnhub's global data. You can ask it any
        finance-related questions just like with other LLM models and receive results in texts and widgets.</p>

        Args:
            search: Search body
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.ai_chat(search=search, request_options=request_options).unwrap()

    def airline_price_index(
        self, airline: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> AirlinePriceIndexData:
        """<p>The Flight Ticket Price Index API provides comprehensive data on airline ticket prices, including the
        average daily ticket price and its percentage change (price index). This data, collected weekly and projected
        two weeks ahead, aggregates daily prices and indexes from the 50 busiest and largest airports across the USA.
        The dataset includes detailed information on airlines, dates, and average ticket prices, offering valuable
        insights for market analysis and pricing strategies.</p><p>The price index is calculated as percentage change of
        average daily ticket price from the previous weekly reading. Raw ticket prices data is available for Enterprise
        users. <a href="mailto:support@finnhub.io">Contact us</a> to inquire about the raw price data.</p>

        Args:
            airline: Filter data by airline. Accepted values:
                <code>united</code>,<code>delta</code>,<code>american_airlines</code>,<code>southwest</code>,<code>southern_airways_express</code>,<code>alaska_airlines</code>,<code>frontier_airlines</code>,<code>jetblue_airways</code>,<code>spirit_airlines</code>,<code>sun_country_airlines</code>,<code>breeze_airways</code>,<code>hawaiian_airlines</code>
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.airline_price_index(airline, from_, to, request_options=request_options).unwrap()

    def bank_branch(self, symbol: Any, *, request_options: RequestOptionsOrDict | None = None) -> BankBranchRes:
        """Retrieve list of US bank branches information for a given symbol.

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bank_branch(symbol, request_options=request_options).unwrap()

    def country(self, *, request_options: RequestOptionsOrDict | None = None) -> list[CountryMetadata]:
        """List all countries and metadata.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.country(request_options=request_options).unwrap()

    def covid_19(self, *, request_options: RequestOptionsOrDict | None = None) -> list[CovidInfo]:
        """Get real-time updates on the number of COVID-19 (Corona virus) cases in the US with a state-by-state
        breakdown. Data is sourced from CDC and reputable sources. You can also access this API <a
        href="https://rapidapi.com/Finnhub/api/finnhub-real-time-covid-19" target="_blank" rel="nofollow">here</a>

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.covid_19(request_options=request_options).unwrap()

    def fda_committee_meeting_calendar(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[FdacomitteeMeeting]:
        """FDA's advisory committees are established to provide functions which support the agency's mission of
        protecting and promoting the public health, while meeting the requirements set forth in the Federal Advisory
        Committee Act. Committees are either mandated by statute or established at the discretion of the Department of
        Health and Human Services. Each committee is subject to renewal at two-year intervals unless the committee
        charter states otherwise.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fda_committee_meeting_calendar(request_options=request_options).unwrap()

    def quote(self, symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> Quote:
        """<p>Get real-time quote data for US stocks. Constant polling is not recommended. Use websocket if you need
        real-time updates.</p><p>Real-time stock prices for international markets are supported for Enterprise clients
        via our partner's feed. <a href="mailto:support@finnhub.io">Contact Us</a> to learn more.</p>

        Args:
            symbol: Symbol
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.quote(symbol, request_options=request_options).unwrap()

    def sector_metric(self, region: str, *, request_options: RequestOptionsOrDict | None = None) -> SectorMetric:
        """Get ratios for different sectors and regions/indices.

        Args:
            region: Region. A list of supported values for this field can be found <a
                href="https://docs.google.com/spreadsheets/d/1afedyv7yWJ-z7pMjaAZK-f6ENY3mI3EBCk95QffpoHw/edit?usp=sharing"
                target="_blank">here</a>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.sector_metric(region, request_options=request_options).unwrap()

    def symbol_search(
        self, q: str, *, exchange: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> SymbolLookup:
        """Search for best-matching symbols based on your query. You can input anything from symbol, security's name to
        ISIN and Cusip.

        Args:
            q: Query text can be symbol, name, isin, or cusip.
            exchange: Exchange limit.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.symbol_search(q, exchange=exchange, request_options=request_options).unwrap()

    def technical_indicator(
        self,
        symbol: str,
        resolution: str,
        from_: int,
        to: int,
        indicator: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Return technical indicator with price data. List of supported indicators can be found <a
        href="https://docs.google.com/spreadsheets/d/1ylUvKHVYN2E87WdwIza8ROaCpd48ggEl1k5i5SgA29k/edit?usp=sharing"
        target="_blank">here</a>.

        Args:
            symbol: symbol
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            from_: UNIX timestamp. Interval initial value.
            to: UNIX timestamp. Interval end value.
            indicator: Indicator name. Full list can be found <a
                href="https://docs.google.com/spreadsheets/d/1ylUvKHVYN2E87WdwIza8ROaCpd48ggEl1k5i5SgA29k/edit?usp=sharing"
                target="_blank">here</a>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.technical_indicator(
            symbol, resolution, from_, to, indicator, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> MiscWithRawResponse:
        return self._with_raw_response


class AsyncMisc:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMiscWithRawResponse(client, server, auth)

    async def ai_chat(
        self, *, search: AichatBody | AichatBodyDict | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> AichatResponse:
        """<p>Chat with our AI copilot trained on the extensive Finnhub's global data. You can ask it any
        finance-related questions just like with other LLM models and receive results in texts and widgets.</p>

        Args:
            search: Search body
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.ai_chat(search=search, request_options=request_options)).unwrap()

    async def airline_price_index(
        self, airline: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> AirlinePriceIndexData:
        """<p>The Flight Ticket Price Index API provides comprehensive data on airline ticket prices, including the
        average daily ticket price and its percentage change (price index). This data, collected weekly and projected
        two weeks ahead, aggregates daily prices and indexes from the 50 busiest and largest airports across the USA.
        The dataset includes detailed information on airlines, dates, and average ticket prices, offering valuable
        insights for market analysis and pricing strategies.</p><p>The price index is calculated as percentage change of
        average daily ticket price from the previous weekly reading. Raw ticket prices data is available for Enterprise
        users. <a href="mailto:support@finnhub.io">Contact us</a> to inquire about the raw price data.</p>

        Args:
            airline: Filter data by airline. Accepted values:
                <code>united</code>,<code>delta</code>,<code>american_airlines</code>,<code>southwest</code>,<code>southern_airways_express</code>,<code>alaska_airlines</code>,<code>frontier_airlines</code>,<code>jetblue_airways</code>,<code>spirit_airlines</code>,<code>sun_country_airlines</code>,<code>breeze_airways</code>,<code>hawaiian_airlines</code>
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.airline_price_index(airline, from_, to, request_options=request_options)
        ).unwrap()

    async def bank_branch(self, symbol: Any, *, request_options: RequestOptionsOrDict | None = None) -> BankBranchRes:
        """Retrieve list of US bank branches information for a given symbol.

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.bank_branch(symbol, request_options=request_options)).unwrap()

    async def country(self, *, request_options: RequestOptionsOrDict | None = None) -> list[CountryMetadata]:
        """List all countries and metadata.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.country(request_options=request_options)).unwrap()

    async def covid_19(self, *, request_options: RequestOptionsOrDict | None = None) -> list[CovidInfo]:
        """Get real-time updates on the number of COVID-19 (Corona virus) cases in the US with a state-by-state
        breakdown. Data is sourced from CDC and reputable sources. You can also access this API <a
        href="https://rapidapi.com/Finnhub/api/finnhub-real-time-covid-19" target="_blank" rel="nofollow">here</a>

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.covid_19(request_options=request_options)).unwrap()

    async def fda_committee_meeting_calendar(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[FdacomitteeMeeting]:
        """FDA's advisory committees are established to provide functions which support the agency's mission of
        protecting and promoting the public health, while meeting the requirements set forth in the Federal Advisory
        Committee Act. Committees are either mandated by statute or established at the discretion of the Department of
        Health and Human Services. Each committee is subject to renewal at two-year intervals unless the committee
        charter states otherwise.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.fda_committee_meeting_calendar(request_options=request_options)).unwrap()

    async def quote(self, symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> Quote:
        """<p>Get real-time quote data for US stocks. Constant polling is not recommended. Use websocket if you need
        real-time updates.</p><p>Real-time stock prices for international markets are supported for Enterprise clients
        via our partner's feed. <a href="mailto:support@finnhub.io">Contact Us</a> to learn more.</p>

        Args:
            symbol: Symbol
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.quote(symbol, request_options=request_options)).unwrap()

    async def sector_metric(self, region: str, *, request_options: RequestOptionsOrDict | None = None) -> SectorMetric:
        """Get ratios for different sectors and regions/indices.

        Args:
            region: Region. A list of supported values for this field can be found <a
                href="https://docs.google.com/spreadsheets/d/1afedyv7yWJ-z7pMjaAZK-f6ENY3mI3EBCk95QffpoHw/edit?usp=sharing"
                target="_blank">here</a>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.sector_metric(region, request_options=request_options)).unwrap()

    async def symbol_search(
        self, q: str, *, exchange: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> SymbolLookup:
        """Search for best-matching symbols based on your query. You can input anything from symbol, security's name to
        ISIN and Cusip.

        Args:
            q: Query text can be symbol, name, isin, or cusip.
            exchange: Exchange limit.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.symbol_search(q, exchange=exchange, request_options=request_options)
        ).unwrap()

    async def technical_indicator(
        self,
        symbol: str,
        resolution: str,
        from_: int,
        to: int,
        indicator: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Return technical indicator with price data. List of supported indicators can be found <a
        href="https://docs.google.com/spreadsheets/d/1ylUvKHVYN2E87WdwIza8ROaCpd48ggEl1k5i5SgA29k/edit?usp=sharing"
        target="_blank">here</a>.

        Args:
            symbol: symbol
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            from_: UNIX timestamp. Interval initial value.
            to: UNIX timestamp. Interval end value.
            indicator: Indicator name. Full list can be found <a
                href="https://docs.google.com/spreadsheets/d/1ylUvKHVYN2E87WdwIza8ROaCpd48ggEl1k5i5SgA29k/edit?usp=sharing"
                target="_blank">here</a>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.technical_indicator(
                symbol, resolution, from_, to, indicator, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMiscWithRawResponse:
        return self._with_raw_response


class MiscWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def ai_chat(
        self, *, search: AichatBody | AichatBodyDict | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AichatResponse, RawError]:
        """<p>Chat with our AI copilot trained on the extensive Finnhub's global data. You can ask it any
        finance-related questions just like with other LLM models and receive results in texts and widgets.</p>

        Args:
            search: Search body
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/ai-chat"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AichatBody | AichatBodyDict | None](search),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[AichatResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def airline_price_index(
        self, airline: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AirlinePriceIndexData, RawError]:
        """<p>The Flight Ticket Price Index API provides comprehensive data on airline ticket prices, including the
        average daily ticket price and its percentage change (price index). This data, collected weekly and projected
        two weeks ahead, aggregates daily prices and indexes from the 50 busiest and largest airports across the USA.
        The dataset includes detailed information on airlines, dates, and average ticket prices, offering valuable
        insights for market analysis and pricing strategies.</p><p>The price index is calculated as percentage change of
        average daily ticket price from the previous weekly reading. Raw ticket prices data is available for Enterprise
        users. <a href="mailto:support@finnhub.io">Contact us</a> to inquire about the raw price data.</p>

        Args:
            airline: Filter data by airline. Accepted values:
                <code>united</code>,<code>delta</code>,<code>american_airlines</code>,<code>southwest</code>,<code>southern_airways_express</code>,<code>alaska_airlines</code>,<code>frontier_airlines</code>,<code>jetblue_airways</code>,<code>spirit_airlines</code>,<code>sun_country_airlines</code>,<code>breeze_airways</code>,<code>hawaiian_airlines</code>
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/airline/price-index"),
            query_params=[param[str]("airline", airline), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[AirlinePriceIndexData],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bank_branch(
        self, symbol: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BankBranchRes, RawError]:
        """Retrieve list of US bank branches information for a given symbol.

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/bank-branch"),
            query_params=[param[Any]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[BankBranchRes],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def country(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[CountryMetadata], RawError]:
        """List all countries and metadata.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/country"),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[CountryMetadata]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def covid_19(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[CovidInfo], RawError]:
        """Get real-time updates on the number of COVID-19 (Corona virus) cases in the US with a state-by-state
        breakdown. Data is sourced from CDC and reputable sources. You can also access this API <a
        href="https://rapidapi.com/Finnhub/api/finnhub-real-time-covid-19" target="_blank" rel="nofollow">here</a>

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/covid19/us"),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[CovidInfo]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fda_committee_meeting_calendar(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[FdacomitteeMeeting], RawError]:
        """FDA's advisory committees are established to provide functions which support the agency's mission of
        protecting and promoting the public health, while meeting the requirements set forth in the Federal Advisory
        Committee Act. Committees are either mandated by statute or established at the discretion of the Department of
        Health and Human Services. Each committee is subject to renewal at two-year intervals unless the committee
        charter states otherwise.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/fda-advisory-committee-calendar"),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[FdacomitteeMeeting]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def quote(self, symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Quote, RawError]:
        """<p>Get real-time quote data for US stocks. Constant polling is not recommended. Use websocket if you need
        real-time updates.</p><p>Real-time stock prices for international markets are supported for Enterprise clients
        via our partner's feed. <a href="mailto:support@finnhub.io">Contact Us</a> to learn more.</p>

        Args:
            symbol: Symbol
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/quote"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[Quote],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def sector_metric(
        self, region: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SectorMetric, RawError]:
        """Get ratios for different sectors and regions/indices.

        Args:
            region: Region. A list of supported values for this field can be found <a
                href="https://docs.google.com/spreadsheets/d/1afedyv7yWJ-z7pMjaAZK-f6ENY3mI3EBCk95QffpoHw/edit?usp=sharing"
                target="_blank">here</a>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sector/metrics"),
            query_params=[param[str]("region", region)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[SectorMetric],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def symbol_search(
        self, q: str, *, exchange: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SymbolLookup, RawError]:
        """Search for best-matching symbols based on your query. You can input anything from symbol, security's name to
        ISIN and Cusip.

        Args:
            q: Query text can be symbol, name, isin, or cusip.
            exchange: Exchange limit.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search"),
            query_params=[param[str]("q", q), param[str | None]("exchange", exchange)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[SymbolLookup],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def technical_indicator(
        self,
        symbol: str,
        resolution: str,
        from_: int,
        to: int,
        indicator: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, RawError]:
        """Return technical indicator with price data. List of supported indicators can be found <a
        href="https://docs.google.com/spreadsheets/d/1ylUvKHVYN2E87WdwIza8ROaCpd48ggEl1k5i5SgA29k/edit?usp=sharing"
        target="_blank">here</a>.

        Args:
            symbol: symbol
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            from_: UNIX timestamp. Interval initial value.
            to: UNIX timestamp. Interval end value.
            indicator: Indicator name. Full list can be found <a
                href="https://docs.google.com/spreadsheets/d/1ylUvKHVYN2E87WdwIza8ROaCpd48ggEl1k5i5SgA29k/edit?usp=sharing"
                target="_blank">here</a>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/indicator"),
            query_params=[
                param[str]("symbol", symbol),
                param[str]("resolution", resolution),
                param[int]("from", from_),
                param[int]("to", to),
                param[str]("indicator", indicator),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMiscWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def ai_chat(
        self, *, search: AichatBody | AichatBodyDict | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AichatResponse, RawError]:
        """<p>Chat with our AI copilot trained on the extensive Finnhub's global data. You can ask it any
        finance-related questions just like with other LLM models and receive results in texts and widgets.</p>

        Args:
            search: Search body
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/ai-chat"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AichatBody | AichatBodyDict | None](search),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[AichatResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def airline_price_index(
        self, airline: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AirlinePriceIndexData, RawError]:
        """<p>The Flight Ticket Price Index API provides comprehensive data on airline ticket prices, including the
        average daily ticket price and its percentage change (price index). This data, collected weekly and projected
        two weeks ahead, aggregates daily prices and indexes from the 50 busiest and largest airports across the USA.
        The dataset includes detailed information on airlines, dates, and average ticket prices, offering valuable
        insights for market analysis and pricing strategies.</p><p>The price index is calculated as percentage change of
        average daily ticket price from the previous weekly reading. Raw ticket prices data is available for Enterprise
        users. <a href="mailto:support@finnhub.io">Contact us</a> to inquire about the raw price data.</p>

        Args:
            airline: Filter data by airline. Accepted values:
                <code>united</code>,<code>delta</code>,<code>american_airlines</code>,<code>southwest</code>,<code>southern_airways_express</code>,<code>alaska_airlines</code>,<code>frontier_airlines</code>,<code>jetblue_airways</code>,<code>spirit_airlines</code>,<code>sun_country_airlines</code>,<code>breeze_airways</code>,<code>hawaiian_airlines</code>
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/airline/price-index"),
            query_params=[param[str]("airline", airline), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[AirlinePriceIndexData],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bank_branch(
        self, symbol: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BankBranchRes, RawError]:
        """Retrieve list of US bank branches information for a given symbol.

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/bank-branch"),
            query_params=[param[Any]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[BankBranchRes],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def country(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[CountryMetadata], RawError]:
        """List all countries and metadata.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/country"),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[CountryMetadata]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def covid_19(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[CovidInfo], RawError]:
        """Get real-time updates on the number of COVID-19 (Corona virus) cases in the US with a state-by-state
        breakdown. Data is sourced from CDC and reputable sources. You can also access this API <a
        href="https://rapidapi.com/Finnhub/api/finnhub-real-time-covid-19" target="_blank" rel="nofollow">here</a>

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/covid19/us"),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[CovidInfo]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fda_committee_meeting_calendar(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[FdacomitteeMeeting], RawError]:
        """FDA's advisory committees are established to provide functions which support the agency's mission of
        protecting and promoting the public health, while meeting the requirements set forth in the Federal Advisory
        Committee Act. Committees are either mandated by statute or established at the discretion of the Department of
        Health and Human Services. Each committee is subject to renewal at two-year intervals unless the committee
        charter states otherwise.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/fda-advisory-committee-calendar"),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[FdacomitteeMeeting]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def quote(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Quote, RawError]:
        """<p>Get real-time quote data for US stocks. Constant polling is not recommended. Use websocket if you need
        real-time updates.</p><p>Real-time stock prices for international markets are supported for Enterprise clients
        via our partner's feed. <a href="mailto:support@finnhub.io">Contact Us</a> to learn more.</p>

        Args:
            symbol: Symbol
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/quote"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[Quote],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def sector_metric(
        self, region: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SectorMetric, RawError]:
        """Get ratios for different sectors and regions/indices.

        Args:
            region: Region. A list of supported values for this field can be found <a
                href="https://docs.google.com/spreadsheets/d/1afedyv7yWJ-z7pMjaAZK-f6ENY3mI3EBCk95QffpoHw/edit?usp=sharing"
                target="_blank">here</a>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sector/metrics"),
            query_params=[param[str]("region", region)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[SectorMetric],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def symbol_search(
        self, q: str, *, exchange: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SymbolLookup, RawError]:
        """Search for best-matching symbols based on your query. You can input anything from symbol, security's name to
        ISIN and Cusip.

        Args:
            q: Query text can be symbol, name, isin, or cusip.
            exchange: Exchange limit.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search"),
            query_params=[param[str]("q", q), param[str | None]("exchange", exchange)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[SymbolLookup],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def technical_indicator(
        self,
        symbol: str,
        resolution: str,
        from_: int,
        to: int,
        indicator: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, RawError]:
        """Return technical indicator with price data. List of supported indicators can be found <a
        href="https://docs.google.com/spreadsheets/d/1ylUvKHVYN2E87WdwIza8ROaCpd48ggEl1k5i5SgA29k/edit?usp=sharing"
        target="_blank">here</a>.

        Args:
            symbol: symbol
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            from_: UNIX timestamp. Interval initial value.
            to: UNIX timestamp. Interval end value.
            indicator: Indicator name. Full list can be found <a
                href="https://docs.google.com/spreadsheets/d/1ylUvKHVYN2E87WdwIza8ROaCpd48ggEl1k5i5SgA29k/edit?usp=sharing"
                target="_blank">here</a>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/indicator"),
            query_params=[
                param[str]("symbol", symbol),
                param[str]("resolution", resolution),
                param[int]("from", from_),
                param[int]("to", to),
                param[str]("indicator", indicator),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
