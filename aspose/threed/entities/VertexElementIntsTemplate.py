from typing import List, TYPE_CHECKING

from .VertexElement import VertexElement

if TYPE_CHECKING:
    from .MappingMode import MappingMode
    from .ReferenceMode import ReferenceMode
    from .VertexElementType import VertexElementType


class VertexElementIntsTemplate(VertexElement):
    def __init__(self, element_type: 'VertexElementType', name: str = "", mapping_mode: 'MappingMode' = None, reference_mode: 'ReferenceMode' = None):
        super().__init__(element_type, name, mapping_mode, reference_mode)
        self._data: List[int] = []
        self._indices: List[int] = []

    def set_data(self, data: List[int]):
        self._data = list(data)

    def set_indices(self, data: List[int]):
        self._indices = list(data)

    def clear(self):
        self._data.clear()
        self._indices.clear()

    def copy_to(self, target: 'VertexElementIntsTemplate'):
        target._data = list(self._data)
        target._indices = list(self._indices)

    @property
    def data(self) -> List[int]:
        return list(self._data)

    @property
    def indices(self) -> List[int]:
        return list(self._indices)
