from typing import List
from ...FileFormat import FileFormat


class ColladaFormat(FileFormat):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def extension(self) -> str:
        return "dae"

    @property
    def extensions(self) -> List[str]:
        return ["dae"]

    @property
    def content_type(self) -> str:
        return "model/vnd.collada+xml"

    @property
    def file_format_type(self):
        return None

    @property
    def version(self) -> str:
        return "1.4.1"

    @property
    def can_export(self) -> bool:
        return True

    @property
    def can_import(self) -> bool:
        return True

    @property
    def formats(self) -> List:
        return []

    def create_load_options(self):
        from .ColladaLoadOptions import ColladaLoadOptions
        return ColladaLoadOptions()

    def create_save_options(self):
        from .ColladaSaveOptions import ColladaSaveOptions
        return ColladaSaveOptions()
