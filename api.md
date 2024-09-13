# Generations

Types:

```python
from lumaai.types import Generation, GenerationListResponse
```

Methods:

- <code title="post /generations">client.generations.<a href="./src/lumaai/resources/generations/generations.py">create</a>(\*\*<a href="src/lumaai/types/generation_create_params.py">params</a>) -> <a href="./src/lumaai/types/generation.py">Generation</a></code>
- <code title="get /generations">client.generations.<a href="./src/lumaai/resources/generations/generations.py">list</a>(\*\*<a href="src/lumaai/types/generation_list_params.py">params</a>) -> <a href="./src/lumaai/types/generation_list_response.py">GenerationListResponse</a></code>
- <code title="delete /generations/{id}">client.generations.<a href="./src/lumaai/resources/generations/generations.py">delete</a>(id) -> None</code>
- <code title="get /generations/{id}">client.generations.<a href="./src/lumaai/resources/generations/generations.py">get</a>(id) -> <a href="./src/lumaai/types/generation.py">Generation</a></code>

## CameraMotion

Types:

```python
from lumaai.types.generations import CameraMotionListResponse
```

Methods:

- <code title="get /generations/camera_motion/list">client.generations.camera_motion.<a href="./src/lumaai/resources/generations/camera_motion.py">list</a>() -> <a href="./src/lumaai/types/generations/camera_motion_list_response.py">CameraMotionListResponse</a></code>

# Ping

Types:

```python
from lumaai.types import PingCheckResponse
```

Methods:

- <code title="get /ping">client.ping.<a href="./src/lumaai/resources/ping.py">check</a>() -> <a href="./src/lumaai/types/ping_check_response.py">PingCheckResponse</a></code>
