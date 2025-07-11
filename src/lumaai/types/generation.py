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
    "RequestGenerationRequestConcept",
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
    "RequestReframeImageRequest",
    "RequestReframeImageRequestMedia",
    "RequestReframeVideoRequest",
    "RequestReframeVideoRequestMedia",
    "RequestReframeVideoRequestFirstFrame",
    "RequestModifyVideoRequest",
    "RequestModifyVideoRequestMedia",
    "RequestModifyVideoRequestFirstFrame",
]


class Assets(BaseModel):
    image: Optional[str] = None
    """The URL of the image"""

    progress_video: Optional[str] = None
    """The URL of the progress video"""

    video: Optional[str] = None
    """The URL of the video"""


class RequestGenerationRequestConcept(BaseModel):
    key: str
    """The key of the concept"""


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
    model: Literal["ray-1-6", "ray-2", "ray-flash-2"]
    """The model used for the generation"""

    aspect_ratio: Optional[Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"]] = None
    """The aspect ratio of the generation"""

    callback_url: Optional[str] = None
    """
    The callback URL of the generation, a POST request with Generation object will
    be sent to the callback URL when the generation is dreaming, completed, or
    failed
    """

    concepts: Optional[List[RequestGenerationRequestConcept]] = None
    """The concepts of the generation"""

    duration: Union[Literal["5s", "9s"], str, None] = None
    """The duration of the generation"""

    generation_type: Optional[Literal["video"]] = None

    keyframes: Optional[RequestGenerationRequestKeyframes] = None
    """The keyframes of the generation"""

    loop: Optional[bool] = None
    """Whether to loop the video"""

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
    model: Literal["photon-1", "photon-flash-1"]
    """The model used for the generation"""

    aspect_ratio: Optional[Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"]] = None
    """The aspect ratio of the generation"""

    callback_url: Optional[str] = None
    """The callback URL for the generation"""

    character_ref: Optional[RequestImageGenerationRequestCharacterRef] = None

    format: Optional[Literal["jpg", "png"]] = None
    """The format of the image"""

    generation_type: Optional[Literal["image"]] = None

    image_ref: Optional[List[RequestImageGenerationRequestImageRef]] = None

    modify_image_ref: Optional[RequestImageGenerationRequestModifyImageRef] = None
    """The modify image reference object"""

    prompt: Optional[str] = None
    """The prompt of the generation"""

    style_ref: Optional[List[RequestImageGenerationRequestStyleRef]] = None

    sync: Optional[bool] = None
    """Create image in synchronous mode and return complated image"""

    sync_timeout: Optional[float] = None
    """The timeout for the synchronous image generation"""


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


class RequestReframeImageRequestMedia(BaseModel):
    url: str
    """The URL of the media"""


class RequestReframeImageRequest(BaseModel):
    aspect_ratio: Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"]
    """The aspect ratio of the generation"""

    generation_type: Literal["reframe_image"]

    media: RequestReframeImageRequestMedia
    """The image entity object"""

    model: Literal["photon-1", "photon-flash-1"]
    """The model used for the reframe image"""

    callback_url: Optional[str] = None
    """
    The callback URL of the generation, a POST request with Generation object will
    be sent to the callback URL when the generation is dreaming, completed, or
    failed
    """

    format: Optional[Literal["jpg", "png"]] = None
    """The format of the image"""

    grid_position_x: Optional[int] = None
    """The x position of the image in the grid"""

    grid_position_y: Optional[int] = None
    """The y position of the image in the grid"""

    prompt: Optional[str] = None
    """The prompt of the generation"""

    resized_height: Optional[int] = None
    """Resized height of source image"""

    resized_width: Optional[int] = None
    """Resized width of source image"""

    x_end: Optional[int] = None
    """The x end of the crop bounds"""

    x_start: Optional[int] = None
    """The x start of the crop bounds"""

    y_end: Optional[int] = None
    """The y end of the crop bounds"""

    y_start: Optional[int] = None
    """The y start of the crop bounds"""


class RequestReframeVideoRequestMedia(BaseModel):
    url: str
    """The URL of the media"""


class RequestReframeVideoRequestFirstFrame(BaseModel):
    url: str
    """The URL of the media"""


class RequestReframeVideoRequest(BaseModel):
    aspect_ratio: Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"]
    """The aspect ratio of the generation"""

    generation_type: Literal["reframe_video"]

    media: RequestReframeVideoRequestMedia
    """The image entity object"""

    model: Literal["ray-2", "ray-flash-2"]
    """The model used for the reframe video"""

    callback_url: Optional[str] = None
    """
    The callback URL of the generation, a POST request with Generation object will
    be sent to the callback URL when the generation is dreaming, completed, or
    failed
    """

    first_frame: Optional[RequestReframeVideoRequestFirstFrame] = None
    """The image entity object"""

    grid_position_x: Optional[int] = None
    """The x position of the image in the grid"""

    grid_position_y: Optional[int] = None
    """The y position of the image in the grid"""

    prompt: Optional[str] = None
    """The prompt of the generation"""

    resized_height: Optional[int] = None
    """Resized height of source video"""

    resized_width: Optional[int] = None
    """Resized width of source video"""

    x_end: Optional[int] = None
    """The x end of the crop bounds"""

    x_start: Optional[int] = None
    """The x start of the crop bounds"""

    y_end: Optional[int] = None
    """The y end of the crop bounds"""

    y_start: Optional[int] = None
    """The y start of the crop bounds"""


class RequestModifyVideoRequestMedia(BaseModel):
    url: str
    """The URL of the media"""


class RequestModifyVideoRequestFirstFrame(BaseModel):
    url: str
    """The URL of the media"""


class RequestModifyVideoRequest(BaseModel):
    generation_type: Literal["modify_video"]

    media: RequestModifyVideoRequestMedia
    """The image entity object"""

    mode: Literal[
        "adhere_1", "adhere_2", "adhere_3", "flex_1", "flex_2", "flex_3", "reimagine_1", "reimagine_2", "reimagine_3"
    ]
    """The mode of the modify video"""

    model: Literal["ray-2", "ray-flash-2"]
    """The model used for the modify video"""

    callback_url: Optional[str] = None
    """
    The callback URL of the generation, a POST request with Generation object will
    be sent to the callback URL when the generation is dreaming, completed, or
    failed
    """

    first_frame: Optional[RequestModifyVideoRequestFirstFrame] = None
    """The image entity object"""

    prompt: Optional[str] = None
    """The prompt of the generation"""


Request: TypeAlias = Union[
    RequestGenerationRequest,
    RequestImageGenerationRequest,
    RequestUpscaleVideoGenerationRequest,
    RequestAudioGenerationRequest,
    RequestReframeImageRequest,
    RequestReframeVideoRequest,
    RequestModifyVideoRequest,
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
