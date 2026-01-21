from typing import List


class StlFormat:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def extension(self) -> str:
        return "stl"

    @property
    def extensions(self) -> List[str]:
        return ["stl"]

    @property
    def content_type(self) -> str:
        return "model/stl"

    @property
    def file_format_type(self):
        return None

    @property
    def version(self) -> str:
        return ""

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
        from .StlLoadOptions import StlLoadOptions
        return StlLoadOptions()

    def create_save_options(self):
        from .StlSaveOptions import StlSaveOptions
        return StlSaveOptions(self)
