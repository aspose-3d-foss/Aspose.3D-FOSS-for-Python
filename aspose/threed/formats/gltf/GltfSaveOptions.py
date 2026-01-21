from typing import TYPE_CHECKING

from ..SaveOptions import SaveOptions

if TYPE_CHECKING:
    from aspose.threed import FileFormat


class GltfSaveOptions(SaveOptions):
    def __init__(self, file_format: 'FileFormat' = None):
        super().__init__()
        if file_format is not None:
            self._file_format = file_format
        self._binary_mode = False
        self._flip_tex_coord_v = True

    @property
    def file_format(self) -> 'FileFormat':
        return self._file_format

    @property
    def binary_mode(self) -> bool:
        return self._binary_mode

    @binary_mode.setter
    def binary_mode(self, value: bool):
        self._binary_mode = bool(value)

    @property
    def flip_tex_coord_v(self) -> bool:
        return self._flip_tex_coord_v

    @flip_tex_coord_v.setter
    def flip_tex_coord_v(self, value: bool):
        self._flip_tex_coord_v = bool(value)
