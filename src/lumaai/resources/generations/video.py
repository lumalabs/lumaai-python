# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.generation import Generation
from ...types.generations import video_create_params

__all__ = ["VideoResource", "AsyncVideoResource"]


class VideoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VideoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lumalabs/lumaai-python#accessing-raw-response-data-eg-headers
        """
        return VideoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lumalabs/lumaai-python#with_streaming_response
        """
        return VideoResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        aspect_ratio: Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"] | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        duration: Union[Literal["5s", "9s"], str] | NotGiven = NOT_GIVEN,
        generation_type: Literal["video"] | NotGiven = NOT_GIVEN,
        keyframes: video_create_params.Keyframes | NotGiven = NOT_GIVEN,
        loop: bool | NotGiven = NOT_GIVEN,
        model: Literal["ray-1-6", "ray-2", "ray-flash-2"] | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        resolution: Union[Literal["540p", "720p", "1080p", "4k"], str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Generation:
        """
        Initiate a new generation with the provided prompt

        Args:
          aspect_ratio: The aspect ratio of the generation

          callback_url: The callback URL of the generation, a POST request with Generation object will
              be sent to the callback URL when the generation is dreaming, completed, or
              failed

          duration: The duration of the generation

          keyframes: The keyframes of the generation

          loop: Whether to loop the video

          model: The model used for the generation

          prompt: The prompt of the generation

          resolution: The resolution of the generation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/generations",
            body=maybe_transform(
                {
                    "aspect_ratio": aspect_ratio,
                    "callback_url": callback_url,
                    "duration": duration,
                    "generation_type": generation_type,
                    "keyframes": keyframes,
                    "loop": loop,
                    "model": model,
                    "prompt": prompt,
                    "resolution": resolution,
                },
                video_create_params.VideoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Generation,
        )


class AsyncVideoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVideoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lumalabs/lumaai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVideoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lumalabs/lumaai-python#with_streaming_response
        """
        return AsyncVideoResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        aspect_ratio: Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"] | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        duration: Union[Literal["5s", "9s"], str] | NotGiven = NOT_GIVEN,
        generation_type: Literal["video"] | NotGiven = NOT_GIVEN,
        keyframes: video_create_params.Keyframes | NotGiven = NOT_GIVEN,
        loop: bool | NotGiven = NOT_GIVEN,
        model: Literal["ray-1-6", "ray-2", "ray-flash-2"] | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        resolution: Union[Literal["540p", "720p", "1080p", "4k"], str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Generation:
        """
        Initiate a new generation with the provided prompt

        Args:
          aspect_ratio: The aspect ratio of the generation

          callback_url: The callback URL of the generation, a POST request with Generation object will
              be sent to the callback URL when the generation is dreaming, completed, or
              failed

          duration: The duration of the generation

          keyframes: The keyframes of the generation

          loop: Whether to loop the video

          model: The model used for the generation

          prompt: The prompt of the generation

          resolution: The resolution of the generation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/generations",
            body=await async_maybe_transform(
                {
                    "aspect_ratio": aspect_ratio,
                    "callback_url": callback_url,
                    "duration": duration,
                    "generation_type": generation_type,
                    "keyframes": keyframes,
                    "loop": loop,
                    "model": model,
                    "prompt": prompt,
                    "resolution": resolution,
                },
                video_create_params.VideoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Generation,
        )


class VideoResourceWithRawResponse:
    def __init__(self, video: VideoResource) -> None:
        self._video = video

        self.create = to_raw_response_wrapper(
            video.create,
        )


class AsyncVideoResourceWithRawResponse:
    def __init__(self, video: AsyncVideoResource) -> None:
        self._video = video

        self.create = async_to_raw_response_wrapper(
            video.create,
        )


class VideoResourceWithStreamingResponse:
    def __init__(self, video: VideoResource) -> None:
        self._video = video

        self.create = to_streamed_response_wrapper(
            video.create,
        )


class AsyncVideoResourceWithStreamingResponse:
    def __init__(self, video: AsyncVideoResource) -> None:
        self._video = video

        self.create = async_to_streamed_response_wrapper(
            video.create,
        )
