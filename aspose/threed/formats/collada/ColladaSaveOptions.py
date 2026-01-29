from typing import TYPE_CHECKING

from ..SaveOptions import SaveOptions
from .ColladaTransformStyle import ColladaTransformStyle

if TYPE_CHECKING:
    pass


class ColladaSaveOptions(SaveOptions):
    def __init__(self):
        super().__init__()
        self._flip_coordinate_system = False
        self._enable_materials = True
        self._indented = True

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
    def indented(self) -> bool:
        return self._indented

    @indented.setter
    def indented(self, value: bool):
        self._indented = bool(value)
