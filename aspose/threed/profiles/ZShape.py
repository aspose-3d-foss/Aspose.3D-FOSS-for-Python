from typing import TYPE_CHECKING

from .ParameterizedProfile import ParameterizedProfile

if TYPE_CHECKING:
    from aspose.threed.utilities.Vector2 import Vector2


class ZShape(ParameterizedProfile):
    """IFC compatible Z-shape profile that defined by parameters."""
    
    def __init__(self, name: str = None):
        super().__init__(name)
        self._depth = 10.0
        self._flange_width = 10.0
        self._flange_thickness = 1.0
        self._web_thickness = 1.0
        self._fillet_radius = 0.0
        self._edge_radius = 0.0
    
    @property
    def depth(self) -> float:
        return self._depth
    
    @depth.setter
    def depth(self, value: float):
        self._depth = float(value)
    
    @property
    def flange_width(self) -> float:
        return self._flange_width
    
    @flange_width.setter
    def flange_width(self, value: float):
        self._flange_width = float(value)
    
    @property
    def flange_thickness(self) -> float:
        return self._flange_thickness
    
    @flange_thickness.setter
    def flange_thickness(self, value: float):
        self._flange_thickness = float(value)
    
    @property
    def web_thickness(self) -> float:
        return self._web_thickness
    
    @web_thickness.setter
    def web_thickness(self, value: float):
        self._web_thickness = float(value)
    
    @property
    def fillet_radius(self) -> float:
        return self._fillet_radius
    
    @fillet_radius.setter
    def fillet_radius(self, value: float):
        self._fillet_radius = float(value)
    
    @property
    def edge_radius(self) -> float:
        return self._edge_radius
    
    @edge_radius.setter
    def edge_radius(self, value: float):
        self._edge_radius = float(value)
    
    def get_extent(self) -> 'Vector2':
        """Gets the extent in x and y dimension."""
        from aspose.threed.utilities.Vector2 import Vector2
        return Vector2(self._flange_width, self._depth)
