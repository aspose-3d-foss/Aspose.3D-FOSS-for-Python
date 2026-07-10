from typing import TYPE_CHECKING, List

from .VertexElement import VertexElement

if TYPE_CHECKING:
    from .MappingMode import MappingMode
    from .ReferenceMode import ReferenceMode
    from .VertexElementType import VertexElementType
    from ..utilities.Vector4 import Vector4


class VertexElementVector4(VertexElement):
    """Defines the vector4 data for specified components."""

    def set_indices(self, data: List[int]):
        raise NotImplementedError("set_indices is not implemented")

    def clear(self):
        raise NotImplementedError("clear is not implemented")

    def copy_to(self, target: 'VertexElementVector4'):
        raise NotImplementedError("copy_to is not implemented")

    def set_data(self, data: List['Vector4']):
        raise NotImplementedError("set_data is not implemented")

    @property
    def data(self) -> List['Vector4']:
        raise NotImplementedError("data is not implemented")
