# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from luma_ai import LumaAI, AsyncLumaAI
from tests.utils import assert_matches_type
from luma_ai.types import Generation, GenerationListResponse

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
            camera_motion="static",
            keyframes={
                "frame0": {
                    "type": "image",
                    "url": "https://api.lumalabs.ai/dream-machine/v1alpha/images/123.jpg",
                },
                "frame1": {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "type": "generation",
                },
            },
            loop=True,
            prompt="prompt",
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
    def test_method_retrieve(self, client: LumaAI) -> None:
        generation = client.generations.retrieve(
            "id",
        )
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LumaAI) -> None:
        response = client.generations.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LumaAI) -> None:
        with client.generations.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(Generation, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: LumaAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.generations.with_raw_response.retrieve(
                "",
            )

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
            camera_motion="static",
            keyframes={
                "frame0": {
                    "type": "image",
                    "url": "https://api.lumalabs.ai/dream-machine/v1alpha/images/123.jpg",
                },
                "frame1": {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "type": "generation",
                },
            },
            loop=True,
            prompt="prompt",
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
    async def test_method_retrieve(self, async_client: AsyncLumaAI) -> None:
        generation = await async_client.generations.retrieve(
            "id",
        )
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLumaAI) -> None:
        response = await async_client.generations.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLumaAI) -> None:
        async with async_client.generations.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(Generation, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLumaAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.generations.with_raw_response.retrieve(
                "",
            )

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