from typing import TYPE_CHECKING

from .Geometry import Geometry
from ..utilities import BoundingBox

if TYPE_CHECKING:
    from ..utilities import BoundingBox
    from ..render import EntityRendererKey


class Primitive(Geometry):
    def __init__(self, name: str = None):
        if name is None:
            name = ""
        super().__init__(name)
        self._cast_shadows = True
        self._receive_shadows = True

    @property
    def cast_shadows(self) -> bool:
        return self._cast_shadows

    @cast_shadows.setter
    def cast_shadows(self, value: bool):
        self._cast_shadows = bool(value)

    @property
    def receive_shadows(self) -> bool:
        return self._receive_shadows

    @receive_shadows.setter
    def receive_shadows(self, value: bool):
        self._receive_shadows = bool(value)

    def to_mesh(self):
        raise NotImplementedError("to_mesh is not implemented for Primitive")
