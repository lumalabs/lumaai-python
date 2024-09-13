# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lumaai import Lumaai, AsyncLumaai
from tests.utils import assert_matches_type
from lumaai.types.generations import CameraMotionListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCameraMotion:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Lumaai) -> None:
        camera_motion = client.generations.camera_motion.list()
        assert_matches_type(CameraMotionListResponse, camera_motion, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lumaai) -> None:
        response = client.generations.camera_motion.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        camera_motion = response.parse()
        assert_matches_type(CameraMotionListResponse, camera_motion, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lumaai) -> None:
        with client.generations.camera_motion.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            camera_motion = response.parse()
            assert_matches_type(CameraMotionListResponse, camera_motion, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCameraMotion:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncLumaai) -> None:
        camera_motion = await async_client.generations.camera_motion.list()
        assert_matches_type(CameraMotionListResponse, camera_motion, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLumaai) -> None:
        response = await async_client.generations.camera_motion.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        camera_motion = await response.parse()
        assert_matches_type(CameraMotionListResponse, camera_motion, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLumaai) -> None:
        async with async_client.generations.camera_motion.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            camera_motion = await response.parse()
            assert_matches_type(CameraMotionListResponse, camera_motion, path=["response"])

        assert cast(Any, response.is_closed) is True
