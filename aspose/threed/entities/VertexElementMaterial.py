from typing import TYPE_CHECKING

from .VertexElement import VertexElement

if TYPE_CHECKING:
    from .MappingMode import MappingMode
    from .ReferenceMode import ReferenceMode
    from .VertexElementType import VertexElementType


class VertexElementMaterial(VertexElement):
    """Defines the material for specified components."""

    def set_indices(self, data):
        raise NotImplementedError("set_indices is not implemented")

    def clear(self):
        raise NotImplementedError("clear is not implemented")

    def copy_to(self, target):
        raise NotImplementedError("copy_to is not implemented")

    def set_data(self, data):
        raise NotImplementedError("set_data is not implemented")
