# Ping

Types:

```python
from luma_ai.types import PingRetrieveResponse
```

Methods:

- <code title="get /ping">client.ping.<a href="./src/luma_ai/resources/ping.py">retrieve</a>() -> <a href="./src/luma_ai/types/ping_retrieve_response.py">PingRetrieveResponse</a></code>

# Generations

Types:

```python
from luma_ai.types import Generation, GenerationListResponse
```

Methods:

- <code title="post /generations">client.generations.<a href="./src/luma_ai/resources/generations/generations.py">create</a>(\*\*<a href="src/luma_ai/types/generation_create_params.py">params</a>) -> <a href="./src/luma_ai/types/generation.py">Generation</a></code>
- <code title="get /generations/{id}">client.generations.<a href="./src/luma_ai/resources/generations/generations.py">retrieve</a>(id) -> <a href="./src/luma_ai/types/generation.py">Generation</a></code>
- <code title="get /generations">client.generations.<a href="./src/luma_ai/resources/generations/generations.py">list</a>(\*\*<a href="src/luma_ai/types/generation_list_params.py">params</a>) -> <a href="./src/luma_ai/types/generation_list_response.py">GenerationListResponse</a></code>
- <code title="delete /generations/{id}">client.generations.<a href="./src/luma_ai/resources/generations/generations.py">delete</a>(id) -> None</code>

## CameraMotion

Types:

```python
from luma_ai.types.generations import CameraMotion, CameraMotionListResponse
```

Methods:

- <code title="get /generations/camera_motion/list">client.generations.camera_motion.<a href="./src/luma_ai/resources/generations/camera_motion.py">list</a>() -> <a href="./src/luma_ai/types/generations/camera_motion_list_response.py">CameraMotionListResponse</a></code>
