from typing import TYPE_CHECKING

from .Profile import Profile

if TYPE_CHECKING:
    from .Curve import Curve


class CenterLineProfile(Profile):
    """IFC compatible center line profile."""
    
    def __init__(self, name: str = None, curve: 'Curve' = None, thickness: float = 1.0):
        super().__init__(name)
        self._curve = curve
        self._thickness = thickness
    
    @property
    def curve(self) -> 'Curve':
        return self._curve
    
    @curve.setter
    def curve(self, value: 'Curve'):
        self._curve = value
    
    @property
    def thickness(self) -> float:
        return self._thickness
    
    @thickness.setter
    def thickness(self, value: float):
        self._thickness = float(value)
