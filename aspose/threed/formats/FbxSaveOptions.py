class FbxSaveOptions:
    """Save options for FBX"""

    def __init__(self, format=None, content_type=None):
        self._reuse_primitive_mesh = False
        self._enable_compression = False
        self._fold_repeated_curve_data = None
        self._export_legacy_material_properties = False
        self._video_for_texture = False
        self._embed_textures = False
        self._generate_vertex_element_material = False

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
    def fold_repeated_curve_data(self):
        return self._fold_repeated_curve_data

    @fold_repeated_curve_data.setter
    def fold_repeated_curve_data(self, value):
        self._fold_repeated_curve_data = value

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
