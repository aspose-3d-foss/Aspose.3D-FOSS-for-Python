from typing import TYPE_CHECKING, List, Dict
import xml.etree.ElementTree as ET
import io

from ..Importer import Importer

if TYPE_CHECKING:
    from aspose.threed import Scene
    from .ColladaLoadOptions import ColladaLoadOptions


class ColladaImporter(Importer):
    def __init__(self):
        super().__init__()

    def supports_format(self, file_format) -> bool:
        from .ColladaFormat import ColladaFormat
        return isinstance(file_format, ColladaFormat)

    def import_scene(self, scene: 'Scene', stream, options):
        from .ColladaLoadOptions import ColladaLoadOptions
        from aspose.threed import Node
        from aspose.threed.entities import Mesh
        from aspose.threed.utilities import Vector4, Vector2, Matrix4, Quaternion

        if not isinstance(options, ColladaLoadOptions):
            options = ColladaLoadOptions()

        content = ""
        if hasattr(stream, 'read'):
            if hasattr(stream, 'seek'):
                stream.seek(0)
            content = stream.read()
            if isinstance(content, bytes):
                content = content.decode('utf-8', errors='ignore')
        else:
            raise TypeError("Stream must support read() method")

        scale = options.scale
        flip_coords = options.flip_coordinate_system

        root = ET.fromstring(content)
        ns = {'collada': 'http://www.collada.org/2005/11/COLLADASchema'}

        material_map = {}
        effect_map = {}

        if options.enable_materials:
            for library_effects in root.findall('.//collada:library_effects', ns):
                for effect in library_effects.findall('collada:effect', ns):
                    effect_id = effect.get('id', '')
                    effect_data = self._parse_effect(effect, ns)
                    effect_map[effect_id] = effect_data

            for library_materials in root.findall('.//collada:library_materials', ns):
                for material in library_materials.findall('collada:material', ns):
                    mat_id = material.get('id', '')
                    mat_name = material.get('name', '')
                    instance_effect = material.find('collada:instance_effect', ns)
                    if instance_effect is not None:
                        effect_url = instance_effect.get('url', '').replace('#', '')
                        material_map[mat_id] = {
                            'name': mat_name,
                            'effect': effect_url
                        }

        mesh_map = {}

        for library_geometries in root.findall('.//collada:library_geometries', ns):
            for geometry in library_geometries.findall('collada:geometry', ns):
                geom_id = geometry.get('id', '')

                for mesh in geometry.findall('collada:mesh', ns):
                    mesh_data = {'positions': [], 'normals': [], 'uvs': [], 'vertices': {}}

                    for source in mesh.findall('collada:source', ns):
                        source_id = source.get('id', '')

                        float_array = source.find('collada:float_array', ns)
                        if float_array is not None:
                            values_str = float_array.text.strip() if float_array.text else ''
                            values = [float(x) for x in values_str.split() if x]

                            if 'position' in source_id:
                                mesh_data['positions'] = values
                            elif 'normal' in source_id:
                                mesh_data['normals'] = values
                            elif 'texcoord' in source_id:
                                mesh_data['uvs'] = values

                    for vertices_elem in mesh.findall('collada:vertices', ns):
                        vert_id = vertices_elem.get('id', '')
                        for input_elem in vertices_elem.findall('collada:input', ns):
                            if input_elem.get('semantic') == 'POSITION':
                                mesh_data['vertices'][vert_id] = input_elem.get('source', '').replace('#', '')

                    for triangles in mesh.findall('collada:triangles', ns):
                        mesh_data['triangles'] = mesh_data.get('triangles', [])
                        mesh_data['triangles'].append(triangles)
                    
                    for polylist in mesh.findall('collada:polylist', ns):
                        mesh_data['polylists'] = mesh_data.get('polylists', [])
                        mesh_data['polylists'].append(polylist)

                    mesh_map[geom_id] = mesh_data

        for library_visual_scenes in root.findall('.//collada:library_visual_scenes', ns):
            for visual_scene in library_visual_scenes.findall('collada:visual_scene', ns):
                for node_elem in visual_scene.findall('collada:node', ns):
                    self._process_node(node_elem, scene.root_node, mesh_map, ns, scale, flip_coords, options, scene, material_map, effect_map)

    def _process_node(self, node_elem, parent_node, mesh_map, ns, scale, flip_coords, options, scene, material_map, effect_map):
        from aspose.threed import Node
        from aspose.threed.entities import Mesh
        from aspose.threed.utilities import Vector4, Vector3, Matrix4, Quaternion

        node_name = node_elem.get('name', 'node')
        node = Node(node_name)
        node.parent_node = parent_node

        translation = Vector3(0, 0, 0)
        rotation = Quaternion(1, 0, 0, 0)
        scale_factor = Vector3(1, 1, 1)

        for translate_elem in node_elem.findall('collada:translate', ns):
            if translate_elem.text:
                values = [float(x) for x in translate_elem.text.split() if x]
                if len(values) >= 3:
                    x, y, z = values[0], values[1], values[2]
                    if flip_coords:
                        y, z = z, y
                    translation = Vector3(x * scale, y * scale, z * scale)

        for rotate_elem in node_elem.findall('collada:rotate', ns):
            if rotate_elem.text:
                values = [float(x) for x in rotate_elem.text.split() if x]
                if len(values) >= 4:
                    rx, ry, rz, angle_deg = values[0], values[1], values[2], values[3]
                    angle_rad = angle_deg * 3.141592653589793 / 180.0
                    axis = Vector4(rx, ry, rz, 0)
                    if flip_coords:
                        axis.y, axis.z = axis.z, axis.y
                    rotation = Quaternion.from_angle_axis(angle_rad, axis)

        for scale_elem in node_elem.findall('collada:scale', ns):
            if scale_elem.text:
                values = [float(x) for x in scale_elem.text.split() if x]
                if len(values) >= 3:
                    scale_factor = Vector3(values[0], values[1], values[2])

        node.transform.translation = translation
        node.transform.rotation = rotation
        node.transform.scaling = scale_factor

        for instance_geometry in node_elem.findall('collada:instance_geometry', ns):
            geometry_url = instance_geometry.get('url', '').replace('#', '')
            if geometry_url in mesh_map:
                mesh_data = mesh_map[geometry_url]

                if mesh_data['positions']:
                    mesh = Mesh(node_name)
                    node.entity = mesh

                    positions = mesh_data['positions']
                    normals = mesh_data['normals']

                    vertex_map = {}

                    for i in range(0, len(positions), 3):
                        if i + 2 < len(positions):
                            x = positions[i] * scale
                            y = positions[i + 1] * scale
                            z = positions[i + 2] * scale

                            if flip_coords:
                                y, z = z, y

                            vertex_map[i // 3] = len(mesh._control_points)
                            mesh._control_points.append(Vector4(x, y, z, 1))

                    if 'triangles' in mesh_data:
                        for triangles_elem in mesh_data['triangles']:
                            self._process_triangles(triangles_elem, mesh, mesh_map, geometry_url, vertex_map, normals, options, flip_coords)

                    if 'polylists' in mesh_data:
                        for polylist_elem in mesh_data['polylists']:
                            self._process_polylist(polylist_elem, mesh, mesh_map, geometry_url, vertex_map, normals, options, flip_coords)

                    if options.enable_materials:
                        bind_material = instance_geometry.find('collada:bind_material', ns)
                        if bind_material is not None:
                            technique_common = bind_material.find('collada:technique_common', ns)
                            if technique_common is not None:
                                instance_material = technique_common.find('collada:instance_material', ns)
                                if instance_material is not None:
                                    material_symbol = instance_material.get('symbol', '')
                                    target = instance_material.get('target', '').replace('#', '')

                                    material_info = None
                                    for mat_id, mat_data in material_map.items():
                                        if mat_id == target:
                                            material_info = mat_data
                                            break

                                    if material_info and material_info['effect'] in effect_map:
                                        effect_data = effect_map[material_info['effect']]
                                        self._apply_material_to_node(node, effect_data)

        for child_node in node_elem.findall('collada:node', ns):
            self._process_node(child_node, node, mesh_map, ns, scale, flip_coords, options, scene, material_map, effect_map)

    def _process_triangles(self, triangles_elem, mesh, mesh_map, geometry_url, vertex_map, normals, options, flip_coords):
        from aspose.threed.utilities import Vector4
        ns = {'collada': 'http://www.collada.org/2005/11/COLLADASchema'}

        indices = []
        offset_dict = {}

        for input_elem in triangles_elem.findall('collada:input', ns):
            semantic = input_elem.get('semantic')
            source = input_elem.get('source', '').replace('#', '')
            offset = int(input_elem.get('offset', '0'))
            offset_dict[semantic] = (source, offset)

        p_elem = triangles_elem.find('collada:p', ns)
        if p_elem is not None and p_elem.text:
            values = [int(x) for x in p_elem.text.split() if x]

            max_offset = max(offset_dict.values(), key=lambda x: x[1])[1] if offset_dict else 1
            count = len(values) // (max_offset + 1)

            for i in range(count):
                for semantic, (source, offset) in offset_dict.items():
                    idx = i * (max_offset + 1) + offset
                    if idx < len(values):
                        indices.append(values[idx])

            for i in range(0, len(indices), 3):
                face_indices = []
                for j in range(3):
                    if i + j < len(indices):
                        vertex_idx = indices[i + j]
                        if vertex_idx in vertex_map:
                            face_indices.append(vertex_map[vertex_idx])

                if len(face_indices) >= 3:
                    mesh.create_polygon(face_indices)

    def _process_polylist(self, polylist_elem, mesh, mesh_map, geometry_url, vertex_map, normals, options, flip_coords):
        ns = {'collada': 'http://www.collada.org/2005/11/COLLADASchema'}

        vcount_elem = polylist_elem.find('collada:vcount', ns)
        p_elem = polylist_elem.find('collada:p', ns)

        if vcount_elem is not None and p_elem is not None and vcount_elem.text and p_elem.text:
            vcounts = [int(x) for x in vcount_elem.text.split() if x]
            values = [int(x) for x in p_elem.text.split() if x]

            offset_dict = {}
            for input_elem in polylist_elem.findall('collada:input', ns):
                semantic = input_elem.get('semantic')
                source = input_elem.get('source', '').replace('#', '')
                offset = int(input_elem.get('offset', '0'))
                offset_dict[semantic] = (source, offset)

            max_offset = max(offset_dict.values(), key=lambda x: x[1])[1] if offset_dict else 1
            stride = len(offset_dict)

            value_idx = 0
            for vcount in vcounts:
                if vcount < 3:
                    value_idx += vcount * stride
                    continue

                face_indices = []
                for j in range(vcount):
                    if value_idx < len(values):
                        vertex_idx = values[value_idx]
                        if vertex_idx in vertex_map:
                            face_indices.append(vertex_map[vertex_idx])
                        value_idx += stride

                if len(face_indices) >= 3:
                    mesh.create_polygon(face_indices)

    def _parse_effect(self, effect_elem, ns):
        from aspose.threed.utilities import Vector3

        effect_data = {
            'type': None,
            'emission': None,
            'ambient': None,
            'diffuse': None,
            'specular': None,
            'shininess': 0.0,
            'reflective': None,
            'reflectivity': 0.0,
            'transparent': None,
            'transparency': 0.0
        }

        profile_common = effect_elem.find('collada:profile_COMMON', ns)
        if profile_common is None:
            return effect_data

        technique = profile_common.find('collada:technique', ns)
        if technique is None:
            return effect_data

        phong = technique.find('collada:phong', ns)
        lambert = technique.find('collada:lambert', ns)
        blinn = technique.find('collada:blinn', ns)

        shader = phong if phong is not None else (lambert if lambert is not None else blinn)
        if shader is None:
            return effect_data

        if phong is not None:
            effect_data['type'] = 'phong'
        elif lambert is not None:
            effect_data['type'] = 'lambert'
        else:
            effect_data['type'] = 'blinn'

        emission_elem = shader.find('collada:emission/collada:color', ns)
        if emission_elem is not None and emission_elem.text is not None:
            values = [float(x) for x in emission_elem.text.split() if x]
            if len(values) >= 3:
                effect_data['emission'] = Vector3(values[0], values[1], values[2])

        ambient_elem = shader.find('collada:ambient/collada:color', ns)
        if ambient_elem is not None and ambient_elem.text is not None:
            values = [float(x) for x in ambient_elem.text.split() if x]
            if len(values) >= 3:
                effect_data['ambient'] = Vector3(values[0], values[1], values[2])

        diffuse_elem = shader.find('collada:diffuse/collada:color', ns)
        if diffuse_elem is not None and diffuse_elem.text is not None:
            values = [float(x) for x in diffuse_elem.text.split() if x]
            if len(values) >= 3:
                effect_data['diffuse'] = Vector3(values[0], values[1], values[2])

        if phong is not None:
            specular_elem = phong.find('collada:specular/collada:color', ns)
            if specular_elem is not None and specular_elem.text is not None:
                values = [float(x) for x in specular_elem.text.split() if x]
                if len(values) >= 3:
                    effect_data['specular'] = Vector3(values[0], values[1], values[2])

            shininess_elem = phong.find('collada:shininess/collada:float', ns)
            if shininess_elem is not None and shininess_elem.text is not None:
                effect_data['shininess'] = float(shininess_elem.text)

            reflective_elem = phong.find('collada:reflective/collada:color', ns)
            if reflective_elem is not None and reflective_elem.text is not None:
                values = [float(x) for x in reflective_elem.text.split() if x]
                if len(values) >= 3:
                    effect_data['reflective'] = Vector3(values[0], values[1], values[2])

            reflectivity_elem = phong.find('collada:reflectivity/collada:float', ns)
            if reflectivity_elem is not None and reflectivity_elem.text is not None:
                effect_data['reflectivity'] = float(reflectivity_elem.text)

        transparent_elem = shader.find('collada:transparent/collada:color', ns)
        if transparent_elem is not None and transparent_elem.text is not None:
            values = [float(x) for x in transparent_elem.text.split() if x]
            if len(values) >= 3:
                effect_data['transparent'] = Vector3(values[0], values[1], values[2])

        transparency_elem = shader.find('collada:transparency/collada:float', ns)
        if transparency_elem is not None and transparency_elem.text is not None:
            transparency_collada = float(transparency_elem.text)
            effect_data['transparency'] = 1.0 - transparency_collada

        return effect_data

    def _apply_material_to_node(self, node, effect_data):
        from aspose.threed.shading import LambertMaterial, PhongMaterial

        material = None

        if effect_data['type'] == 'phong':
            material = PhongMaterial()
            if effect_data['specular'] is not None:
                material.specular_color = effect_data['specular']
            material.shininess = effect_data['shininess']
            if effect_data['reflective'] is not None:
                material.reflection_color = effect_data['reflective']
            material.reflection_factor = effect_data['reflectivity']
        elif effect_data['type'] in ['lambert', 'blinn']:
            material = LambertMaterial()
        else:
            material = LambertMaterial()

        if effect_data['emission'] is not None:
            material.emissive_color = effect_data['emission']
        if effect_data['ambient'] is not None:
            material.ambient_color = effect_data['ambient']
        if effect_data['diffuse'] is not None:
            material.diffuse_color = effect_data['diffuse']
        if effect_data['transparent'] is not None:
            material.transparent_color = effect_data['transparent']
        material.transparency = effect_data['transparency']

        node.material = material
