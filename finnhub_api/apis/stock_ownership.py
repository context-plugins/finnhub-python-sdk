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
from ..models.congressional_trading import CongressionalTrading
from ..models.fund_ownership import FundOwnership
from ..models.insider_sentiments import InsiderSentiments
from ..models.insider_transactions import InsiderTransactions
from ..models.investment_themes import InvestmentThemes
from ..models.lobbying_result import LobbyingResult
from ..models.ownership import Ownership
from ..models.social_sentiment import SocialSentiment
from ..models.supply_chain_relationships import SupplyChainRelationships
from ..models.usa_spending_result import UsaSpendingResult
from ..models.uspto_patent_result import UsptoPatentResult
from ..models.visa_application_result import VisaApplicationResult
from ..server.server import Server


class StockOwnership:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = StockOwnershipWithRawResponse(client, server, auth)

    def congressional_trading(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> CongressionalTrading:
        """Get stock trades data disclosed by members of congress.

        Args:
            symbol: Symbol of the company: AAPL.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.congressional_trading(
            symbol, from_, to, request_options=request_options
        ).unwrap()

    def fund_ownership(
        self, symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FundOwnership:
        """Get a full list fund and institutional investors of a company in descending order of the number of shares
        held. Data is sourced from <code>13F form</code>, <code>Schedule 13D</code> and <code>13G</code> for US market,
        <code>UK Share Register</code> for UK market, <code>SEDI</code> for Canadian market and equivalent filings for
        other international markets.

        Args:
            symbol: Symbol of the company: AAPL.
            limit: Limit number of results. Leave empty to get the full list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.fund_ownership(symbol, limit=limit, request_options=request_options).unwrap()

    def insider_sentiment(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> InsiderSentiments:
        """Get insider sentiment data for US companies calculated using method discussed <a
        href="https://medium.com/@stock-api/finnhub-insiders-sentiment-analysis-cc43f9f64b3a" target="_blank">here</a>.
        The MSPR ranges from -100 for the most negative to 100 for the most positive which can signal price changes in
        the coming 30-90 days.

        Args:
            symbol: Symbol of the company: AAPL.
            from_: From date: 2020-03-15.
            to: To date: 2020-03-16.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.insider_sentiment(symbol, from_, to, request_options=request_options).unwrap()

    def insider_transactions(
        self,
        symbol: str,
        *,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InsiderTransactions:
        """Company insider transactions data sourced from <code>Form 3,4,5</code>, SEDI and relevant companies' filings.
        This endpoint covers US, UK, Canada, Australia, India, and all major EU markets. Limit to 100 transactions per
        API call.

        Args:
            symbol: Symbol of the company: AAPL. Leave this param blank to get the latest transactions.
            from_: From date: 2020-03-15.
            to: To date: 2020-03-16.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.insider_transactions(
            symbol, from_=from_, to=to, request_options=request_options
        ).unwrap()

    def investment_themes(self, theme: str, *, request_options: RequestOptionsOrDict | None = None) -> InvestmentThemes:
        """<p>Thematic investing involves creating a portfolio (or portion of a portfolio) by gathering together a
        collection of companies involved in certain areas that you predict will generate above-market returns over the
        long term. Themes can be based on a concept such as ageing populations or a sub-sector such as robotics, and
        drones. Thematic investing focuses on predicted long-term trends rather than specific companies or sectors,
        enabling investors to access structural, one-off shifts that can change an entire industry.</p><p>This endpoint
        will help you get portfolios of different investment themes that are changing our life and are the way of the
        future.</p><p>A full list of themes supported can be found <a target="_blank"
        href="https://docs.google.com/spreadsheets/d/1ULj9xDh4iPoQj279M084adZ2_S852ttRthKKJ7madYc/edit?usp=sharing">here</a>.
        The theme coverage and portfolios are updated bi-weekly by our analysts. Our approach excludes penny,
        super-small cap and illiquid stocks.</p>

        Args:
            theme: Investment theme. A full list of themes supported can be found <a target="_blank"
                href="https://docs.google.com/spreadsheets/d/1ULj9xDh4iPoQj279M084adZ2_S852ttRthKKJ7madYc/edit?usp=sharing">here</a>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.investment_themes(theme, request_options=request_options).unwrap()

    def ownership(
        self, symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Ownership:
        """Get a full list of shareholders of a company in descending order of the number of shares held. Data is
        sourced from <code>13F form</code>, <code>Schedule 13D</code> and <code>13G</code> for US market, <code>UK Share
        Register</code> for UK market, <code>SEDI</code> for Canadian market and equivalent filings for other
        international markets.

        Args:
            symbol: Symbol of the company: AAPL.
            limit: Limit number of results. Leave empty to get the full list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.ownership(symbol, limit=limit, request_options=request_options).unwrap()

    def social_sentiment(
        self,
        symbol: str,
        *,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SocialSentiment:
        """<p>Get social sentiment for stocks on Reddit and Twitter.</p>

        Args:
            symbol: Company symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.social_sentiment(
            symbol, from_=from_, to=to, request_options=request_options
        ).unwrap()

    def stock_lobbying(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> LobbyingResult:
        """Get a list of reported lobbying activities in the Senate and the House.

        Args:
            symbol: Symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.stock_lobbying(symbol, from_, to, request_options=request_options).unwrap()

    def stock_usa_spending(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> UsaSpendingResult:
        """<p>Get a list of government's spending activities from USASpending dataset for public companies. This dataset
        can help you identify companies that win big government contracts which is extremely important for industries
        such as Defense, Aerospace, and Education. Only recent data is available via the API.</p><p>For historical data,
        you can download it here: <a href="/api/v1/stock/usa-spending?fileId=before_2021&token="
        target="_blank">Pre-2021</a>, <a href="/api/v1/stock/usa-spending?fileId=2021&token=" target="_blank">2021</a>,
        <a href="/api/v1/stock/usa-spending?fileId=2022&token=" target="_blank">2022</a>, <a
        href="/api/v1/stock/usa-spending?fileId=2023&token=" target="_blank">2023</a>, <a
        href="/api/v1/stock/usa-spending?fileId=2024&token=" target="_blank">2024</a></p>

        Args:
            symbol: Symbol.
            from_: From date <code>YYYY-MM-DD</code>. Filter for <code>actionDate</code>
            to: To date <code>YYYY-MM-DD</code>. Filter for <code>actionDate</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.stock_usa_spending(symbol, from_, to, request_options=request_options).unwrap()

    def stock_uspto_patent(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> UsptoPatentResult:
        """List USPTO patents for companies. Limit to 250 records per API call.

        Args:
            symbol: Symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.stock_uspto_patent(symbol, from_, to, request_options=request_options).unwrap()

    def stock_visa_application(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> VisaApplicationResult:
        """Get a list of H1-B and Permanent visa applications for companies from the DOL. The data is updated quarterly.

        Args:
            symbol: Symbol.
            from_: From date <code>YYYY-MM-DD</code>. Filter on the <code>beginDate</code> column.
            to: To date <code>YYYY-MM-DD</code>. Filter on the <code>beginDate</code> column.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.stock_visa_application(
            symbol, from_, to, request_options=request_options
        ).unwrap()

    def supply_chain_relationships(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SupplyChainRelationships:
        """<p>This endpoint provides an overall map of public companies' key customers and suppliers. The data offers a
        deeper look into a company's supply chain and how products are created. The data will help investors manage
        risk, limit exposure or generate alpha-generating ideas and trading insights.</p>

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.supply_chain_relationships(symbol, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> StockOwnershipWithRawResponse:
        return self._with_raw_response


class AsyncStockOwnership:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncStockOwnershipWithRawResponse(client, server, auth)

    async def congressional_trading(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> CongressionalTrading:
        """Get stock trades data disclosed by members of congress.

        Args:
            symbol: Symbol of the company: AAPL.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.congressional_trading(symbol, from_, to, request_options=request_options)
        ).unwrap()

    async def fund_ownership(
        self, symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FundOwnership:
        """Get a full list fund and institutional investors of a company in descending order of the number of shares
        held. Data is sourced from <code>13F form</code>, <code>Schedule 13D</code> and <code>13G</code> for US market,
        <code>UK Share Register</code> for UK market, <code>SEDI</code> for Canadian market and equivalent filings for
        other international markets.

        Args:
            symbol: Symbol of the company: AAPL.
            limit: Limit number of results. Leave empty to get the full list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.fund_ownership(symbol, limit=limit, request_options=request_options)
        ).unwrap()

    async def insider_sentiment(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> InsiderSentiments:
        """Get insider sentiment data for US companies calculated using method discussed <a
        href="https://medium.com/@stock-api/finnhub-insiders-sentiment-analysis-cc43f9f64b3a" target="_blank">here</a>.
        The MSPR ranges from -100 for the most negative to 100 for the most positive which can signal price changes in
        the coming 30-90 days.

        Args:
            symbol: Symbol of the company: AAPL.
            from_: From date: 2020-03-15.
            to: To date: 2020-03-16.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.insider_sentiment(symbol, from_, to, request_options=request_options)
        ).unwrap()

    async def insider_transactions(
        self,
        symbol: str,
        *,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InsiderTransactions:
        """Company insider transactions data sourced from <code>Form 3,4,5</code>, SEDI and relevant companies' filings.
        This endpoint covers US, UK, Canada, Australia, India, and all major EU markets. Limit to 100 transactions per
        API call.

        Args:
            symbol: Symbol of the company: AAPL. Leave this param blank to get the latest transactions.
            from_: From date: 2020-03-15.
            to: To date: 2020-03-16.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.insider_transactions(
                symbol, from_=from_, to=to, request_options=request_options
            )
        ).unwrap()

    async def investment_themes(
        self, theme: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> InvestmentThemes:
        """<p>Thematic investing involves creating a portfolio (or portion of a portfolio) by gathering together a
        collection of companies involved in certain areas that you predict will generate above-market returns over the
        long term. Themes can be based on a concept such as ageing populations or a sub-sector such as robotics, and
        drones. Thematic investing focuses on predicted long-term trends rather than specific companies or sectors,
        enabling investors to access structural, one-off shifts that can change an entire industry.</p><p>This endpoint
        will help you get portfolios of different investment themes that are changing our life and are the way of the
        future.</p><p>A full list of themes supported can be found <a target="_blank"
        href="https://docs.google.com/spreadsheets/d/1ULj9xDh4iPoQj279M084adZ2_S852ttRthKKJ7madYc/edit?usp=sharing">here</a>.
        The theme coverage and portfolios are updated bi-weekly by our analysts. Our approach excludes penny,
        super-small cap and illiquid stocks.</p>

        Args:
            theme: Investment theme. A full list of themes supported can be found <a target="_blank"
                href="https://docs.google.com/spreadsheets/d/1ULj9xDh4iPoQj279M084adZ2_S852ttRthKKJ7madYc/edit?usp=sharing">here</a>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.investment_themes(theme, request_options=request_options)).unwrap()

    async def ownership(
        self, symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Ownership:
        """Get a full list of shareholders of a company in descending order of the number of shares held. Data is
        sourced from <code>13F form</code>, <code>Schedule 13D</code> and <code>13G</code> for US market, <code>UK Share
        Register</code> for UK market, <code>SEDI</code> for Canadian market and equivalent filings for other
        international markets.

        Args:
            symbol: Symbol of the company: AAPL.
            limit: Limit number of results. Leave empty to get the full list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.ownership(symbol, limit=limit, request_options=request_options)).unwrap()

    async def social_sentiment(
        self,
        symbol: str,
        *,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SocialSentiment:
        """<p>Get social sentiment for stocks on Reddit and Twitter.</p>

        Args:
            symbol: Company symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.social_sentiment(symbol, from_=from_, to=to, request_options=request_options)
        ).unwrap()

    async def stock_lobbying(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> LobbyingResult:
        """Get a list of reported lobbying activities in the Senate and the House.

        Args:
            symbol: Symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.stock_lobbying(symbol, from_, to, request_options=request_options)
        ).unwrap()

    async def stock_usa_spending(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> UsaSpendingResult:
        """<p>Get a list of government's spending activities from USASpending dataset for public companies. This dataset
        can help you identify companies that win big government contracts which is extremely important for industries
        such as Defense, Aerospace, and Education. Only recent data is available via the API.</p><p>For historical data,
        you can download it here: <a href="/api/v1/stock/usa-spending?fileId=before_2021&token="
        target="_blank">Pre-2021</a>, <a href="/api/v1/stock/usa-spending?fileId=2021&token=" target="_blank">2021</a>,
        <a href="/api/v1/stock/usa-spending?fileId=2022&token=" target="_blank">2022</a>, <a
        href="/api/v1/stock/usa-spending?fileId=2023&token=" target="_blank">2023</a>, <a
        href="/api/v1/stock/usa-spending?fileId=2024&token=" target="_blank">2024</a></p>

        Args:
            symbol: Symbol.
            from_: From date <code>YYYY-MM-DD</code>. Filter for <code>actionDate</code>
            to: To date <code>YYYY-MM-DD</code>. Filter for <code>actionDate</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.stock_usa_spending(symbol, from_, to, request_options=request_options)
        ).unwrap()

    async def stock_uspto_patent(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> UsptoPatentResult:
        """List USPTO patents for companies. Limit to 250 records per API call.

        Args:
            symbol: Symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.stock_uspto_patent(symbol, from_, to, request_options=request_options)
        ).unwrap()

    async def stock_visa_application(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> VisaApplicationResult:
        """Get a list of H1-B and Permanent visa applications for companies from the DOL. The data is updated quarterly.

        Args:
            symbol: Symbol.
            from_: From date <code>YYYY-MM-DD</code>. Filter on the <code>beginDate</code> column.
            to: To date <code>YYYY-MM-DD</code>. Filter on the <code>beginDate</code> column.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.stock_visa_application(symbol, from_, to, request_options=request_options)
        ).unwrap()

    async def supply_chain_relationships(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SupplyChainRelationships:
        """<p>This endpoint provides an overall map of public companies' key customers and suppliers. The data offers a
        deeper look into a company's supply chain and how products are created. The data will help investors manage
        risk, limit exposure or generate alpha-generating ideas and trading insights.</p>

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.supply_chain_relationships(symbol, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncStockOwnershipWithRawResponse:
        return self._with_raw_response


class StockOwnershipWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def congressional_trading(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CongressionalTrading, RawError]:
        """Get stock trades data disclosed by members of congress.

        Args:
            symbol: Symbol of the company: AAPL.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/congressional-trading"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[CongressionalTrading],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def fund_ownership(
        self, symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FundOwnership, RawError]:
        """Get a full list fund and institutional investors of a company in descending order of the number of shares
        held. Data is sourced from <code>13F form</code>, <code>Schedule 13D</code> and <code>13G</code> for US market,
        <code>UK Share Register</code> for UK market, <code>SEDI</code> for Canadian market and equivalent filings for
        other international markets.

        Args:
            symbol: Symbol of the company: AAPL.
            limit: Limit number of results. Leave empty to get the full list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/fund-ownership"),
            query_params=[param[str]("symbol", symbol), param[int | None]("limit", limit)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[FundOwnership],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def insider_sentiment(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InsiderSentiments, RawError]:
        """Get insider sentiment data for US companies calculated using method discussed <a
        href="https://medium.com/@stock-api/finnhub-insiders-sentiment-analysis-cc43f9f64b3a" target="_blank">here</a>.
        The MSPR ranges from -100 for the most negative to 100 for the most positive which can signal price changes in
        the coming 30-90 days.

        Args:
            symbol: Symbol of the company: AAPL.
            from_: From date: 2020-03-15.
            to: To date: 2020-03-16.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/insider-sentiment"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[InsiderSentiments],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def insider_transactions(
        self,
        symbol: str,
        *,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InsiderTransactions, RawError]:
        """Company insider transactions data sourced from <code>Form 3,4,5</code>, SEDI and relevant companies' filings.
        This endpoint covers US, UK, Canada, Australia, India, and all major EU markets. Limit to 100 transactions per
        API call.

        Args:
            symbol: Symbol of the company: AAPL. Leave this param blank to get the latest transactions.
            from_: From date: 2020-03-15.
            to: To date: 2020-03-16.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/insider-transactions"),
            query_params=[
                param[str]("symbol", symbol), param[Date | None]("from", from_), param[Date | None]("to", to)
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[InsiderTransactions],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def investment_themes(
        self, theme: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InvestmentThemes, RawError]:
        """<p>Thematic investing involves creating a portfolio (or portion of a portfolio) by gathering together a
        collection of companies involved in certain areas that you predict will generate above-market returns over the
        long term. Themes can be based on a concept such as ageing populations or a sub-sector such as robotics, and
        drones. Thematic investing focuses on predicted long-term trends rather than specific companies or sectors,
        enabling investors to access structural, one-off shifts that can change an entire industry.</p><p>This endpoint
        will help you get portfolios of different investment themes that are changing our life and are the way of the
        future.</p><p>A full list of themes supported can be found <a target="_blank"
        href="https://docs.google.com/spreadsheets/d/1ULj9xDh4iPoQj279M084adZ2_S852ttRthKKJ7madYc/edit?usp=sharing">here</a>.
        The theme coverage and portfolios are updated bi-weekly by our analysts. Our approach excludes penny,
        super-small cap and illiquid stocks.</p>

        Args:
            theme: Investment theme. A full list of themes supported can be found <a target="_blank"
                href="https://docs.google.com/spreadsheets/d/1ULj9xDh4iPoQj279M084adZ2_S852ttRthKKJ7madYc/edit?usp=sharing">here</a>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/investment-theme"),
            query_params=[param[str]("theme", theme)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[InvestmentThemes],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def ownership(
        self, symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Ownership, RawError]:
        """Get a full list of shareholders of a company in descending order of the number of shares held. Data is
        sourced from <code>13F form</code>, <code>Schedule 13D</code> and <code>13G</code> for US market, <code>UK Share
        Register</code> for UK market, <code>SEDI</code> for Canadian market and equivalent filings for other
        international markets.

        Args:
            symbol: Symbol of the company: AAPL.
            limit: Limit number of results. Leave empty to get the full list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/ownership"),
            query_params=[param[str]("symbol", symbol), param[int | None]("limit", limit)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[Ownership],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def social_sentiment(
        self,
        symbol: str,
        *,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SocialSentiment, RawError]:
        """<p>Get social sentiment for stocks on Reddit and Twitter.</p>

        Args:
            symbol: Company symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/social-sentiment"),
            query_params=[
                param[str]("symbol", symbol), param[Date | None]("from", from_), param[Date | None]("to", to)
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[SocialSentiment],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stock_lobbying(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LobbyingResult, RawError]:
        """Get a list of reported lobbying activities in the Senate and the House.

        Args:
            symbol: Symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/lobbying"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[LobbyingResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stock_usa_spending(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UsaSpendingResult, RawError]:
        """<p>Get a list of government's spending activities from USASpending dataset for public companies. This dataset
        can help you identify companies that win big government contracts which is extremely important for industries
        such as Defense, Aerospace, and Education. Only recent data is available via the API.</p><p>For historical data,
        you can download it here: <a href="/api/v1/stock/usa-spending?fileId=before_2021&token="
        target="_blank">Pre-2021</a>, <a href="/api/v1/stock/usa-spending?fileId=2021&token=" target="_blank">2021</a>,
        <a href="/api/v1/stock/usa-spending?fileId=2022&token=" target="_blank">2022</a>, <a
        href="/api/v1/stock/usa-spending?fileId=2023&token=" target="_blank">2023</a>, <a
        href="/api/v1/stock/usa-spending?fileId=2024&token=" target="_blank">2024</a></p>

        Args:
            symbol: Symbol.
            from_: From date <code>YYYY-MM-DD</code>. Filter for <code>actionDate</code>
            to: To date <code>YYYY-MM-DD</code>. Filter for <code>actionDate</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/usa-spending"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[UsaSpendingResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stock_uspto_patent(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UsptoPatentResult, RawError]:
        """List USPTO patents for companies. Limit to 250 records per API call.

        Args:
            symbol: Symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/uspto-patent"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[UsptoPatentResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stock_visa_application(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VisaApplicationResult, RawError]:
        """Get a list of H1-B and Permanent visa applications for companies from the DOL. The data is updated quarterly.

        Args:
            symbol: Symbol.
            from_: From date <code>YYYY-MM-DD</code>. Filter on the <code>beginDate</code> column.
            to: To date <code>YYYY-MM-DD</code>. Filter on the <code>beginDate</code> column.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/visa-application"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[VisaApplicationResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def supply_chain_relationships(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SupplyChainRelationships, RawError]:
        """<p>This endpoint provides an overall map of public companies' key customers and suppliers. The data offers a
        deeper look into a company's supply chain and how products are created. The data will help investors manage
        risk, limit exposure or generate alpha-generating ideas and trading insights.</p>

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/supply-chain"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[SupplyChainRelationships],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncStockOwnershipWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def congressional_trading(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CongressionalTrading, RawError]:
        """Get stock trades data disclosed by members of congress.

        Args:
            symbol: Symbol of the company: AAPL.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/congressional-trading"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[CongressionalTrading],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def fund_ownership(
        self, symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FundOwnership, RawError]:
        """Get a full list fund and institutional investors of a company in descending order of the number of shares
        held. Data is sourced from <code>13F form</code>, <code>Schedule 13D</code> and <code>13G</code> for US market,
        <code>UK Share Register</code> for UK market, <code>SEDI</code> for Canadian market and equivalent filings for
        other international markets.

        Args:
            symbol: Symbol of the company: AAPL.
            limit: Limit number of results. Leave empty to get the full list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/fund-ownership"),
            query_params=[param[str]("symbol", symbol), param[int | None]("limit", limit)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[FundOwnership],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def insider_sentiment(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InsiderSentiments, RawError]:
        """Get insider sentiment data for US companies calculated using method discussed <a
        href="https://medium.com/@stock-api/finnhub-insiders-sentiment-analysis-cc43f9f64b3a" target="_blank">here</a>.
        The MSPR ranges from -100 for the most negative to 100 for the most positive which can signal price changes in
        the coming 30-90 days.

        Args:
            symbol: Symbol of the company: AAPL.
            from_: From date: 2020-03-15.
            to: To date: 2020-03-16.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/insider-sentiment"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[InsiderSentiments],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def insider_transactions(
        self,
        symbol: str,
        *,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InsiderTransactions, RawError]:
        """Company insider transactions data sourced from <code>Form 3,4,5</code>, SEDI and relevant companies' filings.
        This endpoint covers US, UK, Canada, Australia, India, and all major EU markets. Limit to 100 transactions per
        API call.

        Args:
            symbol: Symbol of the company: AAPL. Leave this param blank to get the latest transactions.
            from_: From date: 2020-03-15.
            to: To date: 2020-03-16.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/insider-transactions"),
            query_params=[
                param[str]("symbol", symbol), param[Date | None]("from", from_), param[Date | None]("to", to)
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[InsiderTransactions],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def investment_themes(
        self, theme: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InvestmentThemes, RawError]:
        """<p>Thematic investing involves creating a portfolio (or portion of a portfolio) by gathering together a
        collection of companies involved in certain areas that you predict will generate above-market returns over the
        long term. Themes can be based on a concept such as ageing populations or a sub-sector such as robotics, and
        drones. Thematic investing focuses on predicted long-term trends rather than specific companies or sectors,
        enabling investors to access structural, one-off shifts that can change an entire industry.</p><p>This endpoint
        will help you get portfolios of different investment themes that are changing our life and are the way of the
        future.</p><p>A full list of themes supported can be found <a target="_blank"
        href="https://docs.google.com/spreadsheets/d/1ULj9xDh4iPoQj279M084adZ2_S852ttRthKKJ7madYc/edit?usp=sharing">here</a>.
        The theme coverage and portfolios are updated bi-weekly by our analysts. Our approach excludes penny,
        super-small cap and illiquid stocks.</p>

        Args:
            theme: Investment theme. A full list of themes supported can be found <a target="_blank"
                href="https://docs.google.com/spreadsheets/d/1ULj9xDh4iPoQj279M084adZ2_S852ttRthKKJ7madYc/edit?usp=sharing">here</a>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/investment-theme"),
            query_params=[param[str]("theme", theme)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[InvestmentThemes],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def ownership(
        self, symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Ownership, RawError]:
        """Get a full list of shareholders of a company in descending order of the number of shares held. Data is
        sourced from <code>13F form</code>, <code>Schedule 13D</code> and <code>13G</code> for US market, <code>UK Share
        Register</code> for UK market, <code>SEDI</code> for Canadian market and equivalent filings for other
        international markets.

        Args:
            symbol: Symbol of the company: AAPL.
            limit: Limit number of results. Leave empty to get the full list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/ownership"),
            query_params=[param[str]("symbol", symbol), param[int | None]("limit", limit)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[Ownership],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def social_sentiment(
        self,
        symbol: str,
        *,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SocialSentiment, RawError]:
        """<p>Get social sentiment for stocks on Reddit and Twitter.</p>

        Args:
            symbol: Company symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/social-sentiment"),
            query_params=[
                param[str]("symbol", symbol), param[Date | None]("from", from_), param[Date | None]("to", to)
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[SocialSentiment],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def stock_lobbying(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LobbyingResult, RawError]:
        """Get a list of reported lobbying activities in the Senate and the House.

        Args:
            symbol: Symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/lobbying"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[LobbyingResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def stock_usa_spending(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UsaSpendingResult, RawError]:
        """<p>Get a list of government's spending activities from USASpending dataset for public companies. This dataset
        can help you identify companies that win big government contracts which is extremely important for industries
        such as Defense, Aerospace, and Education. Only recent data is available via the API.</p><p>For historical data,
        you can download it here: <a href="/api/v1/stock/usa-spending?fileId=before_2021&token="
        target="_blank">Pre-2021</a>, <a href="/api/v1/stock/usa-spending?fileId=2021&token=" target="_blank">2021</a>,
        <a href="/api/v1/stock/usa-spending?fileId=2022&token=" target="_blank">2022</a>, <a
        href="/api/v1/stock/usa-spending?fileId=2023&token=" target="_blank">2023</a>, <a
        href="/api/v1/stock/usa-spending?fileId=2024&token=" target="_blank">2024</a></p>

        Args:
            symbol: Symbol.
            from_: From date <code>YYYY-MM-DD</code>. Filter for <code>actionDate</code>
            to: To date <code>YYYY-MM-DD</code>. Filter for <code>actionDate</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/usa-spending"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[UsaSpendingResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def stock_uspto_patent(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UsptoPatentResult, RawError]:
        """List USPTO patents for companies. Limit to 250 records per API call.

        Args:
            symbol: Symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/uspto-patent"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[UsptoPatentResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def stock_visa_application(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VisaApplicationResult, RawError]:
        """Get a list of H1-B and Permanent visa applications for companies from the DOL. The data is updated quarterly.

        Args:
            symbol: Symbol.
            from_: From date <code>YYYY-MM-DD</code>. Filter on the <code>beginDate</code> column.
            to: To date <code>YYYY-MM-DD</code>. Filter on the <code>beginDate</code> column.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/visa-application"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[VisaApplicationResult],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def supply_chain_relationships(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SupplyChainRelationships, RawError]:
        """<p>This endpoint provides an overall map of public companies' key customers and suppliers. The data offers a
        deeper look into a company's supply chain and how products are created. The data will help investors manage
        risk, limit exposure or generate alpha-generating ideas and trading insights.</p>

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/supply-chain"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[SupplyChainRelationships],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
