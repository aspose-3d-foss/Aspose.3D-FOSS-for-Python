from typing import TYPE_CHECKING

from .Geometry import Geometry

if TYPE_CHECKING:
    from .PatchDirection import PatchDirection


class Patch(Geometry):
    def __init__(self, name: str = None):
        if name is None:
            name = "Patch"
        super().__init__(name)
        from .PatchDirection import PatchDirection
        self._u = PatchDirection()
        self._v = PatchDirection()

    @property
    def u(self) -> 'PatchDirection':
        return self._u

    @property
    def v(self) -> 'PatchDirection':
        return self._v
