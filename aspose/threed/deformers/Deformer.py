from typing import TYPE_CHECKING

from ..A3DObject import A3DObject

if TYPE_CHECKING:
    from ..entities.Geometry import Geometry


class Deformer(A3DObject):
    def __init__(self, name: str = None):
        super().__init__(name)
        self._owner = None

    @property
    def owner(self) -> 'Geometry':
        if self._owner is None:
            raise RuntimeError("Owner is not set")
        return self._owner
