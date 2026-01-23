from typing import List, TYPE_CHECKING

from .VertexElement import VertexElement

if TYPE_CHECKING:
    from .MappingMode import MappingMode
    from .ReferenceMode import ReferenceMode
    from .VertexElementType import VertexElementType
    from aspose.threed.utilities.FVector2 import FVector2 as FVector2Type
    from aspose.threed.utilities.FVector3 import FVector3 as FVector3Type
    from aspose.threed.utilities.FVector4 import FVector4 as FVector4Type


class VertexElementFVector(VertexElement):
    def __init__(self, element_type, name: str = "", mapping_mode: 'MappingMode' = None, reference_mode: 'ReferenceMode' = None):
        super().__init__(element_type, name, mapping_mode, reference_mode)
        self._data: List['FVector4'] = []
        self._indices: List[int] = []

    def set_data(self, data):
        from aspose.threed.utilities.FVector2 import FVector2
        from aspose.threed.utilities.FVector3 import FVector3
        from aspose.threed.utilities.FVector4 import FVector4
        
        if isinstance(data, list) and len(data) > 0:
            if isinstance(data[0], FVector2):
                self._data = [FVector4(v.x, v.y, 0.0, 0.0) for v in data]
            elif isinstance(data[0], FVector3):
                self._data = [FVector4(v.x, v.y, v.z, 0.0) for v in data]
            elif isinstance(data[0], FVector4):
                self._data = list(data)
            else:
                raise TypeError(f"Unsupported data type for VertexElementFVector: {type(data[0])}")

    def set_indices(self, data: List[int]):
        self._indices = list(data)

    def clear(self):
        self._data.clear()
        self._indices.clear()

    def copy_to(self, target: 'VertexElementFVector'):
        target._data = list(self._data)
        target._indices = list(self._indices)

    @property
    def data(self) -> List['FVector4']:
        return list(self._data)

    @property
    def indices(self) -> List[int]:
        return list(self._indices)
