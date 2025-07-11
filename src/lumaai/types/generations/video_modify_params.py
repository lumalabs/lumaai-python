# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VideoModifyParams", "Media", "FirstFrame"]


class VideoModifyParams(TypedDict, total=False):
    generation_type: Required[Literal["modify_video"]]

    media: Required[Media]
    """The image entity object"""

    mode: Required[
        Literal[
            "adhere_1",
            "adhere_2",
            "adhere_3",
            "flex_1",
            "flex_2",
            "flex_3",
            "reimagine_1",
            "reimagine_2",
            "reimagine_3",
        ]
    ]
    """The mode of the modify video"""

    model: Required[Literal["ray-2", "ray-flash-2"]]
    """The model used for the modify video"""

    callback_url: str
    """
    The callback URL of the generation, a POST request with Generation object will
    be sent to the callback URL when the generation is dreaming, completed, or
    failed
    """

    first_frame: FirstFrame
    """The image entity object"""

    prompt: str
    """The prompt of the generation"""


class Media(TypedDict, total=False):
    url: Required[str]
    """The URL of the media"""


class FirstFrame(TypedDict, total=False):
    url: Required[str]
    """The URL of the media"""
