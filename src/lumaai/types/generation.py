# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "Generation",
    "Assets",
    "Request",
    "RequestGenerationRequest",
    "RequestGenerationRequestKeyframes",
    "RequestGenerationRequestKeyframesFrame0",
    "RequestGenerationRequestKeyframesFrame0GenerationReference",
    "RequestGenerationRequestKeyframesFrame0ImageReference",
    "RequestGenerationRequestKeyframesFrame1",
    "RequestGenerationRequestKeyframesFrame1GenerationReference",
    "RequestGenerationRequestKeyframesFrame1ImageReference",
    "RequestImageGenerationRequest",
    "RequestImageGenerationRequestCharacterRef",
    "RequestImageGenerationRequestCharacterRefIdentity0",
    "RequestImageGenerationRequestImageRef",
    "RequestImageGenerationRequestModifyImageRef",
    "RequestImageGenerationRequestStyleRef",
    "RequestUpscaleVideoGenerationRequest",
    "RequestAudioGenerationRequest",
]


class Assets(BaseModel):
    image: Optional[str] = None
    """The URL of the image"""

    progress_video: Optional[str] = None
    """The URL of the progress video"""

    video: Optional[str] = None
    """The URL of the video"""


class RequestGenerationRequestKeyframesFrame0GenerationReference(BaseModel):
    id: str
    """The ID of the generation"""

    type: Literal["generation"]


class RequestGenerationRequestKeyframesFrame0ImageReference(BaseModel):
    type: Literal["image"]

    url: str
    """The URL of the image"""


RequestGenerationRequestKeyframesFrame0: TypeAlias = Annotated[
    Union[
        RequestGenerationRequestKeyframesFrame0GenerationReference,
        RequestGenerationRequestKeyframesFrame0ImageReference,
    ],
    PropertyInfo(discriminator="type"),
]


class RequestGenerationRequestKeyframesFrame1GenerationReference(BaseModel):
    id: str
    """The ID of the generation"""

    type: Literal["generation"]


class RequestGenerationRequestKeyframesFrame1ImageReference(BaseModel):
    type: Literal["image"]

    url: str
    """The URL of the image"""


RequestGenerationRequestKeyframesFrame1: TypeAlias = Annotated[
    Union[
        RequestGenerationRequestKeyframesFrame1GenerationReference,
        RequestGenerationRequestKeyframesFrame1ImageReference,
    ],
    PropertyInfo(discriminator="type"),
]


class RequestGenerationRequestKeyframes(BaseModel):
    frame0: Optional[RequestGenerationRequestKeyframesFrame0] = None
    """The frame 0 of the generation"""

    frame1: Optional[RequestGenerationRequestKeyframesFrame1] = None
    """The frame 1 of the generation"""


class RequestGenerationRequest(BaseModel):
    aspect_ratio: Optional[Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"]] = None
    """The aspect ratio of the generation"""

    callback_url: Optional[str] = None
    """
    The callback URL of the generation, a POST request with Generation object will
    be sent to the callback URL when the generation is dreaming, completed, or
    failed
    """

    duration: Union[Literal["5s", "9s"], str, None] = None
    """The duration of the generation"""

    generation_type: Optional[Literal["video"]] = None

    keyframes: Optional[RequestGenerationRequestKeyframes] = None
    """The keyframes of the generation"""

    loop: Optional[bool] = None
    """Whether to loop the video"""

    model: Optional[Literal["ray-1-6", "ray-2", "ray-flash-2"]] = None
    """The model used for the generation"""

    prompt: Optional[str] = None
    """The prompt of the generation"""

    resolution: Union[Literal["540p", "720p", "1080p", "4k"], str, None] = None
    """The resolution of the generation"""


class RequestImageGenerationRequestCharacterRefIdentity0(BaseModel):
    images: Optional[List[str]] = None
    """The URLs of the image identity"""


class RequestImageGenerationRequestCharacterRef(BaseModel):
    identity0: Optional[RequestImageGenerationRequestCharacterRefIdentity0] = None
    """The image identity object"""


class RequestImageGenerationRequestImageRef(BaseModel):
    url: Optional[str] = None
    """The URL of the image reference"""

    weight: Optional[float] = None
    """The weight of the image reference"""


class RequestImageGenerationRequestModifyImageRef(BaseModel):
    url: Optional[str] = None
    """The URL of the image reference"""

    weight: Optional[float] = None
    """The weight of the modify image reference"""


class RequestImageGenerationRequestStyleRef(BaseModel):
    url: Optional[str] = None
    """The URL of the image reference"""

    weight: Optional[float] = None
    """The weight of the image reference"""


class RequestImageGenerationRequest(BaseModel):
    aspect_ratio: Optional[Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"]] = None
    """The aspect ratio of the generation"""

    callback_url: Optional[str] = None
    """The callback URL for the generation"""

    character_ref: Optional[RequestImageGenerationRequestCharacterRef] = None

    generation_type: Optional[Literal["image"]] = None

    image_ref: Optional[List[RequestImageGenerationRequestImageRef]] = None

    model: Optional[Literal["photon-1", "photon-flash-1"]] = None
    """The model used for the generation"""

    modify_image_ref: Optional[RequestImageGenerationRequestModifyImageRef] = None
    """The modify image reference object"""

    prompt: Optional[str] = None
    """The prompt of the generation"""

    style_ref: Optional[List[RequestImageGenerationRequestStyleRef]] = None


class RequestUpscaleVideoGenerationRequest(BaseModel):
    callback_url: Optional[str] = None
    """The callback URL for the upscale"""

    generation_type: Optional[Literal["upscale_video"]] = None

    resolution: Union[Literal["540p", "720p", "1080p", "4k"], str, None] = None
    """The resolution of the upscale"""


class RequestAudioGenerationRequest(BaseModel):
    callback_url: Optional[str] = None
    """The callback URL for the audio"""

    generation_type: Optional[Literal["add_audio"]] = None

    negative_prompt: Optional[str] = None
    """The negative prompt of the audio"""

    prompt: Optional[str] = None
    """The prompt of the audio"""


Request: TypeAlias = Union[
    RequestGenerationRequest,
    RequestImageGenerationRequest,
    RequestUpscaleVideoGenerationRequest,
    RequestAudioGenerationRequest,
]


class Generation(BaseModel):
    id: Optional[str] = None
    """The ID of the generation"""

    assets: Optional[Assets] = None
    """The assets of the generation"""

    created_at: Optional[datetime] = None
    """The date and time when the generation was created"""

    failure_reason: Optional[str] = None
    """The reason for the state of the generation"""

    generation_type: Optional[Literal["video", "image"]] = None
    """The type of the generation"""

    model: Optional[str] = None
    """The model used for the generation"""

    request: Optional[Request] = None
    """The request of the generation"""

    state: Optional[Literal["queued", "dreaming", "completed", "failed"]] = None
    """The state of the generation"""
