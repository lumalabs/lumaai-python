# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
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
from ...types.generations import image_create_params

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
        aspect_ratio: Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"] | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        character_ref: image_create_params.CharacterRef | NotGiven = NOT_GIVEN,
        generation_type: Literal["image"] | NotGiven = NOT_GIVEN,
        image_ref: Iterable[image_create_params.ImageRef] | NotGiven = NOT_GIVEN,
        model: Literal["photon-1", "photon-flash-1"] | NotGiven = NOT_GIVEN,
        modify_image_ref: image_create_params.ModifyImageRef | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        style_ref: Iterable[image_create_params.StyleRef] | NotGiven = NOT_GIVEN,
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
          aspect_ratio: The aspect ratio of the generation

          callback_url: The callback URL for the generation

          model: The model used for the generation

          modify_image_ref: The modify image reference object

          prompt: The prompt of the generation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/generations/image",
            body=maybe_transform(
                {
                    "aspect_ratio": aspect_ratio,
                    "callback_url": callback_url,
                    "character_ref": character_ref,
                    "generation_type": generation_type,
                    "image_ref": image_ref,
                    "model": model,
                    "modify_image_ref": modify_image_ref,
                    "prompt": prompt,
                    "style_ref": style_ref,
                },
                image_create_params.ImageCreateParams,
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
        aspect_ratio: Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"] | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        character_ref: image_create_params.CharacterRef | NotGiven = NOT_GIVEN,
        generation_type: Literal["image"] | NotGiven = NOT_GIVEN,
        image_ref: Iterable[image_create_params.ImageRef] | NotGiven = NOT_GIVEN,
        model: Literal["photon-1", "photon-flash-1"] | NotGiven = NOT_GIVEN,
        modify_image_ref: image_create_params.ModifyImageRef | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        style_ref: Iterable[image_create_params.StyleRef] | NotGiven = NOT_GIVEN,
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
          aspect_ratio: The aspect ratio of the generation

          callback_url: The callback URL for the generation

          model: The model used for the generation

          modify_image_ref: The modify image reference object

          prompt: The prompt of the generation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/generations/image",
            body=await async_maybe_transform(
                {
                    "aspect_ratio": aspect_ratio,
                    "callback_url": callback_url,
                    "character_ref": character_ref,
                    "generation_type": generation_type,
                    "image_ref": image_ref,
                    "model": model,
                    "modify_image_ref": modify_image_ref,
                    "prompt": prompt,
                    "style_ref": style_ref,
                },
                image_create_params.ImageCreateParams,
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


class AsyncImageResourceWithRawResponse:
    def __init__(self, image: AsyncImageResource) -> None:
        self._image = image

        self.create = async_to_raw_response_wrapper(
            image.create,
        )


class ImageResourceWithStreamingResponse:
    def __init__(self, image: ImageResource) -> None:
        self._image = image

        self.create = to_streamed_response_wrapper(
            image.create,
        )


class AsyncImageResourceWithStreamingResponse:
    def __init__(self, image: AsyncImageResource) -> None:
        self._image = image

        self.create = async_to_streamed_response_wrapper(
            image.create,
        )
