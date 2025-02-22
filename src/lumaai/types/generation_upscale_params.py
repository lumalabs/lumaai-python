# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypedDict

__all__ = ["GenerationUpscaleParams"]


class GenerationUpscaleParams(TypedDict, total=False):
    callback_url: str
    """The callback URL for the upscale"""

    generation_type: Literal["upscale_video"]

    resolution: Union[Literal["540p", "720p", "1080p", "4k"], str]
    """The resolution of the upscale"""
