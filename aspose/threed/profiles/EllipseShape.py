from typing import TYPE_CHECKING

from .ParameterizedProfile import ParameterizedProfile

if TYPE_CHECKING:
    from aspose.threed.utilities.Vector2 import Vector2


class EllipseShape(ParameterizedProfile):
    """IFC compatible ellipse profile."""
    
    def __init__(self, name: str = None, semi_axis1: float = 5.0, semi_axis2: float = 5.0):
        super().__init__(name)
        self._semi_axis1 = semi_axis1
        self._semi_axis2 = semi_axis2
    
    @property
    def semi_axis1(self) -> float:
        return self._semi_axis1
    
    @semi_axis1.setter
    def semi_axis1(self, value: float):
        self._semi_axis1 = float(value)
    
    @property
    def semi_axis2(self) -> float:
        return self._semi_axis2
    
    @semi_axis2.setter
    def semi_axis2(self, value: float):
        self._semi_axis2 = float(value)
    
    def get_extent(self) -> 'Vector2':
        """Gets the extent in x and y dimension."""
        from aspose.threed.utilities.Vector2 import Vector2
        return Vector2(self._semi_axis1 * 2, self._semi_axis2 * 2)
