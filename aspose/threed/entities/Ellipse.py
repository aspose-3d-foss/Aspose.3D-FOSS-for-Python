from typing import TYPE_CHECKING
import math

from .Primitive import Primitive

if TYPE_CHECKING:
    from ..utilities.Vector4 import Vector4
    from aspose.threed.entities.Mesh import Mesh


class Ellipse(Primitive):
    def __init__(self, name: str = None, radius_x: float = 1.0, radius_y: float = 1.0,
                 segments: int = 16, theta_start: float = 0.0, theta_length: float = math.pi * 2):
        if name is None:
            name = "Ellipse"
        super().__init__(name)
        self._radius_x = radius_x
        self._radius_y = radius_y
        self._segments = segments
        self._theta_start = theta_start
        self._theta_length = theta_length

    @property
    def radius_x(self) -> float:
        return self._radius_x

    @radius_x.setter
    def radius_x(self, value: float):
        self._radius_x = value

    @property
    def radius_y(self) -> float:
        return self._radius_y

    @radius_y.setter
    def radius_y(self, value: float):
        self._radius_y = value

    @property
    def segments(self) -> int:
        return self._segments

    @segments.setter
    def segments(self, value: int):
        self._segments = value

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
        radius_x = self._radius_x
        radius_y = self._radius_y

        for i in range(self._segments + 1):
            angle = self._theta_start + self._theta_length * i / self._segments
            x = radius_x * math.cos(angle)
            y = 0
            z = radius_y * math.sin(angle)
            mesh._control_points.append(Vector4(x, y, z, 1))

        center_index = len(mesh._control_points)
        mesh._control_points.append(Vector4(0, 0, 0, 1))

        for i in range(self._segments):
            mesh.create_polygon(i, i + 1, center_index)

        return mesh
