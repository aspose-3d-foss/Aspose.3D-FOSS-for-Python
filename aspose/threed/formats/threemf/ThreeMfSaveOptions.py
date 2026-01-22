from typing import TYPE_CHECKING

from ..SaveOptions import SaveOptions

if TYPE_CHECKING:
    pass


class ThreeMfSaveOptions(SaveOptions):
    def __init__(self):
        super().__init__()
        from .ThreeMfFormat import ThreeMfFormat
        self._file_format = ThreeMfFormat()
        self._enable_compression = True
        self._build_all = True
        self._flip_coordinate_system = False
        self._unit = 'millimeter'
        self._pretty_print = False

    @property
    def enable_compression(self) -> bool:
        return self._enable_compression

    @enable_compression.setter
    def enable_compression(self, value: bool):
        self._enable_compression = bool(value)

    @property
    def build_all(self) -> bool:
        return self._build_all

    @build_all.setter
    def build_all(self, value: bool):
        self._build_all = bool(value)

    @property
    def flip_coordinate_system(self) -> bool:
        return self._flip_coordinate_system

    @flip_coordinate_system.setter
    def flip_coordinate_system(self, value: bool):
        self._flip_coordinate_system = bool(value)

    @property
    def unit(self) -> str:
        return self._unit

    @unit.setter
    def unit(self, value: str):
        valid_units = ['micron', 'millimeter', 'centimeter', 'inch', 'foot', 'meter']
        if value not in valid_units:
            raise ValueError(f'Invalid unit. Must be one of: {valid_units}')
        self._unit = value

    @property
    def pretty_print(self) -> bool:
        return self._pretty_print

    @pretty_print.setter
    def pretty_print(self, value: bool):
        self._pretty_print = bool(value)
