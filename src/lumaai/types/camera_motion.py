# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["CameraMotion"]

CameraMotion: TypeAlias = Literal[
    "static",
    "move_left",
    "move_right",
    "move_up",
    "move_down",
    "push_in",
    "pull_out",
    "zoom_in",
    "zoom_out",
    "pan_left",
    "pan_right",
    "orbit_left",
    "orbit_right",
    "crane_up",
    "crane_down",
]
