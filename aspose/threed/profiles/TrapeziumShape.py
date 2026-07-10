from typing import TYPE_CHECKING

from .ParameterizedProfile import ParameterizedProfile

if TYPE_CHECKING:
    from aspose.threed.utilities.Vector2 import Vector2


class TrapeziumShape(ParameterizedProfile):
    """IFC compatible Trapezium shape defined by parameters."""
    
    def __init__(self, name: str = None):
        super().__init__(name)
        self._bottom_x_dim = 10.0
        self._top_x_dim = 8.0
        self._y_dim = 10.0
        self._top_x_offset = 1.0
    
    @property
    def bottom_x_dim(self) -> float:
        return self._bottom_x_dim
    
    @bottom_x_dim.setter
    def bottom_x_dim(self, value: float):
        self._bottom_x_dim = float(value)
    
    @property
    def top_x_dim(self) -> float:
        return self._top_x_dim
    
    @top_x_dim.setter
    def top_x_dim(self, value: float):
        self._top_x_dim = float(value)
    
    @property
    def y_dim(self) -> float:
        return self._y_dim
    
    @y_dim.setter
    def y_dim(self, value: float):
        self._y_dim = float(value)
    
    @property
    def top_x_offset(self) -> float:
        return self._top_x_offset
    
    @top_x_offset.setter
    def top_x_offset(self, value: float):
        self._top_x_offset = float(value)
    
    def get_extent(self) -> 'Vector2':
        """Gets the extent in x and y dimension."""
        from aspose.threed.utilities.Vector2 import Vector2
        return Vector2(self._bottom_x_dim, self._y_dim)
