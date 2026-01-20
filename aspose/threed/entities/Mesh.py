from typing import List, Optional, TYPE_CHECKING

from .Geometry import Geometry
from .BooleanOperation import BooleanOperation
from ..utilities.Matrix4 import Matrix4
from ..utilities.Vector4 import Vector4

if TYPE_CHECKING:
    from .VertexElement import VertexElement
    from .VertexElementUV import VertexElementUV
    from .VertexElementType import VertexElementType
    from .MappingMode import MappingMode
    from .ReferenceMode import ReferenceMode
    from .TextureMapping import TextureMapping


class Mesh(Geometry):
    def __init__(self, name: str = None, height_map=None, transform: Matrix4 = None, tri_mesh: bool = None):
        if name is None:
            name = ""
        super().__init__(name)

        self._control_points: List[Vector4] = []
        self._edges: List[int] = []
        self._polygons: List[int] = []
        self._polygon_sizes: List[int] = []

        if height_map is not None:
            raise NotImplementedError("height_map constructor is not implemented")

    @property
    def control_points(self) -> List[Vector4]:
        return list(self._control_points)

    @property
    def edges(self) -> List[int]:
        return list(self._edges)

    @property
    def polygon_count(self) -> int:
        return len(self._polygon_sizes)

    @property
    def polygons(self) -> List[List[int]]:
        result = []
        offset = 0
        for size in self._polygon_sizes:
            polygon = self._polygons[offset:offset + size]
            result.append(list(polygon))
            offset += size
        return result

    def create_polygon(self, *args):
        if len(args) == 1 and isinstance(args[0], list):
            indices = args[0]
            if len(indices) == 3:
                self.create_polygon(indices[0], indices[1], indices[2])
            elif len(indices) == 4:
                self.create_polygon(indices[0], indices[1], indices[2], indices[3])
            else:
                self._create_polygon_from_list(indices)
        elif len(args) == 3:
            v1, v2, v3 = args
            self._polygon_sizes.append(3)
            self._polygons.extend([v1, v2, v3])
        elif len(args) == 4:
            v1, v2, v3, v4 = args
            self._polygon_sizes.append(4)
            self._polygons.extend([v1, v2, v3, v4])
        elif len(args) == 3 and isinstance(args[2], int):
            indices, offset, length = args
            self._polygon_sizes.append(length)
            self._polygons.extend(indices[offset:offset + length])
        else:
            raise TypeError("Invalid arguments for create_polygon")

    def _create_polygon_from_list(self, indices: List[int]):
        self._polygon_sizes.append(len(indices))
        self._polygons.extend(indices)

    def get_polygon_size(self, index: int) -> int:
        if index < 0 or index >= len(self._polygon_sizes):
            raise IndexError("Polygon index out of range")
        return self._polygon_sizes[index]

    def to_mesh(self) -> 'Mesh':
        return self

    def optimize(self, vertex_elements: bool = False, tolerance_control_point: float = 1e-9, tolerance_normal: float = 1e-9, tolerance_uv: float = 1e-9) -> 'Mesh':
        raise NotImplementedError("optimize is not implemented")

    @staticmethod
    def do_boolean(op: BooleanOperation, a: 'Mesh', transform_a: Optional[Matrix4], b: 'Mesh', transform_b: Optional[Matrix4]) -> 'Mesh':
        raise NotImplementedError("do_boolean is not implemented")

    def is_manifold(self) -> bool:
        raise NotImplementedError("is_manifold is not implemented")

    @staticmethod
    def union(a: 'Mesh', b: 'Mesh') -> 'Mesh':
        raise NotImplementedError("union is not implemented")

    @staticmethod
    def difference(a: 'Mesh', b: 'Mesh') -> 'Mesh':
        raise NotImplementedError("difference is not implemented")

    @staticmethod
    def intersect(a: 'Mesh', b: 'Mesh') -> 'Mesh':
        raise NotImplementedError("intersect is not implemented")

    def triangulate(self) -> 'Mesh':
        raise NotImplementedError("triangulate is not implemented")

    @property
    def deformers(self):
        return []

    def get_bounding_box(self):
        from ..utilities import BoundingBox
        return BoundingBox()

    def get_entity_renderer_key(self):
        raise NotImplementedError("get_entity_renderer_key is not implemented for Mesh")
