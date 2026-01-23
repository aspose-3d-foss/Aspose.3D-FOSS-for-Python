from typing import List

class FbxFormat:
    _instance = None

    def __new__(cls, version="7.4.0", content_type="ASCII"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._version = version
            cls._instance._content_type = content_type
        return cls._instance

    @property
    def extension(self) -> str:
        return "fbx"

    @property
    def extensions(self) -> List[str]:
        return ["fbx", "FBX"]

    @property
    def content_type(self) -> str:
        return f"model/fbx-{self._version.lower()}-{self._content_type.lower()}"

    @property
    def file_format_type(self):
        return None

    @property
    def version(self) -> str:
        return self._version

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
