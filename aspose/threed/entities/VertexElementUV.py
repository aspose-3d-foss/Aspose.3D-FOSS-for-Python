from typing import List, TYPE_CHECKING

from .VertexElementFVector import VertexElementFVector
from .VertexElementType import VertexElementType
from .TextureMapping import TextureMapping
from .MappingMode import MappingMode
from .ReferenceMode import ReferenceMode

from aspose.threed.utilities.FVector2 import FVector2
from aspose.threed.utilities.FVector3 import FVector3
from aspose.threed.utilities.FVector4 import FVector4
from aspose.threed.utilities.Vector2 import Vector2
from aspose.threed.utilities.Vector3 import Vector3


class VertexElementUV(VertexElementFVector):
    def __init__(self, texture_mapping: 'TextureMapping' = None, name: str = "", mapping_mode: 'MappingMode' = None, reference_mode: 'ReferenceMode' = None):
        if texture_mapping is None:
            texture_mapping = TextureMapping.DIFFUSE
        
        super().__init__(VertexElementType.UV, name, mapping_mode, reference_mode)
        self._texture_mapping = texture_mapping

    @property
    def texture_mapping(self) -> 'TextureMapping':
        return self._texture_mapping

    def add_data(self, data):
        if isinstance(data, list) and len(data) > 0:
            if isinstance(data[0], Vector2):
                for v in data:
                    self._data.append(aspose.threed.utilities.FVector4(v.x, v.y, 0.0, 0.0))
            elif isinstance(data[0], Vector3):
                for v in data:
                    self._data.append(aspose.threed.utilities.FVector4(v.x, v.y, v.z, 0.0))
            elif isinstance(data[0], FVector2):
                for v in data:
                    self._data.append(aspose.threed.utilities.FVector4(v.x, v.y, 0.0, 0.0))
            elif isinstance(data[0], FVector3):
                for v in data:
                    self._data.append(aspose.threed.utilities.FVector4(v.x, v.y, v.z, 0.0))
            elif isinstance(data[0], FVector4):
                self._data.extend(data)
            else:
                raise TypeError(f"Unsupported data type for VertexElementUV: {type(data[0])}")
