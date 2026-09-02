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
from ..models.capex_estimates import CapexEstimates
from ..models.company_earnings_quality_score import CompanyEarningsQualityScore
from ..models.dps_estimates import DpsEstimates
from ..models.earning_result import EarningResult
from ..models.earnings_estimates import EarningsEstimates
from ..models.ebit_estimates import EbitEstimates
from ..models.ebitda_estimates import EbitdaEstimates
from ..models.fcf_estimates import FcfEstimates
from ..models.gross_income_estimates import GrossIncomeEstimates
from ..models.net_income_estimates import NetIncomeEstimates
from ..models.ocf_estimates import OcfEstimates
from ..models.pretax_income_estimates import PretaxIncomeEstimates
from ..models.price_target import PriceTarget
from ..models.recommendation_trend import RecommendationTrend
from ..models.revenue_breakdown import RevenueBreakdown
from ..models.revenue_breakdown2 import RevenueBreakdown2
from ..models.revenue_estimates import RevenueEstimates
from ..models.upgrade_downgrade import UpgradeDowngrade
from ..server.server import Server


class StockEstimates:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = StockEstimatesWithRawResponse(client, server, auth)

    def company_capex_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> CapexEstimates:
        """Get company's capital expenditure estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.company_capex_estimates(
            symbol, freq=freq, request_options=request_options
        ).unwrap()

    def company_dps_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> DpsEstimates:
        """Get company's Dividend per Share estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.company_dps_estimates(
            symbol, freq=freq, request_options=request_options
        ).unwrap()

    def company_earnings(
        self, symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[EarningResult]:
        """Get company historical quarterly earnings surprise going back to 2000.

        Args:
            symbol: Symbol of the company: AAPL.
            limit: Limit number of period returned. Leave blank to get the full history.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.company_earnings(symbol, limit=limit, request_options=request_options).unwrap()

    def company_earnings_quality_score(
        self, symbol: str, freq: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CompanyEarningsQualityScore:
        """<p>This endpoint provides Earnings Quality Score for global companies.</p><p> Earnings quality refers to the
        extent to which current earnings predict future earnings. "High-quality" earnings are expected to persist, while
        "low-quality" earnings do not. A higher score means a higher earnings quality</p><p>Finnhub uses a proprietary
        model which takes into consideration 4 criteria:</p> <ul style="list-style-type: unset; margin-left:
        30px;"><li>Profitability</li><li>Growth</li><li>Cash Generation & Capital
        Allocation</li><li>Leverage</li></ul><br/><p>We then compare the metrics of each company in each category
        against its peers in the same industry to gauge how quality its earnings is.</p>

        Args:
            symbol: Symbol.
            freq: Frequency. Currently support <code>annual</code> and <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.company_earnings_quality_score(
            symbol, freq, request_options=request_options
        ).unwrap()

    def company_ebit_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> EbitEstimates:
        """Get company's ebit estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.company_ebit_estimates(
            symbol, freq=freq, request_options=request_options
        ).unwrap()

    def company_ebitda_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> EbitdaEstimates:
        """Get company's ebitda estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.company_ebitda_estimates(
            symbol, freq=freq, request_options=request_options
        ).unwrap()

    def company_eps_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> EarningsEstimates:
        """Get company's EPS estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.company_eps_estimates(
            symbol, freq=freq, request_options=request_options
        ).unwrap()

    def company_fcf_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FcfEstimates:
        """Get company's free cash flow estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.company_fcf_estimates(
            symbol, freq=freq, request_options=request_options
        ).unwrap()

    def company_gross_income_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> GrossIncomeEstimates:
        """Get company's gross income estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.company_gross_income_estimates(
            symbol, freq=freq, request_options=request_options
        ).unwrap()

    def company_net_income_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> NetIncomeEstimates:
        """Get company's net income estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.company_net_income_estimates(
            symbol, freq=freq, request_options=request_options
        ).unwrap()

    def company_ocf_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> OcfEstimates:
        """Get company's operating cash flow estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.company_ocf_estimates(
            symbol, freq=freq, request_options=request_options
        ).unwrap()

    def company_pretax_income_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> PretaxIncomeEstimates:
        """Get company's pretax income estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.company_pretax_income_estimates(
            symbol, freq=freq, request_options=request_options
        ).unwrap()

    def company_revenue_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> RevenueEstimates:
        """Get company's revenue estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.company_revenue_estimates(
            symbol, freq=freq, request_options=request_options
        ).unwrap()

    def price_target(self, symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> PriceTarget:
        """Get latest price target consensus.

        Args:
            symbol: Symbol of the company: AAPL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.price_target(symbol, request_options=request_options).unwrap()

    def recommendation_trends(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[RecommendationTrend]:
        """Get latest analyst recommendation trends for a company.

        Args:
            symbol: Symbol of the company: AAPL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.recommendation_trends(symbol, request_options=request_options).unwrap()

    def revenue_breakdown(
        self, *, symbol: str | None = None, cik: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> RevenueBreakdown:
        """<p>Get revenue breakdown as-reporetd by product and geography. Users on personal plans can access data for US
        companies which disclose their revenue breakdown in the annual or quarterly reports.</p><p>Global standardized
        revenue breakdown/segments data is available for Enterprise users. <a href="mailto:support@finnhub.io">Contact
        us</a> to inquire about the access for Global standardized data.</p>

        Args:
            symbol: Symbol.
            cik: CIK.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.revenue_breakdown(
            symbol=symbol, cik=cik, request_options=request_options
        ).unwrap()

    def revenue_breakdown2(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RevenueBreakdown2:
        """<p>Get standardized revenue breakdown and KPIs data for 30,000+ global companies.</p>

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.revenue_breakdown2(symbol, request_options=request_options).unwrap()

    def upgrade_downgrade(
        self,
        *,
        symbol: str | None = None,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[UpgradeDowngrade]:
        """Get latest stock upgrade and downgrade.

        Args:
            symbol: Symbol of the company: AAPL. If left blank, the API will return latest stock upgrades/downgrades.
            from_: From date: 2000-03-15.
            to: To date: 2020-03-16.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.upgrade_downgrade(
            symbol=symbol, from_=from_, to=to, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> StockEstimatesWithRawResponse:
        return self._with_raw_response


class AsyncStockEstimates:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncStockEstimatesWithRawResponse(client, server, auth)

    async def company_capex_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> CapexEstimates:
        """Get company's capital expenditure estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.company_capex_estimates(symbol, freq=freq, request_options=request_options)
        ).unwrap()

    async def company_dps_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> DpsEstimates:
        """Get company's Dividend per Share estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.company_dps_estimates(symbol, freq=freq, request_options=request_options)
        ).unwrap()

    async def company_earnings(
        self, symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[EarningResult]:
        """Get company historical quarterly earnings surprise going back to 2000.

        Args:
            symbol: Symbol of the company: AAPL.
            limit: Limit number of period returned. Leave blank to get the full history.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.company_earnings(symbol, limit=limit, request_options=request_options)
        ).unwrap()

    async def company_earnings_quality_score(
        self, symbol: str, freq: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CompanyEarningsQualityScore:
        """<p>This endpoint provides Earnings Quality Score for global companies.</p><p> Earnings quality refers to the
        extent to which current earnings predict future earnings. "High-quality" earnings are expected to persist, while
        "low-quality" earnings do not. A higher score means a higher earnings quality</p><p>Finnhub uses a proprietary
        model which takes into consideration 4 criteria:</p> <ul style="list-style-type: unset; margin-left:
        30px;"><li>Profitability</li><li>Growth</li><li>Cash Generation & Capital
        Allocation</li><li>Leverage</li></ul><br/><p>We then compare the metrics of each company in each category
        against its peers in the same industry to gauge how quality its earnings is.</p>

        Args:
            symbol: Symbol.
            freq: Frequency. Currently support <code>annual</code> and <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.company_earnings_quality_score(symbol, freq, request_options=request_options)
        ).unwrap()

    async def company_ebit_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> EbitEstimates:
        """Get company's ebit estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.company_ebit_estimates(symbol, freq=freq, request_options=request_options)
        ).unwrap()

    async def company_ebitda_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> EbitdaEstimates:
        """Get company's ebitda estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.company_ebitda_estimates(symbol, freq=freq, request_options=request_options)
        ).unwrap()

    async def company_eps_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> EarningsEstimates:
        """Get company's EPS estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.company_eps_estimates(symbol, freq=freq, request_options=request_options)
        ).unwrap()

    async def company_fcf_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> FcfEstimates:
        """Get company's free cash flow estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.company_fcf_estimates(symbol, freq=freq, request_options=request_options)
        ).unwrap()

    async def company_gross_income_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> GrossIncomeEstimates:
        """Get company's gross income estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.company_gross_income_estimates(
                symbol, freq=freq, request_options=request_options
            )
        ).unwrap()

    async def company_net_income_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> NetIncomeEstimates:
        """Get company's net income estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.company_net_income_estimates(
                symbol, freq=freq, request_options=request_options
            )
        ).unwrap()

    async def company_ocf_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> OcfEstimates:
        """Get company's operating cash flow estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.company_ocf_estimates(symbol, freq=freq, request_options=request_options)
        ).unwrap()

    async def company_pretax_income_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> PretaxIncomeEstimates:
        """Get company's pretax income estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.company_pretax_income_estimates(
                symbol, freq=freq, request_options=request_options
            )
        ).unwrap()

    async def company_revenue_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> RevenueEstimates:
        """Get company's revenue estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.company_revenue_estimates(symbol, freq=freq, request_options=request_options)
        ).unwrap()

    async def price_target(self, symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> PriceTarget:
        """Get latest price target consensus.

        Args:
            symbol: Symbol of the company: AAPL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.price_target(symbol, request_options=request_options)).unwrap()

    async def recommendation_trends(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[RecommendationTrend]:
        """Get latest analyst recommendation trends for a company.

        Args:
            symbol: Symbol of the company: AAPL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.recommendation_trends(symbol, request_options=request_options)).unwrap()

    async def revenue_breakdown(
        self, *, symbol: str | None = None, cik: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> RevenueBreakdown:
        """<p>Get revenue breakdown as-reporetd by product and geography. Users on personal plans can access data for US
        companies which disclose their revenue breakdown in the annual or quarterly reports.</p><p>Global standardized
        revenue breakdown/segments data is available for Enterprise users. <a href="mailto:support@finnhub.io">Contact
        us</a> to inquire about the access for Global standardized data.</p>

        Args:
            symbol: Symbol.
            cik: CIK.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.revenue_breakdown(symbol=symbol, cik=cik, request_options=request_options)
        ).unwrap()

    async def revenue_breakdown2(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RevenueBreakdown2:
        """<p>Get standardized revenue breakdown and KPIs data for 30,000+ global companies.</p>

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.revenue_breakdown2(symbol, request_options=request_options)).unwrap()

    async def upgrade_downgrade(
        self,
        *,
        symbol: str | None = None,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[UpgradeDowngrade]:
        """Get latest stock upgrade and downgrade.

        Args:
            symbol: Symbol of the company: AAPL. If left blank, the API will return latest stock upgrades/downgrades.
            from_: From date: 2000-03-15.
            to: To date: 2020-03-16.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.upgrade_downgrade(
                symbol=symbol, from_=from_, to=to, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncStockEstimatesWithRawResponse:
        return self._with_raw_response


class StockEstimatesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def company_capex_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CapexEstimates, RawError]:
        """Get company's capital expenditure estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/capex-estimate"),
            query_params=[param[str]("symbol", symbol), param[str | None]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[CapexEstimates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def company_dps_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DpsEstimates, RawError]:
        """Get company's Dividend per Share estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/dps-estimate"),
            query_params=[param[str]("symbol", symbol), param[str | None]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[DpsEstimates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def company_earnings(
        self, symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[EarningResult], RawError]:
        """Get company historical quarterly earnings surprise going back to 2000.

        Args:
            symbol: Symbol of the company: AAPL.
            limit: Limit number of period returned. Leave blank to get the full history.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/earnings"),
            query_params=[param[str]("symbol", symbol), param[int | None]("limit", limit)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[EarningResult]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def company_earnings_quality_score(
        self, symbol: str, freq: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CompanyEarningsQualityScore, RawError]:
        """<p>This endpoint provides Earnings Quality Score for global companies.</p><p> Earnings quality refers to the
        extent to which current earnings predict future earnings. "High-quality" earnings are expected to persist, while
        "low-quality" earnings do not. A higher score means a higher earnings quality</p><p>Finnhub uses a proprietary
        model which takes into consideration 4 criteria:</p> <ul style="list-style-type: unset; margin-left:
        30px;"><li>Profitability</li><li>Growth</li><li>Cash Generation & Capital
        Allocation</li><li>Leverage</li></ul><br/><p>We then compare the metrics of each company in each category
        against its peers in the same industry to gauge how quality its earnings is.</p>

        Args:
            symbol: Symbol.
            freq: Frequency. Currently support <code>annual</code> and <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/earnings-quality-score"),
            query_params=[param[str]("symbol", symbol), param[str]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[CompanyEarningsQualityScore],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def company_ebit_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EbitEstimates, RawError]:
        """Get company's ebit estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/ebit-estimate"),
            query_params=[param[str]("symbol", symbol), param[str | None]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EbitEstimates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def company_ebitda_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EbitdaEstimates, RawError]:
        """Get company's ebitda estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/ebitda-estimate"),
            query_params=[param[str]("symbol", symbol), param[str | None]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EbitdaEstimates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def company_eps_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EarningsEstimates, RawError]:
        """Get company's EPS estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/eps-estimate"),
            query_params=[param[str]("symbol", symbol), param[str | None]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EarningsEstimates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def company_fcf_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FcfEstimates, RawError]:
        """Get company's free cash flow estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/fcf-estimate"),
            query_params=[param[str]("symbol", symbol), param[str | None]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[FcfEstimates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def company_gross_income_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GrossIncomeEstimates, RawError]:
        """Get company's gross income estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/gross-income-estimate"),
            query_params=[param[str]("symbol", symbol), param[str | None]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[GrossIncomeEstimates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def company_net_income_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NetIncomeEstimates, RawError]:
        """Get company's net income estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/net-income-estimate"),
            query_params=[param[str]("symbol", symbol), param[str | None]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[NetIncomeEstimates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def company_ocf_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OcfEstimates, RawError]:
        """Get company's operating cash flow estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/ocf-estimate"),
            query_params=[param[str]("symbol", symbol), param[str | None]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[OcfEstimates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def company_pretax_income_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PretaxIncomeEstimates, RawError]:
        """Get company's pretax income estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/pretax-income-estimate"),
            query_params=[param[str]("symbol", symbol), param[str | None]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[PretaxIncomeEstimates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def company_revenue_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RevenueEstimates, RawError]:
        """Get company's revenue estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/revenue-estimate"),
            query_params=[param[str]("symbol", symbol), param[str | None]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[RevenueEstimates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def price_target(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PriceTarget, RawError]:
        """Get latest price target consensus.

        Args:
            symbol: Symbol of the company: AAPL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/price-target"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[PriceTarget],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def recommendation_trends(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[RecommendationTrend], RawError]:
        """Get latest analyst recommendation trends for a company.

        Args:
            symbol: Symbol of the company: AAPL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/recommendation"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[RecommendationTrend]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def revenue_breakdown(
        self, *, symbol: str | None = None, cik: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RevenueBreakdown, RawError]:
        """<p>Get revenue breakdown as-reporetd by product and geography. Users on personal plans can access data for US
        companies which disclose their revenue breakdown in the annual or quarterly reports.</p><p>Global standardized
        revenue breakdown/segments data is available for Enterprise users. <a href="mailto:support@finnhub.io">Contact
        us</a> to inquire about the access for Global standardized data.</p>

        Args:
            symbol: Symbol.
            cik: CIK.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/revenue-breakdown"),
            query_params=[param[str | None]("symbol", symbol), param[str | None]("cik", cik)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[RevenueBreakdown],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def revenue_breakdown2(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RevenueBreakdown2, RawError]:
        """<p>Get standardized revenue breakdown and KPIs data for 30,000+ global companies.</p>

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/revenue-breakdown2"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[RevenueBreakdown2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def upgrade_downgrade(
        self,
        *,
        symbol: str | None = None,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[UpgradeDowngrade], RawError]:
        """Get latest stock upgrade and downgrade.

        Args:
            symbol: Symbol of the company: AAPL. If left blank, the API will return latest stock upgrades/downgrades.
            from_: From date: 2000-03-15.
            to: To date: 2020-03-16.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/upgrade-downgrade"),
            query_params=[
                param[str | None]("symbol", symbol), param[Date | None]("from", from_), param[Date | None]("to", to)
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[UpgradeDowngrade]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncStockEstimatesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def company_capex_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CapexEstimates, RawError]:
        """Get company's capital expenditure estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/capex-estimate"),
            query_params=[param[str]("symbol", symbol), param[str | None]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[CapexEstimates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def company_dps_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DpsEstimates, RawError]:
        """Get company's Dividend per Share estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/dps-estimate"),
            query_params=[param[str]("symbol", symbol), param[str | None]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[DpsEstimates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def company_earnings(
        self, symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[EarningResult], RawError]:
        """Get company historical quarterly earnings surprise going back to 2000.

        Args:
            symbol: Symbol of the company: AAPL.
            limit: Limit number of period returned. Leave blank to get the full history.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/earnings"),
            query_params=[param[str]("symbol", symbol), param[int | None]("limit", limit)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[EarningResult]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def company_earnings_quality_score(
        self, symbol: str, freq: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CompanyEarningsQualityScore, RawError]:
        """<p>This endpoint provides Earnings Quality Score for global companies.</p><p> Earnings quality refers to the
        extent to which current earnings predict future earnings. "High-quality" earnings are expected to persist, while
        "low-quality" earnings do not. A higher score means a higher earnings quality</p><p>Finnhub uses a proprietary
        model which takes into consideration 4 criteria:</p> <ul style="list-style-type: unset; margin-left:
        30px;"><li>Profitability</li><li>Growth</li><li>Cash Generation & Capital
        Allocation</li><li>Leverage</li></ul><br/><p>We then compare the metrics of each company in each category
        against its peers in the same industry to gauge how quality its earnings is.</p>

        Args:
            symbol: Symbol.
            freq: Frequency. Currently support <code>annual</code> and <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/earnings-quality-score"),
            query_params=[param[str]("symbol", symbol), param[str]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[CompanyEarningsQualityScore],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def company_ebit_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EbitEstimates, RawError]:
        """Get company's ebit estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/ebit-estimate"),
            query_params=[param[str]("symbol", symbol), param[str | None]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EbitEstimates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def company_ebitda_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EbitdaEstimates, RawError]:
        """Get company's ebitda estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/ebitda-estimate"),
            query_params=[param[str]("symbol", symbol), param[str | None]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EbitdaEstimates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def company_eps_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EarningsEstimates, RawError]:
        """Get company's EPS estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/eps-estimate"),
            query_params=[param[str]("symbol", symbol), param[str | None]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EarningsEstimates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def company_fcf_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FcfEstimates, RawError]:
        """Get company's free cash flow estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/fcf-estimate"),
            query_params=[param[str]("symbol", symbol), param[str | None]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[FcfEstimates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def company_gross_income_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GrossIncomeEstimates, RawError]:
        """Get company's gross income estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/gross-income-estimate"),
            query_params=[param[str]("symbol", symbol), param[str | None]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[GrossIncomeEstimates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def company_net_income_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NetIncomeEstimates, RawError]:
        """Get company's net income estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/net-income-estimate"),
            query_params=[param[str]("symbol", symbol), param[str | None]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[NetIncomeEstimates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def company_ocf_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OcfEstimates, RawError]:
        """Get company's operating cash flow estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/ocf-estimate"),
            query_params=[param[str]("symbol", symbol), param[str | None]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[OcfEstimates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def company_pretax_income_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PretaxIncomeEstimates, RawError]:
        """Get company's pretax income estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/pretax-income-estimate"),
            query_params=[param[str]("symbol", symbol), param[str | None]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[PretaxIncomeEstimates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def company_revenue_estimates(
        self, symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RevenueEstimates, RawError]:
        """Get company's revenue estimates.

        Args:
            symbol: Symbol of the company: AAPL.
            freq: Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/revenue-estimate"),
            query_params=[param[str]("symbol", symbol), param[str | None]("freq", freq)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[RevenueEstimates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def price_target(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PriceTarget, RawError]:
        """Get latest price target consensus.

        Args:
            symbol: Symbol of the company: AAPL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/price-target"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[PriceTarget],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def recommendation_trends(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[RecommendationTrend], RawError]:
        """Get latest analyst recommendation trends for a company.

        Args:
            symbol: Symbol of the company: AAPL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/recommendation"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[RecommendationTrend]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def revenue_breakdown(
        self, *, symbol: str | None = None, cik: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RevenueBreakdown, RawError]:
        """<p>Get revenue breakdown as-reporetd by product and geography. Users on personal plans can access data for US
        companies which disclose their revenue breakdown in the annual or quarterly reports.</p><p>Global standardized
        revenue breakdown/segments data is available for Enterprise users. <a href="mailto:support@finnhub.io">Contact
        us</a> to inquire about the access for Global standardized data.</p>

        Args:
            symbol: Symbol.
            cik: CIK.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/revenue-breakdown"),
            query_params=[param[str | None]("symbol", symbol), param[str | None]("cik", cik)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[RevenueBreakdown],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def revenue_breakdown2(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RevenueBreakdown2, RawError]:
        """<p>Get standardized revenue breakdown and KPIs data for 30,000+ global companies.</p>

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/revenue-breakdown2"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[RevenueBreakdown2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def upgrade_downgrade(
        self,
        *,
        symbol: str | None = None,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[UpgradeDowngrade], RawError]:
        """Get latest stock upgrade and downgrade.

        Args:
            symbol: Symbol of the company: AAPL. If left blank, the API will return latest stock upgrades/downgrades.
            from_: From date: 2000-03-15.
            to: To date: 2020-03-16.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/upgrade-downgrade"),
            query_params=[
                param[str | None]("symbol", symbol), param[Date | None]("from", from_), param[Date | None]("to", to)
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[UpgradeDowngrade]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
