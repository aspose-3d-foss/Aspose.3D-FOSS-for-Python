from typing import TYPE_CHECKING

from .Curve import Curve

if TYPE_CHECKING:
    from ..Entity import Entity
    from .IMeshConvertible import IMeshConvertible


class TrimmedCurve(Curve):
    """TrimmedCurve entity."""
    
    def __init__(self, name: str = None):
        """Constructor of TrimmedCurve."""
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
    def start_parameter(self):
        """Gets the start parameter."""
        raise NotImplementedError("start_parameter is not implemented")
    
    @start_parameter.setter
    def start_parameter(self, value):
        """Sets the start parameter."""
        raise NotImplementedError("start_parameter is not implemented")
    
    @property
    def end_parameter(self):
        """Gets the end parameter."""
        raise NotImplementedError("end_parameter is not implemented")
    
    @end_parameter.setter
    def end_parameter(self, value):
        """Sets the end parameter."""
        raise NotImplementedError("end_parameter is not implemented")
