# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lumaai import LumaAI, AsyncLumaAI
from tests.utils import assert_matches_type
from lumaai.types import Generation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVideo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LumaAI) -> None:
        video = client.generations.video.create()
        assert_matches_type(Generation, video, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LumaAI) -> None:
        video = client.generations.video.create(
            aspect_ratio="1:1",
            callback_url="https://example.com",
            duration="5s",
            generation_type="video",
            keyframes={
                "frame0": {
                    "type": "image",
                    "url": "https://example.com/image.jpg",
                },
                "frame1": {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "type": "generation",
                },
            },
            loop=True,
            model="ray-1-6",
            prompt="A serene lake surrounded by mountains at sunset",
            resolution="540p",
        )
        assert_matches_type(Generation, video, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LumaAI) -> None:
        response = client.generations.video.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert_matches_type(Generation, video, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LumaAI) -> None:
        with client.generations.video.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert_matches_type(Generation, video, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVideo:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLumaAI) -> None:
        video = await async_client.generations.video.create()
        assert_matches_type(Generation, video, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLumaAI) -> None:
        video = await async_client.generations.video.create(
            aspect_ratio="1:1",
            callback_url="https://example.com",
            duration="5s",
            generation_type="video",
            keyframes={
                "frame0": {
                    "type": "image",
                    "url": "https://example.com/image.jpg",
                },
                "frame1": {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "type": "generation",
                },
            },
            loop=True,
            model="ray-1-6",
            prompt="A serene lake surrounded by mountains at sunset",
            resolution="540p",
        )
        assert_matches_type(Generation, video, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLumaAI) -> None:
        response = await async_client.generations.video.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert_matches_type(Generation, video, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLumaAI) -> None:
        async with async_client.generations.video.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert_matches_type(Generation, video, path=["response"])

        assert cast(Any, response.is_closed) is True
