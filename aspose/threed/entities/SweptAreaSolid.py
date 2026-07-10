from typing import TYPE_CHECKING

from .Curve import Curve

if TYPE_CHECKING:
    from ..Entity import Entity
    from .IMeshConvertible import IMeshConvertible


class SweptAreaSolid(Curve):
    """SweptAreaSolid entity."""
    
    def __init__(self, name: str = None):
        """Constructor of SweptAreaSolid."""
        raise NotImplementedError("__init__ is not implemented")
    
    @property
    def area(self):
        """Gets the area of the sweep."""
        raise NotImplementedError("area is not implemented")
    
    @area.setter
    def area(self, value):
        """Sets the area of the sweep."""
        raise NotImplementedError("area is not implemented")
    
    @property
    def path(self):
        """Gets the path of the sweep."""
        raise NotImplementedError("path is not implemented")
    
    @path.setter
    def path(self, value):
        """Sets the path of the sweep."""
        raise NotImplementedError("path is not implemented")
