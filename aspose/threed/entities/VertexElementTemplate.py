from typing import List, Generic, TypeVar

from ..utilities.ArrayListAdapter import ArrayListAdapter
from .VertexElement import VertexElement
from .MappingMode import MappingMode
from .ReferenceMode import ReferenceMode

T = TypeVar('T')


class VertexElementTemplate(VertexElement, Generic[T]):
    """A helper class for defining concrete implementations of vertex elements with typed data."""

    def __init__(self, mapping_mode: MappingMode = None, reference_mode: ReferenceMode = None):
        """Initialize a new instance of the VertexElementTemplate class."""
        super().__init__("Unknown", "", mapping_mode, reference_mode)
        self._data: List[T] = []
        self._internal_data: List[T] = []
        self._data_adapter = ArrayListAdapter(self._internal_data)

    @property
    def data(self) -> ArrayListAdapter[T]:
        """Gets the vertex data."""
        return self._data_adapter

    def copy_to(self, target: 'VertexElementTemplate[T]'):
        """Copies data to specified element."""
        if target is None:
            raise ValueError("target cannot be None")
        target._internal_data.clear()
        target._internal_data.extend(self._internal_data)

    def set_data(self, data: List[T]):
        """Sets the data."""
        self._data.clear()
        self._data.extend(data)
        self._internal_data.clear()
        self._internal_data.extend(self._data)

    def clear(self):
        """Removes all elements from the direct and the index arrays."""
        self._data.clear()
        self._internal_data.clear()
        super().clear()
