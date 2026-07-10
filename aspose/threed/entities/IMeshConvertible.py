from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Mesh import Mesh


class IMeshConvertible:
    """Entities that implemented this interface can be converted to Mesh"""
    
    def to_mesh(self) -> "Mesh":
        """Convert current object to mesh."""
        raise NotImplementedError("to_mesh is not implemented")
