from typing import TYPE_CHECKING

from ..Entity import Entity

if TYPE_CHECKING:
    from aspose.threed.profiles.Profile import Profile
    from ..utilities.Vector3 import Vector3
    from ..utilities.Vector4 import Vector4
    from aspose.threed.entities.Mesh import Mesh


class LinearExtrusion(Entity):
    def __init__(self, name: str = None, shape: 'Profile' = None, height: float = 1.0):
        if name is None:
            name = "LinearExtrusion"
        super().__init__(name)
        self._shape = shape
        self._direction = None
        self._height = height
        self._slices = 1
        self._center = False
        self._twist_offset = None
        self._twist = 0.0
        self._init_defaults()

    def _init_defaults(self):
        from ..utilities.Vector3 import Vector3
        self._direction = Vector3(0, 0, 1)
        self._twist_offset = Vector3(0, 0, 0)

    @property
    def shape(self) -> 'Profile':
        return self._shape

    @shape.setter
    def shape(self, value: 'Profile'):
        self._shape = value

    @property
    def direction(self) -> 'Vector3':
        return self._direction

    @direction.setter
    def direction(self, value: 'Vector3'):
        self._direction = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        self._height = value

    @property
    def slices(self) -> int:
        return self._slices

    @slices.setter
    def slices(self, value: int):
        self._slices = value

    @property
    def center(self) -> bool:
        return self._center

    @center.setter
    def center(self, value: bool):
        self._center = bool(value)

    @property
    def twist_offset(self) -> 'Vector3':
        return self._twist_offset

    @twist_offset.setter
    def twist_offset(self, value: 'Vector3'):
        self._twist_offset = value

    @property
    def twist(self) -> float:
        return self._twist

    @twist.setter
    def twist(self, value: float):
        self._twist = value

    def to_mesh(self) -> 'Mesh':
        raise NotImplementedError("LinearExtrusion to_mesh is not implemented")
