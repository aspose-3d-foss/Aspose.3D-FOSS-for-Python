from typing import TYPE_CHECKING

from .VertexElement import VertexElement

if TYPE_CHECKING:
    from .VertexElementDoublesTemplate import VertexElementDoublesTemplate


class VertexElementDoublesTemplate(VertexElement):
    """A helper class for defining concrete VertexElement implementations."""

    def set_indices(self, data):
        raise NotImplementedError("set_indices is not implemented")

    def clear(self):
        raise NotImplementedError("clear is not implemented")

    def copy_to(self, target: "VertexElementDoublesTemplate"):
        raise NotImplementedError("copy_to is not implemented")

    def set_data(self, data):
        raise NotImplementedError("set_data is not implemented")
