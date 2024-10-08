# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lumaai import LumaAI, AsyncLumaAI
from tests.utils import assert_matches_type
from lumaai.types import CreditGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCredits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: LumaAI) -> None:
        credit = client.credits.get()
        assert_matches_type(CreditGetResponse, credit, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: LumaAI) -> None:
        response = client.credits.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = response.parse()
        assert_matches_type(CreditGetResponse, credit, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: LumaAI) -> None:
        with client.credits.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = response.parse()
            assert_matches_type(CreditGetResponse, credit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCredits:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncLumaAI) -> None:
        credit = await async_client.credits.get()
        assert_matches_type(CreditGetResponse, credit, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLumaAI) -> None:
        response = await async_client.credits.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = await response.parse()
        assert_matches_type(CreditGetResponse, credit, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLumaAI) -> None:
        async with async_client.credits.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = await response.parse()
            assert_matches_type(CreditGetResponse, credit, path=["response"])

        assert cast(Any, response.is_closed) is True
