from typing import TYPE_CHECKING

from ..LoadOptions import LoadOptions

if TYPE_CHECKING:
    pass


class ThreeMfLoadOptions(LoadOptions):
    def __init__(self):
        super().__init__()
        self._flip_coordinate_system = False

    @property
    def flip_coordinate_system(self) -> bool:
        return self._flip_coordinate_system

    @flip_coordinate_system.setter
    def flip_coordinate_system(self, value: bool):
        self._flip_coordinate_system = bool(value)
