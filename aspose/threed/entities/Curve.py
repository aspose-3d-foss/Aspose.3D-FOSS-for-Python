from typing import TYPE_CHECKING

from ..Entity import Entity

if TYPE_CHECKING:
    from .utilities import Vector3


class Curve(Entity):
    def __init__(self, name: str = None):
        if name is None:
            name = ""
        super().__init__(name)
        self._color = None

    @property
    def color(self) -> 'Vector3':
        if self._color is None:
            from .utilities.Vector3 import Vector3
            self._color = Vector3(1, 1, 1)
        return self._color

    @color.setter
    def color(self, value: 'Vector3'):
        self._color = value
