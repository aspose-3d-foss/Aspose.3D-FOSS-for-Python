from typing import TYPE_CHECKING
import math

from .Primitive import Primitive

if TYPE_CHECKING:
    from ..utilities.Vector4 import Vector4
    from aspose.threed.entities.Mesh import Mesh


class Sphere(Primitive):
    def __init__(self, name: str = None, radius: float = 1.0, width_segments: int = 16,
                 height_segments: int = 16, phi_start: float = 0.0, phi_length: float = math.pi * 2,
                 theta_start: float = 0.0, theta_length: float = math.pi * 2):
        if name is None:
            name = "Sphere"
        super().__init__(name)
        self._radius = radius
        self._width_segments = width_segments
        self._height_segments = height_segments
        self._phi_start = phi_start
        self._phi_length = phi_length
        self._theta_start = theta_start
        self._theta_length = theta_length

    @property
    def width_segments(self) -> int:
        return self._width_segments

    @width_segments.setter
    def width_segments(self, value: int):
        self._width_segments = value

    @property
    def height_segments(self) -> int:
        return self._height_segments

    @height_segments.setter
    def height_segments(self, value: int):
        self._height_segments = value

    @property
    def phi_start(self) -> float:
        return self._phi_start

    @phi_start.setter
    def phi_start(self, value: float):
        self._phi_start = value

    @property
    def phi_length(self) -> float:
        return self._phi_length

    @phi_length.setter
    def phi_length(self, value: float):
        self._phi_length = value

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

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        self._radius = value

    def to_mesh(self):
        from ..utilities.Vector4 import Vector4
        from aspose.threed.entities.Mesh import Mesh
        mesh = Mesh(self.name)
        radius = self._radius

        for lat in range(self._height_segments + 1):
            theta = self._theta_start + self._theta_length * lat / self._height_segments
            sin_theta = math.sin(theta)
            cos_theta = math.cos(theta)

            for lon in range(self._width_segments + 1):
                phi = self._phi_start + self._phi_length * lon / self._width_segments
                sin_phi = math.sin(phi)
                cos_phi = math.cos(phi)

                x = radius * cos_phi * sin_theta
                y = radius * cos_theta
                z = radius * sin_phi * sin_theta

                mesh._control_points.append(Vector4(x, y, z, 1))

        for lat in range(self._height_segments):
            for lon in range(self._width_segments):
                first = lat * (self._width_segments + 1) + lon
                second = first + self._width_segments + 1

                mesh.create_polygon(first, second, second + 1, first + 1)

        return mesh
