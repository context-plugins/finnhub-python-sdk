from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.bond import Bond
from .apis.calendar import Calendar
from .apis.corporate_actions import CorporateActions
from .apis.crypto import Crypto
from .apis.economic import Economic
from .apis.etf import Etf
from .apis.forex import Forex
from .apis.global_filings import GlobalFilings
from .apis.index import Index
from .apis.institutional import Institutional
from .apis.misc import Misc
from .apis.mutual_fund import MutualFund
from .apis.news import News
from .apis.scan import Scan
from .apis.stock_estimates import StockEstimates
from .apis.stock_fundamentals import StockFundamentals
from .apis.stock_ownership import StockOwnership
from .apis.stock_prices import StockPrices
from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseFinnhubApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyQueryScheme,
    HttpClient,
    HttpxClient,
    RawClient,
    no_auth,
    param,
)


class FinnhubApiClient(BaseFinnhubApiClient[RawClient]):
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
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout),
            global_headers=[
                param[str]("User-Agent", "FinnhubApiClient/1.0.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "1.0.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AuthSchemes(api_key=ApiKeyQueryScheme("token", api_key) if api_key is not None else no_auth)

    @cached_property
    def bond(self) -> Bond:
        return Bond(self._raw_client, self._server, self._auth)

    @cached_property
    def calendar(self) -> Calendar:
        return Calendar(self._raw_client, self._server, self._auth)

    @cached_property
    def corporate_actions(self) -> CorporateActions:
        return CorporateActions(self._raw_client, self._server, self._auth)

    @cached_property
    def crypto(self) -> Crypto:
        return Crypto(self._raw_client, self._server, self._auth)

    @cached_property
    def economic(self) -> Economic:
        return Economic(self._raw_client, self._server, self._auth)

    @cached_property
    def etf(self) -> Etf:
        return Etf(self._raw_client, self._server, self._auth)

    @cached_property
    def forex(self) -> Forex:
        return Forex(self._raw_client, self._server, self._auth)

    @cached_property
    def global_filings(self) -> GlobalFilings:
        return GlobalFilings(self._raw_client, self._server, self._auth)

    @cached_property
    def index(self) -> Index:
        return Index(self._raw_client, self._server, self._auth)

    @cached_property
    def institutional(self) -> Institutional:
        return Institutional(self._raw_client, self._server, self._auth)

    @cached_property
    def misc(self) -> Misc:
        return Misc(self._raw_client, self._server, self._auth)

    @cached_property
    def mutual_fund(self) -> MutualFund:
        return MutualFund(self._raw_client, self._server, self._auth)

    @cached_property
    def news(self) -> News:
        return News(self._raw_client, self._server, self._auth)

    @cached_property
    def scan(self) -> Scan:
        return Scan(self._raw_client, self._server, self._auth)

    @cached_property
    def stock_estimates(self) -> StockEstimates:
        return StockEstimates(self._raw_client, self._server, self._auth)

    @cached_property
    def stock_fundamentals(self) -> StockFundamentals:
        return StockFundamentals(self._raw_client, self._server, self._auth)

    @cached_property
    def stock_ownership(self) -> StockOwnership:
        return StockOwnership(self._raw_client, self._server, self._auth)

    @cached_property
    def stock_prices(self) -> StockPrices:
        return StockPrices(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = FinnhubApiClient
