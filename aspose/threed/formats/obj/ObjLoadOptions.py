from typing import TYPE_CHECKING

from ..LoadOptions import LoadOptions

if TYPE_CHECKING:
    pass


class ObjLoadOptions(LoadOptions):
    def __init__(self):
        super().__init__()
        self._flip_coordinate_system = False
        self._enable_materials = True
        self._scale = 1.0
        self._normalize_normal = True

    @property
    def flip_coordinate_system(self) -> bool:
        return self._flip_coordinate_system

    @flip_coordinate_system.setter
    def flip_coordinate_system(self, value: bool):
        self._flip_coordinate_system = bool(value)

    @property
    def enable_materials(self) -> bool:
        return self._enable_materials

    @enable_materials.setter
    def enable_materials(self, value: bool):
        self._enable_materials = bool(value)

    @property
    def scale(self) -> float:
        return self._scale

    @scale.setter
    def scale(self, value: float):
        self._scale = float(value)

    @property
    def normalize_normal(self) -> bool:
        return self._normalize_normal

    @normalize_normal.setter
    def normalize_normal(self, value: bool):
        self._normalize_normal = bool(value)
