from typing import TYPE_CHECKING
from aspose.threed.utilities import Vector3

if TYPE_CHECKING:
    from .CoordinateSystem import CoordinateSystem
    from .Axis import Axis


class AxisSystem:
    """Axis system is an combination of coordinate system, up vector and front vector."""
    
    def __init__(self, *args):
        raise NotImplementedError("__init__ is not implemented")
    
    def transform_to(self, target_system: "AxisSystem") -> "aspose.threed.utilities.Matrix4":
        """Create a matrix used to convert from current axis system to target axis system."""
        raise NotImplementedError("transform_to is not implemented")
    
    @staticmethod
    def from_asset_info(asset_info: "aspose.threed.AssetInfo") -> "AxisSystem":
        """Create AxisSystem from AssetInfo."""
        raise NotImplementedError("from_asset_info is not implemented")
    
    @property
    def coordinate_system(self) -> "CoordinateSystem":
        """Gets the coordinate system of this axis system."""
        raise NotImplementedError("coordinate_system is not implemented")
    
    @property
    def up(self) -> "Axis":
        """Gets the up vector of this axis system."""
        raise NotImplementedError("up is not implemented")
    
    @property
    def front(self) -> "Axis":
        """Gets the front vector of this axis system."""
        raise NotImplementedError("front is not implemented")
