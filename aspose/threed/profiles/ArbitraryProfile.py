from typing import List, TYPE_CHECKING

from .Profile import Profile

if TYPE_CHECKING:
    from .Curve import Curve


class ArbitraryProfile(Profile):
    """This class allows you to construct a 2D profile directly from arbitrary curve."""
    
    def __init__(self, name: str = None):
        super().__init__(name)
        self._curve = None
        self._holes: List['Curve'] = []
    
    @property
    def curve(self) -> 'Curve':
        return self._curve
    
    @curve.setter
    def curve(self, value: 'Curve'):
        self._curve = value
    
    @property
    def holes(self) -> List['Curve']:
        return list(self._holes)
    
    def add_hole(self, hole: 'Curve'):
        self._holes.append(hole)
