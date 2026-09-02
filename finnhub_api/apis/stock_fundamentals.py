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
from ..models.basic_financials import BasicFinancials
from ..models.company_esg import CompanyEsg
from ..models.company_executive import CompanyExecutive
from ..models.company_profile import CompanyProfile
from ..models.company_profile2 import CompanyProfile2
from ..models.earnings_call_live import EarningsCallLive
from ..models.earnings_call_transcripts import EarningsCallTranscripts
from ..models.earnings_call_transcripts_list import EarningsCallTranscriptsList
from ..models.filing import Filing
from ..models.financial_statements import FinancialStatements
from ..models.financials_as_reported import FinancialsAsReported
from ..models.historical_company_esg import HistoricalCompanyEsg
from ..models.historical_employee_count import HistoricalEmployeeCount
from ..models.international_filing import InternationalFiling
from ..models.newsroom import Newsroom
from ..models.secsentiment_analysis import SecsentimentAnalysis
from ..models.similarity_index import SimilarityIndex
from ..models.stock_presentation import StockPresentation
from ..server.server import Server


class StockFundamentals:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = StockFundamentalsWithRawResponse(client, server, auth)

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
        return self._with_raw_response.company_basic_financials(
            symbol, metric, request_options=request_options
        ).unwrap()

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
        return self._with_raw_response.company_esg_score(symbol, request_options=request_options).unwrap()

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
        return self._with_raw_response.company_executive(symbol, request_options=request_options).unwrap()

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
        return self._with_raw_response.company_historical_esg_score(symbol, request_options=request_options).unwrap()

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
        return self._with_raw_response.company_profile(
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
        return self._with_raw_response.company_profile2(
            symbol=symbol, isin=isin, cusip=cusip, request_options=request_options
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
        return self._with_raw_response.earnings_call_live(
            from_=from_, to=to, symbol=symbol, request_options=request_options
        ).unwrap()

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
        return self._with_raw_response.filings(
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
        return self._with_raw_response.filings_sentiment(access_number, request_options=request_options).unwrap()

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
        return self._with_raw_response.financials(
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
        return self._with_raw_response.financials_reported(
            symbol=symbol,
            cik=cik,
            access_number=access_number,
            freq=freq,
            from_=from_,
            to=to,
            request_options=request_options,
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
        return self._with_raw_response.historical_employee_count(
            symbol, from_, to, request_options=request_options
        ).unwrap()

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
        return self._with_raw_response.international_filings(
            symbol=symbol, country=country, from_=from_, to=to, request_options=request_options
        ).unwrap()

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
        return self._with_raw_response.newsroom(symbol, from_=from_, to=to, request_options=request_options).unwrap()

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
        return self._with_raw_response.similarity_index(
            symbol=symbol, cik=cik, freq=freq, request_options=request_options
        ).unwrap()

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
        return self._with_raw_response.stock_presentation(symbol, request_options=request_options).unwrap()

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
        return self._with_raw_response.transcripts(id, request_options=request_options).unwrap()

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
        return self._with_raw_response.transcripts_list(symbol, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> StockFundamentalsWithRawResponse:
        return self._with_raw_response


class AsyncStockFundamentals:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncStockFundamentalsWithRawResponse(client, server, auth)

    async def company_basic_financials(
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
        return (
            await self._with_raw_response.company_basic_financials(symbol, metric, request_options=request_options)
        ).unwrap()

    async def company_esg_score(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CompanyEsg:
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
        return (await self._with_raw_response.company_esg_score(symbol, request_options=request_options)).unwrap()

    async def company_executive(
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
        return (await self._with_raw_response.company_executive(symbol, request_options=request_options)).unwrap()

    async def company_historical_esg_score(
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
        return (
            await self._with_raw_response.company_historical_esg_score(symbol, request_options=request_options)
        ).unwrap()

    async def company_profile(
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
        return (
            await self._with_raw_response.company_profile(
                symbol=symbol, isin=isin, cusip=cusip, request_options=request_options
            )
        ).unwrap()

    async def company_profile2(
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
        return (
            await self._with_raw_response.company_profile2(
                symbol=symbol, isin=isin, cusip=cusip, request_options=request_options
            )
        ).unwrap()

    async def earnings_call_live(
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
        return (
            await self._with_raw_response.earnings_call_live(
                from_=from_, to=to, symbol=symbol, request_options=request_options
            )
        ).unwrap()

    async def filings(
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
        return (
            await self._with_raw_response.filings(
                symbol=symbol,
                cik=cik,
                access_number=access_number,
                form=form,
                from_=from_,
                to=to,
                request_options=request_options,
            )
        ).unwrap()

    async def filings_sentiment(
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
        return (
            await self._with_raw_response.filings_sentiment(access_number, request_options=request_options)
        ).unwrap()

    async def financials(
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
        return (
            await self._with_raw_response.financials(
                symbol, statement, freq, preliminary=preliminary, request_options=request_options
            )
        ).unwrap()

    async def financials_reported(
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
        return (
            await self._with_raw_response.financials_reported(
                symbol=symbol,
                cik=cik,
                access_number=access_number,
                freq=freq,
                from_=from_,
                to=to,
                request_options=request_options,
            )
        ).unwrap()

    async def historical_employee_count(
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
        return (
            await self._with_raw_response.historical_employee_count(symbol, from_, to, request_options=request_options)
        ).unwrap()

    async def international_filings(
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
        return (
            await self._with_raw_response.international_filings(
                symbol=symbol, country=country, from_=from_, to=to, request_options=request_options
            )
        ).unwrap()

    async def newsroom(
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
        return (
            await self._with_raw_response.newsroom(symbol, from_=from_, to=to, request_options=request_options)
        ).unwrap()

    async def similarity_index(
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
        return (
            await self._with_raw_response.similarity_index(
                symbol=symbol, cik=cik, freq=freq, request_options=request_options
            )
        ).unwrap()

    async def stock_presentation(
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
        return (await self._with_raw_response.stock_presentation(symbol, request_options=request_options)).unwrap()

    async def transcripts(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> EarningsCallTranscripts:
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
        return (await self._with_raw_response.transcripts(id, request_options=request_options)).unwrap()

    async def transcripts_list(
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
        return (await self._with_raw_response.transcripts_list(symbol, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncStockFundamentalsWithRawResponse:
        return self._with_raw_response


class StockFundamentalsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
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


class AsyncStockFundamentalsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def company_basic_financials(
        self, symbol: str, metric: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BasicFinancials, RawError]:
        """Get company basic financials such as margin, P/E ratio, 52-week high/low etc.

        Args:
            symbol: Symbol of the company: AAPL.
            metric: Metric type. Can be 1 of the following values <code>all</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/metric"),
            query_params=[param[str]("symbol", symbol), param[str]("metric", metric)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[BasicFinancials],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def company_esg_score(
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
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/esg"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[CompanyEsg],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def company_executive(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CompanyExecutive, RawError]:
        """Get a list of company's executives and members of the Board.

        Args:
            symbol: Symbol of the company: AAPL.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/executive"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[CompanyExecutive],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def company_historical_esg_score(
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
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/historical-esg"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[HistoricalCompanyEsg],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def company_profile(
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
        return await self._client.execute(
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

    async def company_profile2(
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
        return await self._client.execute(
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

    async def earnings_call_live(
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
        return await self._client.execute(
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

    async def filings(
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
        return await self._client.execute(
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

    async def filings_sentiment(
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
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/filings-sentiment"),
            query_params=[param[str]("accessNumber", access_number)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[SecsentimentAnalysis],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def financials(
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
        return await self._client.execute(
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

    async def financials_reported(
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
        return await self._client.execute(
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

    async def historical_employee_count(
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
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/historical-employee-count"),
            query_params=[param[str]("symbol", symbol), param[Date]("from", from_), param[Date]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[HistoricalEmployeeCount],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def international_filings(
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
        return await self._client.execute(
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

    async def newsroom(
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
        return await self._client.execute(
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

    async def similarity_index(
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
        return await self._client.execute(
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

    async def stock_presentation(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StockPresentation, RawError]:
        """<p>Get presentations/slides data in PDF format that are usually used during earnings calls. You can get a
        list of supported symbols <a target="_blank" href="/api/v1/stock/presentation/symbol?token=">here</a></p>

        Args:
            symbol: Company symbol.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/presentation"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[StockPresentation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def transcripts(
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
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/transcripts"),
            query_params=[param[str]("id", id)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EarningsCallTranscripts],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def transcripts_list(
        self, symbol: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EarningsCallTranscriptsList, RawError]:
        """List earnings call transcripts' metadata. This endpoint is available for Global companies. You can get a list
        of supported symbols <a target="_blank" href="/api/v1/stock/transcripts/symbol?token=">here</a>

        Args:
            symbol: Company symbol: AAPL. Leave empty to list the latest transcripts
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/stock/transcripts/list"),
            query_params=[param[str]("symbol", symbol)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EarningsCallTranscriptsList],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
