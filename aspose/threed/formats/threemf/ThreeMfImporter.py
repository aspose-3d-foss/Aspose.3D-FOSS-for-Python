from typing import TYPE_CHECKING, Dict, List
import io
import zipfile
import xml.etree.ElementTree as ET

from ..Importer import Importer

if TYPE_CHECKING:
    from aspose.threed import Scene
    from .ThreeMfLoadOptions import ThreeMfLoadOptions


class ThreeMfImporter(Importer):
    def __init__(self):
        super().__init__()

    def supports_format(self, file_format) -> bool:
        from .ThreeMfFormat import ThreeMfFormat
        return isinstance(file_format, ThreeMfFormat)

    def import_scene(self, scene: 'Scene', stream, options):
        from .ThreeMfLoadOptions import ThreeMfLoadOptions
        from aspose.threed import Node
        from aspose.threed.entities import Mesh
        from aspose.threed.utilities import Vector4, Matrix4
        
        if not isinstance(options, ThreeMfLoadOptions):
            options = ThreeMfLoadOptions()
        
        if not hasattr(stream, 'read'):
            raise TypeError("Stream must support read() method")
        
        try:
            zip_file = zipfile.ZipFile(io.BytesIO(stream.read()))
        except Exception as e:
            raise ValueError(f"Failed to open 3MF file: {e}")
        
        model_content = self._find_model_content(zip_file)
        if model_content is None:
            raise ValueError("No 3D model found in 3MF file")
        
        root = ET.fromstring(model_content)
        
        model_unit = root.get('unit', 'millimeter')
        scale_factor = self._get_unit_scale(model_unit)
        
        resources = {}
        vertices_map = {}
        triangles_map = {}
        object_transforms = {}
        
        resources_elem = root.find('.//{http://schemas.microsoft.com/3dmanufacturing/core/2015/02}resources')
        if resources_elem is None:
            resources_elem = root.find('.//resources')
        
        if resources_elem is not None:
            self._parse_resources(resources_elem, resources, vertices_map, triangles_map, object_transforms, options, scale_factor)
        
        build_elem = root.find('.//{http://schemas.microsoft.com/3dmanufacturing/core/2015/02}build')
        if build_elem is None:
            build_elem = root.find('.//build')
        
        if build_elem is not None:
            self._parse_build(build_elem, scene, resources, vertices_map, triangles_map, options)
        
        zip_file.close()

    def _find_model_content(self, zip_file):
        for name in zip_file.namelist():
            if name.endswith('.model') or '3dmodel.model' in name.lower():
                try:
                    return zip_file.read(name)
                except:
                    pass
        return None

    def _get_unit_scale(self, unit):
        scales = {
            'micron': 0.000001,
            'millimeter': 0.001,
            'centimeter': 0.01,
            'meter': 1.0,
            'inch': 0.0254,
            'foot': 0.3048
        }
        return scales.get(unit.lower(), 0.001)

    def _parse_resources(self, resources_elem, resources, vertices_map, triangles_map, object_transforms, options, scale):
        from aspose.threed.utilities import Vector4
        ns = {'m': 'http://schemas.microsoft.com/3dmanufacturing/core/2015/02'}
        
        for obj_elem in resources_elem.findall('.//m:object', ns):
            if resources_elem.findall('.//m:object', ns):
                break
        
        obj_elems = resources_elem.findall('.//m:object', ns)
        if not obj_elems:
            obj_elems = resources_elem.findall('object')
        
        for obj_elem in obj_elems:
            obj_id = obj_elem.get('id')
            obj_name = obj_elem.get('name', f'object_{obj_id}')
            
            mesh_elem = obj_elem.find('m:mesh', ns)
            if mesh_elem is None:
                mesh_elem = obj_elem.find('mesh')
            
            if mesh_elem is not None:
                vertices = []
                triangles = []
                
                verts_elem = mesh_elem.find('m:vertices', ns)
                if verts_elem is None:
                    verts_elem = mesh_elem.find('vertices')
                
                if verts_elem is not None:
                    vert_elems = verts_elem.findall('m:vertex', ns)
                    if not vert_elems:
                        vert_elems = verts_elem.findall('vertex')
                    
                    for v_elem in vert_elems:
                        x = float(v_elem.get('x', 0)) * scale
                        y = float(v_elem.get('y', 0)) * scale
                        z = float(v_elem.get('z', 0)) * scale
                        
                        if options.flip_coordinate_system:
                            y, z = z, y
                        
                        vertices.append(Vector4(x, y, z, 1.0))
                
                tris_elem = mesh_elem.find('m:triangles', ns)
                if tris_elem is None:
                    tris_elem = mesh_elem.find('triangles')
                
                if tris_elem is not None:
                    tri_elems = tris_elem.findall('m:triangle', ns)
                    if not tri_elems:
                        tri_elems = tris_elem.findall('triangle')
                    
                    for t_elem in tri_elems:
                        v1 = int(t_elem.get('v1', 0))
                        v2 = int(t_elem.get('v2', 0))
                        v3 = int(t_elem.get('v3', 0))
                        triangles.append([v1, v2, v3])
                
                vertices_map[obj_id] = vertices
                triangles_map[obj_id] = triangles
                resources[obj_id] = {'name': obj_name, 'type': 'mesh'}
            
            comp_elems = obj_elem.findall('m:components/m:component', ns)
            if not comp_elems:
                comp_elems = obj_elem.findall('components/component')
            
            if comp_elems:
                resources[obj_id] = {'name': obj_name, 'type': 'components', 'components': []}
                for comp_elem in comp_elems:
                    comp_id = comp_elem.get('objectid')
                    transform_str = comp_elem.get('transform', '')
                    transform = self._parse_transform(transform_str)
                    resources[obj_id]['components'].append((comp_id, transform))

    def _parse_transform(self, transform_str):
        if not transform_str:
            return None
        
        try:
            values = [float(x) for x in transform_str.split()]
            if len(values) == 12:
                from aspose.threed.utilities import Matrix4
                return Matrix4(values[0], values[1], values[2], 0,
                                values[3], values[4], values[5], 0,
                                values[6], values[7], values[8], 0,
                                values[9], values[10], values[11], 1)
        except:
            pass
        
        return None

    def _parse_build(self, build_elem, scene, resources, vertices_map, triangles_map, options):
        ns = {'m': 'http://schemas.microsoft.com/3dmanufacturing/core/2015/02'}
        
        item_elems = build_elem.findall('m:item', ns)
        if not item_elems:
            item_elems = build_elem.findall('item')
        
        for item_elem in item_elems:
            obj_id = item_elem.get('objectid')
            item_name = resources[obj_id]['name'] if obj_id in resources else f'item_{obj_id}'
            
            transform_str = item_elem.get('transform', '')
            transform = self._parse_transform(transform_str)
            
            if obj_id in resources and resources[obj_id]['type'] == 'mesh':
                self._create_mesh_node(scene, obj_id, item_name, transform, vertices_map, triangles_map)

    def _create_mesh_node(self, scene, obj_id, name, transform, vertices_map, triangles_map):
        from aspose.threed import Node
        from aspose.threed.entities import Mesh
        from aspose.threed.utilities import Vector4
        
        if obj_id not in vertices_map or obj_id not in triangles_map:
            return
        
        vertices = vertices_map[obj_id]
        triangles = triangles_map[obj_id]
        
        mesh = Mesh(name)
        
        for v in vertices:
            mesh._control_points.append(v)
        
        for tri in triangles:
            mesh.create_polygon(tri[0], tri[1], tri[2])
        
        node = Node(name)
        node.entity = mesh
        node.parent_node = scene.root_node
        
        if transform is not None:
            node.transform.transform_matrix = transform
