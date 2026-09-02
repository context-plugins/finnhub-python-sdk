from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.bond import AsyncBond
from .apis.calendar import AsyncCalendar
from .apis.corporate_actions import AsyncCorporateActions
from .apis.crypto import AsyncCrypto
from .apis.economic import AsyncEconomic
from .apis.etf import AsyncEtf
from .apis.forex import AsyncForex
from .apis.global_filings import AsyncGlobalFilings
from .apis.index import AsyncIndex
from .apis.institutional import AsyncInstitutional
from .apis.misc import AsyncMisc
from .apis.mutual_fund import AsyncMutualFund
from .apis.news import AsyncNews
from .apis.scan import AsyncScan
from .apis.stock_estimates import AsyncStockEstimates
from .apis.stock_fundamentals import AsyncStockFundamentals
from .apis.stock_ownership import AsyncStockOwnership
from .apis.stock_prices import AsyncStockPrices
from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseFinnhubApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyQueryScheme,
    AsyncHttpClient,
    AsyncHttpxClient,
    AsyncRawClient,
    no_auth,
    param,
)


class AsyncFinnhubApiClient(BaseFinnhubApiClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_async_http_client: AsyncHttpClient | None = None,
        api_key: str | None = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpxClient(timeout=timeout)
            ),
            global_headers=[
                param[str]("User-Agent", "FinnhubApiClient/1.0.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "1.0.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(api_key=ApiKeyQueryScheme("token", api_key) if api_key is not None else no_auth)

    @cached_property
    def bond(self) -> AsyncBond:
        return AsyncBond(self._raw_client, self._server, self._auth)

    @cached_property
    def calendar(self) -> AsyncCalendar:
        return AsyncCalendar(self._raw_client, self._server, self._auth)

    @cached_property
    def corporate_actions(self) -> AsyncCorporateActions:
        return AsyncCorporateActions(self._raw_client, self._server, self._auth)

    @cached_property
    def crypto(self) -> AsyncCrypto:
        return AsyncCrypto(self._raw_client, self._server, self._auth)

    @cached_property
    def economic(self) -> AsyncEconomic:
        return AsyncEconomic(self._raw_client, self._server, self._auth)

    @cached_property
    def etf(self) -> AsyncEtf:
        return AsyncEtf(self._raw_client, self._server, self._auth)

    @cached_property
    def forex(self) -> AsyncForex:
        return AsyncForex(self._raw_client, self._server, self._auth)

    @cached_property
    def global_filings(self) -> AsyncGlobalFilings:
        return AsyncGlobalFilings(self._raw_client, self._server, self._auth)

    @cached_property
    def index(self) -> AsyncIndex:
        return AsyncIndex(self._raw_client, self._server, self._auth)

    @cached_property
    def institutional(self) -> AsyncInstitutional:
        return AsyncInstitutional(self._raw_client, self._server, self._auth)

    @cached_property
    def misc(self) -> AsyncMisc:
        return AsyncMisc(self._raw_client, self._server, self._auth)

    @cached_property
    def mutual_fund(self) -> AsyncMutualFund:
        return AsyncMutualFund(self._raw_client, self._server, self._auth)

    @cached_property
    def news(self) -> AsyncNews:
        return AsyncNews(self._raw_client, self._server, self._auth)

    @cached_property
    def scan(self) -> AsyncScan:
        return AsyncScan(self._raw_client, self._server, self._auth)

    @cached_property
    def stock_estimates(self) -> AsyncStockEstimates:
        return AsyncStockEstimates(self._raw_client, self._server, self._auth)

    @cached_property
    def stock_fundamentals(self) -> AsyncStockFundamentals:
        return AsyncStockFundamentals(self._raw_client, self._server, self._auth)

    @cached_property
    def stock_ownership(self) -> AsyncStockOwnership:
        return AsyncStockOwnership(self._raw_client, self._server, self._auth)

    @cached_property
    def stock_prices(self) -> AsyncStockPrices:
        return AsyncStockPrices(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncFinnhubApiClient
