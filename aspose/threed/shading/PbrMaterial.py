from typing import TYPE_CHECKING

from .Material import Material

if TYPE_CHECKING:
    from ..utilities import Vector3


class PbrMaterial(Material):
    def __init__(self, name: str = None, albedo: 'Vector3' = None):
        super().__init__(name)
        self._albedo = albedo
        self._albedo_texture = None
        self._normal_texture = None
        self._metallic_factor = 0.0
        self._roughness_factor = 0.0
        self._metallic_roughness = None
        self._occlusion_texture = None
        self._occlusion_factor = 0.0
        self._emissive_texture = None
        self._emissive_color = None
        self._transparency = 0.0

    @property
    def albedo(self) -> 'Vector3':
        return self._albedo

    @albedo.setter
    def albedo(self, value: 'Vector3'):
        self._albedo = value

    @property
    def albedo_texture(self):
        return self._albedo_texture

    @albedo_texture.setter
    def albedo_texture(self, value):
        self._albedo_texture = value

    @property
    def normal_texture(self):
        return self._normal_texture

    @normal_texture.setter
    def normal_texture(self, value):
        self._normal_texture = value

    @property
    def metallic_factor(self) -> float:
        return self._metallic_factor

    @metallic_factor.setter
    def metallic_factor(self, value: float):
        self._metallic_factor = float(value)

    @property
    def roughness_factor(self) -> float:
        return self._roughness_factor

    @roughness_factor.setter
    def roughness_factor(self, value: float):
        self._roughness_factor = float(value)

    @property
    def metallic_roughness(self):
        return self._metallic_roughness

    @metallic_roughness.setter
    def metallic_roughness(self, value):
        self._metallic_roughness = value

    @property
    def occlusion_texture(self):
        return self._occlusion_texture

    @occlusion_texture.setter
    def occlusion_texture(self, value):
        self._occlusion_texture = value

    @property
    def occlusion_factor(self) -> float:
        return self._occlusion_factor

    @occlusion_factor.setter
    def occlusion_factor(self, value: float):
        self._occlusion_factor = float(value)

    @property
    def emissive_texture(self):
        return self._emissive_texture

    @emissive_texture.setter
    def emissive_texture(self, value):
        self._emissive_texture = value

    @property
    def emissive_color(self) -> 'Vector3':
        return self._emissive_color

    @emissive_color.setter
    def emissive_color(self, value: 'Vector3'):
        self._emissive_color = value

    @property
    def transparency(self) -> float:
        return self._transparency

    @transparency.setter
    def transparency(self, value: float):
        self._transparency = float(value)

    @staticmethod
    def from_material(material: 'Material') -> 'PbrMaterial':
        return PbrMaterial(material.name if material else None)
