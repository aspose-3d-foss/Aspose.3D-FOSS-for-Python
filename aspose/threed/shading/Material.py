from ..A3DObject import A3DObject


class Material(A3DObject):
    MAP_SPECULAR = "Specular"
    MAP_DIFFUSE = "Diffuse"
    MAP_EMISSIVE = "Emissive"
    MAP_AMBIENT = "Ambient"
    MAP_NORMAL = "Normal"

    def __init__(self, name: str = None):
        super().__init__(name)

    def get_texture(self, slot_name: str):
        raise NotImplementedError("get_texture is not implemented")

    def set_texture(self, slot_name: str, texture):
        raise NotImplementedError("set_texture is not implemented")
