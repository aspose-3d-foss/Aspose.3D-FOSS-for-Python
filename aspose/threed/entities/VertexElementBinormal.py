from typing import List, TYPE_CHECKING

from .VertexElementFVector import VertexElementFVector
from .VertexElementType import VertexElementType
from .MappingMode import MappingMode
from .ReferenceMode import ReferenceMode


class VertexElementBinormal(VertexElementFVector):
    def __init__(self, name: str = "", mapping_mode: 'MappingMode' = None, reference_mode: 'ReferenceMode' = None):
        super().__init__(VertexElementType.BINORMAL, name, mapping_mode, reference_mode)
