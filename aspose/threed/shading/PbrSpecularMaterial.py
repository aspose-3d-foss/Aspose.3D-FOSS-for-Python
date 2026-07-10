from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .TextureBase import TextureBase
    from ..Property import Property


class PbrSpecularMaterial:
    """Material for physically based rendering based on diffuse color/specular/glossiness."""
    
    MAP_SPECULAR = "MapSpecular"
    MAP_DIFFUSE = "MapDiffuse"
    MAP_EMISSIVE = "MapEmissive"
    MAP_AMBIENT = "MapAmbient"
    MAP_NORMAL = "MapNormal"
    MAP_SPECULAR_GLOSSINESS = "MapSpecularGlossiness"
    
    def __init__(self, *args):
        raise NotImplementedError("PbrSpecularMaterial is not implemented")
    
    def remove_property(self, property):
        raise NotImplementedError("PbrSpecularMaterial.remove_property is not implemented")
    
    def get_property(self, property):
        raise NotImplementedError("PbrSpecularMaterial.get_property is not implemented")
    
    def set_property(self, property, value):
        raise NotImplementedError("PbrSpecularMaterial.set_property is not implemented")
    
    def find_property(self, property_name: str) -> 'Property':
        raise NotImplementedError("PbrSpecularMaterial.find_property is not implemented")
    
    def get_texture(self, slot_name: str) -> 'TextureBase':
        raise NotImplementedError("PbrSpecularMaterial.get_texture is not implemented")
    
    def set_texture(self, slot_name: str, texture: 'TextureBase') -> None:
        raise NotImplementedError("PbrSpecularMaterial.set_texture is not implemented")
    
    @property
    def name(self) -> str:
        raise NotImplementedError("PbrSpecularMaterial.name is not implemented")
    
    @name.setter
    def name(self, value: str) -> None:
        raise NotImplementedError("PbrSpecularMaterial.name setter is not implemented")
    
    @property
    def properties(self):
        raise NotImplementedError("PbrSpecularMaterial.properties is not implemented")
    
    @property
    def transparency(self) -> float:
        raise NotImplementedError("PbrSpecularMaterial.transparency is not implemented")
    
    @transparency.setter
    def transparency(self, value: float) -> None:
        raise NotImplementedError("PbrSpecularMaterial.transparency setter is not implemented")
    
    @property
    def normal_texture(self) -> 'TextureBase':
        raise NotImplementedError("PbrSpecularMaterial.normal_texture is not implemented")
    
    @normal_texture.setter
    def normal_texture(self, value: 'TextureBase') -> None:
        raise NotImplementedError("PbrSpecularMaterial.normal_texture setter is not implemented")
    
    @property
    def specular_glossiness_texture(self) -> 'TextureBase':
        raise NotImplementedError("PbrSpecularMaterial.specular_glossiness_texture is not implemented")
    
    @specular_glossiness_texture.setter
    def specular_glossiness_texture(self, value: 'TextureBase') -> None:
        raise NotImplementedError("PbrSpecularMaterial.specular_glossiness_texture setter is not implemented")
    
    @property
    def glossiness_factor(self) -> float:
        raise NotImplementedError("PbrSpecularMaterial.glossiness_factor is not implemented")
    
    @glossiness_factor.setter
    def glossiness_factor(self, value: float) -> None:
        raise NotImplementedError("PbrSpecularMaterial.glossiness_factor setter is not implemented")
    
    @property
    def specular(self):
        raise NotImplementedError("PbrSpecularMaterial.specular is not implemented")
    
    @specular.setter
    def specular(self, value):
        raise NotImplementedError("PbrSpecularMaterial.specular setter is not implemented")
    
    @property
    def diffuse_texture(self) -> 'TextureBase':
        raise NotImplementedError("PbrSpecularMaterial.diffuse_texture is not implemented")
    
    @diffuse_texture.setter
    def diffuse_texture(self, value: 'TextureBase') -> None:
        raise NotImplementedError("PbrSpecularMaterial.diffuse_texture setter is not implemented")
    
    @property
    def diffuse(self):
        raise NotImplementedError("PbrSpecularMaterial.diffuse is not implemented")
    
    @diffuse.setter
    def diffuse(self, value):
        raise NotImplementedError("PbrSpecularMaterial.diffuse setter is not implemented")
    
    @property
    def emissive_texture(self) -> 'TextureBase':
        raise NotImplementedError("PbrSpecularMaterial.emissive_texture is not implemented")
    
    @emissive_texture.setter
    def emissive_texture(self, value: 'TextureBase') -> None:
        raise NotImplementedError("PbrSpecularMaterial.emissive_texture setter is not implemented")
    
    @property
    def emissive_color(self):
        raise NotImplementedError("PbrSpecularMaterial.emissive_color is not implemented")
    
    @emissive_color.setter
    def emissive_color(self, value):
        raise NotImplementedError("PbrSpecularMaterial.emissive_color setter is not implemented")
