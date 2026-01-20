from typing import TYPE_CHECKING, Dict

from ..Exporter import Exporter

if TYPE_CHECKING:
    from aspose.threed import Scene
    from aspose.threed.formats import SaveOptions


class ObjExporter(Exporter):
    def __init__(self):
        super().__init__()

    def supports_format(self, file_format) -> bool:
        from .ObjFormat import ObjFormat
        return isinstance(file_format, ObjFormat)

    def export(self, scene: 'Scene', stream, options: 'SaveOptions'):
        from .ObjSaveOptions import ObjSaveOptions
        from .ObjFormat import ObjFormat
        
        if not isinstance(options, ObjSaveOptions):
            options = ObjSaveOptions()
        
        self._write_obj(scene, stream, options)

    def _write_obj(self, scene: 'Scene', stream, options: 'SaveOptions'):
        lines = []
        node_map = {}
        material_map = {}
        mat_index = 1
        
        self._collect_nodes(scene.root_node, node_map, material_map)
        
        for mat_id, mat in material_map.items():
            lines.extend(self._write_material(mat, mat_id))
        
        lines.append("")
        
        for node_id, node in sorted(node_map.items()):
            lines.extend(self._write_node(node, node_id))
            mesh = node.entity
            if mesh is not None:
                lines.extend(self._write_mesh_data(mesh, options))
                lines.extend(self._write_faces(mesh))
        
        content = '\n'.join(lines)
        
        if hasattr(stream, 'write'):
            stream.write(content)
        else:
            raise TypeError("Stream must support write() method")

    def _collect_nodes(self, node, node_map: Dict, material_map: Dict, node_id: int = 0):
        if node.entity is not None and node not in node_map.values():
            node_map[node_id] = node
            
            material = node.material
            if material is not None and id(material) not in material_map:
                material_map[id(material)] = material
            
            for child in node.child_nodes:
                node_id = self._collect_nodes(child, node_map, material_map, node_id + 1)
        
        return node_id

    def _write_material(self, material, mat_id: int):
        lines = []
        mat_name = material.name or f'Material_{mat_id}'
        lines.append(f"newmtl {mat_name}")
        
        if hasattr(material, 'diffuse_color') and material.diffuse_color is not None:
            lines.append(f"Kd {material.diffuse_color.x:.6f} {material.diffuse_color.y:.6f} {material.diffuse_color.z:.6f}")
        
        if hasattr(material, 'ambient_color') and material.ambient_color is not None:
            lines.append(f"Ka {material.ambient_color.x:.6f} {material.ambient_color.y:.6f} {material.ambient_color.z:.6f}")
        
        if hasattr(material, 'specular_color') and material.specular_color is not None:
            lines.append(f"Ks {material.specular_color.x:.6f} {material.specular_color.y:.6f} {material.specular_color.z:.6f}")
        
        if hasattr(material, 'shininess') and material.shininess > 0:
            lines.append(f"Ns {material.shininess:.6f}")
        
        if hasattr(material, 'transparency') and material.transparency > 0:
            lines.append(f"d {1.0 - material.transparency:.6f}")
        
        return lines

    def _write_node(self, node, node_id: int):
        lines = []
        lines.append(f"o {node.name or f'Node_{node_id}'}")
        return lines

    def _write_mesh_data(self, mesh, options):
        lines = []
        
        for cp in mesh.control_points:
            if hasattr(options, 'flip_coordinate_system') and options.flip_coordinate_system:
                lines.append(f"v {cp.x:.6f} {cp.z:.6f} {cp.y:.6f}")
            else:
                lines.append(f"v {cp.x:.6f} {cp.y:.6f} {cp.z:.6f}")
        
        lines.append("")
        return lines

    def _write_faces(self, mesh):
        lines = []
        polygons = mesh.polygons
        
        for face_indices in polygons:
            line = self._format_face(face_indices)
            lines.append(line)
        
        return lines

    def _format_face(self, indices):
        return "f " + " ".join(str(idx + 1) for idx in indices)
