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

    @property
    def file_format(self) -> Optional['FileFormat']:
        return self._file_format

    @property
    def encoding(self) -> Optional[str]:
        return self._encoding

    @encoding.setter
    def encoding(self, value: Optional[str]):
        self._encoding = value

    @property
    def file_system(self):
        return self._file_system

    @file_system.setter
    def file_system(self, value):
        self._file_system = value

    @property
    def lookup_paths(self) -> list:
        return list(self._lookup_paths)

    @lookup_paths.setter
    def lookup_paths(self, value: list):
        self._lookup_paths = list(value)

    @property
    def file_name(self) -> Optional[str]:
        return self._file_name

    @file_name.setter
    def file_name(self, value: Optional[str]):
        self._file_name = value
