from typing import TYPE_CHECKING
import math

from .Primitive import Primitive

if TYPE_CHECKING:
    from ..utilities.Vector4 import Vector4
    from aspose.threed.entities.Mesh import Mesh


class Circle(Primitive):
    def __init__(self, name: str = None, radius: float = 1.0, segments: int = 16,
                 theta_start: float = 0.0, theta_length: float = math.pi * 2):
        if name is None:
            name = "Circle"
        super().__init__(name)
        self._radius = radius
        self._segments = segments
        self._theta_start = theta_start
        self._theta_length = theta_length

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        self._radius = value

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
        radius = self._radius

        for i in range(self._segments + 1):
            angle = self._theta_start + self._theta_length * i / self._segments
            x = radius * math.cos(angle)
            y = 0
            z = radius * math.sin(angle)
            mesh._control_points.append(Vector4(x, y, z, 1))

        center_index = len(mesh._control_points)
        mesh._control_points.append(Vector4(0, 0, 0, 1))

        for i in range(self._segments):
            mesh.create_polygon(i, i + 1, center_index)

        return mesh
