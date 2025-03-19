# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["GenerationAudioParams"]


class GenerationAudioParams(TypedDict, total=False):
    callback_url: str
    """The callback URL for the audio"""

    generation_type: Literal["add_audio"]

    negative_prompt: str
    """The negative prompt of the audio"""

    prompt: str
    """The prompt of the audio"""
