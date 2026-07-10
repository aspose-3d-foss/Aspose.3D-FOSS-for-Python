from typing import TYPE_CHECKING
import math

from .Primitive import Primitive

if TYPE_CHECKING:
    from ..utilities.Vector4 import Vector4
    from aspose.threed.entities.Mesh import Mesh


class Dish(Primitive):
    def __init__(self, name: str = None, radius: float = 10.0, height: float = 5.0,
                 width_segments: int = 32, height_segments: int = 16):
        if name is None:
            name = "Dish"
        super().__init__(name)
        self._radius = radius
        self._height = height
        self._width_segments = width_segments
        self._height_segments = height_segments

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        self._radius = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        self._height = value

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

    def to_mesh(self) -> 'Mesh':
        from ..utilities.Vector4 import Vector4
        from aspose.threed.entities.Mesh import Mesh
        mesh = Mesh(self.name)
        radius = self._radius
        height = self._height

        for lat in range(self._height_segments + 1):
            t = lat / self._height_segments
            z = height * t
            r = math.sqrt(2 * radius * z - z * z)

            for lon in range(self._width_segments + 1):
                angle = 2 * math.pi * lon / self._width_segments
                x = r * math.cos(angle)
                y = r * math.sin(angle)

                mesh._control_points.append(Vector4(x, y, z, 1))

        for lat in range(self._height_segments):
            for lon in range(self._width_segments):
                first = lat * (self._width_segments + 1) + lon
                second = first + self._width_segments + 1

                mesh.create_polygon(first, second, second + 1, first + 1)

        return mesh

    def get_bounding_box(self):
        from ..utilities import BoundingBox
        from ..utilities.FVector3 import FVector3
        radius = float(self._radius)
        height = float(self._height)
        min_vec = FVector3(-radius, -radius, 0)
        max_vec = FVector3(radius, radius, height)
        return BoundingBox(min_vec, max_vec)
