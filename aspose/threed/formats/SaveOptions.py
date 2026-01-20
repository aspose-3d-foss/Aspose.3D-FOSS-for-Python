from typing import TYPE_CHECKING

from .IOConfig import IOConfig

if TYPE_CHECKING:
    from aspose.threed import FileFormat


class SaveOptions(IOConfig):
    def __init__(self):
        super().__init__()
        self._export_textures = False

    @property
    def export_textures(self) -> bool:
        return self._export_textures

    @export_textures.setter
    def export_textures(self, value: bool):
        self._export_textures = value
