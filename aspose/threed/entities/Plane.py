from typing import TYPE_CHECKING

from .Primitive import Primitive
from ..utilities.Vector3 import Vector3

if TYPE_CHECKING:
    from .Mesh import Mesh


class Plane(Primitive):
    def __init__(self, name: str = None, length: float = 1.0, width: float = 1.0,
                 length_segments: int = 1, width_segments: int = 1):
        if name is None:
            name = "Plane"
        super().__init__(name)
        self._length = length
        self._width = width
        self._length_segments = length_segments
        self._width_segments = width_segments
        self._up = Vector3(0, 1, 0)

    @property
    def up(self) -> Vector3:
        return self._up

    @up.setter
    def up(self, value: Vector3):
        self._up = value

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

    def to_mesh(self) -> 'Mesh':
        from aspose.threed.entities.Mesh import Mesh
        mesh = Mesh(self.name)
        return mesh
