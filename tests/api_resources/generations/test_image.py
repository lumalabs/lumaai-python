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
        image = client.generations.image.create()
        assert_matches_type(Generation, image, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LumaAI) -> None:
        image = client.generations.image.create(
            aspect_ratio="1:1",
            callback_url="https://example.com",
            character_ref={"identity0": {"images": ["https://example.com"]}},
            generation_type="image",
            image_ref=[
                {
                    "url": "https://example.com",
                    "weight": 0,
                }
            ],
            model="photon-1",
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
        )
        assert_matches_type(Generation, image, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LumaAI) -> None:
        response = client.generations.image.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(Generation, image, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LumaAI) -> None:
        with client.generations.image.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(Generation, image, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncImage:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLumaAI) -> None:
        image = await async_client.generations.image.create()
        assert_matches_type(Generation, image, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLumaAI) -> None:
        image = await async_client.generations.image.create(
            aspect_ratio="1:1",
            callback_url="https://example.com",
            character_ref={"identity0": {"images": ["https://example.com"]}},
            generation_type="image",
            image_ref=[
                {
                    "url": "https://example.com",
                    "weight": 0,
                }
            ],
            model="photon-1",
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
        )
        assert_matches_type(Generation, image, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLumaAI) -> None:
        response = await async_client.generations.image.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(Generation, image, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLumaAI) -> None:
        async with async_client.generations.image.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(Generation, image, path=["response"])

        assert cast(Any, response.is_closed) is True
