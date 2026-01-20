from typing import TYPE_CHECKING

from .VertexElementIntsTemplate import VertexElementIntsTemplate
from .VertexElementType import VertexElementType

if TYPE_CHECKING:
    from .MappingMode import MappingMode
    from .ReferenceMode import ReferenceMode


class VertexElementSmoothingGroup(VertexElementIntsTemplate):
    def __init__(self, name: str = "", mapping_mode: 'MappingMode' = None, reference_mode: 'ReferenceMode' = None):
        super().__init__(VertexElementType.SMOOTHING_GROUP, name, mapping_mode, reference_mode)
