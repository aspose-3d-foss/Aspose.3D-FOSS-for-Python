from typing import TYPE_CHECKING

from .Curve import Curve

if TYPE_CHECKING:
    from ..Entity import Entity
    from .IMeshConvertible import IMeshConvertible


class Shape(Curve):
    """Base class for all shape entities."""
    
    def __init__(self, name: str = None):
        """Constructor of Shape."""
        raise NotImplementedError("__init__ is not implemented")
    
    @property
    def segments(self):
        """Gets the segments of the shape."""
        raise NotImplementedError("segments is not implemented")
