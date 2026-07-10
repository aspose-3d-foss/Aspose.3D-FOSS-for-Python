from typing import TYPE_CHECKING

from .Curve import Curve

if TYPE_CHECKING:
    from ..Entity import Entity
    from .IMeshConvertible import IMeshConvertible


class RevolvedAreaSolid(Curve):
    """RevolvedAreaSolid entity."""
    
    def __init__(self, name: str = None):
        """Constructor of RevolvedAreaSolid."""
        raise NotImplementedError("__init__ is not implemented")
    
    @property
    def profile(self):
        """Gets the profile."""
        raise NotImplementedError("profile is not implemented")
    
    @profile.setter
    def profile(self, value):
        """Sets the profile."""
        raise NotImplementedError("profile is not implemented")
    
    @property
    def axis(self):
        """Gets the axis of revolution."""
        raise NotImplementedError("axis is not implemented")
    
    @axis.setter
    def axis(self, value):
        """Sets the axis of revolution."""
        raise NotImplementedError("axis is not implemented")
    
    @property
    def start_angle(self):
        """Gets the start angle."""
        raise NotImplementedError("start_angle is not implemented")
    
    @start_angle.setter
    def start_angle(self, value):
        """Sets the start angle."""
        raise NotImplementedError("start_angle is not implemented")
    
    @property
    def end_angle(self):
        """Gets the end angle."""
        raise NotImplementedError("end_angle is not implemented")
    
    @end_angle.setter
    def end_angle(self, value):
        """Sets the end angle."""
        raise NotImplementedError("end_angle is not implemented")
