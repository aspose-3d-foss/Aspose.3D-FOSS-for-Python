from typing import TYPE_CHECKING

from .LambertMaterial import LambertMaterial

if TYPE_CHECKING:
    from ..utilities import Vector3


class PhongMaterial(LambertMaterial):
    def __init__(self, name: str = None):
        super().__init__(name)
        self._specular_color = None
        self._specular_factor = 0.0
        self._shininess = 0.0
        self._reflection_color = None
        self._reflection_factor = 0.0

    @property
    def specular_color(self) -> 'Vector3':
        return self._specular_color

    @specular_color.setter
    def specular_color(self, value: 'Vector3'):
        self._specular_color = value

    @property
    def specular_factor(self) -> float:
        return self._specular_factor

    @specular_factor.setter
    def specular_factor(self, value: float):
        self._specular_factor = float(value)

    @property
    def shininess(self) -> float:
        return self._shininess

    @shininess.setter
    def shininess(self, value: float):
        self._shininess = float(value)

    @property
    def reflection_color(self) -> 'Vector3':
        return self._reflection_color

    @reflection_color.setter
    def reflection_color(self, value: 'Vector3'):
        self._reflection_color = value

    @property
    def reflection_factor(self) -> float:
        return self._reflection_factor

    @reflection_factor.setter
    def reflection_factor(self, value: float):
        self._reflection_factor = float(value)
