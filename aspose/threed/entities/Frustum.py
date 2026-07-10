from typing import TYPE_CHECKING
import math

from .Primitive import Primitive

if TYPE_CHECKING:
    from ..utilities.Vector4 import Vector4
    from aspose.threed.entities.Mesh import Mesh


class Frustum(Primitive):
    def __init__(self, name: str = None, radius_top: float = 1.0, radius_bottom: float = 1.0,
                 height: float = 1.0, radial_segments: int = 32, height_segments: int = 1,
                 theta_start: float = 0.0, theta_length: float = math.pi * 2):
        if name is None:
            name = "Frustum"
        super().__init__(name)
        self._radius_top = radius_top
        self._radius_bottom = radius_bottom
        self._height = height
        self._radial_segments = radial_segments
        self._height_segments = height_segments
        self._theta_start = theta_start
        self._theta_length = theta_length

    @property
    def radius_top(self) -> float:
        return self._radius_top

    @radius_top.setter
    def radius_top(self, value: float):
        self._radius_top = value

    @property
    def radius_bottom(self) -> float:
        return self._radius_bottom

    @radius_bottom.setter
    def radius_bottom(self, value: float):
        self._radius_bottom = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        self._height = value

    @property
    def radial_segments(self) -> int:
        return self._radial_segments

    @radial_segments.setter
    def radial_segments(self, value: int):
        self._radial_segments = value

    @property
    def height_segments(self) -> int:
        return self._height_segments

    @height_segments.setter
    def height_segments(self, value: int):
        self._height_segments = value

    @property
    def theta_start(self) -> float:
        return self._theta_start

    @theta_start.setter
    def theta_start(self, value: float):
        self._theta_start = value

    @property
    def theta_length(self) -> float:
        return self._theta_length

    @theta_length.setter
    def theta_length(self, value: float):
        self._theta_length = value

    def to_mesh(self) -> 'Mesh':
        from ..utilities.Vector4 import Vector4
        from aspose.threed.entities.Mesh import Mesh
        mesh = Mesh(self.name)
        radius_top = self._radius_top
        radius_bottom = self._radius_bottom
        height = self._height
        half_height = height / 2

        for i in range(self._radial_segments + 1):
            angle = self._theta_start + self._theta_length * i / self._radial_segments
            sin_angle = math.sin(angle)
            cos_angle = math.cos(angle)

            x = radius_top * cos_angle
            z = radius_top * sin_angle
            mesh._control_points.append(Vector4(x, half_height, z, 1))

        for i in range(self._radial_segments + 1):
            angle = self._theta_start + self._theta_length * i / self._radial_segments
            sin_angle = math.sin(angle)
            cos_angle = math.cos(angle)

            x = radius_bottom * cos_angle
            z = radius_bottom * sin_angle
            mesh._control_points.append(Vector4(x, -half_height, z, 1))

        for i in range(self._radial_segments):
            mesh.create_polygon(i, i + 1, self._radial_segments + i + 2, self._radial_segments + i + 1)

        return mesh
