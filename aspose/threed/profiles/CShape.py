from typing import TYPE_CHECKING

from .ParameterizedProfile import ParameterizedProfile

if TYPE_CHECKING:
    from aspose.threed.utilities.Vector2 import Vector2


class CShape(ParameterizedProfile):
    """IFC compatible C-shape profile that defined by parameters.
    The center position of the profile is in the center of the bounding box."""
    
    def __init__(self, name: str = None):
        super().__init__(name)
        self._depth = 10.0
        self._width = 10.0
        self._girth = 10.0
        self._wall_thickness = 1.0
        self._internal_fillet_radius = 0.0
    
    @property
    def depth(self) -> float:
        return self._depth
    
    @depth.setter
    def depth(self, value: float):
        self._depth = float(value)
    
    @property
    def width(self) -> float:
        return self._width
    
    @width.setter
    def width(self, value: float):
        self._width = float(value)
    
    @property
    def girth(self) -> float:
        return self._girth
    
    @girth.setter
    def girth(self, value: float):
        self._girth = float(value)
    
    @property
    def wall_thickness(self) -> float:
        return self._wall_thickness
    
    @wall_thickness.setter
    def wall_thickness(self, value: float):
        self._wall_thickness = float(value)
    
    @property
    def internal_fillet_radius(self) -> float:
        return self._internal_fillet_radius
    
    @internal_fillet_radius.setter
    def internal_fillet_radius(self, value: float):
        self._internal_fillet_radius = float(value)
    
    def get_extent(self) -> 'Vector2':
        """Gets the extent in x and y dimension."""
        from aspose.threed.utilities.Vector2 import Vector2
        return Vector2(self._width, self._depth)
