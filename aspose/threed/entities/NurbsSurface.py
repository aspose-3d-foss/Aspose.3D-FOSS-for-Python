from typing import TYPE_CHECKING

from .Geometry import Geometry

if TYPE_CHECKING:
    from .NurbsDirection import NurbsDirection


class NurbsSurface(Geometry):
    def __init__(self, name: str = None):
        if name is None:
            name = "NurbsSurface"
        super().__init__(name)
        from .NurbsDirection import NurbsDirection
        self._u = NurbsDirection()
        self._v = NurbsDirection()

    @property
    def u(self) -> 'NurbsDirection':
        return self._u

    @property
    def v(self) -> 'NurbsDirection':
        return self._v

    def to_mesh(self):
        raise NotImplementedError("NURBS surface to mesh conversion is not implemented")
