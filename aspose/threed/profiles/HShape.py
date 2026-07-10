from typing import TYPE_CHECKING

from .ParameterizedProfile import ParameterizedProfile

if TYPE_CHECKING:
    from aspose.threed.utilities.Vector2 import Vector2


class HShape(ParameterizedProfile):
    """IFC compatible H-shape profile."""
    
    def __init__(self, name: str = None, width: float = 10.0, depth: float = 10.0, web_thickness: float = 1.0, flange_thickness: float = 1.0):
        super().__init__(name)
        self._width = width
        self._depth = depth
        self._web_thickness = web_thickness
        self._flange_thickness = flange_thickness
    
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
    
    @property
    def web_thickness(self) -> float:
        return self._web_thickness
    
    @web_thickness.setter
    def web_thickness(self, value: float):
        self._web_thickness = float(value)
    
    @property
    def flange_thickness(self) -> float:
        return self._flange_thickness
    
    @flange_thickness.setter
    def flange_thickness(self, value: float):
        self._flange_thickness = float(value)
    
    def get_extent(self) -> 'Vector2':
        """Gets the extent in x and y dimension."""
        from aspose.threed.utilities.Vector2 import Vector2
        return Vector2(self._width, self._depth)
