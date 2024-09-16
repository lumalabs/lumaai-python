# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lumaai import LumaAI, AsyncLumaAI
from tests.utils import assert_matches_type
from lumaai.types import PingCheckResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPing:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_check(self, client: LumaAI) -> None:
        ping = client.ping.check()
        assert_matches_type(PingCheckResponse, ping, path=["response"])

    @parametrize
    def test_raw_response_check(self, client: LumaAI) -> None:
        response = client.ping.with_raw_response.check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ping = response.parse()
        assert_matches_type(PingCheckResponse, ping, path=["response"])

    @parametrize
    def test_streaming_response_check(self, client: LumaAI) -> None:
        with client.ping.with_streaming_response.check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ping = response.parse()
            assert_matches_type(PingCheckResponse, ping, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPing:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_check(self, async_client: AsyncLumaAI) -> None:
        ping = await async_client.ping.check()
        assert_matches_type(PingCheckResponse, ping, path=["response"])

    @parametrize
    async def test_raw_response_check(self, async_client: AsyncLumaAI) -> None:
        response = await async_client.ping.with_raw_response.check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ping = await response.parse()
        assert_matches_type(PingCheckResponse, ping, path=["response"])

    @parametrize
    async def test_streaming_response_check(self, async_client: AsyncLumaAI) -> None:
        async with async_client.ping.with_streaming_response.check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ping = await response.parse()
            assert_matches_type(PingCheckResponse, ping, path=["response"])

        assert cast(Any, response.is_closed) is True
