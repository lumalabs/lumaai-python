# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.generations.concept_list_response import ConceptListResponse

__all__ = ["ConceptsResource", "AsyncConceptsResource"]


class ConceptsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConceptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lumalabs/lumaai-python#accessing-raw-response-data-eg-headers
        """
        return ConceptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConceptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lumalabs/lumaai-python#with_streaming_response
        """
        return ConceptsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConceptListResponse:
        """Get all possible concepts"""
        return self._get(
            "/generations/concepts/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConceptListResponse,
        )


class AsyncConceptsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConceptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lumalabs/lumaai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConceptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConceptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lumalabs/lumaai-python#with_streaming_response
        """
        return AsyncConceptsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConceptListResponse:
        """Get all possible concepts"""
        return await self._get(
            "/generations/concepts/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConceptListResponse,
        )


class ConceptsResourceWithRawResponse:
    def __init__(self, concepts: ConceptsResource) -> None:
        self._concepts = concepts

        self.list = to_raw_response_wrapper(
            concepts.list,
        )


class AsyncConceptsResourceWithRawResponse:
    def __init__(self, concepts: AsyncConceptsResource) -> None:
        self._concepts = concepts

        self.list = async_to_raw_response_wrapper(
            concepts.list,
        )


class ConceptsResourceWithStreamingResponse:
    def __init__(self, concepts: ConceptsResource) -> None:
        self._concepts = concepts

        self.list = to_streamed_response_wrapper(
            concepts.list,
        )


class AsyncConceptsResourceWithStreamingResponse:
    def __init__(self, concepts: AsyncConceptsResource) -> None:
        self._concepts = concepts

        self.list = async_to_streamed_response_wrapper(
            concepts.list,
        )
