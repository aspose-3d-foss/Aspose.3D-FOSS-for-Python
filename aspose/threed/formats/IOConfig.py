from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from aspose.threed import FileFormat


class IOConfig:
    def __init__(self):
        self._file_format = None
        self._encoding = None
        self._file_system = None
        self._lookup_paths = []
        self._file_name = None
