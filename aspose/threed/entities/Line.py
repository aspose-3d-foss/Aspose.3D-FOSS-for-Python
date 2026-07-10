from typing import TYPE_CHECKING

from .Curve import Curve

if TYPE_CHECKING:
    from ..Entity import Entity
    from .IMeshConvertible import IMeshConvertible
    from .utilities import Vector3


class Line(Curve):
    """A polyline is a path defined by a set of points with control_points, and connected by segments."""
    
    def __init__(self, name: str = None):
        """Initializes a new instance of the Line class."""
        raise NotImplementedError("__init__ is not implemented")
    
    @staticmethod
    def from_points(points):
        """Construct a Line instance from a set of points."""
        raise NotImplementedError("from_points is not implemented")
    
    def make_default_indices(self) -> None:
        """Generate default indices for the line."""
        raise NotImplementedError("make_default_indices is not implemented")
    
    @property
    def segments(self):
        """Gets the segments of the line."""
        raise NotImplementedError("segments is not implemented")
