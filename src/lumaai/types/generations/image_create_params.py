# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ImageCreateParams", "CharacterRef", "CharacterRefIdentity0", "ImageRef", "ModifyImageRef", "StyleRef"]


class ImageCreateParams(TypedDict, total=False):
    model: Required[Literal["photon-1", "photon-flash-1"]]
    """The model used for the generation"""

    aspect_ratio: Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"]
    """The aspect ratio of the generation"""

    callback_url: str
    """The callback URL for the generation"""

    character_ref: CharacterRef

    format: Literal["jpg", "png"]
    """The format of the image"""

    generation_type: Literal["image"]

    image_ref: Iterable[ImageRef]

    modify_image_ref: ModifyImageRef
    """The modify image reference object"""

    prompt: str
    """The prompt of the generation"""

    style_ref: Iterable[StyleRef]

    sync: bool
    """Create image in synchronous mode and return complated image"""

    sync_timeout: float
    """The timeout for the synchronous image generation"""


class CharacterRefIdentity0(TypedDict, total=False):
    images: List[str]
    """The URLs of the image identity"""


class CharacterRef(TypedDict, total=False):
    identity0: CharacterRefIdentity0
    """The image identity object"""


class ImageRef(TypedDict, total=False):
    url: str
    """The URL of the image reference"""

    weight: float
    """The weight of the image reference"""


class ModifyImageRef(TypedDict, total=False):
    url: str
    """The URL of the image reference"""

    weight: float
    """The weight of the modify image reference"""


class StyleRef(TypedDict, total=False):
    url: str
    """The URL of the image reference"""

    weight: float
    """The weight of the image reference"""
