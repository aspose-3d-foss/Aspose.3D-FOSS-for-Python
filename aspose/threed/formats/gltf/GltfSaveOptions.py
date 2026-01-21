from typing import TYPE_CHECKING

from ..SaveOptions import SaveOptions

if TYPE_CHECKING:
    from aspose.threed import FileFormat


class GltfSaveOptions(SaveOptions):
    def __init__(self, format: 'FileFormat' = None):
        super().__init__()
        self._file_format = format

    @property
    def file_format(self) -> 'FileFormat':
        return self._file_format
