from typing import TYPE_CHECKING

from .CircleShape import CircleShape

if TYPE_CHECKING:
    from aspose.threed.utilities.Vector2 import Vector2


class HollowCircleShape(CircleShape):
    """IFC compatible hollow circle profile."""
    
    def __init__(self, name: str = None):
        super().__init__(name)
        self._wall_thickness = 1.0
    
    @property
    def wall_thickness(self) -> float:
        return self._wall_thickness
    
    @wall_thickness.setter
    def wall_thickness(self, value: float):
        self._wall_thickness = float(value)
    
    def get_extent(self) -> 'Vector2':
        """Gets the extent in x and y dimension."""
        from aspose.threed.utilities.Vector2 import Vector2
        return Vector2(self.radius * 2, self.radius * 2)
