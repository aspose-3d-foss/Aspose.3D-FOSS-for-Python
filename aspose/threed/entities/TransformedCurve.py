from typing import TYPE_CHECKING

from .Curve import Curve

if TYPE_CHECKING:
    from ..Entity import Entity
    from .IMeshConvertible import IMeshConvertible


class TransformedCurve(Curve):
    """TransformedCurve entity."""
    
    def __init__(self, name: str = None):
        """Constructor of TransformedCurve."""
        raise NotImplementedError("__init__ is not implemented")
    
    @property
    def source(self):
        """Gets the source curve."""
        raise NotImplementedError("source is not implemented")
    
    @source.setter
    def source(self, value):
        """Sets the source curve."""
        raise NotImplementedError("source is not implemented")
    
    @property
    def transform(self):
        """Gets the transform matrix."""
        raise NotImplementedError("transform is not implemented")
    
    @transform.setter
    def transform(self, value):
        """Sets the transform matrix."""
        raise NotImplementedError("transform is not implemented")
