from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.in_filing_response import InFilingResponse
from ..models.in_filing_search_body import InFilingSearchBody, InFilingSearchBodyDict
from ..models.search_body import SearchBody, SearchBodyDict
from ..models.search_filter import SearchFilter
from ..models.search_response import SearchResponse
from ..server.server import Server


class GlobalFilings:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = GlobalFilingsWithRawResponse(client, server, auth)

    def global_filings_download(self, document_id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """<p>Download filings using document ids.</p>

        Args:
            document_id: Document's id. Note that this is different from filingId as 1 filing can contain multiple
                documents.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.global_filings_download(document_id, request_options=request_options).unwrap()

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
        return self._with_raw_response.global_filings_search(search=search, request_options=request_options).unwrap()

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
        return self._with_raw_response.global_filings_search_filter(
            field, source=source, request_options=request_options
        ).unwrap()

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
        return self._with_raw_response.search_in_filing(search=search, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> GlobalFilingsWithRawResponse:
        return self._with_raw_response


class AsyncGlobalFilings:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncGlobalFilingsWithRawResponse(client, server, auth)

    async def global_filings_download(
        self, document_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """<p>Download filings using document ids.</p>

        Args:
            document_id: Document's id. Note that this is different from filingId as 1 filing can contain multiple
                documents.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.global_filings_download(document_id, request_options=request_options)
        ).unwrap()

    async def global_filings_search(
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
        return (
            await self._with_raw_response.global_filings_search(search=search, request_options=request_options)
        ).unwrap()

    async def global_filings_search_filter(
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
        return (
            await self._with_raw_response.global_filings_search_filter(
                field, source=source, request_options=request_options
            )
        ).unwrap()

    async def search_in_filing(
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
        return (await self._with_raw_response.search_in_filing(search=search, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncGlobalFilingsWithRawResponse:
        return self._with_raw_response


class GlobalFilingsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
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
            headers=[param[UUID]("Idempotency-Key", uuid4())],
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
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[InFilingSearchBody | InFilingSearchBodyDict | None](search),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[InFilingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncGlobalFilingsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def global_filings_download(
        self, document_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """<p>Download filings using document ids.</p>

        Args:
            document_id: Document's id. Note that this is different from filingId as 1 filing can contain multiple
                documents.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/global-filings/download"),
            query_params=[param[str]("documentId", document_id)],
            auth_scheme=self._auth.api_key,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def global_filings_search(
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
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/global-filings/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchBody | SearchBodyDict | None](search),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[SearchResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def global_filings_search_filter(
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
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/global-filings/filter"),
            query_params=[param[str]("field", field), param[str | None]("source", source)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[SearchFilter],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_in_filing(
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
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/global-filings/search-in-filing"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[InFilingSearchBody | InFilingSearchBodyDict | None](search),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[InFilingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
