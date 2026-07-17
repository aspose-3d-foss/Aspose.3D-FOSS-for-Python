from typing import List, TYPE_CHECKING

from .VertexElement import VertexElement
from ..utilities.ArrayListAdapter import ArrayListAdapter
from .VertexElementType import VertexElementType

if TYPE_CHECKING:
    from .MappingMode import MappingMode
    from .ReferenceMode import ReferenceMode


class VertexElementDoublesTemplate(VertexElement):
    """A helper class for defining concrete implementations."""

    def __init__(self, element_type: 'VertexElementType' = None, name: str = "", mapping_mode: 'MappingMode' = None, reference_mode: 'ReferenceMode' = None):
        super().__init__(element_type or VertexElementType(), name, mapping_mode, reference_mode)
        self._data: List[float] = []
        self._data_adapter = ArrayListAdapter(self._data)

    @property
    def data(self) -> ArrayListAdapter[float]:
        """Gets the vertex data."""
        return self._data_adapter

    def set_data(self, data: List[float]):
        """Sets the data."""
        self._data.clear()
        self._data.extend(data)

    def clear(self):
        """Removes all elements from the direct and the index arrays."""
        self._data.clear()
        super().clear()

    def copy_to(self, target: 'VertexElementDoublesTemplate'):
        """Copies data to specified element."""
        if target is None:
            raise ValueError("target cannot be None")
        target._data.clear()
        target._data.extend(self._data)
