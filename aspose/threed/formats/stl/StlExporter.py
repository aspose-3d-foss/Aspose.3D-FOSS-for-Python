from typing import TYPE_CHECKING
import struct
import io

from ..Exporter import Exporter

if TYPE_CHECKING:
    from aspose.threed import Scene
    from aspose.threed.entities import Mesh
    from .StlSaveOptions import StlSaveOptions


class StlExporter(Exporter):
    def __init__(self):
        super().__init__()

    def supports_format(self, file_format) -> bool:
        from .StlFormat import StlFormat
        return isinstance(file_format, StlFormat)

    def export(self, scene: 'Scene', stream, options: 'StlSaveOptions'):
        from .StlSaveOptions import StlSaveOptions
        from aspose.threed.entities import Mesh
        from aspose.threed.utilities import Vector4
        
        if not isinstance(options, StlSaveOptions):
            options = StlSaveOptions()
        
        meshes = self._collect_meshes(scene)
        
        if options.binary_mode:
            self._write_binary_stl(stream, meshes, scene, options)
        else:
            self._write_ascii_stl(stream, meshes, scene, options)

    def _collect_meshes(self, scene: 'Scene'):
        meshes = []
        
        def visit_node(node):
            if node.entity:
                from aspose.threed.entities import Mesh
                if isinstance(node.entity, Mesh):
                    mesh = node.entity
                    if not self._is_triangulated(mesh):
                        mesh = mesh.triangulate()
                    meshes.append(mesh)
            for child in node.child_nodes:
                visit_node(child)
        
        visit_node(scene.root_node)
        return meshes

    def _is_triangulated(self, mesh: 'Mesh') -> bool:
        for i in range(mesh.polygon_count):
            if mesh.get_polygon_size(i) != 3:
                return False
        return True

    def _write_ascii_stl(self, stream, meshes, scene: 'Scene', options: 'StlSaveOptions'):
        from aspose.threed.utilities import Vector4
        
        header_name = options.file_name if options.file_name else "exported"
        header_name = header_name.split('/')[-1].split('\\')[-1]
        header_name = header_name.rsplit('.', 1)[0] if '.' in header_name else header_name
        header_name = ''.join(c for c in header_name if c.isalnum() or c in ' _-')
        
        if not header_name:
            header_name = "exported"
        
        lines = [f"solid {header_name}"]
        
        for mesh in meshes:
            for i in range(mesh.polygon_count):
                v0_idx = mesh._polygons[i * 3]
                v1_idx = mesh._polygons[i * 3 + 1]
                v2_idx = mesh._polygons[i * 3 + 2]
                
                v1 = mesh._control_points[v0_idx]
                v2 = mesh._control_points[v1_idx]
                v3 = mesh._control_points[v2_idx]
                
                normal = self._compute_normal(v1, v2, v3)
                
                if options.flip_coordinate_system:
                    y1, z1 = v1.y, v1.z
                    v1 = Vector4(v1.x, z1, y1, v1.w)
                    y2, z2 = v2.y, v2.z
                    v2 = Vector4(v2.x, z2, y2, v2.w)
                    y3, z3 = v3.y, v3.z
                    v3 = Vector4(v3.x, z3, y3, v3.w)
                    ny, nz = normal.y, normal.z
                    normal = Vector4(normal.x, nz, ny, normal.w)
                
                nx = normal.x
                ny = normal.y
                nz = normal.z
                
                x1, y1, z1 = v1.x * options.scale, v1.y * options.scale, v1.z * options.scale
                x2, y2, z2 = v2.x * options.scale, v2.y * options.scale, v2.z * options.scale
                x3, y3, z3 = v3.x * options.scale, v3.y * options.scale, v3.z * options.scale
                
                lines.append(f"  facet normal {nx:.6e} {ny:.6e} {nz:.6e}")
                lines.append("    outer loop")
                lines.append(f"      vertex {x1:.6e} {y1:.6e} {z1:.6e}")
                lines.append(f"      vertex {x2:.6e} {y2:.6e} {z2:.6e}")
                lines.append(f"      vertex {x3:.6e} {y3:.6e} {z3:.6e}")
                lines.append("    endloop")
                lines.append("  endfacet")
        
        lines.append(f"endsolid {header_name}")
        
        content = '\n'.join(lines)
        if hasattr(stream, 'write'):
            try:
                stream.write(content)
            except TypeError:
                stream.write(content.encode('utf-8'))

    def _write_binary_stl(self, stream, meshes, scene: 'Scene', options: 'StlSaveOptions'):
        from aspose.threed.utilities import Vector4
        
        triangles_data = b""
        
        for mesh in meshes:
            for i in range(mesh.polygon_count):
                v0_idx = mesh._polygons[i * 3]
                v1_idx = mesh._polygons[i * 3 + 1]
                v2_idx = mesh._polygons[i * 3 + 2]
                
                v1 = mesh._control_points[v0_idx]
                v2 = mesh._control_points[v1_idx]
                v3 = mesh._control_points[v2_idx]
                
                normal = self._compute_normal(v1, v2, v3)
                
                if options.flip_coordinate_system:
                    y1, z1 = v1.y, v1.z
                    v1 = Vector4(v1.x, z1, y1, v1.w)
                    y2, z2 = v2.y, v2.z
                    v2 = Vector4(v2.x, z2, y2, v2.w)
                    y3, z3 = v3.y, v3.z
                    v3 = Vector4(v3.x, z3, y3, v3.w)
                    ny, nz = normal.y, normal.z
                    normal = Vector4(normal.x, nz, ny, normal.w)
                
                x1, y1, z1 = v1.x * options.scale, v1.y * options.scale, v1.z * options.scale
                x2, y2, z2 = v2.x * options.scale, v2.y * options.scale, v2.z * options.scale
                x3, y3, z3 = v3.x * options.scale, v3.y * options.scale, v3.z * options.scale
                
                nx, ny, nz = normal.x, normal.y, normal.z
                
                triangles_data += struct.pack('<12f', nx, ny, nz, x1, y1, z1, x2, y2, z2, x3, y3, z3)
                triangles_data += struct.pack('<H', 0)
        
        header_name = options.file_name if options.file_name else "exported"
        header_name = header_name.encode('utf-8', errors='ignore')[:80]
        header = header_name.ljust(80, b'\x00')
        
        facet_count = len(triangles_data) // 50
        
        content = header + struct.pack('<I', facet_count) + triangles_data
        
        if hasattr(stream, 'write'):
            stream.write(content)

    def _compute_normal(self, v1, v2, v3):
        from aspose.threed.utilities import Vector4
        
        dx1 = v2.x - v1.x
        dy1 = v2.y - v1.y
        dz1 = v2.z - v1.z
        dx2 = v3.x - v1.x
        dy2 = v3.y - v1.y
        dz2 = v3.z - v1.z
        
        nx = dy1 * dz2 - dz1 * dy2
        ny = dz1 * dx2 - dx1 * dz2
        nz = dx1 * dy2 - dy1 * dx2
        
        length = (nx * nx + ny * ny + nz * nz) ** 0.5
        if length > 1e-10:
            nx /= length
            ny /= length
            nz /= length
        
        return Vector4(nx, ny, nz, 0)
