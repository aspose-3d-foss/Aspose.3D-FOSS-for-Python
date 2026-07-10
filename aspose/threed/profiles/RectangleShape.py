from typing import TYPE_CHECKING

from .ParameterizedProfile import ParameterizedProfile

if TYPE_CHECKING:
    from aspose.threed.utilities.Vector2 import Vector2


class RectangleShape(ParameterizedProfile):
    """IFC compatible rectangle profile."""
    
    def __init__(self, name: str = None, width: float = 10.0, depth: float = 10.0):
        super().__init__(name)
        self._width = width
        self._depth = depth
    
    @property
    def width(self) -> float:
        return self._width
    
    @width.setter
    def width(self, value: float):
        self._width = float(value)
    
    @property
    def depth(self) -> float:
        return self._depth
    
    @depth.setter
    def depth(self, value: float):
        self._depth = float(value)
    
    def get_extent(self) -> 'Vector2':
        """Gets the extent in x and y dimension."""
        from aspose.threed.utilities.Vector2 import Vector2
        return Vector2(self._width, self._depth)
