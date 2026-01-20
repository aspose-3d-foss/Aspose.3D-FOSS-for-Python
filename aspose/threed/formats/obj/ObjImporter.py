from typing import TYPE_CHECKING, List, Dict, Tuple
import io

from ..Importer import Importer

if TYPE_CHECKING:
    from aspose.threed import Scene
    from .ObjLoadOptions import ObjLoadOptions


class ObjImporter(Importer):
    def __init__(self):
        super().__init__()

    def supports_format(self, file_format) -> bool:
        from .ObjFormat import ObjFormat
        return isinstance(file_format, ObjFormat)

    def import_scene(self, scene: 'Scene', stream, options: 'ObjLoadOptions'):
        from .ObjLoadOptions import ObjLoadOptions
        from aspose.threed import Node
        from aspose.threed.entities import Mesh
        from aspose.threed.utilities import Vector4, Vector2
        
        if not isinstance(options, ObjLoadOptions):
            options = ObjLoadOptions()
        
        vertices: List[Vector4] = []
        normals: List[Vector4] = []
        uvs: List[Vector2] = []
        
        current_object_name = None
        current_group_name = None
        current_mesh = None
        current_node = None
        current_vertex_map: Dict[int, int] = {}
        smoothing_group = 0
        
        content = ""
        if hasattr(stream, 'read'):
            if hasattr(stream, 'seek'):
                stream.seek(0)
            content = stream.read()
            if isinstance(content, bytes):
                content = content.decode('utf-8', errors='ignore')
        else:
            raise TypeError("Stream must support read() method")
        
        lines = content.split('\n')
        
        scale = options.scale
        
        for line in lines:
            line = line.strip()
            
            if not line or line.startswith('#'):
                continue
            
            parts = line.split()
            if not parts:
                continue
            
            keyword = parts[0].lower()
            
            if keyword == 'v':
                x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
                w = float(parts[4]) if len(parts) > 4 else 1.0
                
                if options.flip_coordinate_system:
                    y, z = z, y
                
                vertices.append(Vector4(x * scale, y * scale, z * scale, w))
            
            elif keyword == 'vn':
                nx, ny, nz = float(parts[1]), float(parts[2]), float(parts[3])
                
                if options.normalize_normal:
                    length = (nx * nx + ny * ny + nz * nz) ** 0.5
                    if length > 0:
                        nx, ny, nz = nx / length, ny / length, nz / length
                
                if options.flip_coordinate_system:
                    ny, nz = nz, ny
                
                normals.append(Vector4(nx, ny, nz, 0))
            
            elif keyword == 'vt':
                u = float(parts[1])
                v = float(parts[2]) if len(parts) > 2 else 0.0
                uvs.append(Vector2(u, v))
            
            elif keyword == 'f':
                if current_mesh is None:
                    current_mesh = Mesh(current_object_name or "mesh")
                    current_node = Node(current_object_name or "mesh")
                    current_node.entity = current_mesh
                    current_node.parent_node = scene.root_node
                    current_vertex_map = {}
                
                face_indices = []
                vertex_normals = []
                vertex_uvs = []
                
                for part in parts[1:]:
                    indices = part.split('/')
                    
                    v_idx = int(indices[0]) if indices[0] else 0
                    vt_idx = int(indices[1]) if len(indices) > 1 and indices[1] else 0
                    vn_idx = int(indices[2]) if len(indices) > 2 and indices[2] else 0
                    
                    if v_idx < 0:
                        v_idx = len(vertices) + v_idx
                    else:
                        v_idx = v_idx - 1
                    
                    if v_idx < 0:
                        v_idx = 0
                    
                    if v_idx not in current_vertex_map:
                        if v_idx < len(vertices):
                            current_vertex_map[v_idx] = len(current_mesh._control_points)
                            current_mesh._control_points.append(vertices[v_idx])
                        else:
                            current_vertex_map[v_idx] = len(current_mesh._control_points)
                            current_mesh._control_points.append(Vector4(0, 0, 0, 1))
                    
                    local_idx = current_vertex_map[v_idx]
                    face_indices.append(local_idx)
                    
                    if vt_idx < 0:
                        vt_idx = len(uvs) + vt_idx
                    else:
                        vt_idx = vt_idx - 1
                    
                    if vn_idx < 0:
                        vn_idx = len(normals) + vn_idx
                    else:
                        vn_idx = vn_idx - 1
                    
                    if vt_idx >= 0:
                        vertex_uvs.append((len(face_indices) - 1, vt_idx))
                    if vn_idx >= 0:
                        vertex_normals.append((len(face_indices) - 1, vn_idx))
                
                if len(face_indices) >= 3:
                    current_mesh.create_polygon(face_indices)
            
            elif keyword == 'o':
                current_object_name = parts[1] if len(parts) > 1 else None
                current_group_name = None
                current_mesh = None
                current_node = None
                current_vertex_map = {}
            
            elif keyword == 'g':
                current_group_name = parts[1] if len(parts) > 1 else None
                if current_object_name is None:
                    current_object_name = current_group_name
                current_mesh = None
                current_node = None
                current_vertex_map = {}
            
            elif keyword == 's':
                smoothing_group = int(parts[1]) if len(parts) > 1 and parts[1] != 'off' else 0
            
            elif keyword == 'usemtl' and options.enable_materials:
                pass
