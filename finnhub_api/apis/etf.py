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
from ..models.etfs_allocation import EtfsAllocation
from ..models.etfs_country_exposure import EtfsCountryExposure
from ..models.etfs_holdings import EtfsHoldings
from ..models.etfs_profile import EtfsProfile
from ..models.etfs_sector_exposure import EtfsSectorExposure
from ..server.server import Server


class Etf:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EtfWithRawResponse(client, server, auth)

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
        return self._with_raw_response.etfs_allocation(
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
        return self._with_raw_response.etfs_country_exposure(
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
        return self._with_raw_response.etfs_holdings(
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
        return self._with_raw_response.etfs_profile(symbol=symbol, isin=isin, request_options=request_options).unwrap()

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
        return self._with_raw_response.etfs_sector_exposure(
            symbol=symbol, isin=isin, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> EtfWithRawResponse:
        return self._with_raw_response


class AsyncEtf:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEtfWithRawResponse(client, server, auth)

    async def etfs_allocation(
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
        return (
            await self._with_raw_response.etfs_allocation(symbol=symbol, isin=isin, request_options=request_options)
        ).unwrap()

    async def etfs_country_exposure(
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
        return (
            await self._with_raw_response.etfs_country_exposure(
                symbol=symbol, isin=isin, request_options=request_options
            )
        ).unwrap()

    async def etfs_holdings(
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
        return (
            await self._with_raw_response.etfs_holdings(
                symbol=symbol, isin=isin, skip=skip, date=date, request_options=request_options
            )
        ).unwrap()

    async def etfs_profile(
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
        return (
            await self._with_raw_response.etfs_profile(symbol=symbol, isin=isin, request_options=request_options)
        ).unwrap()

    async def etfs_sector_exposure(
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
        return (
            await self._with_raw_response.etfs_sector_exposure(
                symbol=symbol, isin=isin, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncEtfWithRawResponse:
        return self._with_raw_response


class EtfWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
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


class AsyncEtfWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def etfs_allocation(
        self, *, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EtfsAllocation, RawError]:
        """Get ETF equity allocation based on the characteristics of the holdings.

        Args:
            symbol: ETF symbol.
            isin: ETF isin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/etf/allocation"),
            query_params=[param[str | None]("symbol", symbol), param[str | None]("isin", isin)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EtfsAllocation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def etfs_country_exposure(
        self, *, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EtfsCountryExposure, RawError]:
        """Get ETF country exposure data.

        Args:
            symbol: ETF symbol.
            isin: ETF isin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/etf/country"),
            query_params=[param[str | None]("symbol", symbol), param[str | None]("isin", isin)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EtfsCountryExposure],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def etfs_holdings(
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
        return await self._client.execute(
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

    async def etfs_profile(
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
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/etf/profile"),
            query_params=[param[str | None]("symbol", symbol), param[str | None]("isin", isin)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EtfsProfile],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def etfs_sector_exposure(
        self, *, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EtfsSectorExposure, RawError]:
        """Get ETF sector exposure data.

        Args:
            symbol: ETF symbol.
            isin: ETF isin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/etf/sector"),
            query_params=[param[str | None]("symbol", symbol), param[str | None]("isin", isin)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[EtfsSectorExposure],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
