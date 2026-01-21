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

        PolygonModifier._copy_vertex_elements(mesh, new_mesh)

        return new_mesh

    @staticmethod
    def _copy_vertex_elements(source_mesh: 'Mesh', target_mesh: 'Mesh'):
        from .VertexElement import VertexElement
        from .MappingMode import MappingMode
        from .ReferenceMode import ReferenceMode

        for ve in source_mesh.vertex_elements:
            new_ve = target_mesh.create_element(ve.vertex_element_type, ve.mapping_mode, ve.reference_mode)
            new_ve._data = list(ve._data)
            new_ve._indices = list(ve._indices) if ve._indices else None

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

        vertices = list(polygon)
        triangles = []

        while len(vertices) > 3:
            ear_found = False
            for i in range(len(vertices)):
                prev_idx = (i - 1) % len(vertices)
                next_idx = (i + 1) % len(vertices)

                prev = vertices[prev_idx]
                curr = vertices[i]
                next_v = vertices[next_idx]

                if PolygonModifier._is_ear(control_points, vertices, prev, curr, next_v):
                    triangles.append([prev, curr, next_v])

                    if generate_normals and nor_out is not None:
                        normal = PolygonModifier._calculate_normal(control_points, [prev, curr, next_v])
                        nor_out.append(normal)

                    vertices.pop(i)
                    ear_found = True
                    break

            if not ear_found:
                for i in range(1, len(vertices)):
                    triangles.append([vertices[0], vertices[i], vertices[(i + 1) % len(vertices)]])
                    if generate_normals and nor_out is not None:
                        normal = PolygonModifier._calculate_normal(control_points, [vertices[0], vertices[i], vertices[(i + 1) % len(vertices)]])
                        nor_out.append(normal)
                break

        if len(vertices) == 3:
            triangles.append(vertices[:])
            if generate_normals and nor_out is not None:
                normal = PolygonModifier._calculate_normal(control_points, vertices)
                nor_out.append(normal)

        return triangles

    @staticmethod
    def _is_ear(control_points: List[Vector4], vertices: List[int], prev: int, curr: int, next_v: int) -> bool:
        if not PolygonModifier._is_convex(control_points, prev, curr, next_v):
            return False

        p0 = Vector3(control_points[prev].x, control_points[prev].y, control_points[prev].z)
        p1 = Vector3(control_points[curr].x, control_points[curr].y, control_points[curr].z)
        p2 = Vector3(control_points[next_v].x, control_points[next_v].y, control_points[next_v].z)

        for v in vertices:
            if v == prev or v == curr or v == next_v:
                continue

            p_test = Vector3(control_points[v].x, control_points[v].y, control_points[v].z)

            if PolygonModifier._point_in_triangle(p_test, p0, p1, p2):
                return False

        return True

    @staticmethod
    def _is_convex(control_points: List[Vector4], prev: int, curr: int, next_v: int) -> bool:
        p_prev = Vector3(control_points[prev].x, control_points[prev].y, control_points[prev].z)
        p_curr = Vector3(control_points[curr].x, control_points[curr].y, control_points[curr].z)
        p_next = Vector3(control_points[next_v].x, control_points[next_v].y, control_points[next_v].z)

        edge1 = Vector3(p_curr.x - p_prev.x, p_curr.y - p_prev.y, p_curr.z - p_prev.z)
        edge2 = Vector3(p_next.x - p_curr.x, p_next.y - p_curr.y, p_next.z - p_curr.z)

        cross = edge1.cross(edge2)
        normal = PolygonModifier._calculate_polygon_normal(control_points, [prev, curr, next_v])

        return cross.dot(normal) > 0

    @staticmethod
    def _point_in_triangle(p: Vector3, a: Vector3, b: Vector3, c: Vector3) -> bool:
        v0 = Vector3(c.x - a.x, c.y - a.y, c.z - a.z)
        v1 = Vector3(b.x - a.x, b.y - a.y, b.z - a.z)
        v2 = Vector3(p.x - a.x, p.y - a.y, p.z - a.z)

        dot00 = v0.x * v0.x + v0.y * v0.y + v0.z * v0.z
        dot01 = v0.x * v1.x + v0.y * v1.y + v0.z * v1.z
        dot02 = v0.x * v2.x + v0.y * v2.y + v0.z * v2.z
        dot11 = v1.x * v1.x + v1.y * v1.y + v1.z * v1.z
        dot12 = v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

        inv_denom = 1 / (dot00 * dot11 - dot01 * dot01)
        u = (dot11 * dot02 - dot01 * dot12) * inv_denom
        v = (dot00 * dot12 - dot01 * dot02) * inv_denom

        return (u >= 0) and (v >= 0) and (u + v < 1)

    @staticmethod
    def _polygon_normal(control_points: List[Vector4], polygon: List[int]) -> Vector3:
        if len(polygon) < 3:
            return Vector3(0, 0, 1)

        normal = Vector3(0, 0, 0)
        for i in range(len(polygon)):
            j = (i + 1) % len(polygon)
            p0 = Vector3(control_points[polygon[i]].x, control_points[polygon[i]].y, control_points[polygon[i]].z)
            p1 = Vector3(control_points[polygon[j]].x, control_points[polygon[j]].y, control_points[polygon[j]].z)
            normal.x += (p0.y - p1.y) * (p0.z + p1.z)
            normal.y += (p0.z - p1.z) * (p0.x + p1.x)
            normal.z += (p0.x - p1.x) * (p0.y + p1.y)

        return normal.normalize()

    @staticmethod
    def _calculate_polygon_normal(control_points: List[Vector4], polygon: List[int]) -> Vector3:
        return PolygonModifier._polygon_normal(control_points, polygon)

    @staticmethod
    def _triangulate_polygon_to_mesh(mesh: 'Mesh', polygon: List[int]):
        triangles = PolygonModifier._triangulate_polygon(mesh._control_points, polygon, False, None)
        for triangle in triangles:
            if len(triangle) == 3:
                mesh.create_polygon(triangle[0], triangle[1], triangle[2])

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
