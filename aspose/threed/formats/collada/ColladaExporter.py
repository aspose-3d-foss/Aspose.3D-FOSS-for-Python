from typing import TYPE_CHECKING, Dict, List
import xml.etree.ElementTree as ET
import io

from ..Exporter import Exporter

if TYPE_CHECKING:
    from aspose.threed import Scene
    from .ColladaSaveOptions import ColladaSaveOptions


class ColladaExporter(Exporter):
    def __init__(self):
        super().__init__()
        self._node_counter = 0
        self._geometry_counter = 0
        self._material_counter = 0
        self._effect_counter = 0

    def supports_format(self, file_format) -> bool:
        from .ColladaFormat import ColladaFormat
        return isinstance(file_format, ColladaFormat)

    def export(self, scene: 'Scene', stream, options: 'SaveOptions'):
        from .ColladaSaveOptions import ColladaSaveOptions

        if not isinstance(options, ColladaSaveOptions):
            from .ColladaSaveOptions import ColladaSaveOptions
            options = ColladaSaveOptions()

        content = self._write_collada(scene, options)

        if hasattr(stream, 'write'):
            if isinstance(content, str):
                content_bytes = content.encode('utf-8')
            else:
                content_bytes = content
            stream.write(content_bytes)
        else:
            raise TypeError("Stream must support write() method")

    def _write_collada(self, scene: 'Scene', options: 'ColladaSaveOptions') -> str:
        ns = {'collada': 'http://www.collada.org/2005/11/COLLADASchema'}

        collada = ET.Element('COLLADA', attrib={
            'xmlns': 'http://www.collada.org/2005/11/COLLADASchema',
            'version': '1.4.1'
        })

        asset = self._write_asset()
        collada.append(asset)

        nodes_with_meshes = []
        materials = {}
        self._collect_nodes(scene.root_node, nodes_with_meshes, materials)

        geometries = self._write_geometries(nodes_with_meshes, options)
        if geometries is not None:
            collada.append(geometries)

        if materials:
            materials_elem, effects_elem = self._write_materials_and_effects(materials)
            if materials_elem is not None:
                collada.append(materials_elem)
            if effects_elem is not None:
                collada.append(effects_elem)

        visual_scene = self._write_visual_scene(nodes_with_meshes, materials, scene.root_node, options)
        collada.append(visual_scene)

        scene_elem = self._write_scene_element()
        collada.append(scene_elem)

        self._indent(collada)
        xml_str = ET.tostring(collada, encoding='unicode')

        if options.indented:
            return xml_str
        else:
            return ET.tostring(collada, encoding='unicode', method='xml')

    def _write_asset(self):
        from datetime import datetime
        import time

        asset = ET.Element('asset')

        contributor = ET.SubElement(asset, 'contributor')
        authoring_tool = ET.SubElement(contributor, 'authoring_tool')
        authoring_tool.text = 'Aspose.3D Collada Exporter'

        created = ET.SubElement(asset, 'created')
        created.text = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

        modified = ET.SubElement(asset, 'modified')
        modified.text = created.text

        unit = ET.SubElement(asset, 'unit')
        unit.set('meter', '1.0')
        unit.set('name', 'meter')

        up_axis = ET.SubElement(asset, 'up_axis')
        up_axis.text = 'Y_UP'

        return asset

    def _collect_nodes(self, node, nodes_with_meshes: List, materials: Dict, visited=None):
        if visited is None:
            visited = set()

        if node in visited:
            return

        visited.add(node)

        if node.entity is not None:
            nodes_with_meshes.append(node)

            material = node.material
            if material is not None and id(material) not in materials:
                materials[id(material)] = material

        for child in node.child_nodes:
            self._collect_nodes(child, nodes_with_meshes, materials, visited)

    def _write_geometries(self, nodes: List, options: 'ColladaSaveOptions'):
        if not nodes:
            return None

        library_geometries = ET.Element('library_geometries')

        for node in nodes:
            mesh = node.entity
            if mesh is None:
                continue

            self._geometry_counter += 1
            geom_id = f'geom_{self._geometry_counter}'
            geom_name = node.name or f'Geometry_{self._geometry_counter}'

            geometry = ET.SubElement(library_geometries, 'geometry')
            geometry.set('id', geom_id)
            geometry.set('name', geom_name)

            mesh_elem = ET.SubElement(geometry, 'mesh')

            self._write_positions(mesh_elem, geom_id, mesh, options)
            self._write_normals(mesh_elem, geom_id, mesh)
            self._write_uvs(mesh_elem, geom_id, mesh)
            self._write_vertices(mesh_elem, geom_id)
            self._write_triangles(mesh_elem, geom_id, mesh)

        return library_geometries

    def _write_positions(self, mesh_elem: ET.Element, geom_id: str, mesh, options: 'ColladaSaveOptions'):
        control_points = mesh.control_points
        if not control_points:
            return

        positions_id = f'{geom_id}-positions'
        source = ET.SubElement(mesh_elem, 'source')
        source.set('id', positions_id)

        float_array = ET.SubElement(source, 'float_array')
        float_array.set('id', f'{positions_id}-array')
        float_array.set('count', str(len(control_points) * 3))

        positions = []
        for cp in control_points:
            x = cp.x
            y = cp.y
            z = cp.z

            if hasattr(options, 'flip_coordinate_system') and options.flip_coordinate_system:
                y, z = z, y

            positions.extend([f'{x:.6f}', f'{y:.6f}', f'{z:.6f}'])

        float_array.text = ' '.join(positions)

        technique_common = ET.SubElement(source, 'technique_common')
        accessor = ET.SubElement(technique_common, 'accessor')
        accessor.set('source', f'#{positions_id}-array')
        accessor.set('count', str(len(control_points)))
        accessor.set('stride', '3')

        for param_name in ['X', 'Y', 'Z']:
            param = ET.SubElement(accessor, 'param')
            param.set('name', param_name)
            param.set('type', 'float')

    def _write_normals(self, mesh_elem: ET.Element, geom_id: str, mesh):
        if not hasattr(mesh, 'normals') or not mesh.normals:
            return

        normals = mesh.normals
        if not normals:
            return

        normals_id = f'{geom_id}-normals'
        source = ET.SubElement(mesh_elem, 'source')
        source.set('id', normals_id)

        float_array = ET.SubElement(source, 'float_array')
        float_array.set('id', f'{normals_id}-array')
        float_array.set('count', str(len(normals) * 3))

        normal_values = []
        for normal in normals:
            normal_values.extend([f'{normal.x:.6f}', f'{normal.y:.6f}', f'{normal.z:.6f}'])

        float_array.text = ' '.join(normal_values)

        technique_common = ET.SubElement(source, 'technique_common')
        accessor = ET.SubElement(technique_common, 'accessor')
        accessor.set('source', f'#{normals_id}-array')
        accessor.set('count', str(len(normals)))
        accessor.set('stride', '3')

        for param_name in ['X', 'Y', 'Z']:
            param = ET.SubElement(accessor, 'param')
            param.set('name', param_name)
            param.set('type', 'float')

    def _write_uvs(self, mesh_elem: ET.Element, geom_id: str, mesh):
        if not hasattr(mesh, 'texture_coordinates') or not mesh.texture_coordinates:
            return

        uvs = mesh.texture_coordinates
        if not uvs:
            return

        uvs_id = f'{geom_id}-uvs'
        source = ET.SubElement(mesh_elem, 'source')
        source.set('id', uvs_id)

        float_array = ET.SubElement(source, 'float_array')
        float_array.set('id', f'{uvs_id}-array')
        float_array.set('count', str(len(uvs) * 2))

        uv_values = []
        for uv in uvs:
            uv_values.extend([f'{uv.x:.6f}', f'{uv.y:.6f}'])

        float_array.text = ' '.join(uv_values)

        technique_common = ET.SubElement(source, 'technique_common')
        accessor = ET.SubElement(technique_common, 'accessor')
        accessor.set('source', f'#{uvs_id}-array')
        accessor.set('count', str(len(uvs)))
        accessor.set('stride', '2')

        for param_name in ['U', 'V']:
            param = ET.SubElement(accessor, 'param')
            param.set('name', param_name)
            param.set('type', 'float')

    def _write_vertices(self, mesh_elem: ET.Element, geom_id: str):
        positions_id = f'{geom_id}-positions'
        vertices_id = f'{geom_id}-vertices'

        vertices = ET.SubElement(mesh_elem, 'vertices')
        vertices.set('id', vertices_id)

        input_elem = ET.SubElement(vertices, 'input')
        input_elem.set('semantic', 'POSITION')
        input_elem.set('source', f'#{positions_id}')

    def _write_triangles(self, mesh_elem: ET.Element, geom_id: str, mesh):
        polygons = mesh.polygons
        if not polygons:
            return

        triangles_count = len(polygons)
        triangles = ET.SubElement(mesh_elem, 'triangles')
        triangles.set('count', str(triangles_count))
        triangles.set('material', 'Material')

        positions_id = f'{geom_id}-positions'
        vertices_id = f'{geom_id}-vertices'

        offset = 0

        input_pos = ET.SubElement(triangles, 'input')
        input_pos.set('semantic', 'VERTEX')
        input_pos.set('source', f'#{vertices_id}')
        input_pos.set('offset', str(offset))

        offset += 1

        normals_id = f'{geom_id}-normals'
        if hasattr(mesh, 'normals') and mesh.normals:
            input_normal = ET.SubElement(triangles, 'input')
            input_normal.set('semantic', 'NORMAL')
            input_normal.set('source', f'#{normals_id}')
            input_normal.set('offset', str(offset))
            offset += 1

        uvs_id = f'{geom_id}-uvs'
        if hasattr(mesh, 'texture_coordinates') and mesh.texture_coordinates:
            input_uv = ET.SubElement(triangles, 'input')
            input_uv.set('semantic', 'TEXCOORD')
            input_uv.set('source', f'#{uvs_id}')
            input_uv.set('offset', str(offset))
            offset += 1

        p_values = []
        for face_indices in polygons:
            for idx in face_indices:
                for i in range(offset):
                    p_values.append(str(idx))

        p_elem = ET.SubElement(triangles, 'p')
        p_elem.text = ' '.join(p_values)

    def _write_materials_and_effects(self, materials: Dict):
        library_materials = ET.Element('library_materials')
        library_effects = ET.Element('library_effects')

        for mat_id, material in materials.items():
            self._material_counter += 1
            self._effect_counter += 1

            mat_element_id = f'material_{self._material_counter}'
            effect_element_id = f'effect_{self._effect_counter}'

            material_elem = ET.SubElement(library_materials, 'material')
            material_elem.set('id', mat_element_id)
            material_elem.set('name', material.name or f'Material_{self._material_counter}')

            instance_effect = ET.SubElement(material_elem, 'instance_effect')
            instance_effect.set('url', f'#{effect_element_id}')

            effect = ET.SubElement(library_effects, 'effect')
            effect.set('id', effect_element_id)
            effect.set('name', f'{material.name or f"Material_{self._material_counter}"}-fx')

            profile_common = ET.SubElement(effect, 'profile_COMMON')
            technique = ET.SubElement(profile_common, 'technique')
            technique.set('sid', 'common')

            shader_type = type(material).__name__
            shader_elem = None

            if shader_type == 'PhongMaterial':
                shader_elem = ET.SubElement(technique, 'phong')
            elif shader_type == 'LambertMaterial':
                shader_elem = ET.SubElement(technique, 'lambert')

            if shader_elem is not None:
                self._write_shader_properties(shader_elem, material, shader_type)

        return library_materials, library_effects

    def _write_shader_properties(self, shader_elem: ET.Element, material, shader_type: str):
        if hasattr(material, 'emissive_color') and material.emissive_color is not None:
            emissive = ET.SubElement(shader_elem, 'emission')
            color = ET.SubElement(emissive, 'color')
            color.text = f'{material.emissive_color.x:.6f} {material.emissive_color.y:.6f} {material.emissive_color.z:.6f} 1.0'

        if hasattr(material, 'ambient_color') and material.ambient_color is not None:
            ambient = ET.SubElement(shader_elem, 'ambient')
            color = ET.SubElement(ambient, 'color')
            color.text = f'{material.ambient_color.x:.6f} {material.ambient_color.y:.6f} {material.ambient_color.z:.6f} 1.0'

        if hasattr(material, 'diffuse_color') and material.diffuse_color is not None:
            diffuse = ET.SubElement(shader_elem, 'diffuse')
            color = ET.SubElement(diffuse, 'color')
            color.text = f'{material.diffuse_color.x:.6f} {material.diffuse_color.y:.6f} {material.diffuse_color.z:.6f} 1.0'

        if shader_type == 'PhongMaterial':
            if hasattr(material, 'specular_color') and material.specular_color is not None:
                specular = ET.SubElement(shader_elem, 'specular')
                color = ET.SubElement(specular, 'color')
                color.text = f'{material.specular_color.x:.6f} {material.specular_color.y:.6f} {material.specular_color.z:.6f} 1.0'

            if hasattr(material, 'shininess'):
                shininess = ET.SubElement(shader_elem, 'shininess')
                float_elem = ET.SubElement(shininess, 'float')
                shininess_val = material.shininess if material.shininess > 0 else 0.0
                float_elem.text = f'{shininess_val:.6f}'

            if hasattr(material, 'reflection_color') and material.reflection_color is not None:
                reflective = ET.SubElement(shader_elem, 'reflective')
                color = ET.SubElement(reflective, 'color')
                color.text = f'{material.reflection_color.x:.6f} {material.reflection_color.y:.6f} {material.reflection_color.z:.6f} 1.0'

            if hasattr(material, 'reflection_factor'):
                reflectivity = ET.SubElement(shader_elem, 'reflectivity')
                float_elem = ET.SubElement(reflectivity, 'float')
                float_elem.text = f'{material.reflection_factor:.6f}'

        if hasattr(material, 'transparent_color') and material.transparent_color is not None:
            transparent = ET.SubElement(shader_elem, 'transparent')
            color = ET.SubElement(transparent, 'color')
            color.text = f'{material.transparent_color.x:.6f} {material.transparent_color.y:.6f} {material.transparent_color.z:.6f} 1.0'

        if hasattr(material, 'transparency'):
            transparency = ET.SubElement(shader_elem, 'transparency')
            float_elem = ET.SubElement(transparency, 'float')
            transp_val = 1.0 - material.transparency
            float_elem.text = f'{transp_val:.6f}'

    def _write_visual_scene(self, nodes: List, materials: Dict, root_node, options: 'ColladaSaveOptions'):
        library_visual_scenes = ET.Element('library_visual_scenes')

        visual_scene = ET.SubElement(library_visual_scenes, 'visual_scene')
        visual_scene.set('id', 'VisualSceneNode')
        visual_scene.set('name', 'Scene')

        self._node_counter = 0

        for node in nodes:
            self._write_node(visual_scene, node, materials, root_node, options, 0)

        for child in root_node.child_nodes:
            if child.entity is None:
                self._write_node(visual_scene, child, materials, root_node, options, 0)

        return library_visual_scenes

    def _write_node(self, visual_scene: ET.Element, node, materials: Dict, root_node, options: 'ColladaSaveOptions', depth: int, visited=None):
        if visited is None:
            visited = set()

        if node in visited:
            return

        visited.add(node)

        self._node_counter += 1
        node_name = node.name or f'Node_{self._node_counter}'

        node_elem = ET.SubElement(visual_scene, 'node')
        node_elem.set('id', node_name)
        node_elem.set('name', node_name)

        transform = node.transform
        self._write_transforms(node_elem, transform, options)

        if node.entity is not None:
            self._geometry_counter += 1
            geom_id = f'geom_{self._geometry_counter}'

            instance_geometry = ET.SubElement(node_elem, 'instance_geometry')
            instance_geometry.set('url', f'#{geom_id}')

            material = node.material
            if material is not None and id(material) in materials:
                mat_index = list(materials.keys()).index(id(material)) + 1
                mat_symbol = f'material_{mat_index}'

                bind_material = ET.SubElement(instance_geometry, 'bind_material')
                technique_common = ET.SubElement(bind_material, 'technique_common')

                instance_material = ET.SubElement(technique_common, 'instance_material')
                instance_material.set('symbol', mat_symbol)
                instance_material.set('target', f'#{mat_symbol}')

        for child in node.child_nodes:
            self._write_node(visual_scene, child, materials, root_node, options, depth + 1, visited)

    def _write_transforms(self, node_elem: ET.Element, transform, options: 'ColladaSaveOptions'):
        translation = transform.translation
        if translation is not None:
            tx = translation.x
            ty = translation.y
            tz = translation.z

            if hasattr(options, 'flip_coordinate_system') and options.flip_coordinate_system:
                ty, tz = tz, ty

            translate = ET.SubElement(node_elem, 'translate')
            translate.set('sid', 'translate')
            translate.text = f'{tx:.6f} {ty:.6f} {tz:.6f}'

        rotation_quat = transform.rotation
        if rotation_quat is not None:
            from aspose.threed.utilities import Vector3
            angle = [0.0]
            axis = [Vector3(1, 0, 0)]
            rotation_quat.to_angle_axis(angle, axis)
            angle_deg = angle[0] * 180.0 / 3.141592653589793
            axis_vec = axis[0]

            if hasattr(options, 'flip_coordinate_system') and options.flip_coordinate_system:
                axis_vec = Vector3(axis_vec.x, axis_vec.z, axis_vec.y)

            rotate = ET.SubElement(node_elem, 'rotate')
            rotate.set('sid', 'rotate')
            rotate.text = f'{axis_vec.x:.6f} {axis_vec.y:.6f} {axis_vec.z:.6f} {angle_deg:.6f}'

        scaling = transform.scaling
        if scaling is not None:
            sx = scaling.x
            sy = scaling.y
            sz = scaling.z

            scale = ET.SubElement(node_elem, 'scale')
            scale.set('sid', 'scale')
            scale.text = f'{sx:.6f} {sy:.6f} {sz:.6f}'

    def _write_scene_element(self):
        scene = ET.Element('scene')
        instance_visual_scene = ET.SubElement(scene, 'instance_visual_scene')
        instance_visual_scene.set('url', '#VisualSceneNode')
        return scene

    def _indent(self, elem, level=0):
        indent = '\n' + '  ' * level
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = indent + '  '
            if not elem.tail or not elem.tail.strip():
                elem.tail = indent
            for child in elem:
                self._indent(child, level + 1)
            if not child.tail or not child.tail.strip():
                child.tail = indent
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = indent
