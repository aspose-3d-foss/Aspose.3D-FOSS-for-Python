from typing import TYPE_CHECKING

from ..Entity import Entity

if TYPE_CHECKING:
    from .IMeshConvertible import IMeshConvertible
    from .Curve import Curve


class TriMesh(Entity):
    """TriMesh is a triangle mesh that stores triangles."""

    def __init__(self, name: str = None):
        """Initializes a new instance of the TriMesh class."""
        raise NotImplementedError(
            "__init__ is not implemented")

    @property
    def triangles(self):
        """Gets the triangles of the mesh."""
        raise NotImplementedError(
            "triangles is not implemented")

    @property
    def control_points(self):
        """Gets the control points of the mesh."""
        raise NotImplementedError(
            "control_points is not implemented")
