from typing import TYPE_CHECKING

from .Material import Material

if TYPE_CHECKING:
    from ..utilities import Vector3


class LambertMaterial(Material):
    MAP_SPECULAR = "Specular"
    MAP_DIFFUSE = "Diffuse"
    MAP_EMISSIVE = "Emissive"
    MAP_AMBIENT = "Ambient"
    MAP_NORMAL = "Normal"

    def __init__(self, name: str = None):
        super().__init__(name)
        self._emissive_color = None
        self._ambient_color = None
        self._diffuse_color = None
        self._transparent_color = None
        self._transparency = 0.0

    @property
    def emissive_color(self) -> 'Vector3':
        return self._emissive_color

    @emissive_color.setter
    def emissive_color(self, value: 'Vector3'):
        self._emissive_color = value

    @property
    def ambient_color(self) -> 'Vector3':
        return self._ambient_color

    @ambient_color.setter
    def ambient_color(self, value: 'Vector3'):
        self._ambient_color = value

    @property
    def diffuse_color(self) -> 'Vector3':
        return self._diffuse_color

    @diffuse_color.setter
    def diffuse_color(self, value: 'Vector3'):
        self._diffuse_color = value

    @property
    def transparent_color(self) -> 'Vector3':
        return self._transparent_color

    @transparent_color.setter
    def transparent_color(self, value: 'Vector3'):
        self._transparent_color = value

    @property
    def transparency(self) -> float:
        return self._transparency

    @transparency.setter
    def transparency(self, value: float):
        self._transparency = max(0.0, min(1.0, float(value)))
