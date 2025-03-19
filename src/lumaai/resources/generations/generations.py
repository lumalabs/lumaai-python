# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal

import httpx

from .image import (
    ImageResource,
    AsyncImageResource,
    ImageResourceWithRawResponse,
    AsyncImageResourceWithRawResponse,
    ImageResourceWithStreamingResponse,
    AsyncImageResourceWithStreamingResponse,
)
from .video import (
    VideoResource,
    AsyncVideoResource,
    VideoResourceWithRawResponse,
    AsyncVideoResourceWithRawResponse,
    VideoResourceWithStreamingResponse,
    AsyncVideoResourceWithStreamingResponse,
)
from ...types import (
    generation_list_params,
    generation_audio_params,
    generation_create_params,
    generation_upscale_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from .camera_motion import (
    CameraMotionResource,
    AsyncCameraMotionResource,
    CameraMotionResourceWithRawResponse,
    AsyncCameraMotionResourceWithRawResponse,
    CameraMotionResourceWithStreamingResponse,
    AsyncCameraMotionResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.generation import Generation
from ...types.generation_list_response import GenerationListResponse

__all__ = ["GenerationsResource", "AsyncGenerationsResource"]


class GenerationsResource(SyncAPIResource):
    @cached_property
    def camera_motion(self) -> CameraMotionResource:
        return CameraMotionResource(self._client)

    @cached_property
    def image(self) -> ImageResource:
        return ImageResource(self._client)

    @cached_property
    def video(self) -> VideoResource:
        return VideoResource(self._client)

    @cached_property
    def with_raw_response(self) -> GenerationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lumalabs/lumaai-python#accessing-raw-response-data-eg-headers
        """
        return GenerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lumalabs/lumaai-python#with_streaming_response
        """
        return GenerationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        aspect_ratio: Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"] | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        duration: Union[Literal["5s", "9s"], str] | NotGiven = NOT_GIVEN,
        generation_type: Literal["video"] | NotGiven = NOT_GIVEN,
        keyframes: generation_create_params.Keyframes | NotGiven = NOT_GIVEN,
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
                generation_create_params.GenerationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Generation,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationListResponse:
        """
        Retrieve a list of generations with optional filtering and sorting

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/generations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    generation_list_params.GenerationListParams,
                ),
            ),
            cast_to=GenerationListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Remove a specific generation by its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/generations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def audio(
        self,
        id: str,
        *,
        callback_url: str | NotGiven = NOT_GIVEN,
        generation_type: Literal["add_audio"] | NotGiven = NOT_GIVEN,
        negative_prompt: str | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Generation:
        """
        Add audio to a generation by its ID

        Args:
          callback_url: The callback URL for the audio

          negative_prompt: The negative prompt of the audio

          prompt: The prompt of the audio

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/generations/{id}/audio",
            body=maybe_transform(
                {
                    "callback_url": callback_url,
                    "generation_type": generation_type,
                    "negative_prompt": negative_prompt,
                    "prompt": prompt,
                },
                generation_audio_params.GenerationAudioParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Generation,
        )

    def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Generation:
        """
        Retrieve details of a specific generation by its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/generations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Generation,
        )

    def upscale(
        self,
        id: str,
        *,
        callback_url: str | NotGiven = NOT_GIVEN,
        generation_type: Literal["upscale_video"] | NotGiven = NOT_GIVEN,
        resolution: Union[Literal["540p", "720p", "1080p", "4k"], str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Generation:
        """
        Upscale a generation by its ID

        Args:
          callback_url: The callback URL for the upscale

          resolution: The resolution of the upscale

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/generations/{id}/upscale",
            body=maybe_transform(
                {
                    "callback_url": callback_url,
                    "generation_type": generation_type,
                    "resolution": resolution,
                },
                generation_upscale_params.GenerationUpscaleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Generation,
        )


class AsyncGenerationsResource(AsyncAPIResource):
    @cached_property
    def camera_motion(self) -> AsyncCameraMotionResource:
        return AsyncCameraMotionResource(self._client)

    @cached_property
    def image(self) -> AsyncImageResource:
        return AsyncImageResource(self._client)

    @cached_property
    def video(self) -> AsyncVideoResource:
        return AsyncVideoResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGenerationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lumalabs/lumaai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lumalabs/lumaai-python#with_streaming_response
        """
        return AsyncGenerationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        aspect_ratio: Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"] | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        duration: Union[Literal["5s", "9s"], str] | NotGiven = NOT_GIVEN,
        generation_type: Literal["video"] | NotGiven = NOT_GIVEN,
        keyframes: generation_create_params.Keyframes | NotGiven = NOT_GIVEN,
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
                generation_create_params.GenerationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Generation,
        )

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationListResponse:
        """
        Retrieve a list of generations with optional filtering and sorting

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/generations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    generation_list_params.GenerationListParams,
                ),
            ),
            cast_to=GenerationListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Remove a specific generation by its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/generations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def audio(
        self,
        id: str,
        *,
        callback_url: str | NotGiven = NOT_GIVEN,
        generation_type: Literal["add_audio"] | NotGiven = NOT_GIVEN,
        negative_prompt: str | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Generation:
        """
        Add audio to a generation by its ID

        Args:
          callback_url: The callback URL for the audio

          negative_prompt: The negative prompt of the audio

          prompt: The prompt of the audio

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/generations/{id}/audio",
            body=await async_maybe_transform(
                {
                    "callback_url": callback_url,
                    "generation_type": generation_type,
                    "negative_prompt": negative_prompt,
                    "prompt": prompt,
                },
                generation_audio_params.GenerationAudioParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Generation,
        )

    async def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Generation:
        """
        Retrieve details of a specific generation by its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/generations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Generation,
        )

    async def upscale(
        self,
        id: str,
        *,
        callback_url: str | NotGiven = NOT_GIVEN,
        generation_type: Literal["upscale_video"] | NotGiven = NOT_GIVEN,
        resolution: Union[Literal["540p", "720p", "1080p", "4k"], str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Generation:
        """
        Upscale a generation by its ID

        Args:
          callback_url: The callback URL for the upscale

          resolution: The resolution of the upscale

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/generations/{id}/upscale",
            body=await async_maybe_transform(
                {
                    "callback_url": callback_url,
                    "generation_type": generation_type,
                    "resolution": resolution,
                },
                generation_upscale_params.GenerationUpscaleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Generation,
        )


class GenerationsResourceWithRawResponse:
    def __init__(self, generations: GenerationsResource) -> None:
        self._generations = generations

        self.create = to_raw_response_wrapper(
            generations.create,
        )
        self.list = to_raw_response_wrapper(
            generations.list,
        )
        self.delete = to_raw_response_wrapper(
            generations.delete,
        )
        self.audio = to_raw_response_wrapper(
            generations.audio,
        )
        self.get = to_raw_response_wrapper(
            generations.get,
        )
        self.upscale = to_raw_response_wrapper(
            generations.upscale,
        )

    @cached_property
    def camera_motion(self) -> CameraMotionResourceWithRawResponse:
        return CameraMotionResourceWithRawResponse(self._generations.camera_motion)

    @cached_property
    def image(self) -> ImageResourceWithRawResponse:
        return ImageResourceWithRawResponse(self._generations.image)

    @cached_property
    def video(self) -> VideoResourceWithRawResponse:
        return VideoResourceWithRawResponse(self._generations.video)


class AsyncGenerationsResourceWithRawResponse:
    def __init__(self, generations: AsyncGenerationsResource) -> None:
        self._generations = generations

        self.create = async_to_raw_response_wrapper(
            generations.create,
        )
        self.list = async_to_raw_response_wrapper(
            generations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            generations.delete,
        )
        self.audio = async_to_raw_response_wrapper(
            generations.audio,
        )
        self.get = async_to_raw_response_wrapper(
            generations.get,
        )
        self.upscale = async_to_raw_response_wrapper(
            generations.upscale,
        )

    @cached_property
    def camera_motion(self) -> AsyncCameraMotionResourceWithRawResponse:
        return AsyncCameraMotionResourceWithRawResponse(self._generations.camera_motion)

    @cached_property
    def image(self) -> AsyncImageResourceWithRawResponse:
        return AsyncImageResourceWithRawResponse(self._generations.image)

    @cached_property
    def video(self) -> AsyncVideoResourceWithRawResponse:
        return AsyncVideoResourceWithRawResponse(self._generations.video)


class GenerationsResourceWithStreamingResponse:
    def __init__(self, generations: GenerationsResource) -> None:
        self._generations = generations

        self.create = to_streamed_response_wrapper(
            generations.create,
        )
        self.list = to_streamed_response_wrapper(
            generations.list,
        )
        self.delete = to_streamed_response_wrapper(
            generations.delete,
        )
        self.audio = to_streamed_response_wrapper(
            generations.audio,
        )
        self.get = to_streamed_response_wrapper(
            generations.get,
        )
        self.upscale = to_streamed_response_wrapper(
            generations.upscale,
        )

    @cached_property
    def camera_motion(self) -> CameraMotionResourceWithStreamingResponse:
        return CameraMotionResourceWithStreamingResponse(self._generations.camera_motion)

    @cached_property
    def image(self) -> ImageResourceWithStreamingResponse:
        return ImageResourceWithStreamingResponse(self._generations.image)

    @cached_property
    def video(self) -> VideoResourceWithStreamingResponse:
        return VideoResourceWithStreamingResponse(self._generations.video)


class AsyncGenerationsResourceWithStreamingResponse:
    def __init__(self, generations: AsyncGenerationsResource) -> None:
        self._generations = generations

        self.create = async_to_streamed_response_wrapper(
            generations.create,
        )
        self.list = async_to_streamed_response_wrapper(
            generations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            generations.delete,
        )
        self.audio = async_to_streamed_response_wrapper(
            generations.audio,
        )
        self.get = async_to_streamed_response_wrapper(
            generations.get,
        )
        self.upscale = async_to_streamed_response_wrapper(
            generations.upscale,
        )

    @cached_property
    def camera_motion(self) -> AsyncCameraMotionResourceWithStreamingResponse:
        return AsyncCameraMotionResourceWithStreamingResponse(self._generations.camera_motion)

    @cached_property
    def image(self) -> AsyncImageResourceWithStreamingResponse:
        return AsyncImageResourceWithStreamingResponse(self._generations.image)

    @cached_property
    def video(self) -> AsyncVideoResourceWithStreamingResponse:
        return AsyncVideoResourceWithStreamingResponse(self._generations.video)
