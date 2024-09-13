# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "GenerationCreateParams",
    "Keyframes",
    "KeyframesFrame0",
    "KeyframesFrame0GenerationReference",
    "KeyframesFrame0ImageReference",
    "KeyframesFrame1",
    "KeyframesFrame1GenerationReference",
    "KeyframesFrame1ImageReference",
]


class GenerationCreateParams(TypedDict, total=False):
    aspect_ratio: Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"]
    """The aspect ratio of the generation"""

    keyframes: Keyframes
    """The keyframes of the generation"""

    loop: bool
    """Whether to loop the video"""

    prompt: str
    """The prompt of the generation"""


class KeyframesFrame0GenerationReference(TypedDict, total=False):
    id: Required[str]
    """The ID of the generation"""

    type: Required[Literal["generation"]]


class KeyframesFrame0ImageReference(TypedDict, total=False):
    type: Required[Literal["image"]]

    url: Required[str]
    """The URL of the image"""


KeyframesFrame0: TypeAlias = Union[KeyframesFrame0GenerationReference, KeyframesFrame0ImageReference]


class KeyframesFrame1GenerationReference(TypedDict, total=False):
    id: Required[str]
    """The ID of the generation"""

    type: Required[Literal["generation"]]


class KeyframesFrame1ImageReference(TypedDict, total=False):
    type: Required[Literal["image"]]

    url: Required[str]
    """The URL of the image"""


KeyframesFrame1: TypeAlias = Union[KeyframesFrame1GenerationReference, KeyframesFrame1ImageReference]


class Keyframes(TypedDict, total=False):
    frame0: KeyframesFrame0
    """The frame 0 of the generation"""

    frame1: KeyframesFrame1
    """The frame 1 of the generation"""
