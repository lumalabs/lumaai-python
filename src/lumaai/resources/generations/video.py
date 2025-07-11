# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
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
from ...types.generations import video_create_params, video_modify_params, video_reframe_params

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
        model: Literal["ray-1-6", "ray-2", "ray-flash-2"],
        aspect_ratio: Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"] | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        concepts: Iterable[video_create_params.Concept] | NotGiven = NOT_GIVEN,
        duration: Union[Literal["5s", "9s"], str] | NotGiven = NOT_GIVEN,
        generation_type: Literal["video"] | NotGiven = NOT_GIVEN,
        keyframes: video_create_params.Keyframes | NotGiven = NOT_GIVEN,
        loop: bool | NotGiven = NOT_GIVEN,
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
          model: The model used for the generation

          aspect_ratio: The aspect ratio of the generation

          callback_url: The callback URL of the generation, a POST request with Generation object will
              be sent to the callback URL when the generation is dreaming, completed, or
              failed

          concepts: The concepts of the generation

          duration: The duration of the generation

          keyframes: The keyframes of the generation

          loop: Whether to loop the video

          prompt: The prompt of the generation

          resolution: The resolution of the generation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/generations/video",
            body=maybe_transform(
                {
                    "model": model,
                    "aspect_ratio": aspect_ratio,
                    "callback_url": callback_url,
                    "concepts": concepts,
                    "duration": duration,
                    "generation_type": generation_type,
                    "keyframes": keyframes,
                    "loop": loop,
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

    def modify(
        self,
        *,
        generation_type: Literal["modify_video"],
        media: video_modify_params.Media,
        mode: Literal[
            "adhere_1",
            "adhere_2",
            "adhere_3",
            "flex_1",
            "flex_2",
            "flex_3",
            "reimagine_1",
            "reimagine_2",
            "reimagine_3",
        ],
        model: Literal["ray-2", "ray-flash-2"],
        callback_url: str | NotGiven = NOT_GIVEN,
        first_frame: video_modify_params.FirstFrame | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Generation:
        """
        Modify a video with style transfer and prompt-based editing

        Args:
          media: The image entity object

          mode: The mode of the modify video

          model: The model used for the modify video

          callback_url: The callback URL of the generation, a POST request with Generation object will
              be sent to the callback URL when the generation is dreaming, completed, or
              failed

          first_frame: The image entity object

          prompt: The prompt of the generation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/generations/video/modify",
            body=maybe_transform(
                {
                    "generation_type": generation_type,
                    "media": media,
                    "mode": mode,
                    "model": model,
                    "callback_url": callback_url,
                    "first_frame": first_frame,
                    "prompt": prompt,
                },
                video_modify_params.VideoModifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Generation,
        )

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
        resized_height: int | NotGiven = NOT_GIVEN,
        resized_width: int | NotGiven = NOT_GIVEN,
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

          resized_height: Resized height of source video

          resized_width: Resized width of source video

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
                    "resized_height": resized_height,
                    "resized_width": resized_width,
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

    async def create(
        self,
        *,
        model: Literal["ray-1-6", "ray-2", "ray-flash-2"],
        aspect_ratio: Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"] | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        concepts: Iterable[video_create_params.Concept] | NotGiven = NOT_GIVEN,
        duration: Union[Literal["5s", "9s"], str] | NotGiven = NOT_GIVEN,
        generation_type: Literal["video"] | NotGiven = NOT_GIVEN,
        keyframes: video_create_params.Keyframes | NotGiven = NOT_GIVEN,
        loop: bool | NotGiven = NOT_GIVEN,
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
          model: The model used for the generation

          aspect_ratio: The aspect ratio of the generation

          callback_url: The callback URL of the generation, a POST request with Generation object will
              be sent to the callback URL when the generation is dreaming, completed, or
              failed

          concepts: The concepts of the generation

          duration: The duration of the generation

          keyframes: The keyframes of the generation

          loop: Whether to loop the video

          prompt: The prompt of the generation

          resolution: The resolution of the generation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/generations/video",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "aspect_ratio": aspect_ratio,
                    "callback_url": callback_url,
                    "concepts": concepts,
                    "duration": duration,
                    "generation_type": generation_type,
                    "keyframes": keyframes,
                    "loop": loop,
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

    async def modify(
        self,
        *,
        generation_type: Literal["modify_video"],
        media: video_modify_params.Media,
        mode: Literal[
            "adhere_1",
            "adhere_2",
            "adhere_3",
            "flex_1",
            "flex_2",
            "flex_3",
            "reimagine_1",
            "reimagine_2",
            "reimagine_3",
        ],
        model: Literal["ray-2", "ray-flash-2"],
        callback_url: str | NotGiven = NOT_GIVEN,
        first_frame: video_modify_params.FirstFrame | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Generation:
        """
        Modify a video with style transfer and prompt-based editing

        Args:
          media: The image entity object

          mode: The mode of the modify video

          model: The model used for the modify video

          callback_url: The callback URL of the generation, a POST request with Generation object will
              be sent to the callback URL when the generation is dreaming, completed, or
              failed

          first_frame: The image entity object

          prompt: The prompt of the generation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/generations/video/modify",
            body=await async_maybe_transform(
                {
                    "generation_type": generation_type,
                    "media": media,
                    "mode": mode,
                    "model": model,
                    "callback_url": callback_url,
                    "first_frame": first_frame,
                    "prompt": prompt,
                },
                video_modify_params.VideoModifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Generation,
        )

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
        resized_height: int | NotGiven = NOT_GIVEN,
        resized_width: int | NotGiven = NOT_GIVEN,
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

          resized_height: Resized height of source video

          resized_width: Resized width of source video

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
                    "resized_height": resized_height,
                    "resized_width": resized_width,
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

        self.create = to_raw_response_wrapper(
            video.create,
        )
        self.modify = to_raw_response_wrapper(
            video.modify,
        )
        self.reframe = to_raw_response_wrapper(
            video.reframe,
        )


class AsyncVideoResourceWithRawResponse:
    def __init__(self, video: AsyncVideoResource) -> None:
        self._video = video

        self.create = async_to_raw_response_wrapper(
            video.create,
        )
        self.modify = async_to_raw_response_wrapper(
            video.modify,
        )
        self.reframe = async_to_raw_response_wrapper(
            video.reframe,
        )


class VideoResourceWithStreamingResponse:
    def __init__(self, video: VideoResource) -> None:
        self._video = video

        self.create = to_streamed_response_wrapper(
            video.create,
        )
        self.modify = to_streamed_response_wrapper(
            video.modify,
        )
        self.reframe = to_streamed_response_wrapper(
            video.reframe,
        )


class AsyncVideoResourceWithStreamingResponse:
    def __init__(self, video: AsyncVideoResource) -> None:
        self._video = video

        self.create = async_to_streamed_response_wrapper(
            video.create,
        )
        self.modify = async_to_streamed_response_wrapper(
            video.modify,
        )
        self.reframe = async_to_streamed_response_wrapper(
            video.reframe,
        )
