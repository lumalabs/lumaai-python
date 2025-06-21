# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lumaai import LumaAI, AsyncLumaAI
from tests.utils import assert_matches_type
from lumaai.types import Generation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestImage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LumaAI) -> None:
        image = client.generations.image.create(
            model="photon-1",
        )
        assert_matches_type(Generation, image, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LumaAI) -> None:
        image = client.generations.image.create(
            model="photon-1",
            aspect_ratio="16:9",
            callback_url="https://example.com",
            character_ref={"identity0": {"images": ["https://example.com"]}},
            format="jpg",
            generation_type="image",
            image_ref=[
                {
                    "url": "https://example.com",
                    "weight": 0,
                }
            ],
            modify_image_ref={
                "url": "https://example.com",
                "weight": 0,
            },
            prompt="prompt",
            style_ref=[
                {
                    "url": "https://example.com",
                    "weight": 0,
                }
            ],
            sync=True,
            sync_timeout=0,
        )
        assert_matches_type(Generation, image, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LumaAI) -> None:
        response = client.generations.image.with_raw_response.create(
            model="photon-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(Generation, image, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LumaAI) -> None:
        with client.generations.image.with_streaming_response.create(
            model="photon-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(Generation, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_reframe(self, client: LumaAI) -> None:
        image = client.generations.image.reframe(
            aspect_ratio="16:9",
            generation_type="reframe_image",
            media={"url": "https://example.com"},
            model="photon-1",
        )
        assert_matches_type(Generation, image, path=["response"])

    @parametrize
    def test_method_reframe_with_all_params(self, client: LumaAI) -> None:
        image = client.generations.image.reframe(
            aspect_ratio="16:9",
            generation_type="reframe_image",
            media={"url": "https://example.com"},
            model="photon-1",
            callback_url="https://example.com",
            format="jpg",
            grid_position_x=0,
            grid_position_y=0,
            prompt="prompt",
            resized_height=0,
            resized_width=0,
            x_end=0,
            x_start=0,
            y_end=0,
            y_start=0,
        )
        assert_matches_type(Generation, image, path=["response"])

    @parametrize
    def test_raw_response_reframe(self, client: LumaAI) -> None:
        response = client.generations.image.with_raw_response.reframe(
            aspect_ratio="16:9",
            generation_type="reframe_image",
            media={"url": "https://example.com"},
            model="photon-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(Generation, image, path=["response"])

    @parametrize
    def test_streaming_response_reframe(self, client: LumaAI) -> None:
        with client.generations.image.with_streaming_response.reframe(
            aspect_ratio="16:9",
            generation_type="reframe_image",
            media={"url": "https://example.com"},
            model="photon-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(Generation, image, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncImage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncLumaAI) -> None:
        image = await async_client.generations.image.create(
            model="photon-1",
        )
        assert_matches_type(Generation, image, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLumaAI) -> None:
        image = await async_client.generations.image.create(
            model="photon-1",
            aspect_ratio="16:9",
            callback_url="https://example.com",
            character_ref={"identity0": {"images": ["https://example.com"]}},
            format="jpg",
            generation_type="image",
            image_ref=[
                {
                    "url": "https://example.com",
                    "weight": 0,
                }
            ],
            modify_image_ref={
                "url": "https://example.com",
                "weight": 0,
            },
            prompt="prompt",
            style_ref=[
                {
                    "url": "https://example.com",
                    "weight": 0,
                }
            ],
            sync=True,
            sync_timeout=0,
        )
        assert_matches_type(Generation, image, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLumaAI) -> None:
        response = await async_client.generations.image.with_raw_response.create(
            model="photon-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(Generation, image, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLumaAI) -> None:
        async with async_client.generations.image.with_streaming_response.create(
            model="photon-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(Generation, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_reframe(self, async_client: AsyncLumaAI) -> None:
        image = await async_client.generations.image.reframe(
            aspect_ratio="16:9",
            generation_type="reframe_image",
            media={"url": "https://example.com"},
            model="photon-1",
        )
        assert_matches_type(Generation, image, path=["response"])

    @parametrize
    async def test_method_reframe_with_all_params(self, async_client: AsyncLumaAI) -> None:
        image = await async_client.generations.image.reframe(
            aspect_ratio="16:9",
            generation_type="reframe_image",
            media={"url": "https://example.com"},
            model="photon-1",
            callback_url="https://example.com",
            format="jpg",
            grid_position_x=0,
            grid_position_y=0,
            prompt="prompt",
            resized_height=0,
            resized_width=0,
            x_end=0,
            x_start=0,
            y_end=0,
            y_start=0,
        )
        assert_matches_type(Generation, image, path=["response"])

    @parametrize
    async def test_raw_response_reframe(self, async_client: AsyncLumaAI) -> None:
        response = await async_client.generations.image.with_raw_response.reframe(
            aspect_ratio="16:9",
            generation_type="reframe_image",
            media={"url": "https://example.com"},
            model="photon-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(Generation, image, path=["response"])

    @parametrize
    async def test_streaming_response_reframe(self, async_client: AsyncLumaAI) -> None:
        async with async_client.generations.image.with_streaming_response.reframe(
            aspect_ratio="16:9",
            generation_type="reframe_image",
            media={"url": "https://example.com"},
            model="photon-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(Generation, image, path=["response"])

        assert cast(Any, response.is_closed) is True
