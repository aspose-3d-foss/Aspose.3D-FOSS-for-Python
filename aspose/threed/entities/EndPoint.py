class EndPoint:
    """The end point to trim the curve, can be a parameter value or a Cartesian point."""
    
    def __init__(self, *args):
        raise NotImplementedError("__init__ is not implemented")
    
    @staticmethod
    def from_degree(degree: float) -> "EndPoint":
        """Create an end point measured in degree."""
        raise NotImplementedError("from_degree is not implemented")
    
    @staticmethod
    def from_radian(degree: float) -> "EndPoint":
        """Create an end point measured in radian."""
        raise NotImplementedError("from_radian is not implemented")
    
    @property
    def is_cartesian_point(self) -> bool:
        """Is the end point a Cartesian point?"""
        raise NotImplementedError("is_cartesian_point is not implemented")
    
    @property
    def as_point(self) -> "aspose.threed.utilities.Vector3":
        """Gets the end point as Cartesian point, or thrown an exception."""
        raise NotImplementedError("as_point is not implemented")
    
    @property
    def as_value(self) -> float:
        """Gets the end point as a real parameter, or throw an exception."""
        raise NotImplementedError("as_value is not implemented")
