# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
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
from ...types.generations import image_create_params, image_reframe_params

__all__ = ["ImageResource", "AsyncImageResource"]


class ImageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ImageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lumalabs/lumaai-python#accessing-raw-response-data-eg-headers
        """
        return ImageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lumalabs/lumaai-python#with_streaming_response
        """
        return ImageResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model: Literal["photon-1", "photon-flash-1"],
        aspect_ratio: Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"] | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        character_ref: image_create_params.CharacterRef | NotGiven = NOT_GIVEN,
        format: Literal["jpg", "png"] | NotGiven = NOT_GIVEN,
        generation_type: Literal["image"] | NotGiven = NOT_GIVEN,
        image_ref: Iterable[image_create_params.ImageRef] | NotGiven = NOT_GIVEN,
        modify_image_ref: image_create_params.ModifyImageRef | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        style_ref: Iterable[image_create_params.StyleRef] | NotGiven = NOT_GIVEN,
        sync: bool | NotGiven = NOT_GIVEN,
        sync_timeout: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Generation:
        """
        Generate an image with the provided prompt

        Args:
          model: The model used for the generation

          aspect_ratio: The aspect ratio of the generation

          callback_url: The callback URL for the generation

          format: The format of the image

          modify_image_ref: The modify image reference object

          prompt: The prompt of the generation

          sync: Create image in synchronous mode and return complated image

          sync_timeout: The timeout for the synchronous image generation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/generations/image",
            body=maybe_transform(
                {
                    "model": model,
                    "aspect_ratio": aspect_ratio,
                    "callback_url": callback_url,
                    "character_ref": character_ref,
                    "format": format,
                    "generation_type": generation_type,
                    "image_ref": image_ref,
                    "modify_image_ref": modify_image_ref,
                    "prompt": prompt,
                    "style_ref": style_ref,
                    "sync": sync,
                    "sync_timeout": sync_timeout,
                },
                image_create_params.ImageCreateParams,
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
        generation_type: Literal["reframe_image"],
        media: image_reframe_params.Media,
        model: Literal["photon-1", "photon-flash-1"],
        callback_url: str | NotGiven = NOT_GIVEN,
        format: Literal["jpg", "png"] | NotGiven = NOT_GIVEN,
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
        Reframe an image by its ID

        Args:
          aspect_ratio: The aspect ratio of the generation

          media: The image entity object

          model: The model used for the reframe image

          callback_url: The callback URL of the generation, a POST request with Generation object will
              be sent to the callback URL when the generation is dreaming, completed, or
              failed

          format: The format of the image

          grid_position_x: The x position of the image in the grid

          grid_position_y: The y position of the image in the grid

          prompt: The prompt of the generation

          resized_height: Resized height of source image

          resized_width: Resized width of source image

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
            "/generations/image/reframe",
            body=maybe_transform(
                {
                    "aspect_ratio": aspect_ratio,
                    "generation_type": generation_type,
                    "media": media,
                    "model": model,
                    "callback_url": callback_url,
                    "format": format,
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
                image_reframe_params.ImageReframeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Generation,
        )


class AsyncImageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncImageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lumalabs/lumaai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lumalabs/lumaai-python#with_streaming_response
        """
        return AsyncImageResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model: Literal["photon-1", "photon-flash-1"],
        aspect_ratio: Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"] | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        character_ref: image_create_params.CharacterRef | NotGiven = NOT_GIVEN,
        format: Literal["jpg", "png"] | NotGiven = NOT_GIVEN,
        generation_type: Literal["image"] | NotGiven = NOT_GIVEN,
        image_ref: Iterable[image_create_params.ImageRef] | NotGiven = NOT_GIVEN,
        modify_image_ref: image_create_params.ModifyImageRef | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        style_ref: Iterable[image_create_params.StyleRef] | NotGiven = NOT_GIVEN,
        sync: bool | NotGiven = NOT_GIVEN,
        sync_timeout: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Generation:
        """
        Generate an image with the provided prompt

        Args:
          model: The model used for the generation

          aspect_ratio: The aspect ratio of the generation

          callback_url: The callback URL for the generation

          format: The format of the image

          modify_image_ref: The modify image reference object

          prompt: The prompt of the generation

          sync: Create image in synchronous mode and return complated image

          sync_timeout: The timeout for the synchronous image generation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/generations/image",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "aspect_ratio": aspect_ratio,
                    "callback_url": callback_url,
                    "character_ref": character_ref,
                    "format": format,
                    "generation_type": generation_type,
                    "image_ref": image_ref,
                    "modify_image_ref": modify_image_ref,
                    "prompt": prompt,
                    "style_ref": style_ref,
                    "sync": sync,
                    "sync_timeout": sync_timeout,
                },
                image_create_params.ImageCreateParams,
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
        generation_type: Literal["reframe_image"],
        media: image_reframe_params.Media,
        model: Literal["photon-1", "photon-flash-1"],
        callback_url: str | NotGiven = NOT_GIVEN,
        format: Literal["jpg", "png"] | NotGiven = NOT_GIVEN,
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
        Reframe an image by its ID

        Args:
          aspect_ratio: The aspect ratio of the generation

          media: The image entity object

          model: The model used for the reframe image

          callback_url: The callback URL of the generation, a POST request with Generation object will
              be sent to the callback URL when the generation is dreaming, completed, or
              failed

          format: The format of the image

          grid_position_x: The x position of the image in the grid

          grid_position_y: The y position of the image in the grid

          prompt: The prompt of the generation

          resized_height: Resized height of source image

          resized_width: Resized width of source image

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
            "/generations/image/reframe",
            body=await async_maybe_transform(
                {
                    "aspect_ratio": aspect_ratio,
                    "generation_type": generation_type,
                    "media": media,
                    "model": model,
                    "callback_url": callback_url,
                    "format": format,
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
                image_reframe_params.ImageReframeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Generation,
        )


class ImageResourceWithRawResponse:
    def __init__(self, image: ImageResource) -> None:
        self._image = image

        self.create = to_raw_response_wrapper(
            image.create,
        )
        self.reframe = to_raw_response_wrapper(
            image.reframe,
        )


class AsyncImageResourceWithRawResponse:
    def __init__(self, image: AsyncImageResource) -> None:
        self._image = image

        self.create = async_to_raw_response_wrapper(
            image.create,
        )
        self.reframe = async_to_raw_response_wrapper(
            image.reframe,
        )


class ImageResourceWithStreamingResponse:
    def __init__(self, image: ImageResource) -> None:
        self._image = image

        self.create = to_streamed_response_wrapper(
            image.create,
        )
        self.reframe = to_streamed_response_wrapper(
            image.reframe,
        )


class AsyncImageResourceWithStreamingResponse:
    def __init__(self, image: AsyncImageResource) -> None:
        self._image = image

        self.create = async_to_streamed_response_wrapper(
            image.create,
        )
        self.reframe = async_to_streamed_response_wrapper(
            image.reframe,
        )
