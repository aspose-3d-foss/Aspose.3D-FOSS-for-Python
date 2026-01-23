from typing import TYPE_CHECKING, Dict, List
import io
import zipfile
import xml.etree.ElementTree as ET

from ..Importer import Importer

if TYPE_CHECKING:
    from aspose.threed import Scene
    from .ThreeMfLoadOptions import ThreeMfLoadOptions

from aspose.threed.utilities.FVector4 import FVector4
from aspose.threed.entities.MappingMode import MappingMode
from aspose.threed.entities.ReferenceMode import ReferenceMode


class ThreeMfImporter(Importer):
    def __init__(self):
        super().__init__()
        self._material_map = {}

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
        
        ns = None
        if '}' in root.tag:
            ns = root.tag.split('}')[0] + '}'
        
        if ns:
            ns_dict = {'m': ns}
        else:
            ns_dict = {}
        
        resources = {}
        vertices_map = {}
        triangles_map = {}
        object_materials = {}
        triangle_materials = {}
        
        resources_elem = root.find(f'.//{ns}resources') if ns else root.find('.//resources')
        if resources_elem is None:
            resources_elem = root.find('.//resources')
        
        if resources_elem is not None:
            self._parse_resources(resources_elem, resources, vertices_map, triangles_map, object_materials, triangle_materials, options, scale_factor, ns_dict)
        
        build_elem = root.find(f'.//{ns}build') if ns else root.find('.//build')
        if build_elem is None:
            build_elem = root.find('.//build')
        
        if build_elem is not None:
            self._parse_build(build_elem, scene, resources, vertices_map, triangles_map, object_materials, triangle_materials, options, ns_dict)
        
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

    def _parse_resources(self, resources_elem, resources, vertices_map, triangles_map, object_materials, triangle_materials, options, scale, ns_dict):
        from aspose.threed.utilities import Vector4
        
        ns = ns_dict.get('m', '') if isinstance(ns_dict, dict) and 'm' in ns_dict else ''
        
        color_map = {}
        material_map = {}
        
        color_elems = resources_elem.findall(f'{ns}color') if ns else resources_elem.findall('color')
        for color_elem in color_elems:
            color_id = color_elem.get('id')
            color_value = color_elem.get('value')
            color_map[color_id] = color_value
        
        material_elems = resources_elem.findall(f'{ns}material') if ns else resources_elem.findall('material')
        for material_elem in material_elems:
            material_id = material_elem.get('id')
            color_id = material_elem.get('colorid')
            if color_id in color_map:
                material_map[material_id] = color_map[color_id]
        
        for color_id, color_value in color_map.items():
            if color_id not in material_map:
                material_map[color_id] = color_value
        
        self._material_map = material_map
        
        obj_elems = resources_elem.findall(f'{ns}object') if ns else resources_elem.findall('object')
        
        for obj_elem in obj_elems:
            obj_id = obj_elem.get('id')
            obj_name = obj_elem.get('name', f'object_{obj_id}')
            obj_material_id = obj_elem.get('materialid')
            
            mesh_elem = obj_elem.find(f'{ns}mesh') if ns else obj_elem.find('mesh')
            
            if mesh_elem is not None:
                vertices = []
                triangles = []
                
                verts_elem = mesh_elem.find(f'{ns}vertices') if ns else mesh_elem.find('vertices')
                
                if verts_elem is not None:
                    vert_elems = verts_elem.findall(f'{ns}vertex') if ns else verts_elem.findall('vertex')
                    
                    for v_elem in vert_elems:
                        x = float(v_elem.get('x', 0)) * scale
                        y = float(v_elem.get('y', 0)) * scale
                        z = float(v_elem.get('z', 0)) * scale
                        
                        if options.flip_coordinate_system:
                            y, z = z, y
                        
                        vertices.append(Vector4(x, y, z, 1.0))
                
                tris_elem = mesh_elem.find(f'{ns}triangles') if ns else mesh_elem.find('triangles')
                
                if tris_elem is not None:
                    tri_elems = tris_elem.findall(f'{ns}triangle') if ns else tris_elem.findall('triangle')
                    
                    for t_elem in tri_elems:
                        v1 = int(t_elem.get('v1', 0))
                        v2 = int(t_elem.get('v2', 0))
                        v3 = int(t_elem.get('v3', 0))
                        tri_material_id = t_elem.get('materialid')
                        triangles.append([v1, v2, v3, tri_material_id])
                
                vertices_map[obj_id] = vertices
                triangles_map[obj_id] = triangles
                resources[obj_id] = {'name': obj_name, 'type': 'mesh'}
                if obj_material_id is not None:
                    object_materials[obj_id] = obj_material_id
            
            comp_elems = obj_elem.findall(f'{ns}components/{ns}component') if ns else obj_elem.findall('components/component')
            
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

    def _parse_build(self, build_elem, scene, resources, vertices_map, triangles_map, object_materials, triangle_materials, options, ns_dict):
        ns = ns_dict.get('m', '') if isinstance(ns_dict, dict) and 'm' in ns_dict else ''
        
        item_elems = build_elem.findall(f'{ns}item') if ns else build_elem.findall('item')
        
        for item_elem in item_elems:
            obj_id = item_elem.get('objectid')
            item_name = resources[obj_id]['name'] if obj_id in resources else f'item_{obj_id}'
            
            transform_str = item_elem.get('transform', '')
            transform = self._parse_transform(transform_str)
            
            if obj_id in resources and resources[obj_id]['type'] == 'mesh':
                self._create_mesh_node(scene, obj_id, item_name, transform, vertices_map, triangles_map, object_materials, triangle_materials)

    def _create_mesh_node(self, scene, obj_id, name, transform, vertices_map, triangles_map, object_materials, triangle_materials):
        from aspose.threed import Node
        from aspose.threed.entities import Mesh
        from aspose.threed.utilities import Vector4
        from aspose.threed.shading import LambertMaterial
        from aspose.threed.utilities import Vector3
        
        if obj_id not in vertices_map or obj_id not in triangles_map:
            return
        
        vertices = vertices_map[obj_id]
        triangles = triangles_map[obj_id]
        
        mesh = Mesh(name)
        
        for v in vertices:
            mesh._control_points.append(v)
        
        for tri in triangles:
            if len(tri) == 3:
                mesh.create_polygon(tri[0], tri[1], tri[2])
            elif len(tri) == 4:
                mesh.create_polygon(tri[0], tri[1], tri[2], tri[3])
        
        node = Node(name)
        node.entity = mesh
        node.parent_node = scene.root_node
        
        if transform is not None:
            node.transform.transform_matrix = transform
        
        if obj_id in object_materials:
            self._apply_object_material(node, object_materials[obj_id])
        else:
            tri_material_ids = set()
            for tri in triangles:
                if len(tri) > 3 and tri[3] is not None:
                    tri_material_ids.add(tri[3])
            
            if len(tri_material_ids) == 1:
                single_material_id = tri_material_ids.pop()
                self._apply_object_material(node, single_material_id)
        
        self._apply_triangle_materials(mesh, vertices, triangles, triangle_materials)
    
    def _apply_object_material(self, node, material_id):
        from aspose.threed.shading import LambertMaterial
        from aspose.threed.utilities import Vector3
        
        material = LambertMaterial(f'material_{material_id}')
        hex_color = self._material_map.get(material_id)
        color = self._parse_color(hex_color)
        if color is not None:
            material.diffuse_color = color
        node.material = material
    
    def _apply_triangle_materials(self, mesh, vertices, triangles, triangle_materials):
        from aspose.threed.entities import VertexElementVertexColor
        from aspose.threed.utilities.FVector4 import FVector4
        from aspose.threed.entities.MappingMode import MappingMode
        from aspose.threed.entities.ReferenceMode import ReferenceMode
        
        triangle_material_ids = set()
        for tri in triangles:
            if len(tri) > 3:
                tri_mat_id = tri[3]
                if tri_mat_id is not None:
                    triangle_material_ids.add(tri_mat_id)
        
        if len(triangle_material_ids) <= 1:
            return
        
        triangle_colors = {}
        for mat_id in triangle_material_ids:
            hex_color = self._material_map.get(mat_id)
            color = self._parse_color(hex_color)
            if color is not None:
                triangle_colors[mat_id] = color
        
        vertex_color_element = VertexElementVertexColor()
        from aspose.threed.entities.MappingMode import MappingMode
        from aspose.threed.entities.ReferenceMode import ReferenceMode
        vertex_color_element.mapping_mode = MappingMode.POLYGON
        vertex_color_element.reference_mode = ReferenceMode.INDEX_TO_DIRECT
        
        vertex_colors = []
        for tri in triangles:
            if len(tri) > 3:
                tri_mat_id = tri[3]
                if tri_mat_id is not None and tri_mat_id in triangle_colors:
                    color = triangle_colors[tri_mat_id]
                    vertex_colors.append(FVector4(color.x, color.y, color.z, 1.0))
                else:
                    vertex_colors.append(FVector4(1.0, 1.0, 1.0, 1.0))
            else:
                vertex_colors.append(FVector4(1.0, 1.0, 1.0, 1.0))
        
        vertex_color_element.set_data(vertex_colors)
        mesh._vertex_elements.append(vertex_color_element)
    
    def _parse_color(self, material_id):
        from aspose.threed.utilities import Vector3
        
        hex_color = material_id
        if hex_color is None or not hex_color.startswith('#'):
            return None
        
        hex_color = hex_color.lstrip('#')
        
        if len(hex_color) == 6:
            r = int(hex_color[0:2], 16) / 255.0
            g = int(hex_color[2:4], 16) / 255.0
            b = int(hex_color[4:6], 16) / 255.0
            return Vector3(r, g, b)
        elif len(hex_color) == 8:
            r = int(hex_color[0:2], 16) / 255.0
            g = int(hex_color[2:4], 16) / 255.0
            b = int(hex_color[4:6], 16) / 255.0
            a = int(hex_color[6:8], 16) / 255.0
            return Vector3(r, g, b)
        
        return None
