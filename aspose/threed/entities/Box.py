from typing import TYPE_CHECKING

from .Primitive import Primitive
from ..utilities.Vector4 import Vector4

if TYPE_CHECKING:
    from .Mesh import Mesh


class Box(Primitive):
    def __init__(self, name: str = None, length: float = 1.0, width: float = 1.0, height: float = 1.0,
                 length_segments: int = 1, width_segments: int = 1, height_segments: int = 1):
        if name is None:
            name = "Box"
        super().__init__(name)
        self._length = length
        self._width = width
        self._height = height
        self._length_segments = length_segments
        self._width_segments = width_segments
        self._height_segments = height_segments

    @property
    def length_segments(self) -> int:
        return self._length_segments

    @length_segments.setter
    def length_segments(self, value: int):
        self._length_segments = value

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
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, value: float):
        self._length = value

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float):
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        self._height = value

    def to_mesh(self) -> 'Mesh':
        from aspose.threed.entities.Mesh import Mesh
        mesh = Mesh(self.name)
        half_length = self._length / 2
        half_width = self._width / 2
        half_height = self._height / 2

        mesh._control_points.append(Vector4(-half_width, -half_height, -half_length, 1))
        mesh._control_points.append(Vector4(half_width, -half_height, -half_length, 1))
        mesh._control_points.append(Vector4(half_width, half_height, -half_length, 1))
        mesh._control_points.append(Vector4(-half_width, half_height, -half_length, 1))
        mesh._control_points.append(Vector4(-half_width, -half_height, half_length, 1))
        mesh._control_points.append(Vector4(half_width, -half_height, half_length, 1))
        mesh._control_points.append(Vector4(half_width, half_height, half_length, 1))
        mesh._control_points.append(Vector4(-half_width, half_height, half_length, 1))

        mesh.create_polygon(0, 1, 2, 3)
        mesh.create_polygon(4, 5, 6, 7)
        mesh.create_polygon(0, 4, 7, 3)
        mesh.create_polygon(1, 5, 6, 2)
        mesh.create_polygon(0, 1, 5, 4)
        mesh.create_polygon(3, 2, 6, 7)

        return mesh
