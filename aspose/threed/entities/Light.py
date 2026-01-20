from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Camera import Camera
    from ..Entity import Entity

from .Camera import Camera


class Light(Camera):
    def __init__(self, name: str = None, light_type=None):
        super().__init__(name)
        self._light_type = light_type if light_type is not None else "POINT"
