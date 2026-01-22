from typing import TYPE_CHECKING, List, Tuple, Optional
import io
import zipfile
import xml.etree.ElementTree as ET

from ..Exporter import Exporter

if TYPE_CHECKING:
    from aspose.threed import Scene
    from aspose.threed.entities import Mesh
    from aspose.threed import Node
    from .ThreeMfSaveOptions import ThreeMfSaveOptions


class ThreeMfExporter(Exporter):
    def __init__(self):
        super().__init__()

    def supports_format(self, file_format) -> bool:
        from .ThreeMfFormat import ThreeMfFormat
        return isinstance(file_format, ThreeMfFormat)

    def export(self, scene: 'Scene', stream, options):
        from .ThreeMfSaveOptions import ThreeMfSaveOptions
        from aspose.threed.entities import Mesh
        
        if not isinstance(options, ThreeMfSaveOptions):
            options = ThreeMfSaveOptions()
        
        mesh_data_list = self._collect_meshes(scene, options)
        
        if not mesh_data_list:
            return
        
        self._write_3mf_file(stream, mesh_data_list, scene, options)
    
    def _collect_meshes(self, scene: 'Scene', options: 'ThreeMfSaveOptions'):
        from aspose.threed.entities import Mesh
        
        mesh_data_list = []
        obj_id = 1
        
        def visit_node(node, parent_transform=None):
            nonlocal obj_id
            from aspose.threed.utilities import Matrix4
            from .ThreeMfFormat import ThreeMfFormat
            
            if parent_transform is None:
                current_transform = node.transform.transform_matrix
            else:
                current_transform = parent_transform.concatenate(node.transform.transform_matrix)
            
            if node.entity and isinstance(node.entity, Mesh):
                if not options.build_all:
                    format_instance = ThreeMfFormat()
                    if not format_instance.is_buildable(node):
                        return
                
                mesh = node.entity
                if not self._is_triangulated(mesh):
                    mesh = mesh.triangulate()
                
                format_instance = ThreeMfFormat()
                object_type = format_instance.get_object_type(node)
                
                mesh_data = {
                    'id': obj_id,
                    'name': node.name or f'mesh_{obj_id}',
                    'type': object_type,
                    'mesh': mesh,
                    'transform': current_transform
                }
                mesh_data_list.append(mesh_data)
                obj_id += 1
            
            for child in node.child_nodes:
                visit_node(child, current_transform)
        
        for child in scene.root_node.child_nodes:
            visit_node(child)
        
        return mesh_data_list
    
    def _is_triangulated(self, mesh: 'Mesh') -> bool:
        for i in range(mesh.polygon_count):
            if mesh.get_polygon_size(i) != 3:
                return False
        return True
    
    def _write_3mf_file(self, stream, mesh_data_list, scene: 'Scene', options: 'ThreeMfSaveOptions'):
        import xml.etree.ElementTree as ET
        from aspose.threed.utilities import Vector4
        
        xml_content = self._build_3mf_xml(mesh_data_list, options)
        
        compression = zipfile.ZIP_DEFLATED if options.enable_compression else zipfile.ZIP_STORED
        
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', compression) as zf:
            zf.writestr('3D/3dmodel.model', xml_content)
        
        zip_buffer.seek(0)
        
        if hasattr(stream, 'write'):
            try:
                stream.write(zip_buffer.read())
            except TypeError:
                stream.write(zip_buffer.getvalue())
    
    def _build_3mf_xml(self, mesh_data_list, options: 'ThreeMfSaveOptions'):
        root = ET.Element('model', {
            'unit': options.unit,
            'xmlns': 'http://schemas.microsoft.com/3dmanufacturing/core/2015/02'
        })
        
        resources_elem = ET.SubElement(root, 'resources')
        
        scale_factor = self._get_unit_scale_factor(options.unit)
        
        for mesh_data in mesh_data_list:
            object_type = mesh_data.get('type', 'model')
            obj_elem = ET.SubElement(resources_elem, 'object', {
                'id': str(mesh_data['id']),
                'name': mesh_data['name'],
                'type': object_type
            })
            
            mesh_elem = ET.SubElement(obj_elem, 'mesh')
            
            vertices_elem = ET.SubElement(mesh_elem, 'vertices')
            mesh = mesh_data['mesh']
            
            for v in mesh._control_points:
                x = v.x * scale_factor
                y = v.y * scale_factor
                z = v.z * scale_factor
                
                if options.flip_coordinate_system:
                    y, z = z, y
                
                ET.SubElement(vertices_elem, 'vertex', {
                    'x': f'{x:.6f}',
                    'y': f'{y:.6f}',
                    'z': f'{z:.6f}'
                })
            
            triangles_elem = ET.SubElement(mesh_elem, 'triangles')
            
            for i in range(mesh.polygon_count):
                v1 = mesh._polygons[i * 3]
                v2 = mesh._polygons[i * 3 + 1]
                v3 = mesh._polygons[i * 3 + 2]
                
                ET.SubElement(triangles_elem, 'triangle', {
                    'v1': str(v1),
                    'v2': str(v2),
                    'v3': str(v3)
                })
        
        build_elem = ET.SubElement(root, 'build')
        
        for mesh_data in mesh_data_list:
            transform_str = self._matrix_to_string(mesh_data['transform'])
            
            ET.SubElement(build_elem, 'item', {
                'objectid': str(mesh_data['id']),
                'transform': transform_str
            })
        
        if options.pretty_print:
            return self._prettify_xml(root)
        return ET.tostring(root, encoding='unicode', xml_declaration=True)
    
    def _get_unit_scale_factor(self, unit: str) -> float:
        unit_scales = {
            'micron': 1000000.0,
            'millimeter': 1000.0,
            'centimeter': 100.0,
            'inch': 39.37007874015748,
            'foot': 3.280839895013123,
            'meter': 1.0
        }
        return unit_scales.get(unit, 1000.0)
    
    def _prettify_xml(self, elem: ET.Element) -> str:
        from xml.dom import minidom
        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent='  ', encoding='utf-8').decode('utf-8')
    
    def _matrix_to_string(self, matrix):
        m = matrix
        return f'{m.m00:.6f} {m.m01:.6f} {m.m02:.6f} {m.m10:.6f} {m.m11:.6f} {m.m12:.6f} {m.m20:.6f} {m.m21:.6f} {m.m22:.6f} {m.m30:.6f} {m.m31:.6f} {m.m32:.6f}'
