from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .MappingMode import MappingMode
    from .ReferenceMode import ReferenceMode
    from .VertexElementType import VertexElementType
    from .IIndexedVertexElement import IIndexedVertexElement


class VertexElement:
    def __init__(self, element_type: 'VertexElementType', name: str = "", mapping_mode: 'MappingMode' = None, reference_mode: 'ReferenceMode' = None):
        self._vertex_element_type = element_type
        self._name = name
        self._mapping_mode = mapping_mode
        self._reference_mode = reference_mode
        self._indices: List[int] = []

    @property
    def vertex_element_type(self) -> 'VertexElementType':
        return self._vertex_element_type

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = str(value)

    @property
    def mapping_mode(self) -> 'MappingMode':
        return self._mapping_mode

    @mapping_mode.setter
    def mapping_mode(self, value: 'MappingMode'):
        self._mapping_mode = value

    @property
    def reference_mode(self) -> 'ReferenceMode':
        return self._reference_mode

    @reference_mode.setter
    def reference_mode(self, value: 'ReferenceMode'):
        self._reference_mode = value

    def set_indices(self, data: List[int]):
        self._indices = list(data)

    def clear(self):
        self._indices.clear()

    @property
    def indices(self) -> List[int]:
        return list(self._indices)
