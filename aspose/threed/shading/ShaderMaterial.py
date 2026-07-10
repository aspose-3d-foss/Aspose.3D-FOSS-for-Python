from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .ShaderTechnique import ShaderTechnique
    from .TextureBase import TextureBase
    from ..Property import Property


class ShaderMaterial:
    """A shader material allows to describe the material by external rendering engine or shader language."""
    
    MAP_SPECULAR = "MapSpecular"
    MAP_DIFFUSE = "MapDiffuse"
    MAP_EMISSIVE = "MapEmissive"
    MAP_AMBIENT = "MapAmbient"
    MAP_NORMAL = "MapNormal"
    
    def __init__(self, *args):
        raise NotImplementedError("ShaderMaterial is not implemented")
    
    def remove_property(self, property):
        raise NotImplementedError("ShaderMaterial.remove_property is not implemented")
    
    def get_property(self, property):
        raise NotImplementedError("ShaderMaterial.get_property is not implemented")
    
    def set_property(self, property, value):
        raise NotImplementedError("ShaderMaterial.set_property is not implemented")
    
    def find_property(self, property_name: str) -> 'Property':
        raise NotImplementedError("ShaderMaterial.find_property is not implemented")
    
    def get_texture(self, slot_name: str) -> 'TextureBase':
        raise NotImplementedError("ShaderMaterial.get_texture is not implemented")
    
    def set_texture(self, slot_name: str, texture: 'TextureBase') -> None:
        raise NotImplementedError("ShaderMaterial.set_texture is not implemented")
    
    @property
    def name(self) -> str:
        raise NotImplementedError("ShaderMaterial.name is not implemented")
    
    @name.setter
    def name(self, value: str) -> None:
        raise NotImplementedError("ShaderMaterial.name setter is not implemented")
    
    @property
    def techniques(self):
        raise NotImplementedError("ShaderMaterial.techniques is not implemented")
