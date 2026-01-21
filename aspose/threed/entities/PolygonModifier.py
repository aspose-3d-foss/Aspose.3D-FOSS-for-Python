from typing import List, TYPE_CHECKING, Union
import math

from ..utilities.Vector4 import Vector4
from ..utilities.Vector3 import Vector3

if TYPE_CHECKING:
    from ..Scene import Scene
    from .Mesh import Mesh


class PolygonModifier:
    @staticmethod
    def triangulate(arg1, arg2=None, arg3=False, arg4=None) -> Union[None, 'Mesh', List[List[int]]]:
        from ..Scene import Scene
        from .Mesh import Mesh

        if isinstance(arg1, Scene):
            return PolygonModifier._triangulate_scene(arg1)
        elif isinstance(arg1, Mesh):
            return PolygonModifier._triangulate_mesh(arg1)
        elif isinstance(arg1, list):
            if arg2 is None:
                return []
            elif isinstance(arg2, int):
                return PolygonModifier._triangulate_single_polygon_from_size(arg1, arg2)
            elif isinstance(arg2, list):
                if len(arg2) > 0 and isinstance(arg2[0], list):
                    generate_normals = arg3
                    nor_out = arg4
                    if generate_normals and isinstance(nor_out, list) and len(nor_out) > 0 and not isinstance(nor_out[0], Vector3):
                        return PolygonModifier._triangulate_control_points(arg1, arg2, generate_normals, nor_out[0])
                    else:
                        return PolygonModifier._triangulate_control_points(arg1, arg2, generate_normals, nor_out)
                else:
                    return PolygonModifier._triangulate_single_polygon(arg1, arg2)
        raise TypeError(f"Invalid arguments for triangulate: {type(arg1)}, {type(arg2)}")

    @staticmethod
    def _triangulate_scene(scene: 'Scene') -> None:
        root_node = scene.root_node

        def process_node(node):
            for entity in node.entities:
                from .Mesh import Mesh
                if isinstance(entity, Mesh):
                    triangulated = PolygonModifier._triangulate_mesh(entity)
                    node.entity = triangulated
            for child in node.child_nodes:
                process_node(child)

        process_node(root_node)

    @staticmethod
    def _triangulate_mesh(mesh: 'Mesh') -> 'Mesh':
        from .Mesh import Mesh

        new_mesh = Mesh(name=f"{mesh.name}_triangulated" if mesh.name else "triangulated")
        new_mesh._control_points = list(mesh._control_points)

        for polygon in mesh.polygons:
            PolygonModifier._triangulate_polygon_to_mesh(new_mesh, polygon)

        return new_mesh

    @staticmethod
    def _triangulate_control_points(control_points: List[Vector4], polygons: List[List[int]], generate_normals: bool = False, nor_out: List[Vector3] = None) -> List[List[int]]:
        if polygons is None:
            polygons = []

        result = []

        if generate_normals and nor_out is not None:
            nor_out.clear()

        for polygon in polygons:
            triangles = PolygonModifier._triangulate_polygon(control_points, polygon, generate_normals, nor_out)
            result.extend(triangles)

        return result

    @staticmethod
    def _triangulate_single_polygon_from_size(control_points: List[Vector4], polygon_size: int) -> List[List[int]]:
        polygon = list(range(polygon_size))
        return PolygonModifier._triangulate_polygon(control_points, polygon, False, None)

    @staticmethod
    def _triangulate_single_polygon(control_points: List[Vector4], polygon: List[int]) -> List[List[int]]:
        return PolygonModifier._triangulate_polygon(control_points, polygon, False, None)

    @staticmethod
    def _triangulate_polygon(control_points: List[Vector4], polygon: List[int], generate_normals: bool = False, nor_out: List[Vector3] = None) -> List[List[int]]:
        n = len(polygon)
        if n < 3:
            return []

        if n == 3:
            if generate_normals and nor_out is not None:
                normal = PolygonModifier._calculate_normal(control_points, polygon)
                nor_out.append(normal)
            return [polygon[:]]

        triangles = []
        if generate_normals and nor_out is not None:
            for i in range(1, n - 1):
                triangle = [polygon[0], polygon[i], polygon[i + 1]]
                triangles.append(triangle)
                normal = PolygonModifier._calculate_normal(control_points, triangle)
                nor_out.append(normal)
        else:
            for i in range(1, n - 1):
                triangle = [polygon[0], polygon[i], polygon[i + 1]]
                triangles.append(triangle)

        return triangles

    @staticmethod
    def _triangulate_polygon_to_mesh(mesh: 'Mesh', polygon: List[int]):
        n = len(polygon)
        if n < 3:
            return

        if n == 3:
            mesh.create_polygon(polygon[0], polygon[1], polygon[2])
        elif n == 4:
            mesh.create_polygon(polygon[0], polygon[1], polygon[2])
            mesh.create_polygon(polygon[0], polygon[2], polygon[3])
        else:
            for i in range(1, n - 1):
                mesh.create_polygon(polygon[0], polygon[i], polygon[i + 1])

    @staticmethod
    def _calculate_normal(control_points: List[Vector4], triangle: List[int]) -> Vector3:
        if len(triangle) < 3:
            return Vector3(0, 0, 1)

        v0 = control_points[triangle[0]]
        v1 = control_points[triangle[1]]
        v2 = control_points[triangle[2]]

        p0 = Vector3(v0.x, v0.y, v0.z)
        p1 = Vector3(v1.x, v1.y, v1.z)
        p2 = Vector3(v2.x, v2.y, v2.z)

        edge1 = Vector3(p1.x - p0.x, p1.y - p0.y, p1.z - p0.z)
        edge2 = Vector3(p2.x - p0.x, p2.y - p0.y, p2.z - p0.z)

        normal = edge1.cross(edge2)
        return normal.normalize()
