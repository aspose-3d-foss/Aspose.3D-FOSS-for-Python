from typing import TYPE_CHECKING

from .Curve import Curve

if TYPE_CHECKING:
    from ..Entity import Entity
    from .IMeshConvertible import IMeshConvertible


class Torus(Curve):
    """Torus entity."""
    
    def __init__(self, name: str = None):
        """Constructor of Torus."""
        raise NotImplementedError("__init__ is not implemented")
    
    @property
    def radius_major(self):
        """Gets the major radius."""
        raise NotImplementedError("radius_major is not implemented")
    
    @radius_major.setter
    def radius_major(self, value):
        """Sets the major radius."""
        raise NotImplementedError("radius_major is not implemented")
    
    @property
    def radius_minor(self):
        """Gets the minor radius."""
        raise NotImplementedError("radius_minor is not implemented")
    
    @radius_minor.setter
    def radius_minor(self, value):
        """Sets the minor radius."""
        raise NotImplementedError("radius_minor is not implemented")
    
    @property
    def radial_segments(self):
        """Gets the radial segments."""
        raise NotImplementedError("radial_segments is not implemented")
    
    @radial_segments.setter
    def radial_segments(self, value):
        """Sets the radial segments."""
        raise NotImplementedError("radial_segments is not implemented")
    
    @property
    def height_segments(self):
        """Gets the height segments."""
        raise NotImplementedError("height_segments is not implemented")
    
    @height_segments.setter
    def height_segments(self, value):
        """Sets the height segments."""
        raise NotImplementedError("height_segments is not implemented")
