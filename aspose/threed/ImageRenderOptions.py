from .A3DObject import A3DObject
from typing import List


class ImageRenderOptions(A3DObject):
    def __init__(self):
        super().__init__()
        from .utilities import Vector3
        self._background_color = Vector3(0.5, 0.5, 0.5)
        self._enable_shadows = False
        self._asset_directories = []

    @property
    def background_color(self):
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        self._background_color = value

    @property
    def enable_shadows(self) -> bool:
        return self._enable_shadows

    @enable_shadows.setter
    def enable_shadows(self, value: bool):
        self._enable_shadows = bool(value)

    @property
    def asset_directories(self) -> List[str]:
        return list(self._asset_directories)

    @asset_directories.setter
    def asset_directories(self, value: List[str]):
        self._asset_directories = list(value)
