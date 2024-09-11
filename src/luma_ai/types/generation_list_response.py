# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .generation import Generation

__all__ = ["GenerationListResponse"]


class GenerationListResponse(BaseModel):
    generations: List[Generation]
    """The generations requested"""

    count: Optional[int] = None
    """The number of generations returned"""

    has_more: Optional[bool] = None
    """Whether there are more generations"""

    limit: Optional[int] = None
    """The limit of the generations requested"""

    offset: Optional[int] = None
    """The offset of the generations requested"""
