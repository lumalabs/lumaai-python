# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lumaai import LumaAI, AsyncLumaAI
from tests.utils import assert_matches_type
from lumaai.types.generations import ConceptListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConcepts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: LumaAI) -> None:
        concept = client.generations.concepts.list()
        assert_matches_type(ConceptListResponse, concept, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LumaAI) -> None:
        response = client.generations.concepts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        concept = response.parse()
        assert_matches_type(ConceptListResponse, concept, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LumaAI) -> None:
        with client.generations.concepts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            concept = response.parse()
            assert_matches_type(ConceptListResponse, concept, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConcepts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncLumaAI) -> None:
        concept = await async_client.generations.concepts.list()
        assert_matches_type(ConceptListResponse, concept, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLumaAI) -> None:
        response = await async_client.generations.concepts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        concept = await response.parse()
        assert_matches_type(ConceptListResponse, concept, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLumaAI) -> None:
        async with async_client.generations.concepts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            concept = await response.parse()
            assert_matches_type(ConceptListResponse, concept, path=["response"])

        assert cast(Any, response.is_closed) is True
