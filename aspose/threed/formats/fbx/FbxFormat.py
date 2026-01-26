from typing import List


class FbxFormat:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def extension(self) -> str:
        return "fbx"

    @property
    def extensions(self) -> List[str]:
        return ["fbx"]

    @property
    def content_type(self) -> str:
        return "application/octet-stream"

    @property
    def file_format_type(self):
        return None

    @property
    def version(self) -> str:
        return "7400"

    @property
    def can_export(self) -> bool:
        return False

    @property
    def can_import(self) -> bool:
        return True

    @property
    def formats(self) -> List:
        return []

    def create_load_options(self):
        from .FbxLoadOptions import FbxLoadOptions
        return FbxLoadOptions()

    def create_save_options(self):
        from .FbxSaveOptions import FbxSaveOptions
        return FbxSaveOptions()
