from typing import TYPE_CHECKING

from .RectangleShape import RectangleShape

if TYPE_CHECKING:
    from aspose.threed.utilities.Vector2 import Vector2


class HollowRectangleShape(RectangleShape):
    """IFC compatible hollow rectangular shape with both inner/outer rounding corners."""
    
    def __init__(self, name: str = None):
        super().__init__(name)
        self._wall_thickness = 1.0
        self._external_fillet_radius = 0.0
        self._internal_fillet_radius = 0.0
    
    @property
    def wall_thickness(self) -> float:
        return self._wall_thickness
    
    @wall_thickness.setter
    def wall_thickness(self, value: float):
        self._wall_thickness = float(value)
    
    @property
    def external_fillet_radius(self) -> float:
        return self._external_fillet_radius
    
    @external_fillet_radius.setter
    def external_fillet_radius(self, value: float):
        self._external_fillet_radius = float(value)
    
    @property
    def internal_fillet_radius(self) -> float:
        return self._internal_fillet_radius
    
    @internal_fillet_radius.setter
    def internal_fillet_radius(self, value: float):
        self._internal_fillet_radius = float(value)
    
    def get_extent(self) -> 'Vector2':
        """Gets the extent in x and y dimension."""
        from aspose.threed.utilities.Vector2 import Vector2
        return Vector2(self.width, self.depth)
