from typing import TYPE_CHECKING

from .Profile import Profile

if TYPE_CHECKING:
    from aspose.threed.utilities.Vector2 import Vector2


class ParameterizedProfile(Profile):
    """The base class of all parameterized profiles."""
    
    def __init__(self, name: str = None):
        super().__init__(name)
    
    def get_extent(self) -> 'Vector2':
        """Gets the extent in x and y dimension."""
        from aspose.threed.utilities.Vector2 import Vector2
        return Vector2(0, 0)
