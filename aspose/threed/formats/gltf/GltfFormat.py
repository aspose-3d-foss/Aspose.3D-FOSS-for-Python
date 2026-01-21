from typing import List


class GltfFormat:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def extension(self) -> str:
        return "gltf"

    @property
    def extensions(self) -> List[str]:
        return ["gltf", "glb"]

    @property
    def content_type(self) -> str:
        return "model/gltf+json"

    @property
    def file_format_type(self):
        return None

    @property
    def version(self) -> str:
        return "2.0"

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
        from .GltfLoadOptions import GltfLoadOptions
        return GltfLoadOptions()

    def create_save_options(self):
        from .GltfSaveOptions import GltfSaveOptions
        return GltfSaveOptions()
