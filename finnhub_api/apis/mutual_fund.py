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
from ..models.mutual_fund_country_exposure import MutualFundCountryExposure
from ..models.mutual_fund_eet import MutualFundEet
from ..models.mutual_fund_eet_pai import MutualFundEetPai
from ..models.mutual_fund_holdings import MutualFundHoldings
from ..models.mutual_fund_profile import MutualFundProfile
from ..models.mutual_fund_sector_exposure import MutualFundSectorExposure
from ..server.server import Server


class MutualFund:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MutualFundWithRawResponse(client, server, auth)

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
        return self._with_raw_response.mutual_fund_country_exposure(
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
        return self._with_raw_response.mutual_fund_eet(isin, request_options=request_options).unwrap()

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
        return self._with_raw_response.mutual_fund_eet_pai(isin, request_options=request_options).unwrap()

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
        return self._with_raw_response.mutual_fund_holdings(
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
        return self._with_raw_response.mutual_fund_profile(
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
        return self._with_raw_response.mutual_fund_sector_exposure(
            symbol=symbol, isin=isin, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> MutualFundWithRawResponse:
        return self._with_raw_response


class AsyncMutualFund:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMutualFundWithRawResponse(client, server, auth)

    async def mutual_fund_country_exposure(
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
        return (
            await self._with_raw_response.mutual_fund_country_exposure(
                symbol=symbol, isin=isin, request_options=request_options
            )
        ).unwrap()

    async def mutual_fund_eet(self, isin: str, *, request_options: RequestOptionsOrDict | None = None) -> MutualFundEet:
        """Get EET data for EU funds. For PAIs data, please see the EET PAI endpoint.

        Args:
            isin: ISIN.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.mutual_fund_eet(isin, request_options=request_options)).unwrap()

    async def mutual_fund_eet_pai(
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
        return (await self._with_raw_response.mutual_fund_eet_pai(isin, request_options=request_options)).unwrap()

    async def mutual_fund_holdings(
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
        return (
            await self._with_raw_response.mutual_fund_holdings(
                symbol=symbol, isin=isin, skip=skip, request_options=request_options
            )
        ).unwrap()

    async def mutual_fund_profile(
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
        return (
            await self._with_raw_response.mutual_fund_profile(symbol=symbol, isin=isin, request_options=request_options)
        ).unwrap()

    async def mutual_fund_sector_exposure(
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
        return (
            await self._with_raw_response.mutual_fund_sector_exposure(
                symbol=symbol, isin=isin, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMutualFundWithRawResponse:
        return self._with_raw_response


class MutualFundWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
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


class AsyncMutualFundWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def mutual_fund_country_exposure(
        self, *, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MutualFundCountryExposure, RawError]:
        """Get Mutual Funds country exposure data.

        Args:
            symbol: Symbol.
            isin: Fund's isin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/mutual-fund/country"),
            query_params=[param[str | None]("symbol", symbol), param[str | None]("isin", isin)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[MutualFundCountryExposure],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def mutual_fund_eet(
        self, isin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MutualFundEet, RawError]:
        """Get EET data for EU funds. For PAIs data, please see the EET PAI endpoint.

        Args:
            isin: ISIN.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/mutual-fund/eet"),
            query_params=[param[str]("isin", isin)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[MutualFundEet],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def mutual_fund_eet_pai(
        self, isin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MutualFundEetPai, RawError]:
        """Get EET PAI data for EU funds.

        Args:
            isin: ISIN.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/mutual-fund/eet-pai"),
            query_params=[param[str]("isin", isin)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[MutualFundEetPai],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def mutual_fund_holdings(
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
        return await self._client.execute(
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

    async def mutual_fund_profile(
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
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/mutual-fund/profile"),
            query_params=[param[str | None]("symbol", symbol), param[str | None]("isin", isin)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[MutualFundProfile],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def mutual_fund_sector_exposure(
        self, *, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MutualFundSectorExposure, RawError]:
        """Get Mutual Funds sector exposure data.

        Args:
            symbol: Mutual Fund symbol.
            isin: Fund's isin.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/mutual-fund/sector"),
            query_params=[param[str | None]("symbol", symbol), param[str | None]("isin", isin)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[MutualFundSectorExposure],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
