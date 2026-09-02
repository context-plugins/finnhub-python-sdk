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
from ..models.bond_candles import BondCandles
from ..models.bond_profile import BondProfile
from ..models.bond_tick_data import BondTickData
from ..models.bond_yield_curve import BondYieldCurve
from ..server.server import Server


class Bond:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = BondWithRawResponse(client, server, auth)

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
        return self._with_raw_response.bond_price(isin, from_, to, request_options=request_options).unwrap()

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
        return self._with_raw_response.bond_profile(
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
        return self._with_raw_response.bond_tick(
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
        return self._with_raw_response.bond_yield_curve(code, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> BondWithRawResponse:
        return self._with_raw_response


class AsyncBond:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncBondWithRawResponse(client, server, auth)

    async def bond_price(
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
        return (await self._with_raw_response.bond_price(isin, from_, to, request_options=request_options)).unwrap()

    async def bond_profile(
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
        return (
            await self._with_raw_response.bond_profile(
                isin=isin, cusip=cusip, figi=figi, request_options=request_options
            )
        ).unwrap()

    async def bond_tick(
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
        return (
            await self._with_raw_response.bond_tick(isin, date, limit, skip, exchange, request_options=request_options)
        ).unwrap()

    async def bond_yield_curve(
        self, code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BondYieldCurve:
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
        return (await self._with_raw_response.bond_yield_curve(code, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncBondWithRawResponse:
        return self._with_raw_response


class BondWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
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


class AsyncBondWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def bond_price(
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
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/bond/price"),
            query_params=[param[str]("isin", isin), param[int]("from", from_), param[int]("to", to)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[BondCandles],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bond_profile(
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
        return await self._client.execute(
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

    async def bond_tick(
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
        return await self._client.execute(
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

    async def bond_yield_curve(
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
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/bond/yield-curve"),
            query_params=[param[str]("code", code)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[BondYieldCurve],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
