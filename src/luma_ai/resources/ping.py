# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.ping_retrieve_response import PingRetrieveResponse

__all__ = ["PingResource", "AsyncPingResource"]


class PingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/luma_ai-python#accessing-raw-response-data-eg-headers
        """
        return PingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/luma_ai-python#with_streaming_response
        """
        return PingResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PingRetrieveResponse:
        """Check if the API is running"""
        return self._get(
            "/ping",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PingRetrieveResponse,
        )


class AsyncPingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/luma_ai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/luma_ai-python#with_streaming_response
        """
        return AsyncPingResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PingRetrieveResponse:
        """Check if the API is running"""
        return await self._get(
            "/ping",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PingRetrieveResponse,
        )


class PingResourceWithRawResponse:
    def __init__(self, ping: PingResource) -> None:
        self._ping = ping

        self.retrieve = to_raw_response_wrapper(
            ping.retrieve,
        )


class AsyncPingResourceWithRawResponse:
    def __init__(self, ping: AsyncPingResource) -> None:
        self._ping = ping

        self.retrieve = async_to_raw_response_wrapper(
            ping.retrieve,
        )


class PingResourceWithStreamingResponse:
    def __init__(self, ping: PingResource) -> None:
        self._ping = ping

        self.retrieve = to_streamed_response_wrapper(
            ping.retrieve,
        )


class AsyncPingResourceWithStreamingResponse:
    def __init__(self, ping: AsyncPingResource) -> None:
        self._ping = ping

        self.retrieve = async_to_streamed_response_wrapper(
            ping.retrieve,
        )
