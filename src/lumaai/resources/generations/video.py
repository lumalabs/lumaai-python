# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
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
from ...types.generations import video_reframe_params

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

    def reframe(
        self,
        *,
        aspect_ratio: Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"],
        generation_type: Literal["reframe_video"],
        media: video_reframe_params.Media,
        model: Literal["ray-2", "ray-flash-2"],
        callback_url: str | NotGiven = NOT_GIVEN,
        first_frame: video_reframe_params.FirstFrame | NotGiven = NOT_GIVEN,
        grid_position_x: int | NotGiven = NOT_GIVEN,
        grid_position_y: int | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        x_end: int | NotGiven = NOT_GIVEN,
        x_start: int | NotGiven = NOT_GIVEN,
        y_end: int | NotGiven = NOT_GIVEN,
        y_start: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Generation:
        """
        Reframe a video by its ID

        Args:
          aspect_ratio: The aspect ratio of the generation

          media: The image entity object

          model: The model used for the reframe video

          callback_url: The callback URL of the generation, a POST request with Generation object will
              be sent to the callback URL when the generation is dreaming, completed, or
              failed

          first_frame: The image entity object

          grid_position_x: The x position of the image in the grid

          grid_position_y: The y position of the image in the grid

          prompt: The prompt of the generation

          x_end: The x end of the crop bounds

          x_start: The x start of the crop bounds

          y_end: The y end of the crop bounds

          y_start: The y start of the crop bounds

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/generations/video/reframe",
            body=maybe_transform(
                {
                    "aspect_ratio": aspect_ratio,
                    "generation_type": generation_type,
                    "media": media,
                    "model": model,
                    "callback_url": callback_url,
                    "first_frame": first_frame,
                    "grid_position_x": grid_position_x,
                    "grid_position_y": grid_position_y,
                    "prompt": prompt,
                    "x_end": x_end,
                    "x_start": x_start,
                    "y_end": y_end,
                    "y_start": y_start,
                },
                video_reframe_params.VideoReframeParams,
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

    async def reframe(
        self,
        *,
        aspect_ratio: Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"],
        generation_type: Literal["reframe_video"],
        media: video_reframe_params.Media,
        model: Literal["ray-2", "ray-flash-2"],
        callback_url: str | NotGiven = NOT_GIVEN,
        first_frame: video_reframe_params.FirstFrame | NotGiven = NOT_GIVEN,
        grid_position_x: int | NotGiven = NOT_GIVEN,
        grid_position_y: int | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        x_end: int | NotGiven = NOT_GIVEN,
        x_start: int | NotGiven = NOT_GIVEN,
        y_end: int | NotGiven = NOT_GIVEN,
        y_start: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Generation:
        """
        Reframe a video by its ID

        Args:
          aspect_ratio: The aspect ratio of the generation

          media: The image entity object

          model: The model used for the reframe video

          callback_url: The callback URL of the generation, a POST request with Generation object will
              be sent to the callback URL when the generation is dreaming, completed, or
              failed

          first_frame: The image entity object

          grid_position_x: The x position of the image in the grid

          grid_position_y: The y position of the image in the grid

          prompt: The prompt of the generation

          x_end: The x end of the crop bounds

          x_start: The x start of the crop bounds

          y_end: The y end of the crop bounds

          y_start: The y start of the crop bounds

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/generations/video/reframe",
            body=await async_maybe_transform(
                {
                    "aspect_ratio": aspect_ratio,
                    "generation_type": generation_type,
                    "media": media,
                    "model": model,
                    "callback_url": callback_url,
                    "first_frame": first_frame,
                    "grid_position_x": grid_position_x,
                    "grid_position_y": grid_position_y,
                    "prompt": prompt,
                    "x_end": x_end,
                    "x_start": x_start,
                    "y_end": y_end,
                    "y_start": y_start,
                },
                video_reframe_params.VideoReframeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Generation,
        )


class VideoResourceWithRawResponse:
    def __init__(self, video: VideoResource) -> None:
        self._video = video

        self.reframe = to_raw_response_wrapper(
            video.reframe,
        )


class AsyncVideoResourceWithRawResponse:
    def __init__(self, video: AsyncVideoResource) -> None:
        self._video = video

        self.reframe = async_to_raw_response_wrapper(
            video.reframe,
        )


class VideoResourceWithStreamingResponse:
    def __init__(self, video: VideoResource) -> None:
        self._video = video

        self.reframe = to_streamed_response_wrapper(
            video.reframe,
        )


class AsyncVideoResourceWithStreamingResponse:
    def __init__(self, video: AsyncVideoResource) -> None:
        self._video = video

        self.reframe = async_to_streamed_response_wrapper(
            video.reframe,
        )
