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
from ...types.generations.camera_motion_list_response import CameraMotionListResponse

__all__ = ["CameraMotionResource", "AsyncCameraMotionResource"]


class CameraMotionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CameraMotionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lumalabs/lumaai-python#accessing-raw-response-data-eg-headers
        """
        return CameraMotionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CameraMotionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lumalabs/lumaai-python#with_streaming_response
        """
        return CameraMotionResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CameraMotionListResponse:
        """Get all possible camera motions"""
        return self._get(
            "/generations/camera_motion/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CameraMotionListResponse,
        )


class AsyncCameraMotionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCameraMotionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lumalabs/lumaai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCameraMotionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCameraMotionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lumalabs/lumaai-python#with_streaming_response
        """
        return AsyncCameraMotionResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CameraMotionListResponse:
        """Get all possible camera motions"""
        return await self._get(
            "/generations/camera_motion/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CameraMotionListResponse,
        )


class CameraMotionResourceWithRawResponse:
    def __init__(self, camera_motion: CameraMotionResource) -> None:
        self._camera_motion = camera_motion

        self.list = to_raw_response_wrapper(
            camera_motion.list,
        )


class AsyncCameraMotionResourceWithRawResponse:
    def __init__(self, camera_motion: AsyncCameraMotionResource) -> None:
        self._camera_motion = camera_motion

        self.list = async_to_raw_response_wrapper(
            camera_motion.list,
        )


class CameraMotionResourceWithStreamingResponse:
    def __init__(self, camera_motion: CameraMotionResource) -> None:
        self._camera_motion = camera_motion

        self.list = to_streamed_response_wrapper(
            camera_motion.list,
        )


class AsyncCameraMotionResourceWithStreamingResponse:
    def __init__(self, camera_motion: AsyncCameraMotionResource) -> None:
        self._camera_motion = camera_motion

        self.list = async_to_streamed_response_wrapper(
            camera_motion.list,
        )
