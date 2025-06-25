# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ImageReframeParams", "Media"]


class ImageReframeParams(TypedDict, total=False):
    aspect_ratio: Required[Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"]]
    """The aspect ratio of the generation"""

    generation_type: Required[Literal["reframe_image"]]

    media: Required[Media]
    """The image entity object"""

    model: Required[Literal["photon-1", "photon-flash-1"]]
    """The model used for the reframe image"""

    callback_url: str
    """
    The callback URL of the generation, a POST request with Generation object will
    be sent to the callback URL when the generation is dreaming, completed, or
    failed
    """

    format: Literal["jpg", "png"]
    """The format of the image"""

    grid_position_x: int
    """The x position of the image in the grid"""

    grid_position_y: int
    """The y position of the image in the grid"""

    prompt: str
    """The prompt of the generation"""

    resized_height: int
    """Resized height of source image"""

    resized_width: int
    """Resized width of source image"""

    x_end: int
    """The x end of the crop bounds"""

    x_start: int
    """The x start of the crop bounds"""

    y_end: int
    """The y end of the crop bounds"""

    y_start: int
    """The y start of the crop bounds"""


class Media(TypedDict, total=False):
    url: Required[str]
    """The URL of the media"""
