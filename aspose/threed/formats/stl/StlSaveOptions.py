from typing import TYPE_CHECKING

from ..SaveOptions import SaveOptions

if TYPE_CHECKING:
    from aspose.threed import FileFormat


class StlSaveOptions(SaveOptions):
    def __init__(self, file_format: 'FileFormat' = None):
        super().__init__()
        if file_format is not None:
            self._file_format = file_format
        self._flip_coordinate_system = False
        self._scale = 1.0
        self._binary_mode = False

    @property
    def flip_coordinate_system(self) -> bool:
        return self._flip_coordinate_system

    @flip_coordinate_system.setter
    def flip_coordinate_system(self, value: bool):
        self._flip_coordinate_system = bool(value)

    @property
    def scale(self) -> float:
        return self._scale

    @scale.setter
    def scale(self, value: float):
        self._scale = float(value)

    @property
    def binary_mode(self) -> bool:
        return self._binary_mode

    @binary_mode.setter
    def binary_mode(self, value: bool):
        self._binary_mode = bool(value)
