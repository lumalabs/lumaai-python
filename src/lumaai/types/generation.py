# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "Generation",
    "Assets",
    "Request",
    "RequestKeyframes",
    "RequestKeyframesFrame0",
    "RequestKeyframesFrame0GenerationReference",
    "RequestKeyframesFrame0ImageReference",
    "RequestKeyframesFrame1",
    "RequestKeyframesFrame1GenerationReference",
    "RequestKeyframesFrame1ImageReference",
]


class Assets(BaseModel):
    video: Optional[str] = None
    """The URL of the video"""


class RequestKeyframesFrame0GenerationReference(BaseModel):
    id: str
    """The ID of the generation"""

    type: Literal["generation"]


class RequestKeyframesFrame0ImageReference(BaseModel):
    type: Literal["image"]

    url: str
    """The URL of the image"""


RequestKeyframesFrame0: TypeAlias = Annotated[
    Union[RequestKeyframesFrame0GenerationReference, RequestKeyframesFrame0ImageReference],
    PropertyInfo(discriminator="type"),
]


class RequestKeyframesFrame1GenerationReference(BaseModel):
    id: str
    """The ID of the generation"""

    type: Literal["generation"]


class RequestKeyframesFrame1ImageReference(BaseModel):
    type: Literal["image"]

    url: str
    """The URL of the image"""


RequestKeyframesFrame1: TypeAlias = Annotated[
    Union[RequestKeyframesFrame1GenerationReference, RequestKeyframesFrame1ImageReference],
    PropertyInfo(discriminator="type"),
]


class RequestKeyframes(BaseModel):
    frame0: Optional[RequestKeyframesFrame0] = None
    """The frame 0 of the generation"""

    frame1: Optional[RequestKeyframesFrame1] = None
    """The frame 1 of the generation"""


class Request(BaseModel):
    aspect_ratio: Optional[Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"]] = None
    """The aspect ratio of the generation"""

    keyframes: Optional[RequestKeyframes] = None
    """The keyframes of the generation"""

    loop: Optional[bool] = None
    """Whether to loop the video"""

    prompt: Optional[str] = None
    """The prompt of the generation"""


class Generation(BaseModel):
    id: Optional[str] = None
    """The ID of the generation"""

    assets: Optional[Assets] = None
    """The assets of the generation"""

    created_at: Optional[datetime] = None
    """The date and time when the generation was created"""

    failure_reason: Optional[str] = None
    """The reason for the state of the generation"""

    request: Optional[Request] = None
    """The generation request object"""

    state: Optional[Literal["queued", "dreaming", "completed", "failed"]] = None
    """The state of the generation"""

    version: Optional[str] = None
    """The model version used for the generation eg. v1.6"""
