from __future__ import annotations

from functools import cached_property
from types import TracebackType
from typing import Any

from typing_extensions import Self

from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseFinnhubClient
from .core import (
    ApiKeyQueryScheme,
    ApiResult,
    Date,
    HttpClient,
    HttpxClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    json_body,
    json_decoder,
    no_auth,
    param,
    raw_error_response,
)
from .models.aggregate_indicators import AggregateIndicators
from .models.aichat_body import AichatBody, AichatBodyDict
from .models.aichat_response import AichatResponse
from .models.airline_price_index_data import AirlinePriceIndexData
from .models.bank_branch_res import BankBranchRes
from .models.basic_financials import BasicFinancials
from .models.bond_candles import BondCandles
from .models.bond_profile import BondProfile
from .models.bond_tick_data import BondTickData
from .models.bond_yield_curve import BondYieldCurve
from .models.capex_estimates import CapexEstimates
from .models.company_earnings_quality_score import CompanyEarningsQualityScore
from .models.company_esg import CompanyEsg
from .models.company_executive import CompanyExecutive
from .models.company_news import CompanyNews
from .models.company_profile import CompanyProfile
from .models.company_profile2 import CompanyProfile2
from .models.congressional_trading import CongressionalTrading
from .models.country_metadata import CountryMetadata
from .models.covid_info import CovidInfo
from .models.crypto_candles import CryptoCandles
from .models.crypto_profile import CryptoProfile
from .models.crypto_symbol import CryptoSymbol
from .models.dividends import Dividends
from .models.dividends2 import Dividends2
from .models.dps_estimates import DpsEstimates
from .models.earning_result import EarningResult
from .models.earnings_calendar import EarningsCalendar
from .models.earnings_call_live import EarningsCallLive
from .models.earnings_call_transcripts import EarningsCallTranscripts
from .models.earnings_call_transcripts_list import EarningsCallTranscriptsList
from .models.earnings_estimates import EarningsEstimates
from .models.ebit_estimates import EbitEstimates
from .models.ebitda_estimates import EbitdaEstimates
from .models.economic_calendar import EconomicCalendar
from .models.economic_code import EconomicCode
from .models.economic_data import EconomicData
from .models.etfs_allocation import EtfsAllocation
from .models.etfs_country_exposure import EtfsCountryExposure
from .models.etfs_holdings import EtfsHoldings
from .models.etfs_profile import EtfsProfile
from .models.etfs_sector_exposure import EtfsSectorExposure
from .models.fcf_estimates import FcfEstimates
from .models.fdacomittee_meeting import FdacomitteeMeeting
from .models.filing import Filing
from .models.financial_statements import FinancialStatements
from .models.financials_as_reported import FinancialsAsReported
from .models.forex_candles import ForexCandles
from .models.forex_symbol import ForexSymbol
from .models.forexrates import Forexrates
from .models.fund_ownership import FundOwnership
from .models.gross_income_estimates import GrossIncomeEstimates
from .models.historical_company_esg import HistoricalCompanyEsg
from .models.historical_employee_count import HistoricalEmployeeCount
from .models.historical_market_cap_data import HistoricalMarketCapData
from .models.historical_nbbo import HistoricalNbbo
from .models.in_filing_response import InFilingResponse
from .models.in_filing_search_body import InFilingSearchBody, InFilingSearchBodyDict
from .models.indices_constituents import IndicesConstituents
from .models.indices_historical_constituents import IndicesHistoricalConstituents
from .models.insider_sentiments import InsiderSentiments
from .models.insider_transactions import InsiderTransactions
from .models.institutional_ownership import InstitutionalOwnership
from .models.institutional_portfolio import InstitutionalPortfolio
from .models.institutional_profile import InstitutionalProfile
from .models.international_filing import InternationalFiling
from .models.investment_themes import InvestmentThemes
from .models.ipocalendar import Ipocalendar
from .models.isin_change import IsinChange
from .models.last_bid_ask import LastBidAsk
from .models.lobbying_result import LobbyingResult
from .models.market_holiday import MarketHoliday
from .models.market_news import MarketNews
from .models.market_status import MarketStatus
from .models.mutual_fund_country_exposure import MutualFundCountryExposure
from .models.mutual_fund_eet import MutualFundEet
from .models.mutual_fund_eet_pai import MutualFundEetPai
from .models.mutual_fund_holdings import MutualFundHoldings
from .models.mutual_fund_profile import MutualFundProfile
from .models.mutual_fund_sector_exposure import MutualFundSectorExposure
from .models.net_income_estimates import NetIncomeEstimates
from .models.news_sentiment import NewsSentiment
from .models.newsroom import Newsroom
from .models.ocf_estimates import OcfEstimates
from .models.ownership import Ownership
from .models.pattern_recognition import PatternRecognition
from .models.press_release import PressRelease
from .models.pretax_income_estimates import PretaxIncomeEstimates
from .models.price_metrics import PriceMetrics
from .models.price_target import PriceTarget
from .models.quote import Quote
from .models.recommendation_trend import RecommendationTrend
from .models.revenue_breakdown import RevenueBreakdown
from .models.revenue_breakdown2 import RevenueBreakdown2
from .models.revenue_estimates import RevenueEstimates
from .models.search_body import SearchBody, SearchBodyDict
from .models.search_filter import SearchFilter
from .models.search_response import SearchResponse
from .models.secsentiment_analysis import SecsentimentAnalysis
from .models.sector_metric import SectorMetric
from .models.similarity_index import SimilarityIndex
from .models.social_sentiment import SocialSentiment
from .models.split import Split
from .models.stock_candles import StockCandles
from .models.stock_presentation import StockPresentation
from .models.stock_symbol import StockSymbol
from .models.supply_chain_relationships import SupplyChainRelationships
from .models.support_resistance import SupportResistance
from .models.symbol_change import SymbolChange
from .models.symbol_lookup import SymbolLookup
from .models.tick_data import TickData
from .models.upgrade_downgrade import UpgradeDowngrade
from .models.usa_spending_result import UsaSpendingResult
from .models.uspto_patent_result import UsptoPatentResult
from .models.visa_application_result import VisaApplicationResult
from .server.server import Server


class FinnhubClient(BaseFinnhubClient[RawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_http_client: HttpClient | None = None,
        api_key: str | None = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout)
        )
        self._auth = AuthSchemes(api_key=ApiKeyQueryScheme("token", api_key) if api_key is not None else no_auth)

    @cached_property
    def with_raw_response(self) -> ApiWithRawResponse:
        return ApiWithRawResponse(self._raw_client, self._server, self._auth)

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
        return self.with_raw_response.aggregate_indicator(symbol, resolution, request_options=request_options).unwrap()

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
        return self.with_raw_response.ai_chat(search=search, request_options=request_options).unwrap()

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
        return self.with_raw_response.airline_price_index(airline, from_, to, request_options=request_options).unwrap()

    def bank_branch(self, symbol: Any, *, request_options: RequestOptionsOrDict | None = None) -> BankBranchRes:
        """Retrieve list of US bank branches information for a given symbol.

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.bank_branch(symbol, request_options=request_options).unwrap()

    def bond_price(
        self, isin: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> BondCandles:
        """<p>Get bond's price data. The following datasets are supported:</p><table class="table table-hover">
          <thead>
            <tr>
              <th>Exchange</th>
              <th>Segment</th>
              <th>Delay</th>
            </tr>
          </thead>
          <tbody>
          <tr>
              <td class="text-blue">US Government Bonds</td>
              <td>Government Bonds</td>
              <td>End-of-day</td>
            </tr>
            <tr>
              <td class="text-blue">FINRA Trace</td>
              <td>BTDS: US Corporate Bonds</td>
              <td>Delayed 4h</td>
            </tr>
            <tr>
              <td class="text-blue">FINRA Trace</td>
              <td>144A Bonds</td>
              <td>Delayed 4h</td>
            </tr>
            <tr>
             <td class="text-blue">International Bonds</td>
              <td>International Bonds</td>
              <td>End-of-day</td>
            </tr>
        </tbody> </table>

        Args:
            isin: ISIN.
            from_: UNIX timestamp. Interval initial value.
            to: UNIX timestamp. Interval end value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.bond_price(isin, from_, to, request_options=request_options).unwrap()

    def bond_profile(
        self,
        *,
        isin: str | None = None,
        cusip: str | None = None,
        figi: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BondProfile:
        """Get general information of a bond. You can query by FIGI, ISIN or CUSIP. A list of supported bonds can be
        found <a href="/api/v1/bond/list?type=csv&token=" target="_blank">here</a>.

        Args:
            isin: ISIN
            cusip: CUSIP
            figi: FIGI
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.bond_profile(
            isin=isin, cusip=cusip, figi=figi, request_options=request_options
        ).unwrap()

    def bond_tick(
        self,
        isin: str,
        date: Date,
        limit: int,
        skip: int,
        exchange: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BondTickData:
        """<p>Get trade-level data for bonds. The following datasets are supported:</p><table class="table table-hover">
          <thead>
            <tr>
              <th>Exchange</th>
              <th>Segment</th>
              <th>Delay</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-blue">FINRA Trace</th>
              <td>BTDS: US Corporate Bonds</td>
              <td>Delayed 4h</td>
            </tr>
            <tr>
              <td class="text-blue">FINRA Trace</th>
              <td>144A Bonds</td>
              <td>Delayed 4h</td>
            </tr>
          </tbody>
        </table>

        Args:
            isin: ISIN.
            date: Date: 2020-04-02.
            limit: Limit number of ticks returned. Maximum value: <code>25000</code>
            skip: Number of ticks to skip. Use this parameter to loop through the entire data.
            exchange: Currently support the following values: <code>trace</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.bond_tick(
            isin, date, limit, skip, exchange, request_options=request_options
        ).unwrap()

    def bond_yield_curve(self, code: str, *, request_options: RequestOptionsOrDict | None = None) -> BondYieldCurve:
        """Get yield curve data for Treasury bonds.

        Args:
            code: Bond's code. You can find the list of supported code <a
                href="https://docs.google.com/spreadsheets/d/1iA-lM0Kht7lsQZ7Uu_s6r2i1BbQNUNO9eGkO5-zglHg/edit?usp=sharing"
                target="_blank" rel="noopener">here</a>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.bond_yield_curve(code, request_options=request_options).unwrap()

    def company_basic_financials(
        self, symbol: str, metric: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BasicFinancials:
        """Get company basic financials such as margin, P/E ratio, 52-week high/low etc.

        Args:
            symbol: Symbol of the company: AAPL.
            metric: Metric type. Can be 1 of the following values <code>all</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.company_basic_financials(symbol, metric, request_options=request_options).unwrap()

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
        return self.with_raw_response.company_capex_estimates(
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
        return self.with_raw_response.company_dps_estimates(symbol, freq=freq, request_options=request_options).unwrap()

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
        return self.with_raw_response.company_earnings(symbol, limit=limit, request_options=request_options).unwrap()

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
        return self.with_raw_response.company_earnings_quality_score(
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
        return self.with_raw_response.company_ebit_estimates(
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
        return self.with_raw_response.company_ebitda_estimates(
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
        return self.with_raw_response.company_eps_estimates(symbol, freq=freq, request_options=request_options).unwrap()

    def company_esg_score(self, symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> CompanyEsg:
        """<p>This endpoint provides the latest ESG scores and important indicators for 7000+ global companies. The data
        is collected through company's public ESG disclosure and public sources.</p><p>Our ESG scoring models takes into
        account more than 150 different inputs to calculate the level of ESG risks and how well a company is managing
        them. A higher score means lower ESG risk or better ESG management. ESG scores are in the the range of 0-100.
        Some key indicators might contain letter-grade score from C- to A+ with C- is the lowest score and A+ is the
        highest score.</p>

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.company_esg_score(symbol, request_options=request_options).unwrap()

    def company_executive(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CompanyExecutive:
        """Get a list of company's executives and members of the Board.

        Args:
            symbol: Symbol of the company: AAPL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.company_executive(symbol, request_options=request_options).unwrap()

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
        return self.with_raw_response.company_fcf_estimates(symbol, freq=freq, request_options=request_options).unwrap()

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
        return self.with_raw_response.company_gross_income_estimates(
            symbol, freq=freq, request_options=request_options
        ).unwrap()

    def company_historical_esg_score(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> HistoricalCompanyEsg:
        """<p>This endpoint provides historical ESG scores and important indicators for 7000+ global companies. The data
        is collected through company's public ESG disclosure and public sources.</p><p>Our ESG scoring models takes into
        account more than 150 different inputs to calculate the level of ESG risks and how well a company is managing
        them. A higher score means lower ESG risk or better ESG management. ESG scores are in the the range of 0-100.
        Some key indicators might contain letter-grade score from C- to A+ with C- is the lowest score and A+ is the
        highest score.</p>

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.company_historical_esg_score(symbol, request_options=request_options).unwrap()

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
        return self.with_raw_response.company_net_income_estimates(
            symbol, freq=freq, request_options=request_options
        ).unwrap()

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
        return self.with_raw_response.company_news(symbol, from_, to, request_options=request_options).unwrap()

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
        return self.with_raw_response.company_ocf_estimates(symbol, freq=freq, request_options=request_options).unwrap()

    def company_peers(
        self, symbol: str, *, grouping: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> list[str]:
        """Get company peers. Return a list of peers operating in the same country and sector/industry.

        Args:
            symbol: Symbol of the company: AAPL.
            grouping: Specify the grouping criteria for choosing peers.Supporter values: <code>sector</code>,
                <code>industry</code>, <code>subIndustry</code>. Default to <code>subIndustry</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.company_peers(symbol, grouping=grouping, request_options=request_options).unwrap()

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
        return self.with_raw_response.company_pretax_income_estimates(
            symbol, freq=freq, request_options=request_options
        ).unwrap()

    def company_profile(
        self,
        *,
        symbol: str | None = None,
        isin: str | None = None,
        cusip: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CompanyProfile:
        """Get general information of a company. You can query by symbol, ISIN or CUSIP

        Args:
            symbol: Symbol of the company: AAPL e.g.
            isin: ISIN
            cusip: CUSIP
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.company_profile(
            symbol=symbol, isin=isin, cusip=cusip, request_options=request_options
        ).unwrap()

    def company_profile2(
        self,
        *,
        symbol: str | None = None,
        isin: str | None = None,
        cusip: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CompanyProfile2:
        """Get general information of a company. You can query by symbol, ISIN or CUSIP. This is the free version of <a
        href="#company-profile">Company Profile</a>.

        Args:
            symbol: Symbol of the company: AAPL e.g.
            isin: ISIN
            cusip: CUSIP
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.company_profile2(
            symbol=symbol, isin=isin, cusip=cusip, request_options=request_options
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
        return self.with_raw_response.company_revenue_estimates(
            symbol, freq=freq, request_options=request_options
        ).unwrap()

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
        return self.with_raw_response.congressional_trading(symbol, from_, to, request_options=request_options).unwrap()

    def country(self, *, request_options: RequestOptionsOrDict | None = None) -> list[CountryMetadata]:
        """List all countries and metadata.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.country(request_options=request_options).unwrap()

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
        return self.with_raw_response.covid_19(request_options=request_options).unwrap()

    def crypto_candles(
        self, symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> CryptoCandles:
        """Get candlestick data for crypto symbols.

        Args:
            symbol: Use symbol returned in <code>/crypto/symbol</code> endpoint for this field.
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            from_: UNIX timestamp. Interval initial value.
            to: UNIX timestamp. Interval end value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.crypto_candles(
            symbol, resolution, from_, to, request_options=request_options
        ).unwrap()

    def crypto_exchanges(self, *, request_options: RequestOptionsOrDict | None = None) -> list[str]:
        """List supported crypto exchanges

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.crypto_exchanges(request_options=request_options).unwrap()

    def crypto_profile(self, symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> CryptoProfile:
        """Get crypto's profile.

        Args:
            symbol: Crypto symbol such as BTC or ETH.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.crypto_profile(symbol, request_options=request_options).unwrap()

    def crypto_symbols(
        self, exchange: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[CryptoSymbol]:
        """List supported crypto symbols by exchange

        Args:
            exchange: Exchange you want to get the list of symbols from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.crypto_symbols(exchange, request_options=request_options).unwrap()

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
        return self.with_raw_response.earnings_calendar(
            from_=from_, to=to, symbol=symbol, international=international, request_options=request_options
        ).unwrap()

    def earnings_call_live(
        self,
        *,
        from_: Date | None = None,
        to: Date | None = None,
        symbol: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EarningsCallLive:
        """<p>Stream live earnings calls with data provided in the calendar. The data will be available in m3u8 format.
        mp3 files will be available once the calls finish in the <code>recording</code> field.</p>

        Args:
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            symbol: Filter by symbol: AAPL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.earnings_call_live(
            from_=from_, to=to, symbol=symbol, request_options=request_options
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
        return self.with_raw_response.economic_calendar(from_=from_, to=to, request_options=request_options).unwrap()

    def economic_code(self, *, request_options: RequestOptionsOrDict | None = None) -> list[EconomicCode]:
        """List codes of supported economic data.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.economic_code(request_options=request_options).unwrap()

    def economic_data(self, code: str, *, request_options: RequestOptionsOrDict | None = None) -> EconomicData:
        """Get economic data.

        Args:
            code: Economic code.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.economic_data(code, request_options=request_options).unwrap()

    def etfs_allocation(
        self, *, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> EtfsAllocation:
        """Get ETF equity allocation based on the characteristics of the holdings.

        Args:
            symbol: ETF symbol.
            isin: ETF isin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.etfs_allocation(
            symbol=symbol, isin=isin, request_options=request_options
        ).unwrap()

    def etfs_country_exposure(
        self, *, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> EtfsCountryExposure:
        """Get ETF country exposure data.

        Args:
            symbol: ETF symbol.
            isin: ETF isin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.etfs_country_exposure(
            symbol=symbol, isin=isin, request_options=request_options
        ).unwrap()

    def etfs_holdings(
        self,
        *,
        symbol: str | None = None,
        isin: str | None = None,
        skip: int | None = None,
        date: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EtfsHoldings:
        """Get full ETF holdings/constituents. This endpoint has global coverage. Widget only shows top 10 holdings. A
        list of supported ETFs can be found <a href="/api/v1/etf/list?token=" target="_blank">here</a>.

        Args:
            symbol: ETF symbol.
            isin: ETF isin.
            skip: Skip the first n results. You can use this parameter to query historical constituents data. The latest
                result is returned if skip=0 or not set.
            date: Query holdings by date. You can use either this param or <code>skip</code> param, not both.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.etfs_holdings(
            symbol=symbol, isin=isin, skip=skip, date=date, request_options=request_options
        ).unwrap()

    def etfs_profile(
        self, *, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> EtfsProfile:
        """Get ETF profile information. This endpoint has global coverage. A list of supported ETFs can be found <a
        href="/api/v1/etf/list?type=csv&token=" target="_blank">here</a>.

        Args:
            symbol: ETF symbol.
            isin: ETF isin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.etfs_profile(symbol=symbol, isin=isin, request_options=request_options).unwrap()

    def etfs_sector_exposure(
        self, *, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> EtfsSectorExposure:
        """Get ETF sector exposure data.

        Args:
            symbol: ETF symbol.
            isin: ETF isin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.etfs_sector_exposure(
            symbol=symbol, isin=isin, request_options=request_options
        ).unwrap()

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
        return self.with_raw_response.fda_committee_meeting_calendar(request_options=request_options).unwrap()

    def filings(
        self,
        *,
        symbol: str | None = None,
        cik: str | None = None,
        access_number: str | None = None,
        form: str | None = None,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Filing]:
        """List company's filing. Limit to 250 documents at a time. This data is available for bulk download on <a
        href="https://www.kaggle.com/finnhub/sec-filings" target="_blank">Kaggle SEC Filings database</a>.

        Args:
            symbol: Symbol. Leave <code>symbol</code>,<code>cik</code> and <code>accessNumber</code> empty to list
                latest filings.
            cik: CIK.
            access_number: Access number of a specific report you want to retrieve data from.
            form: Filter by form. You can use this value <code>NT 10-K</code> to find non-timely filings for a company.
            from_: From date: 2023-03-15.
            to: To date: 2023-03-16.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.filings(
            symbol=symbol,
            cik=cik,
            access_number=access_number,
            form=form,
            from_=from_,
            to=to,
            request_options=request_options,
        ).unwrap()

    def filings_sentiment(
        self, access_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SecsentimentAnalysis:
        """Get sentiment analysis of 10-K and 10-Q filings from SEC. An abnormal increase in the number of
        positive/negative words in filings can signal a significant change in the company's stock price in the upcoming
        4 quarters. We make use of <a href= "https://sraf.nd.edu/textual-analysis/resources/" target="_blank">Loughran
        and McDonald Sentiment Word Lists</a> to calculate the sentiment for each filing.

        Args:
            access_number: Access number of a specific report you want to retrieve data from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.filings_sentiment(access_number, request_options=request_options).unwrap()

    def financials(
        self,
        symbol: str,
        statement: str,
        freq: str,
        *,
        preliminary: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FinancialStatements:
        """<p>Get standardized balance sheet, income statement and cash flow for global companies going back 30+ years.
        Data is sourced from original filings most of which made available through <a href="#filings">SEC Filings</a>
        and <a href="#international-filings">International Filings</a> endpoints.</p><p>Set <code>preliminary</code>
        param to true for faster updates for US companies.</p><p><i>Wondering why our standardized data is different
        from Bloomberg, Reuters, Factset, S&P or Yahoo Finance ? Check out our <a href="/faq">FAQ page</a> to learn
        more</i></p>

        Args:
            symbol: Symbol of the company: AAPL.
            statement: Statement can take 1 of these values <code>bs, ic, cf</code> for Balance Sheet, Income Statement,
                Cash Flow respectively.
            freq: Frequency can take 1 of these values <code>annual, quarterly, ttm, ytd</code>. TTM (Trailing Twelve
                Months) option is available for Income Statement and Cash Flow. YTD (Year To Date) option is only
                available for Cash Flow.
            preliminary: If set to <code>true</code>, it will return Preliminary financial statements for the latest
                period which are usually available within an hour of the earnings announcement if finalized data is not
                available yet. This preliminary data is currently available for US companies. You will see
                <code>"preliminary": true</code> in the data if that period is using preliminary data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.financials(
            symbol, statement, freq, preliminary=preliminary, request_options=request_options
        ).unwrap()

    def financials_reported(
        self,
        *,
        symbol: str | None = None,
        cik: str | None = None,
        access_number: str | None = None,
        freq: str | None = None,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FinancialsAsReported:
        """Get financials as reported. This data is available for bulk download on <a
        href="https://www.kaggle.com/finnhub/reported-financials" target="_blank">Kaggle SEC Financials database</a>.

        Args:
            symbol: Symbol.
            cik: CIK.
            access_number: Access number of a specific report you want to retrieve financials from.
            freq: Frequency. Can be either <code>annual</code> or <code>quarterly</code>. Default to
                <code>annual</code>.
            from_: From date <code>YYYY-MM-DD</code>. Filter for endDate.
            to: To date <code>YYYY-MM-DD</code>. Filter for endDate.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.financials_reported(
            symbol=symbol,
            cik=cik,
            access_number=access_number,
            freq=freq,
            from_=from_,
            to=to,
            request_options=request_options,
        ).unwrap()

    def forex_candles(
        self, symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ForexCandles:
        """Get candlestick data for forex symbols.

        Args:
            symbol: Use symbol returned in <code>/forex/symbol</code> endpoint for this field.
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            from_: UNIX timestamp. Interval initial value.
            to: UNIX timestamp. Interval end value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.forex_candles(
            symbol, resolution, from_, to, request_options=request_options
        ).unwrap()

    def forex_exchanges(self, *, request_options: RequestOptionsOrDict | None = None) -> list[str]:
        """List supported forex exchanges

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.forex_exchanges(request_options=request_options).unwrap()

    def forex_rates(
        self, *, base: str | None = None, date: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Forexrates:
        """Get rates for all forex pairs. Ideal for currency conversion

        Args:
            base: Base currency. Default to EUR.
            date: Date. Leave blank to get the latest data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.forex_rates(base=base, date=date, request_options=request_options).unwrap()

    def forex_symbols(self, exchange: str, *, request_options: RequestOptionsOrDict | None = None) -> list[ForexSymbol]:
        """List supported forex symbols.

        Args:
            exchange: Exchange you want to get the list of symbols from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.forex_symbols(exchange, request_options=request_options).unwrap()

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
        return self.with_raw_response.fund_ownership(symbol, limit=limit, request_options=request_options).unwrap()

    def global_filings_download(self, document_id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """<p>Download filings using document ids.</p>

        Args:
            document_id: Document's id. Note that this is different from filingId as 1 filing can contain multiple
                documents.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.global_filings_download(document_id, request_options=request_options).unwrap()

    def global_filings_search(
        self, *, search: SearchBody | SearchBodyDict | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> SearchResponse:
        """<p>Search for best-matched filings across global companies' filings, transcripts and press releases. You can
        filter by anything from symbol, ISIN to form type, and document sources.</p><p>This endpoint will return a list
        of documents that match your search criteria. If you would like to get the excerpts as well, please set
        <code>highlighted</code> to <code>true</code>. Once you have the list of documents, you can get a list of
        excerpts and positions to highlight the document using the <code>/search-in-filing</code> endpoint</p>

        Args:
            search: Search body
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.global_filings_search(search=search, request_options=request_options).unwrap()

    def global_filings_search_filter(
        self, field: str, *, source: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> SearchFilter:
        """<p>Get available values for each filter in search body.</p>

        Args:
            field: Field to get available filters. Available filters are "countries", "exchanges", "exhibits", "forms",
                "gics", "naics", "caps", "acts", and "sort".
            source: Get available forms for each source.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.global_filings_search_filter(
            field, source=source, request_options=request_options
        ).unwrap()

    def historical_employee_count(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> HistoricalEmployeeCount:
        """Get historical employee count for global companies.

        Args:
            symbol: Company symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.historical_employee_count(
            symbol, from_, to, request_options=request_options
        ).unwrap()

    def historical_market_cap(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> HistoricalMarketCapData:
        """Get historical market cap data for global companies.

        Args:
            symbol: Company symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.historical_market_cap(symbol, from_, to, request_options=request_options).unwrap()

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
        return self.with_raw_response.indices_constituents(symbol, request_options=request_options).unwrap()

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
        return self.with_raw_response.indices_historical_constituents(symbol, request_options=request_options).unwrap()

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
        return self.with_raw_response.insider_sentiment(symbol, from_, to, request_options=request_options).unwrap()

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
        return self.with_raw_response.insider_transactions(
            symbol, from_=from_, to=to, request_options=request_options
        ).unwrap()

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
        return self.with_raw_response.institutional_ownership(
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
        return self.with_raw_response.institutional_portfolio(cik, from_, to, request_options=request_options).unwrap()

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
        return self.with_raw_response.institutional_profile(cik=cik, request_options=request_options).unwrap()

    def international_filings(
        self,
        *,
        symbol: str | None = None,
        country: str | None = None,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[InternationalFiling]:
        """List filings for international companies. Limit to 500 documents at a time. These are the documents we use to
        source our fundamental data. Enterprise clients who need access to the full filings for global markets should
        contact us for the access.

        Args:
            symbol: Symbol. Leave empty to list latest filings.
            country: Filter by country using country's 2-letter code.
            from_: From date: 2023-01-15.
            to: To date: 2023-12-16.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.international_filings(
            symbol=symbol, country=country, from_=from_, to=to, request_options=request_options
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
        return self.with_raw_response.investment_themes(theme, request_options=request_options).unwrap()

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
        return self.with_raw_response.ipo_calendar(from_, to, request_options=request_options).unwrap()

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
        return self.with_raw_response.isin_change(from_, to, request_options=request_options).unwrap()

    def market_holiday(self, exchange: str, *, request_options: RequestOptionsOrDict | None = None) -> MarketHoliday:
        """Get a list of holidays for global exchanges.

        Args:
            exchange: Exchange code.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.market_holiday(exchange, request_options=request_options).unwrap()

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
        return self.with_raw_response.market_news(category, min_id=min_id, request_options=request_options).unwrap()

    def market_status(self, exchange: str, *, request_options: RequestOptionsOrDict | None = None) -> MarketStatus:
        """Get current market status for global exchanges (whether exchanges are open or close).

        Args:
            exchange: Exchange code.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.market_status(exchange, request_options=request_options).unwrap()

    def mutual_fund_country_exposure(
        self, *, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> MutualFundCountryExposure:
        """Get Mutual Funds country exposure data.

        Args:
            symbol: Symbol.
            isin: Fund's isin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.mutual_fund_country_exposure(
            symbol=symbol, isin=isin, request_options=request_options
        ).unwrap()

    def mutual_fund_eet(self, isin: str, *, request_options: RequestOptionsOrDict | None = None) -> MutualFundEet:
        """Get EET data for EU funds. For PAIs data, please see the EET PAI endpoint.

        Args:
            isin: ISIN.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.mutual_fund_eet(isin, request_options=request_options).unwrap()

    def mutual_fund_eet_pai(
        self, isin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> MutualFundEetPai:
        """Get EET PAI data for EU funds.

        Args:
            isin: ISIN.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.mutual_fund_eet_pai(isin, request_options=request_options).unwrap()

    def mutual_fund_holdings(
        self,
        *,
        symbol: str | None = None,
        isin: str | None = None,
        skip: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MutualFundHoldings:
        """Get full Mutual Funds holdings/constituents. This endpoint covers both US and global mutual funds. For
        international funds, you must query the data using ISIN. A list of supported funds can be found <a
        href="/api/v1/mutual-fund/list?token=" target="_blank">here</a>.

        Args:
            symbol: Fund's symbol.
            isin: Fund's isin.
            skip: Skip the first n results. You can use this parameter to query historical constituents data. The latest
                result is returned if skip=0 or not set.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.mutual_fund_holdings(
            symbol=symbol, isin=isin, skip=skip, request_options=request_options
        ).unwrap()

    def mutual_fund_profile(
        self, *, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> MutualFundProfile:
        """Get mutual funds profile information. This endpoint covers both US and global mutual funds. For international
        funds, you must query the data using ISIN. A list of supported funds can be found <a
        href="/api/v1/mutual-fund/list?type=csv&token=" target="_blank">here</a>.

        Args:
            symbol: Fund's symbol.
            isin: Fund's isin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.mutual_fund_profile(
            symbol=symbol, isin=isin, request_options=request_options
        ).unwrap()

    def mutual_fund_sector_exposure(
        self, *, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> MutualFundSectorExposure:
        """Get Mutual Funds sector exposure data.

        Args:
            symbol: Mutual Fund symbol.
            isin: Fund's isin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.mutual_fund_sector_exposure(
            symbol=symbol, isin=isin, request_options=request_options
        ).unwrap()

    def news_sentiment(self, symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> NewsSentiment:
        """Get company's news sentiment and statistics. This endpoint is only available for US companies.

        Args:
            symbol: Company symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.news_sentiment(symbol, request_options=request_options).unwrap()

    def newsroom(
        self,
        symbol: str,
        *,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Newsroom:
        """<p>Get latest articles posted directly on the companies' newsroom and investor relations page. Newsroom API
        along with the Press Releases API provide a comprehensive text-based dataset directly from the company. We
        currently cover 1,250 US Companies with this dataset.</p>

        Args:
            symbol: Company symbol.
            from_: From time: 2025-01-01.
            to: To time: 2026-01-05.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.newsroom(symbol, from_=from_, to=to, request_options=request_options).unwrap()

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
        return self.with_raw_response.ownership(symbol, limit=limit, request_options=request_options).unwrap()

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
        return self.with_raw_response.pattern_recognition(symbol, resolution, request_options=request_options).unwrap()

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
        return self.with_raw_response.press_releases(
            symbol, from_=from_, to=to, request_options=request_options
        ).unwrap()

    def price_metrics(
        self, symbol: str, *, date: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> PriceMetrics:
        """Get company price performance statistics such as 52-week high/low, YTD return and much more.

        Args:
            symbol: Symbol of the company: AAPL.
            date: Get data on a specific date in the past. The data is available weekly so your date will be
                automatically adjusted to the last day of that week.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.price_metrics(symbol, date=date, request_options=request_options).unwrap()

    def price_target(self, symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> PriceTarget:
        """Get latest price target consensus.

        Args:
            symbol: Symbol of the company: AAPL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.price_target(symbol, request_options=request_options).unwrap()

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
        return self.with_raw_response.quote(symbol, request_options=request_options).unwrap()

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
        return self.with_raw_response.recommendation_trends(symbol, request_options=request_options).unwrap()

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
        return self.with_raw_response.revenue_breakdown(
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
        return self.with_raw_response.revenue_breakdown2(symbol, request_options=request_options).unwrap()

    def search_in_filing(
        self,
        *,
        search: InFilingSearchBody | InFilingSearchBodyDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InFilingResponse:
        """<p>Get a list of excerpts and highlight positions within a document using your query.</p>

        Args:
            search: Search body
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.search_in_filing(search=search, request_options=request_options).unwrap()

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
        return self.with_raw_response.sector_metric(region, request_options=request_options).unwrap()

    def similarity_index(
        self,
        *,
        symbol: str | None = None,
        cik: str | None = None,
        freq: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SimilarityIndex:
        """<p>Calculate the textual difference between a company's 10-K / 10-Q reports and the same type of report in
        the previous year using Cosine Similarity. For example, this endpoint compares 2019's 10-K with 2018's 10-K.
        Companies breaking from its routines in disclosure of financial condition and risk analysis section can signal a
        significant change in the company's stock price in the upcoming 4 quarters.</p>

        Args:
            symbol: Symbol. Required if cik is empty
            cik: CIK. Required if symbol is empty
            freq: <code>annual</code> or <code>quarterly</code>. Default to <code>annual</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.similarity_index(
            symbol=symbol, cik=cik, freq=freq, request_options=request_options
        ).unwrap()

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
        return self.with_raw_response.social_sentiment(
            symbol, from_=from_, to=to, request_options=request_options
        ).unwrap()

    def stock_basic_dividends(self, symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> Dividends2:
        """Get global dividends data.

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.stock_basic_dividends(symbol, request_options=request_options).unwrap()

    def stock_bidask(self, symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> LastBidAsk:
        """Get last bid/ask data for US stocks.

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.stock_bidask(symbol, request_options=request_options).unwrap()

    def stock_candles(
        self, symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> StockCandles:
        """<p>Get candlestick data (OHLCV) for stocks.</p><p>Daily data will be adjusted for Splits. Intraday data will
        remain unadjusted. Only 1 month of intraday will be returned at a time. If you need more historical intraday
        data, please use the from and to params iteratively to request more data.</p>

        Args:
            symbol: Symbol.
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            from_: UNIX timestamp. Interval initial value.
            to: UNIX timestamp. Interval end value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.stock_candles(
            symbol, resolution, from_, to, request_options=request_options
        ).unwrap()

    def stock_dividends(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Dividends]:
        """Get dividends data for common stocks going back 30 years.

        Args:
            symbol: Symbol.
            from_: YYYY-MM-DD.
            to: YYYY-MM-DD.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.stock_dividends(symbol, from_, to, request_options=request_options).unwrap()

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
        return self.with_raw_response.stock_lobbying(symbol, from_, to, request_options=request_options).unwrap()

    def stock_nbbo(
        self, symbol: str, date: Date, limit: int, skip: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> HistoricalNbbo:
        """<p>Get historical best bid and offer for US stocks, LSE, TSX, Euronext and Deutsche Borse.</p><p>For US
        market, this endpoint only serves historical NBBO from the beginning of 2023. To download more historical data,
        please visit our bulk download page in the Dashboard <a target="_blank"
        href="/dashboard/download",>here</a>.</p>

        Args:
            symbol: Symbol.
            date: Date: 2020-04-02.
            limit: Limit number of ticks returned. Maximum value: <code>25000</code>
            skip: Number of ticks to skip. Use this parameter to loop through the entire data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.stock_nbbo(symbol, date, limit, skip, request_options=request_options).unwrap()

    def stock_presentation(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> StockPresentation:
        """<p>Get presentations/slides data in PDF format that are usually used during earnings calls. You can get a
        list of supported symbols <a target="_blank" href="/api/v1/stock/presentation/symbol?token=">here</a></p>

        Args:
            symbol: Company symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.stock_presentation(symbol, request_options=request_options).unwrap()

    def stock_splits(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Split]:
        """Get splits data for stocks.

        Args:
            symbol: Symbol.
            from_: YYYY-MM-DD.
            to: YYYY-MM-DD.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.stock_splits(symbol, from_, to, request_options=request_options).unwrap()

    def stock_symbols(
        self,
        exchange: str,
        *,
        mic: str | None = None,
        security_type: str | None = None,
        currency: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[StockSymbol]:
        """List supported stocks. We use the following symbology to identify stocks on Finnhub
        <code>Exchange_Ticker.Exchange_Code</code>. A list of supported exchange codes can be found <a
        href="https://docs.google.com/spreadsheets/d/1I3pBxjfXB056-g_JYf_6o3Rns3BV2kMGG1nCatb91ls/edit?usp=sharing"
        target="_blank">here</a>.

        Args:
            exchange: Exchange you want to get the list of symbols from. List of exchange codes can be found <a
                href="https://docs.google.com/spreadsheets/d/1I3pBxjfXB056-g_JYf_6o3Rns3BV2kMGG1nCatb91ls/edit?usp=sharing"
                target="_blank">here</a>.
            mic: Filter by MIC code.
            security_type: Filter by security type used by OpenFigi standard.
            currency: Filter by currency.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.stock_symbols(
            exchange, mic=mic, security_type=security_type, currency=currency, request_options=request_options
        ).unwrap()

    def stock_tick(
        self, symbol: str, date: Date, limit: int, skip: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> TickData:
        """<p>Get historical tick data for global exchanges.</p><p>For more historical tick data, you can visit our bulk
        download page in the Dashboard <a target="_blank" href="/dashboard/download",>here</a> to speed up the download
        process.</p><table class="table table-hover">
          <thead>
            <tr>
              <th>Exchange</th>
              <th>Segment</th>
              <th>Delay</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-blue">US CTA/UTP</th>
              <td>Full SIP</td>
              <td>End-of-day</td>
            </tr>
            <tr>
              <td class="text-blue">TSX</th>
              <td><ul><li>TSX</li><li>TSX Venture</li><li>Index</li></ul></td>
              <td>End-of-day</td>
            </tr>
            <tr>
              <td class="text-blue">LSE</th>
              <td><ul><li>London Stock Exchange (L)</li><li>LSE International (L)</li><li>LSE European
                (L)</li></ul></td>
              <td>15 minute</td>
            </tr>
            <tr>
              <td class="text-blue">Euronext</th>
              <td><ul> <li>Euronext Paris (PA)</li> <li>Euronext Amsterdam (AS)</li> <li>Euronext Lisbon (LS)</li>
                <li>Euronext Brussels (BR)</li> <li>Euronext Oslo (OL)</li> <li>Euronext London (LN)</li> <li>Euronext
                Dublin (IR)</li> <li>Index</li> <li>Warrant</li></ul></td>
              <td>End-of-day</td>
            </tr>
            <tr>
              <td class="text-blue">Deutsche Börse</th>
              <td><ul> <li>Frankfurt (F)</li> <li>Xetra (DE)</li> <li>Duesseldorf (DU)</li> <li>Hamburg (HM)</li>
                <li>Berlin (BE)</li> <li>Hanover (HA)</li> <li>Stoxx (SX)</li> <li>TradeGate (TG)</li> <li>Zertifikate
                (SC)</li> <li>Index</li> <li>Warrant</li></ul></td>
              <td>End-of-day</td>
            </tr>
          </tbody>
        </table>

        Args:
            symbol: Symbol.
            date: Date: 2020-04-02.
            limit: Limit number of ticks returned. Maximum value: <code>25000</code>
            skip: Number of ticks to skip. Use this parameter to loop through the entire data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.stock_tick(symbol, date, limit, skip, request_options=request_options).unwrap()

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
        return self.with_raw_response.stock_usa_spending(symbol, from_, to, request_options=request_options).unwrap()

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
        return self.with_raw_response.stock_uspto_patent(symbol, from_, to, request_options=request_options).unwrap()

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
        return self.with_raw_response.stock_visa_application(
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
        return self.with_raw_response.supply_chain_relationships(symbol, request_options=request_options).unwrap()

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
        return self.with_raw_response.support_resistance(symbol, resolution, request_options=request_options).unwrap()

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
        return self.with_raw_response.symbol_change(from_, to, request_options=request_options).unwrap()

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
        return self.with_raw_response.symbol_search(q, exchange=exchange, request_options=request_options).unwrap()

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
        return self.with_raw_response.technical_indicator(
            symbol, resolution, from_, to, indicator, request_options=request_options
        ).unwrap()

    def transcripts(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> EarningsCallTranscripts:
        """<p>Get earnings call transcripts, audio and participants' list. Data is available for US, UK, European,
        Australian and Canadian companies.<p>15+ years of data is available with 220,000+ audio which add up to 7TB in
        size.</p>

        Args:
            id: Transcript's id obtained with <a href="#transcripts-list">Transcripts List endpoint</a>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.transcripts(id, request_options=request_options).unwrap()

    def transcripts_list(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> EarningsCallTranscriptsList:
        """List earnings call transcripts' metadata. This endpoint is available for Global companies. You can get a list
        of supported symbols <a target="_blank" href="/api/v1/stock/transcripts/symbol?token=">here</a>

        Args:
            symbol: Company symbol: AAPL. Leave empty to list the latest transcripts
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self.with_raw_response.transcripts_list(symbol, request_options=request_options).unwrap()

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
        return self.with_raw_response.upgrade_downgrade(
            symbol=symbol, from_=from_, to=to, request_options=request_options
        ).unwrap()

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


class ApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
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

    def bond_price(
        self, isin: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BondCandles, RawError]:
        """<p>Get bond's price data. The following datasets are supported:</p><table class="table table-hover">
          <thead>
            <tr>
              <th>Exchange</th>
              <th>Segment</th>
              <th>Delay</th>
            </tr>
          </thead>
          <tbody>
          <tr>
              <td class="text-blue">US Government Bonds</td>
              <td>Government Bonds</td>
              <td>End-of-day</td>
            </tr>
            <tr>
              <td class="text-blue">FINRA Trace</td>
              <td>BTDS: US Corporate Bonds</td>
              <td>Delayed 4h</td>
            </tr>
            <tr>
              <td class="text-blue">FINRA Trace</td>
              <td>144A Bonds</td>
              <td>Delayed 4h</td>
            </tr>
            <tr>
             <td class="text-blue">International Bonds</td>
              <td>International Bonds</td>
              <td>End-of-day</td>
            </tr>
        </tbody> </table>

        Args:
            isin: ISIN.
            from_: UNIX timestamp. Interval initial value.
            to: UNIX timestamp. Interval end value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/bond/price"),
            query_params=[param[str]("isin", isin), param[int]("from", from_), param[int]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[BondCandles],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bond_profile(
        self,
        *,
        isin: str | None = None,
        cusip: str | None = None,
        figi: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BondProfile, RawError]:
        """Get general information of a bond. You can query by FIGI, ISIN or CUSIP. A list of supported bonds can be
        found <a href="/api/v1/bond/list?type=csv&token=" target="_blank">here</a>.

        Args:
            isin: ISIN
            cusip: CUSIP
            figi: FIGI
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/bond/profile"),
            query_params=[
                param[str | None]("isin", isin), param[str | None]("cusip", cusip), param[str | None]("figi", figi)
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[BondProfile],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bond_tick(
        self,
        isin: str,
        date: Date,
        limit: int,
        skip: int,
        exchange: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BondTickData, RawError]:
        """<p>Get trade-level data for bonds. The following datasets are supported:</p><table class="table table-hover">
          <thead>
            <tr>
              <th>Exchange</th>
              <th>Segment</th>
              <th>Delay</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-blue">FINRA Trace</th>
              <td>BTDS: US Corporate Bonds</td>
              <td>Delayed 4h</td>
            </tr>
            <tr>
              <td class="text-blue">FINRA Trace</th>
              <td>144A Bonds</td>
              <td>Delayed 4h</td>
            </tr>
          </tbody>
        </table>

        Args:
            isin: ISIN.
            date: Date: 2020-04-02.
            limit: Limit number of ticks returned. Maximum value: <code>25000</code>
            skip: Number of ticks to skip. Use this parameter to loop through the entire data.
            exchange: Currently support the following values: <code>trace</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/bond/tick"),
            query_params=[
                param[str]("isin", isin),
                param[Date]("date", date),
                param[int]("limit", limit),
                param[int]("skip", skip),
                param[str]("exchange", exchange),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[BondTickData],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bond_yield_curve(
        self, code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BondYieldCurve, RawError]:
        """Get yield curve data for Treasury bonds.

        Args:
            code: Bond's code. You can find the list of supported code <a
                href="https://docs.google.com/spreadsheets/d/1iA-lM0Kht7lsQZ7Uu_s6r2i1BbQNUNO9eGkO5-zglHg/edit?usp=sharing"
                target="_blank" rel="noopener">here</a>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/bond/yield-curve"),
            query_params=[param[str]("code", code)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[BondYieldCurve],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def company_basic_financials(
        self, symbol: str, metric: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BasicFinancials, RawError]:
        """Get company basic financials such as margin, P/E ratio, 52-week high/low etc.

        Args:
            symbol: Symbol of the company: AAPL.
            metric: Metric type. Can be 1 of the following values <code>all</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/metric"),
            query_params=[param[str]("symbol", symbol), param[str]("metric", metric)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[BasicFinancials],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

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

    def company_esg_score(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CompanyEsg, RawError]:
        """<p>This endpoint provides the latest ESG scores and important indicators for 7000+ global companies. The data
        is collected through company's public ESG disclosure and public sources.</p><p>Our ESG scoring models takes into
        account more than 150 different inputs to calculate the level of ESG risks and how well a company is managing
        them. A higher score means lower ESG risk or better ESG management. ESG scores are in the the range of 0-100.
        Some key indicators might contain letter-grade score from C- to A+ with C- is the lowest score and A+ is the
        highest score.</p>

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/esg"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[CompanyEsg],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def company_executive(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CompanyExecutive, RawError]:
        """Get a list of company's executives and members of the Board.

        Args:
            symbol: Symbol of the company: AAPL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/executive"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[CompanyExecutive],
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

    def company_historical_esg_score(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[HistoricalCompanyEsg, RawError]:
        """<p>This endpoint provides historical ESG scores and important indicators for 7000+ global companies. The data
        is collected through company's public ESG disclosure and public sources.</p><p>Our ESG scoring models takes into
        account more than 150 different inputs to calculate the level of ESG risks and how well a company is managing
        them. A higher score means lower ESG risk or better ESG management. ESG scores are in the the range of 0-100.
        Some key indicators might contain letter-grade score from C- to A+ with C- is the lowest score and A+ is the
        highest score.</p>

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/historical-esg"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[HistoricalCompanyEsg],
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

    def company_peers(
        self, symbol: str, *, grouping: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[str], RawError]:
        """Get company peers. Return a list of peers operating in the same country and sector/industry.

        Args:
            symbol: Symbol of the company: AAPL.
            grouping: Specify the grouping criteria for choosing peers.Supporter values: <code>sector</code>,
                <code>industry</code>, <code>subIndustry</code>. Default to <code>subIndustry</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/peers"),
            query_params=[param[str]("symbol", symbol), param[str | None]("grouping", grouping)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[str]],
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

    def company_profile(
        self,
        *,
        symbol: str | None = None,
        isin: str | None = None,
        cusip: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CompanyProfile, RawError]:
        """Get general information of a company. You can query by symbol, ISIN or CUSIP

        Args:
            symbol: Symbol of the company: AAPL e.g.
            isin: ISIN
            cusip: CUSIP
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/profile"),
            query_params=[
                param[str | None]("symbol", symbol), param[str | None]("isin", isin), param[str | None]("cusip", cusip)
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[CompanyProfile],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def company_profile2(
        self,
        *,
        symbol: str | None = None,
        isin: str | None = None,
        cusip: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CompanyProfile2, RawError]:
        """Get general information of a company. You can query by symbol, ISIN or CUSIP. This is the free version of <a
        href="#company-profile">Company Profile</a>.

        Args:
            symbol: Symbol of the company: AAPL e.g.
            isin: ISIN
            cusip: CUSIP
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/profile2"),
            query_params=[
                param[str | None]("symbol", symbol), param[str | None]("isin", isin), param[str | None]("cusip", cusip)
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[CompanyProfile2],
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

    def crypto_candles(
        self, symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CryptoCandles, RawError]:
        """Get candlestick data for crypto symbols.

        Args:
            symbol: Use symbol returned in <code>/crypto/symbol</code> endpoint for this field.
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            from_: UNIX timestamp. Interval initial value.
            to: UNIX timestamp. Interval end value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/crypto/candle"),
            query_params=[
                param[str]("symbol", symbol),
                param[str]("resolution", resolution),
                param[int]("from", from_),
                param[int]("to", to),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[CryptoCandles],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def crypto_exchanges(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[str], RawError]:
        """List supported crypto exchanges

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/crypto/exchange"),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[str]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def crypto_profile(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CryptoProfile, RawError]:
        """Get crypto's profile.

        Args:
            symbol: Crypto symbol such as BTC or ETH.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/crypto/profile"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[CryptoProfile],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def crypto_symbols(
        self, exchange: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[CryptoSymbol], RawError]:
        """List supported crypto symbols by exchange

        Args:
            exchange: Exchange you want to get the list of symbols from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/crypto/symbol"),
            query_params=[param[str]("exchange", exchange)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[CryptoSymbol]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

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

    def earnings_call_live(
        self,
        *,
        from_: Date | None = None,
        to: Date | None = None,
        symbol: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EarningsCallLive, RawError]:
        """<p>Stream live earnings calls with data provided in the calendar. The data will be available in m3u8 format.
        mp3 files will be available once the calls finish in the <code>recording</code> field.</p>

        Args:
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            symbol: Filter by symbol: AAPL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/earnings-call-live"),
            query_params=[
                param[Date | None]("from", from_), param[Date | None]("to", to), param[str | None]("symbol", symbol)
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EarningsCallLive],
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

    def etfs_allocation(
        self, *, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EtfsAllocation, RawError]:
        """Get ETF equity allocation based on the characteristics of the holdings.

        Args:
            symbol: ETF symbol.
            isin: ETF isin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/etf/allocation"),
            query_params=[param[str | None]("symbol", symbol), param[str | None]("isin", isin)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EtfsAllocation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def etfs_country_exposure(
        self, *, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EtfsCountryExposure, RawError]:
        """Get ETF country exposure data.

        Args:
            symbol: ETF symbol.
            isin: ETF isin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/etf/country"),
            query_params=[param[str | None]("symbol", symbol), param[str | None]("isin", isin)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EtfsCountryExposure],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def etfs_holdings(
        self,
        *,
        symbol: str | None = None,
        isin: str | None = None,
        skip: int | None = None,
        date: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EtfsHoldings, RawError]:
        """Get full ETF holdings/constituents. This endpoint has global coverage. Widget only shows top 10 holdings. A
        list of supported ETFs can be found <a href="/api/v1/etf/list?token=" target="_blank">here</a>.

        Args:
            symbol: ETF symbol.
            isin: ETF isin.
            skip: Skip the first n results. You can use this parameter to query historical constituents data. The latest
                result is returned if skip=0 or not set.
            date: Query holdings by date. You can use either this param or <code>skip</code> param, not both.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/etf/holdings"),
            query_params=[
                param[str | None]("symbol", symbol),
                param[str | None]("isin", isin),
                param[int | None]("skip", skip),
                param[str | None]("date", date),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EtfsHoldings],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def etfs_profile(
        self, *, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EtfsProfile, RawError]:
        """Get ETF profile information. This endpoint has global coverage. A list of supported ETFs can be found <a
        href="/api/v1/etf/list?type=csv&token=" target="_blank">here</a>.

        Args:
            symbol: ETF symbol.
            isin: ETF isin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/etf/profile"),
            query_params=[param[str | None]("symbol", symbol), param[str | None]("isin", isin)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EtfsProfile],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def etfs_sector_exposure(
        self, *, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EtfsSectorExposure, RawError]:
        """Get ETF sector exposure data.

        Args:
            symbol: ETF symbol.
            isin: ETF isin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/etf/sector"),
            query_params=[param[str | None]("symbol", symbol), param[str | None]("isin", isin)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EtfsSectorExposure],
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

    def filings(
        self,
        *,
        symbol: str | None = None,
        cik: str | None = None,
        access_number: str | None = None,
        form: str | None = None,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Filing], RawError]:
        """List company's filing. Limit to 250 documents at a time. This data is available for bulk download on <a
        href="https://www.kaggle.com/finnhub/sec-filings" target="_blank">Kaggle SEC Filings database</a>.

        Args:
            symbol: Symbol. Leave <code>symbol</code>,<code>cik</code> and <code>accessNumber</code> empty to list
                latest filings.
            cik: CIK.
            access_number: Access number of a specific report you want to retrieve data from.
            form: Filter by form. You can use this value <code>NT 10-K</code> to find non-timely filings for a company.
            from_: From date: 2023-03-15.
            to: To date: 2023-03-16.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/filings"),
            query_params=[
                param[str | None]("symbol", symbol),
                param[str | None]("cik", cik),
                param[str | None]("accessNumber", access_number),
                param[str | None]("form", form),
                param[Date | None]("from", from_),
                param[Date | None]("to", to),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[Filing]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def filings_sentiment(
        self, access_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SecsentimentAnalysis, RawError]:
        """Get sentiment analysis of 10-K and 10-Q filings from SEC. An abnormal increase in the number of
        positive/negative words in filings can signal a significant change in the company's stock price in the upcoming
        4 quarters. We make use of <a href= "https://sraf.nd.edu/textual-analysis/resources/" target="_blank">Loughran
        and McDonald Sentiment Word Lists</a> to calculate the sentiment for each filing.

        Args:
            access_number: Access number of a specific report you want to retrieve data from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/filings-sentiment"),
            query_params=[param[str]("accessNumber", access_number)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[SecsentimentAnalysis],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def financials(
        self,
        symbol: str,
        statement: str,
        freq: str,
        *,
        preliminary: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FinancialStatements, RawError]:
        """<p>Get standardized balance sheet, income statement and cash flow for global companies going back 30+ years.
        Data is sourced from original filings most of which made available through <a href="#filings">SEC Filings</a>
        and <a href="#international-filings">International Filings</a> endpoints.</p><p>Set <code>preliminary</code>
        param to true for faster updates for US companies.</p><p><i>Wondering why our standardized data is different
        from Bloomberg, Reuters, Factset, S&P or Yahoo Finance ? Check out our <a href="/faq">FAQ page</a> to learn
        more</i></p>

        Args:
            symbol: Symbol of the company: AAPL.
            statement: Statement can take 1 of these values <code>bs, ic, cf</code> for Balance Sheet, Income Statement,
                Cash Flow respectively.
            freq: Frequency can take 1 of these values <code>annual, quarterly, ttm, ytd</code>. TTM (Trailing Twelve
                Months) option is available for Income Statement and Cash Flow. YTD (Year To Date) option is only
                available for Cash Flow.
            preliminary: If set to <code>true</code>, it will return Preliminary financial statements for the latest
                period which are usually available within an hour of the earnings announcement if finalized data is not
                available yet. This preliminary data is currently available for US companies. You will see
                <code>"preliminary": true</code> in the data if that period is using preliminary data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/financials"),
            query_params=[
                param[str]("symbol", symbol),
                param[str]("statement", statement),
                param[str]("freq", freq),
                param[str | None]("preliminary", preliminary),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[FinancialStatements],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def financials_reported(
        self,
        *,
        symbol: str | None = None,
        cik: str | None = None,
        access_number: str | None = None,
        freq: str | None = None,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FinancialsAsReported, RawError]:
        """Get financials as reported. This data is available for bulk download on <a
        href="https://www.kaggle.com/finnhub/reported-financials" target="_blank">Kaggle SEC Financials database</a>.

        Args:
            symbol: Symbol.
            cik: CIK.
            access_number: Access number of a specific report you want to retrieve financials from.
            freq: Frequency. Can be either <code>annual</code> or <code>quarterly</code>. Default to
                <code>annual</code>.
            from_: From date <code>YYYY-MM-DD</code>. Filter for endDate.
            to: To date <code>YYYY-MM-DD</code>. Filter for endDate.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/financials-reported"),
            query_params=[
                param[str | None]("symbol", symbol),
                param[str | None]("cik", cik),
                param[str | None]("accessNumber", access_number),
                param[str | None]("freq", freq),
                param[Date | None]("from", from_),
                param[Date | None]("to", to),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[FinancialsAsReported],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def forex_candles(
        self, symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ForexCandles, RawError]:
        """Get candlestick data for forex symbols.

        Args:
            symbol: Use symbol returned in <code>/forex/symbol</code> endpoint for this field.
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            from_: UNIX timestamp. Interval initial value.
            to: UNIX timestamp. Interval end value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/forex/candle"),
            query_params=[
                param[str]("symbol", symbol),
                param[str]("resolution", resolution),
                param[int]("from", from_),
                param[int]("to", to),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[ForexCandles],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def forex_exchanges(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[str], RawError]:
        """List supported forex exchanges

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/forex/exchange"),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[str]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def forex_rates(
        self, *, base: str | None = None, date: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Forexrates, RawError]:
        """Get rates for all forex pairs. Ideal for currency conversion

        Args:
            base: Base currency. Default to EUR.
            date: Date. Leave blank to get the latest data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/forex/rates"),
            query_params=[param[str | None]("base", base), param[str | None]("date", date)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[Forexrates],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def forex_symbols(
        self, exchange: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ForexSymbol], RawError]:
        """List supported forex symbols.

        Args:
            exchange: Exchange you want to get the list of symbols from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/forex/symbol"),
            query_params=[param[str]("exchange", exchange)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[ForexSymbol]],
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

    def global_filings_download(
        self, document_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """<p>Download filings using document ids.</p>

        Args:
            document_id: Document's id. Note that this is different from filingId as 1 filing can contain multiple
                documents.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/global-filings/download"),
            query_params=[param[str]("documentId", document_id)],
            auth_scheme=self._auth.api_key,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def global_filings_search(
        self, *, search: SearchBody | SearchBodyDict | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SearchResponse, RawError]:
        """<p>Search for best-matched filings across global companies' filings, transcripts and press releases. You can
        filter by anything from symbol, ISIN to form type, and document sources.</p><p>This endpoint will return a list
        of documents that match your search criteria. If you would like to get the excerpts as well, please set
        <code>highlighted</code> to <code>true</code>. Once you have the list of documents, you can get a list of
        excerpts and positions to highlight the document using the <code>/search-in-filing</code> endpoint</p>

        Args:
            search: Search body
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/global-filings/search"),
            body=json_body[SearchBody | SearchBodyDict | None](search),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[SearchResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def global_filings_search_filter(
        self, field: str, *, source: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SearchFilter, RawError]:
        """<p>Get available values for each filter in search body.</p>

        Args:
            field: Field to get available filters. Available filters are "countries", "exchanges", "exhibits", "forms",
                "gics", "naics", "caps", "acts", and "sort".
            source: Get available forms for each source.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/global-filings/filter"),
            query_params=[param[str]("field", field), param[str | None]("source", source)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[SearchFilter],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def historical_employee_count(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[HistoricalEmployeeCount, RawError]:
        """Get historical employee count for global companies.

        Args:
            symbol: Company symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/historical-employee-count"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[HistoricalEmployeeCount],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def historical_market_cap(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[HistoricalMarketCapData, RawError]:
        """Get historical market cap data for global companies.

        Args:
            symbol: Company symbol.
            from_: From date <code>YYYY-MM-DD</code>.
            to: To date <code>YYYY-MM-DD</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/historical-market-cap"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[HistoricalMarketCapData],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

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

    def international_filings(
        self,
        *,
        symbol: str | None = None,
        country: str | None = None,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[InternationalFiling], RawError]:
        """List filings for international companies. Limit to 500 documents at a time. These are the documents we use to
        source our fundamental data. Enterprise clients who need access to the full filings for global markets should
        contact us for the access.

        Args:
            symbol: Symbol. Leave empty to list latest filings.
            country: Filter by country using country's 2-letter code.
            from_: From date: 2023-01-15.
            to: To date: 2023-12-16.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/international-filings"),
            query_params=[
                param[str | None]("symbol", symbol),
                param[str | None]("country", country),
                param[Date | None]("from", from_),
                param[Date | None]("to", to),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[InternationalFiling]],
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

    def market_holiday(
        self, exchange: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MarketHoliday, RawError]:
        """Get a list of holidays for global exchanges.

        Args:
            exchange: Exchange code.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/market-holiday"),
            query_params=[param[str]("exchange", exchange)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[MarketHoliday],
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

    def market_status(
        self, exchange: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MarketStatus, RawError]:
        """Get current market status for global exchanges (whether exchanges are open or close).

        Args:
            exchange: Exchange code.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/market-status"),
            query_params=[param[str]("exchange", exchange)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[MarketStatus],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def mutual_fund_country_exposure(
        self, *, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MutualFundCountryExposure, RawError]:
        """Get Mutual Funds country exposure data.

        Args:
            symbol: Symbol.
            isin: Fund's isin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/mutual-fund/country"),
            query_params=[param[str | None]("symbol", symbol), param[str | None]("isin", isin)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[MutualFundCountryExposure],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def mutual_fund_eet(
        self, isin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MutualFundEet, RawError]:
        """Get EET data for EU funds. For PAIs data, please see the EET PAI endpoint.

        Args:
            isin: ISIN.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/mutual-fund/eet"),
            query_params=[param[str]("isin", isin)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[MutualFundEet],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def mutual_fund_eet_pai(
        self, isin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MutualFundEetPai, RawError]:
        """Get EET PAI data for EU funds.

        Args:
            isin: ISIN.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/mutual-fund/eet-pai"),
            query_params=[param[str]("isin", isin)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[MutualFundEetPai],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def mutual_fund_holdings(
        self,
        *,
        symbol: str | None = None,
        isin: str | None = None,
        skip: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MutualFundHoldings, RawError]:
        """Get full Mutual Funds holdings/constituents. This endpoint covers both US and global mutual funds. For
        international funds, you must query the data using ISIN. A list of supported funds can be found <a
        href="/api/v1/mutual-fund/list?token=" target="_blank">here</a>.

        Args:
            symbol: Fund's symbol.
            isin: Fund's isin.
            skip: Skip the first n results. You can use this parameter to query historical constituents data. The latest
                result is returned if skip=0 or not set.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/mutual-fund/holdings"),
            query_params=[
                param[str | None]("symbol", symbol), param[str | None]("isin", isin), param[int | None]("skip", skip)
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[MutualFundHoldings],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def mutual_fund_profile(
        self, *, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MutualFundProfile, RawError]:
        """Get mutual funds profile information. This endpoint covers both US and global mutual funds. For international
        funds, you must query the data using ISIN. A list of supported funds can be found <a
        href="/api/v1/mutual-fund/list?type=csv&token=" target="_blank">here</a>.

        Args:
            symbol: Fund's symbol.
            isin: Fund's isin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/mutual-fund/profile"),
            query_params=[param[str | None]("symbol", symbol), param[str | None]("isin", isin)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[MutualFundProfile],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def mutual_fund_sector_exposure(
        self, *, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MutualFundSectorExposure, RawError]:
        """Get Mutual Funds sector exposure data.

        Args:
            symbol: Mutual Fund symbol.
            isin: Fund's isin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/mutual-fund/sector"),
            query_params=[param[str | None]("symbol", symbol), param[str | None]("isin", isin)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[MutualFundSectorExposure],
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

    def newsroom(
        self,
        symbol: str,
        *,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Newsroom, RawError]:
        """<p>Get latest articles posted directly on the companies' newsroom and investor relations page. Newsroom API
        along with the Press Releases API provide a comprehensive text-based dataset directly from the company. We
        currently cover 1,250 US Companies with this dataset.</p>

        Args:
            symbol: Company symbol.
            from_: From time: 2025-01-01.
            to: To time: 2026-01-05.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/newsroom"),
            query_params=[
                param[str]("symbol", symbol), param[Date | None]("from", from_), param[Date | None]("to", to)
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[Newsroom],
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

    def price_metrics(
        self, symbol: str, *, date: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PriceMetrics, RawError]:
        """Get company price performance statistics such as 52-week high/low, YTD return and much more.

        Args:
            symbol: Symbol of the company: AAPL.
            date: Get data on a specific date in the past. The data is available weekly so your date will be
                automatically adjusted to the last day of that week.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/price-metric"),
            query_params=[param[str]("symbol", symbol), param[str | None]("date", date)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[PriceMetrics],
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

    def search_in_filing(
        self,
        *,
        search: InFilingSearchBody | InFilingSearchBodyDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InFilingResponse, RawError]:
        """<p>Get a list of excerpts and highlight positions within a document using your query.</p>

        Args:
            search: Search body
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/global-filings/search-in-filing"),
            body=json_body[InFilingSearchBody | InFilingSearchBodyDict | None](search),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[InFilingResponse],
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

    def similarity_index(
        self,
        *,
        symbol: str | None = None,
        cik: str | None = None,
        freq: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SimilarityIndex, RawError]:
        """<p>Calculate the textual difference between a company's 10-K / 10-Q reports and the same type of report in
        the previous year using Cosine Similarity. For example, this endpoint compares 2019's 10-K with 2018's 10-K.
        Companies breaking from its routines in disclosure of financial condition and risk analysis section can signal a
        significant change in the company's stock price in the upcoming 4 quarters.</p>

        Args:
            symbol: Symbol. Required if cik is empty
            cik: CIK. Required if symbol is empty
            freq: <code>annual</code> or <code>quarterly</code>. Default to <code>annual</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/similarity-index"),
            query_params=[
                param[str | None]("symbol", symbol), param[str | None]("cik", cik), param[str | None]("freq", freq)
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[SimilarityIndex],
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

    def stock_basic_dividends(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Dividends2, RawError]:
        """Get global dividends data.

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/dividend2"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[Dividends2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stock_bidask(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LastBidAsk, RawError]:
        """Get last bid/ask data for US stocks.

        Args:
            symbol: Symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/bidask"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[LastBidAsk],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stock_candles(
        self, symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StockCandles, RawError]:
        """<p>Get candlestick data (OHLCV) for stocks.</p><p>Daily data will be adjusted for Splits. Intraday data will
        remain unadjusted. Only 1 month of intraday will be returned at a time. If you need more historical intraday
        data, please use the from and to params iteratively to request more data.</p>

        Args:
            symbol: Symbol.
            resolution: Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not
                be available depending on the exchange.
            from_: UNIX timestamp. Interval initial value.
            to: UNIX timestamp. Interval end value.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/candle"),
            query_params=[
                param[str]("symbol", symbol),
                param[str]("resolution", resolution),
                param[int]("from", from_),
                param[int]("to", to),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[StockCandles],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stock_dividends(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Dividends], RawError]:
        """Get dividends data for common stocks going back 30 years.

        Args:
            symbol: Symbol.
            from_: YYYY-MM-DD.
            to: YYYY-MM-DD.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/dividend"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[Dividends]],
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

    def stock_nbbo(
        self, symbol: str, date: Date, limit: int, skip: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[HistoricalNbbo, RawError]:
        """<p>Get historical best bid and offer for US stocks, LSE, TSX, Euronext and Deutsche Borse.</p><p>For US
        market, this endpoint only serves historical NBBO from the beginning of 2023. To download more historical data,
        please visit our bulk download page in the Dashboard <a target="_blank"
        href="/dashboard/download",>here</a>.</p>

        Args:
            symbol: Symbol.
            date: Date: 2020-04-02.
            limit: Limit number of ticks returned. Maximum value: <code>25000</code>
            skip: Number of ticks to skip. Use this parameter to loop through the entire data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/bbo"),
            query_params=[
                param[str]("symbol", symbol),
                param[Date]("date", date),
                param[int]("limit", limit),
                param[int]("skip", skip),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[HistoricalNbbo],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stock_presentation(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StockPresentation, RawError]:
        """<p>Get presentations/slides data in PDF format that are usually used during earnings calls. You can get a
        list of supported symbols <a target="_blank" href="/api/v1/stock/presentation/symbol?token=">here</a></p>

        Args:
            symbol: Company symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/presentation"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[StockPresentation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stock_splits(
        self, symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Split], RawError]:
        """Get splits data for stocks.

        Args:
            symbol: Symbol.
            from_: YYYY-MM-DD.
            to: YYYY-MM-DD.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/split"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[Split]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stock_symbols(
        self,
        exchange: str,
        *,
        mic: str | None = None,
        security_type: str | None = None,
        currency: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[StockSymbol], RawError]:
        """List supported stocks. We use the following symbology to identify stocks on Finnhub
        <code>Exchange_Ticker.Exchange_Code</code>. A list of supported exchange codes can be found <a
        href="https://docs.google.com/spreadsheets/d/1I3pBxjfXB056-g_JYf_6o3Rns3BV2kMGG1nCatb91ls/edit?usp=sharing"
        target="_blank">here</a>.

        Args:
            exchange: Exchange you want to get the list of symbols from. List of exchange codes can be found <a
                href="https://docs.google.com/spreadsheets/d/1I3pBxjfXB056-g_JYf_6o3Rns3BV2kMGG1nCatb91ls/edit?usp=sharing"
                target="_blank">here</a>.
            mic: Filter by MIC code.
            security_type: Filter by security type used by OpenFigi standard.
            currency: Filter by currency.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/symbol"),
            query_params=[
                param[str]("exchange", exchange),
                param[str | None]("mic", mic),
                param[str | None]("securityType", security_type),
                param[str | None]("currency", currency),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[list[StockSymbol]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stock_tick(
        self, symbol: str, date: Date, limit: int, skip: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TickData, RawError]:
        """<p>Get historical tick data for global exchanges.</p><p>For more historical tick data, you can visit our bulk
        download page in the Dashboard <a target="_blank" href="/dashboard/download",>here</a> to speed up the download
        process.</p><table class="table table-hover">
          <thead>
            <tr>
              <th>Exchange</th>
              <th>Segment</th>
              <th>Delay</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-blue">US CTA/UTP</th>
              <td>Full SIP</td>
              <td>End-of-day</td>
            </tr>
            <tr>
              <td class="text-blue">TSX</th>
              <td><ul><li>TSX</li><li>TSX Venture</li><li>Index</li></ul></td>
              <td>End-of-day</td>
            </tr>
            <tr>
              <td class="text-blue">LSE</th>
              <td><ul><li>London Stock Exchange (L)</li><li>LSE International (L)</li><li>LSE European
                (L)</li></ul></td>
              <td>15 minute</td>
            </tr>
            <tr>
              <td class="text-blue">Euronext</th>
              <td><ul> <li>Euronext Paris (PA)</li> <li>Euronext Amsterdam (AS)</li> <li>Euronext Lisbon (LS)</li>
                <li>Euronext Brussels (BR)</li> <li>Euronext Oslo (OL)</li> <li>Euronext London (LN)</li> <li>Euronext
                Dublin (IR)</li> <li>Index</li> <li>Warrant</li></ul></td>
              <td>End-of-day</td>
            </tr>
            <tr>
              <td class="text-blue">Deutsche Börse</th>
              <td><ul> <li>Frankfurt (F)</li> <li>Xetra (DE)</li> <li>Duesseldorf (DU)</li> <li>Hamburg (HM)</li>
                <li>Berlin (BE)</li> <li>Hanover (HA)</li> <li>Stoxx (SX)</li> <li>TradeGate (TG)</li> <li>Zertifikate
                (SC)</li> <li>Index</li> <li>Warrant</li></ul></td>
              <td>End-of-day</td>
            </tr>
          </tbody>
        </table>

        Args:
            symbol: Symbol.
            date: Date: 2020-04-02.
            limit: Limit number of ticks returned. Maximum value: <code>25000</code>
            skip: Number of ticks to skip. Use this parameter to loop through the entire data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/tick"),
            query_params=[
                param[str]("symbol", symbol),
                param[Date]("date", date),
                param[int]("limit", limit),
                param[int]("skip", skip),
            ],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[TickData],
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

    def transcripts(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EarningsCallTranscripts, RawError]:
        """<p>Get earnings call transcripts, audio and participants' list. Data is available for US, UK, European,
        Australian and Canadian companies.<p>15+ years of data is available with 220,000+ audio which add up to 7TB in
        size.</p>

        Args:
            id: Transcript's id obtained with <a href="#transcripts-list">Transcripts List endpoint</a>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/transcripts"),
            query_params=[param[str]("id", id)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EarningsCallTranscripts],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def transcripts_list(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EarningsCallTranscriptsList, RawError]:
        """List earnings call transcripts' metadata. This endpoint is available for Global companies. You can get a list
        of supported symbols <a target="_blank" href="/api/v1/stock/transcripts/symbol?token=">here</a>

        Args:
            symbol: Company symbol: AAPL. Leave empty to list the latest transcripts
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/transcripts/list"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EarningsCallTranscriptsList],
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


Client = FinnhubClient
