from typing import TYPE_CHECKING

from ..SaveOptions import SaveOptions

if TYPE_CHECKING:
    from aspose.threed import FileFormat

class FbxSaveOptions(SaveOptions):
    def __init__(self, file_format=None):
        super().__init__()
        if file_format is not None:
            self._file_format = file_format
        self._export_textures = False
        self._reuse_primitive_mesh = False
        self._enable_compression = True
        self._export_legacy_material_properties = True
        self._video_for_texture = False
        self._embed_textures = False
        self._generate_vertex_element_material = False

    @property
    def export_textures(self) -> bool:
        return self._export_textures

    @export_textures.setter
    def export_textures(self, value: bool):
        self._export_textures = bool(value)

    @property
    def reuse_primitive_mesh(self) -> bool:
        return self._reuse_primitive_mesh

    @reuse_primitive_mesh.setter
    def reuse_primitive_mesh(self, value: bool):
        self._reuse_primitive_mesh = bool(value)

    @property
    def enable_compression(self) -> bool:
        return self._enable_compression

    @enable_compression.setter
    def enable_compression(self, value: bool):
        self._enable_compression = bool(value)

    @property
    def export_legacy_material_properties(self) -> bool:
        return self._export_legacy_material_properties

    @export_legacy_material_properties.setter
    def export_legacy_material_properties(self, value: bool):
        self._export_legacy_material_properties = bool(value)

    @property
    def video_for_texture(self) -> bool:
        return self._video_for_texture

    @video_for_texture.setter
    def video_for_texture(self, value: bool):
        self._video_for_texture = bool(value)

    @property
    def embed_textures(self) -> bool:
        return self._embed_textures

    @embed_textures.setter
    def embed_textures(self, value: bool):
        self._embed_textures = bool(value)

    @property
    def generate_vertex_element_material(self) -> bool:
        return self._generate_vertex_element_material

    @generate_vertex_element_material.setter
    def generate_vertex_element_material(self, value: bool):
        self._generate_vertex_element_material = bool(value)
