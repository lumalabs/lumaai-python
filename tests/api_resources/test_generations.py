# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lumaai import LumaAI, AsyncLumaAI
from tests.utils import assert_matches_type
from lumaai.types import (
    Generation,
    GenerationListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LumaAI) -> None:
        generation = client.generations.create()
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LumaAI) -> None:
        generation = client.generations.create(
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
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LumaAI) -> None:
        response = client.generations.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LumaAI) -> None:
        with client.generations.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(Generation, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: LumaAI) -> None:
        generation = client.generations.list()
        assert_matches_type(GenerationListResponse, generation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: LumaAI) -> None:
        generation = client.generations.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(GenerationListResponse, generation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LumaAI) -> None:
        response = client.generations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(GenerationListResponse, generation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LumaAI) -> None:
        with client.generations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(GenerationListResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: LumaAI) -> None:
        generation = client.generations.delete(
            "id",
        )
        assert generation is None

    @parametrize
    def test_raw_response_delete(self, client: LumaAI) -> None:
        response = client.generations.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert generation is None

    @parametrize
    def test_streaming_response_delete(self, client: LumaAI) -> None:
        with client.generations.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert generation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: LumaAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.generations.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_audio(self, client: LumaAI) -> None:
        generation = client.generations.audio(
            id="id",
        )
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    def test_method_audio_with_all_params(self, client: LumaAI) -> None:
        generation = client.generations.audio(
            id="id",
            callback_url="https://example.com",
            generation_type="add_audio",
            negative_prompt="negative_prompt",
            prompt="prompt",
        )
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    def test_raw_response_audio(self, client: LumaAI) -> None:
        response = client.generations.with_raw_response.audio(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    def test_streaming_response_audio(self, client: LumaAI) -> None:
        with client.generations.with_streaming_response.audio(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(Generation, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_audio(self, client: LumaAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.generations.with_raw_response.audio(
                id="",
            )

    @parametrize
    def test_method_get(self, client: LumaAI) -> None:
        generation = client.generations.get(
            "id",
        )
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: LumaAI) -> None:
        response = client.generations.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: LumaAI) -> None:
        with client.generations.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(Generation, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: LumaAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.generations.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_upscale(self, client: LumaAI) -> None:
        generation = client.generations.upscale(
            id="id",
        )
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    def test_method_upscale_with_all_params(self, client: LumaAI) -> None:
        generation = client.generations.upscale(
            id="id",
            callback_url="https://example.com",
            generation_type="upscale_video",
            resolution="540p",
        )
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    def test_raw_response_upscale(self, client: LumaAI) -> None:
        response = client.generations.with_raw_response.upscale(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    def test_streaming_response_upscale(self, client: LumaAI) -> None:
        with client.generations.with_streaming_response.upscale(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(Generation, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_upscale(self, client: LumaAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.generations.with_raw_response.upscale(
                id="",
            )


class TestAsyncGenerations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLumaAI) -> None:
        generation = await async_client.generations.create()
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLumaAI) -> None:
        generation = await async_client.generations.create(
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
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLumaAI) -> None:
        response = await async_client.generations.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLumaAI) -> None:
        async with async_client.generations.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(Generation, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncLumaAI) -> None:
        generation = await async_client.generations.list()
        assert_matches_type(GenerationListResponse, generation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLumaAI) -> None:
        generation = await async_client.generations.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(GenerationListResponse, generation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLumaAI) -> None:
        response = await async_client.generations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(GenerationListResponse, generation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLumaAI) -> None:
        async with async_client.generations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(GenerationListResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLumaAI) -> None:
        generation = await async_client.generations.delete(
            "id",
        )
        assert generation is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLumaAI) -> None:
        response = await async_client.generations.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert generation is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLumaAI) -> None:
        async with async_client.generations.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert generation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLumaAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.generations.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_audio(self, async_client: AsyncLumaAI) -> None:
        generation = await async_client.generations.audio(
            id="id",
        )
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    async def test_method_audio_with_all_params(self, async_client: AsyncLumaAI) -> None:
        generation = await async_client.generations.audio(
            id="id",
            callback_url="https://example.com",
            generation_type="add_audio",
            negative_prompt="negative_prompt",
            prompt="prompt",
        )
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    async def test_raw_response_audio(self, async_client: AsyncLumaAI) -> None:
        response = await async_client.generations.with_raw_response.audio(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    async def test_streaming_response_audio(self, async_client: AsyncLumaAI) -> None:
        async with async_client.generations.with_streaming_response.audio(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(Generation, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_audio(self, async_client: AsyncLumaAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.generations.with_raw_response.audio(
                id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncLumaAI) -> None:
        generation = await async_client.generations.get(
            "id",
        )
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLumaAI) -> None:
        response = await async_client.generations.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLumaAI) -> None:
        async with async_client.generations.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(Generation, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncLumaAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.generations.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_upscale(self, async_client: AsyncLumaAI) -> None:
        generation = await async_client.generations.upscale(
            id="id",
        )
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    async def test_method_upscale_with_all_params(self, async_client: AsyncLumaAI) -> None:
        generation = await async_client.generations.upscale(
            id="id",
            callback_url="https://example.com",
            generation_type="upscale_video",
            resolution="540p",
        )
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    async def test_raw_response_upscale(self, async_client: AsyncLumaAI) -> None:
        response = await async_client.generations.with_raw_response.upscale(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    async def test_streaming_response_upscale(self, async_client: AsyncLumaAI) -> None:
        async with async_client.generations.with_streaming_response.upscale(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(Generation, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_upscale(self, async_client: AsyncLumaAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.generations.with_raw_response.upscale(
                id="",
            )
