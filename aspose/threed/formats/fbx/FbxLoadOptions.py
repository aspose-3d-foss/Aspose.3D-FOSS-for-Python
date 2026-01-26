from typing import TYPE_CHECKING

from ..LoadOptions import LoadOptions

if TYPE_CHECKING:
    from aspose.threed import FileFormat


class FbxLoadOptions(LoadOptions):
    def __init__(self, format=None):
        super().__init__()
        self._keep_builtin_global_settings = False
        self._compatible_mode = False
        if format is not None:
            self._file_format = format

    @property
    def keep_builtin_global_settings(self) -> bool:
        return self._keep_builtin_global_settings

    @keep_builtin_global_settings.setter
    def keep_builtin_global_settings(self, value: bool):
        self._keep_builtin_global_settings = bool(value)

    @property
    def compatible_mode(self) -> bool:
        return self._compatible_mode

    @compatible_mode.setter
    def compatible_mode(self, value: bool):
        self._compatible_mode = bool(value)
