from typing import List, Optional, TYPE_CHECKING

from ..Entity import Entity
from ..utilities.Vector4 import Vector4

if TYPE_CHECKING:
    from .VertexElement import VertexElement
    from .VertexElementUV import VertexElementUV
    from .MappingMode import MappingMode
    from .ReferenceMode import ReferenceMode
    from .TextureMapping import TextureMapping
    from .VertexElementType import VertexElementType


class Geometry(Entity):
    def __init__(self, name: str = None):
        if name is None:
            name = ""
        super().__init__(name)
        self._vertex_elements: List['VertexElement'] = []
        self._control_points: List[Vector4] = []
        self._visible = True
        self._cast_shadows = True
        self._receive_shadows = True

    @property
    def visible(self) -> bool:
        return self._visible

    @visible.setter
    def visible(self, value: bool):
        self._visible = bool(value)

    @property
    def cast_shadows(self) -> bool:
        return self._cast_shadows

    @cast_shadows.setter
    def cast_shadows(self, value: bool):
        self._cast_shadows = bool(value)

    @property
    def receive_shadows(self) -> bool:
        return self._receive_shadows

    @receive_shadows.setter
    def receive_shadows(self, value: bool):
        self._receive_shadows = bool(value)

    @property
    def vertex_elements(self) -> List['VertexElement']:
        return list(self._vertex_elements)

    @property
    def control_points(self) -> List[Vector4]:
        return list(self._control_points)

    def create_element(self, element_type: 'VertexElementType', mapping_mode: 'MappingMode' = None, reference_mode: 'ReferenceMode' = None) -> 'VertexElement':
        from .VertexElementType import VertexElementType
        from .MappingMode import MappingMode
        from .ReferenceMode import ReferenceMode
        from .VertexElementFVector import VertexElementFVector

        element = VertexElementFVector(element_type, "", mapping_mode, reference_mode)
        self._vertex_elements.append(element)
        return element

    def create_element_uv(self, uv_mapping: 'TextureMapping', mapping_mode: 'MappingMode' = None, reference_mode: 'ReferenceMode' = None) -> 'VertexElementUV':
        from .TextureMapping import TextureMapping
        from .MappingMode import MappingMode
        from .ReferenceMode import ReferenceMode
        from .VertexElementUV import VertexElementUV

        element = VertexElementUV(uv_mapping, "", mapping_mode, reference_mode)
        self._vertex_elements.append(element)
        return element

    def add_element(self, element: 'VertexElement'):
        self._vertex_elements.append(element)

    def get_element(self, element_type: 'VertexElementType'):
        for element in self._vertex_elements:
            if element.vertex_element_type == element_type:
                return element
        return None

    def get_vertex_element_of_uv(self, texture_mapping: 'TextureMapping') -> Optional['VertexElementUV']:
        from .VertexElementUV import VertexElementUV

        for element in self._vertex_elements:
            if isinstance(element, VertexElementUV) and element.texture_mapping == texture_mapping:
                return element
        return None

    def remove_property(self, property):
        return False

    def remove_property(self, property_name: str):
        return False

    def get_property(self, property: str):
        return None

    def set_property(self, property: str, value):
        pass

    def find_property(self, property: str):
        return None

    def get_bounding_box(self):
        from ..utilities import BoundingBox
        return BoundingBox()

    def get_entity_renderer_key(self):
        raise NotImplementedError("get_entity_renderer_key is not implemented for Geometry")
