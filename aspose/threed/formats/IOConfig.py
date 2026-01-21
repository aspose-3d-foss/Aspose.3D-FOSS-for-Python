from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from aspose.threed import FileFormat
    from aspose.threed.utilities import FileSystem


class IOConfig:
    def __init__(self):
        self._file_format: 'FileFormat' = None
        self._encoding = ''
        self._file_system: 'FileSystem' = None
        self._lookup_paths: List[str] = []
        self._file_name = ''

    @property
    def file_format(self) -> 'FileFormat':
        return self._file_format

    @property
    def encoding(self) -> str:
        return self._encoding

    @encoding.setter
    def encoding(self, value: str):
        self._encoding = value

    @property
    def file_system(self) -> 'FileSystem':
        return self._file_system

    @file_system.setter
    def file_system(self, value: 'FileSystem'):
        self._file_system = value

    @property
    def lookup_paths(self) -> List[str]:
        return list(self._lookup_paths)

    @lookup_paths.setter
    def lookup_paths(self, value: List[str]):
        self._lookup_paths = list(value)

    @property
    def file_name(self) -> str:
        return self._file_name

    @file_name.setter
    def file_name(self, value: str):
        self._file_name = value
