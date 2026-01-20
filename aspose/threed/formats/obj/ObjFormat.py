from typing import List


class ObjFormat:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def extension(self) -> str:
        return "obj"

    @property
    def extensions(self) -> List[str]:
        return ["obj"]

    @property
    def content_type(self) -> str:
        return "model/obj"

    @property
    def file_format_type(self):
        return None

    @property
    def version(self) -> str:
        return ""

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
        from .ObjLoadOptions import ObjLoadOptions
        return ObjLoadOptions()

    def create_save_options(self):
        from .ObjSaveOptions import ObjSaveOptions
        return ObjSaveOptions()
