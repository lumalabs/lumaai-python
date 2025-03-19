# Generations

Types:

```python
from lumaai.types import Generation, GenerationListResponse
```

Methods:

- <code title="post /generations">client.generations.<a href="./src/lumaai/resources/generations/generations.py">create</a>(\*\*<a href="src/lumaai/types/generation_create_params.py">params</a>) -> <a href="./src/lumaai/types/generation.py">Generation</a></code>
- <code title="get /generations">client.generations.<a href="./src/lumaai/resources/generations/generations.py">list</a>(\*\*<a href="src/lumaai/types/generation_list_params.py">params</a>) -> <a href="./src/lumaai/types/generation_list_response.py">GenerationListResponse</a></code>
- <code title="delete /generations/{id}">client.generations.<a href="./src/lumaai/resources/generations/generations.py">delete</a>(id) -> None</code>
- <code title="post /generations/{id}/audio">client.generations.<a href="./src/lumaai/resources/generations/generations.py">audio</a>(id, \*\*<a href="src/lumaai/types/generation_audio_params.py">params</a>) -> <a href="./src/lumaai/types/generation.py">Generation</a></code>
- <code title="get /generations/{id}">client.generations.<a href="./src/lumaai/resources/generations/generations.py">get</a>(id) -> <a href="./src/lumaai/types/generation.py">Generation</a></code>
- <code title="post /generations/{id}/upscale">client.generations.<a href="./src/lumaai/resources/generations/generations.py">upscale</a>(id, \*\*<a href="src/lumaai/types/generation_upscale_params.py">params</a>) -> <a href="./src/lumaai/types/generation.py">Generation</a></code>

## CameraMotion

Types:

```python
from lumaai.types.generations import CameraMotionListResponse
```

Methods:

- <code title="get /generations/camera_motion/list">client.generations.camera_motion.<a href="./src/lumaai/resources/generations/camera_motion.py">list</a>() -> <a href="./src/lumaai/types/generations/camera_motion_list_response.py">CameraMotionListResponse</a></code>

## Image

Methods:

- <code title="post /generations/image">client.generations.image.<a href="./src/lumaai/resources/generations/image.py">create</a>(\*\*<a href="src/lumaai/types/generations/image_create_params.py">params</a>) -> <a href="./src/lumaai/types/generation.py">Generation</a></code>

## Video

Methods:

- <code title="post /generations">client.generations.video.<a href="./src/lumaai/resources/generations/video.py">create</a>(\*\*<a href="src/lumaai/types/generations/video_create_params.py">params</a>) -> <a href="./src/lumaai/types/generation.py">Generation</a></code>

# Ping

Types:

```python
from lumaai.types import PingCheckResponse
```

Methods:

- <code title="get /ping">client.ping.<a href="./src/lumaai/resources/ping.py">check</a>() -> <a href="./src/lumaai/types/ping_check_response.py">PingCheckResponse</a></code>

# Credits

Types:

```python
from lumaai.types import CreditGetResponse
```

Methods:

- <code title="get /credits">client.credits.<a href="./src/lumaai/resources/credits.py">get</a>() -> <a href="./src/lumaai/types/credit_get_response.py">CreditGetResponse</a></code>
