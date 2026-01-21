from typing import TYPE_CHECKING
import struct
import io

from ..Importer import Importer

if TYPE_CHECKING:
    from aspose.threed import Scene
    from .StlLoadOptions import StlLoadOptions


class StlImporter(Importer):
    def __init__(self):
        super().__init__()

    def supports_format(self, file_format) -> bool:
        from .StlFormat import StlFormat
        return isinstance(file_format, StlFormat)

    def import_scene(self, scene: 'Scene', stream, options: 'StlLoadOptions'):
        from .StlLoadOptions import StlLoadOptions
        from aspose.threed import Node
        from aspose.threed.entities import Mesh
        from aspose.threed.utilities import Vector4
        
        if not isinstance(options, StlLoadOptions):
            options = StlLoadOptions()
        
        content = b""
        if hasattr(stream, 'read'):
            if hasattr(stream, 'seek'):
                stream.seek(0)
            data = stream.read()
            if isinstance(data, str):
                content = data.encode('utf-8', errors='ignore')
            else:
                content = data
        else:
            raise TypeError("Stream must support read() method")
        
        if len(content) == 0:
            return
        
        is_binary = self._is_binary_stl(content)
        
        mesh_name = "mesh"
        vertices = []
        normals = []
        
        if is_binary:
            mesh_name, vertices, normals = self._read_binary_stl(content, options)
        else:
            if isinstance(content, bytes):
                content_text = content.decode('utf-8', errors='ignore')
            else:
                content_text = content
            mesh_name, vertices, normals = self._read_ascii_stl(content_text, options)
        
        mesh = Mesh(mesh_name)
        for v in vertices:
            mesh._control_points.append(v)
        
        for i in range(0, len(vertices), 3):
            mesh.create_polygon(i, i + 1, i + 2)
        
        node = Node(mesh_name)
        node.entity = mesh
        node.parent_node = scene.root_node

    def _is_binary_stl(self, content: bytes) -> bool:
        if len(content) < 84:
            return False
        
        try:
            facet_count = struct.unpack('<I', content[80:84])[0]
            expected_size = 84 + facet_count * 50
            if len(content) >= expected_size:
                return True
        except:
            pass
        
        try:
            text = content.decode('utf-8', errors='ignore').strip().lower()
            return not text.startswith('solid')
        except:
            return True

    def _read_ascii_stl(self, content: str, options: 'StlLoadOptions'):
        from aspose.threed.utilities import Vector4
        
        mesh_name = "mesh"
        vertices = []
        normals = []
        
        lines = content.split('\n')
        
        current_normal = None
        current_vertices = []
        
        for line in lines:
            line = line.strip()
            parts = line.split()
            
            if not parts:
                continue
            
            keyword = parts[0].lower()
            
            if keyword == 'solid':
                if len(parts) > 1:
                    mesh_name = parts[1]
            
            elif keyword == 'facet' and len(parts) > 1 and parts[1].lower() == 'normal':
                if len(parts) >= 5:
                    nx, ny, nz = float(parts[2]), float(parts[3]), float(parts[4])
                    if options.flip_coordinate_system:
                        ny, nz = nz, ny
                    current_normal = Vector4(nx, ny, nz, 0)
            
            elif keyword == 'vertex':
                x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
                if options.flip_coordinate_system:
                    y, z = z, y
                vertices.append(Vector4(x * options.scale, y * options.scale, z * options.scale, 1))
                current_vertices.append(len(vertices) - 1)
            
            elif keyword == 'endfacet':
                if current_normal:
                    for _ in range(len(current_vertices)):
                        normals.append(current_normal)
                current_normal = None
                current_vertices = []
        
        return mesh_name, vertices, normals

    def _read_binary_stl(self, content: bytes, options: 'StlLoadOptions'):
        from aspose.threed.utilities import Vector4
        
        header = content[:80]
        try:
            mesh_name = header.decode('utf-8', errors='ignore').strip()
            if not mesh_name:
                mesh_name = "mesh"
        except:
            mesh_name = "mesh"
        
        facet_count = struct.unpack('<I', content[80:84])[0]
        
        vertices = []
        normals = []
        
        offset = 84
        for _ in range(facet_count):
            if offset + 50 > len(content):
                break
            
            facet_data = content[offset:offset + 50]
            values = struct.unpack('<12fH', facet_data)
            
            nx, ny, nz = values[0], values[1], values[2]
            if options.flip_coordinate_system:
                ny, nz = nz, ny
            normal = Vector4(nx, ny, nz, 0)
            
            for i in range(3):
                vx, vy, vz = values[3 + i * 3], values[4 + i * 3], values[5 + i * 3]
                if options.flip_coordinate_system:
                    vy, vz = vz, vy
                vertices.append(Vector4(vx * options.scale, vy * options.scale, vz * options.scale, 1))
            
            for _ in range(3):
                normals.append(normal)
            
            offset += 50
        
        return mesh_name, vertices, normals
