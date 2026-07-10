from typing import TYPE_CHECKING

from .Curve import Curve

if TYPE_CHECKING:
    from ..Entity import Entity
    from .IMeshConvertible import IMeshConvertible


class CompositeCurve(Curve):
    """A CompositeCurve is consisting of several curve segments."""
    
    def __init__(self):
        """Constructor of CompositeCurve."""
        raise NotImplementedError("__init__ is not implemented")
    
    def add_segment(self, curve, same_direction: bool) -> None:
        """Add a new segment to current curve."""
        raise NotImplementedError("add_segment is not implemented")
    
    @property
    def segments(self):
        """The segments of the curve."""
        raise NotImplementedError("segments is not implemented")
