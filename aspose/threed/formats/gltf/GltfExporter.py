from typing import TYPE_CHECKING
import json
import struct
import io
import base64

from ..Exporter import Exporter
from ..SaveOptions import SaveOptions

if TYPE_CHECKING:
    from aspose.threed import Scene
    from .GltfSaveOptions import GltfSaveOptions


class GltfExporter(Exporter):
    def __init__(self):
        super().__init__()

    def supports_format(self, file_format) -> bool:
        from .GltfFormat import GltfFormat
        return isinstance(file_format, GltfFormat)

    def export(self, scene: 'Scene', stream, options: 'SaveOptions'):
        from .GltfSaveOptions import GltfSaveOptions

        if not isinstance(options, GltfSaveOptions):
            options = GltfSaveOptions()

        is_binary = options.binary_mode or self._is_stream_binary(stream)

        gltf_json, binary_buffer_data = self._build_gltf_data(scene, options)

        if is_binary:
            self._write_binary_gltf(stream, gltf_json, binary_buffer_data)
        else:
            self._write_ascii_gltf(stream, gltf_json, binary_buffer_data)

    def _is_stream_binary(self, stream):
        if hasattr(stream, 'name'):
            name = stream.name
            if name and name.endswith('.glb'):
                return True
        return False

    def _build_gltf_data(self, scene: 'Scene', options: 'GltfSaveOptions'):
        from aspose.threed.entities import Mesh

        all_meshes = []
        all_nodes = []

        def visit_node(node):
            if node not in all_nodes:
                all_nodes.append(node)
                if node.entity and isinstance(node.entity, Mesh):
                    if node.entity not in all_meshes:
                        all_meshes.append(node.entity)
                for child in node.child_nodes:
                    visit_node(child)

        for child in scene.root_node.child_nodes:
            visit_node(child)

        buffers = []
        buffer_views = []
        accessors = []
        meshes = []
        nodes = []

        binary_buffer_data = bytearray()

        mesh_index_map = {}
        node_index_map = {}

        for i, node in enumerate(all_nodes):
            node_index_map[node] = i

        for i, mesh in enumerate(all_meshes):
            mesh_data = self._build_mesh_data(mesh, options, binary_buffer_data, buffer_views, accessors, buffers, i)
            meshes.append(mesh_data)
            mesh_index_map[mesh] = i

        for node in all_nodes:
            node_data = {}
            if node.name:
                node_data['name'] = node.name

            if node.entity and isinstance(node.entity, Mesh):
                if node.entity in mesh_index_map:
                    node_data['mesh'] = mesh_index_map[node.entity]

            translation = node.transform.translation
            if translation.x != 0 or translation.y != 0 or translation.z != 0:
                node_data['translation'] = [translation.x, translation.y, translation.z]

            nodes.append(node_data)

        child_indices = []
        for node in all_nodes:
            if node.parent_node and node.parent_node in node_index_map:
                parent_idx = node_index_map[node.parent_node]
                node_idx = node_index_map[node]
                if 'children' not in nodes[parent_idx]:
                    nodes[parent_idx]['children'] = []
                nodes[parent_idx]['children'].append(node_idx)
            elif node.parent_node == scene.root_node:
                child_indices.append(node_index_map[node])

        scene_data = {
            'nodes': child_indices
        }

        gltf_json = {
            'asset': {
                'version': '2.0',
                'generator': 'Aspose.3D'
            },
            'scene': 0,
            'scenes': [scene_data],
            'nodes': nodes,
            'meshes': meshes,
            'buffers': buffers,
            'bufferViews': buffer_views,
            'accessors': accessors
        }

        return gltf_json, binary_buffer_data

    def _build_mesh_data(self, mesh, options: 'GltfSaveOptions', binary_buffer_data, buffer_views, accessors, buffers, mesh_index):
        from aspose.threed.entities import VertexElementNormal, VertexElementUV, VertexElementVertexColor

        primitive_data = {'attributes': {}, 'mode': 4}

        positions = []
        for cp in mesh._control_points:
            positions.extend([cp.x, cp.y, cp.z])

        position_bytes = self._encode_float_array(positions)
        position_buffer_offset = len(binary_buffer_data)
        binary_buffer_data.extend(position_bytes)

        position_buffer_view_idx = len(buffer_views)
        buffer_views.append({
            'buffer': 0,
            'byteOffset': position_buffer_offset,
            'byteLength': len(position_bytes)
        })

        position_accessor_idx = len(accessors)
        accessors.append({
            'bufferView': position_buffer_view_idx,
            'componentType': 5126,
            'count': len(positions) // 3,
            'type': 'VEC3'
        })

        primitive_data['attributes']['POSITION'] = position_accessor_idx

        normal_element = None
        for element in mesh._vertex_elements:
            if isinstance(element, VertexElementNormal):
                normal_element = element
                break

        if normal_element and len(normal_element._data) > 0:
            normals = []
            for fv in normal_element._data:
                normals.extend([fv.x, fv.y, fv.z])

            normal_bytes = self._encode_float_array(normals)
            normal_buffer_offset = len(binary_buffer_data)
            binary_buffer_data.extend(normal_bytes)

            normal_buffer_view_idx = len(buffer_views)
            buffer_views.append({
                'buffer': 0,
                'byteOffset': normal_buffer_offset,
                'byteLength': len(normal_bytes)
            })

            normal_accessor_idx = len(accessors)
            accessors.append({
                'bufferView': normal_buffer_view_idx,
                'componentType': 5126,
                'count': len(normals) // 3,
                'type': 'VEC3'
            })

            primitive_data['attributes']['NORMAL'] = normal_accessor_idx

        uv_element = None
        for element in mesh._vertex_elements:
            if isinstance(element, VertexElementUV):
                uv_element = element
                break

        if uv_element and len(uv_element._data) > 0:
            texcoords = []
            for fv in uv_element._data:
                if hasattr(options, 'flip_tex_coord_v') and not options.flip_tex_coord_v:
                    texcoords.extend([fv.x, -fv.y])
                else:
                    texcoords.extend([fv.x, fv.y])

            texcoord_bytes = self._encode_float_array(texcoords)
            texcoord_buffer_offset = len(binary_buffer_data)
            binary_buffer_data.extend(texcoord_bytes)

            texcoord_buffer_view_idx = len(buffer_views)
            buffer_views.append({
                'buffer': 0,
                'byteOffset': texcoord_buffer_offset,
                'byteLength': len(texcoord_bytes)
            })

            texcoord_accessor_idx = len(accessors)
            accessors.append({
                'bufferView': texcoord_buffer_view_idx,
                'componentType': 5126,
                'count': len(texcoords) // 2,
                'type': 'VEC2'
            })

            primitive_data['attributes']['TEXCOORD_0'] = texcoord_accessor_idx

        color_element = None
        for element in mesh._vertex_elements:
            if isinstance(element, VertexElementVertexColor):
                color_element = element
                break

        if color_element and len(color_element._data) > 0:
            colors = []
            for fv in color_element._data:
                colors.extend([fv.x, fv.y, fv.z, fv.w])

            color_bytes = self._encode_float_array(colors)
            color_buffer_offset = len(binary_buffer_data)
            binary_buffer_data.extend(color_bytes)

            color_buffer_view_idx = len(buffer_views)
            buffer_views.append({
                'buffer': 0,
                'byteOffset': color_buffer_offset,
                'byteLength': len(color_bytes)
            })

            color_accessor_idx = len(accessors)
            accessors.append({
                'bufferView': color_buffer_view_idx,
                'componentType': 5126,
                'count': len(colors) // 4,
                'type': 'VEC4'
            })

            primitive_data['attributes']['COLOR_0'] = color_accessor_idx

        indices = []
        for i in range(mesh.polygon_count):
            size = mesh.get_polygon_size(i)
            offset = 0
            for j in range(i):
                offset += mesh.get_polygon_size(j)
            for j in range(size):
                indices.append(mesh._polygons[offset + j])

        if indices:
            indices_bytes = self._encode_uint16_array(indices)
            indices_buffer_offset = len(binary_buffer_data)
            binary_buffer_data.extend(indices_bytes)

            indices_buffer_view_idx = len(buffer_views)
            buffer_views.append({
                'buffer': 0,
                'byteOffset': indices_buffer_offset,
                'byteLength': len(indices_bytes)
            })

            indices_accessor_idx = len(accessors)
            accessors.append({
                'bufferView': indices_buffer_view_idx,
                'componentType': 5123,
                'count': len(indices),
                'type': 'SCALAR'
            })

            primitive_data['indices'] = indices_accessor_idx

        mesh_name = mesh.name if mesh.name else f'mesh_{mesh_index}'
        mesh_data = {
            'name': mesh_name,
            'primitives': [primitive_data]
        }

        return mesh_data

    def _encode_float_array(self, values):
        data = bytearray()
        for v in values:
            data.extend(struct.pack('<f', v))
        return data

    def _encode_uint16_array(self, values):
        data = bytearray()
        for v in values:
            data.extend(struct.pack('<H', v))
        return data

    def _write_ascii_gltf(self, stream, gltf_json, binary_buffer_data):
        if binary_buffer_data:
            uri = f"data:application/octet-stream;base64,{base64.b64encode(binary_buffer_data).decode('utf-8')}"
            gltf_json['buffers'] = [{
                'uri': uri,
                'byteLength': len(binary_buffer_data)
            }]
        else:
            gltf_json['buffers'] = []

        json_str = json.dumps(gltf_json, indent=2)

        if hasattr(stream, 'write'):
            try:
                stream.write(json_str)
            except TypeError:
                stream.write(json_str.encode('utf-8'))

    def _write_binary_gltf(self, stream, gltf_json, binary_buffer_data):
        json_str = json.dumps(gltf_json, separators=(',', ':'))
        json_bytes = json_str.encode('utf-8')

        if binary_buffer_data:
            gltf_json['buffers'] = [{'byteLength': len(binary_buffer_data)}]

        json_bytes = json_str.encode('utf-8')

        json_chunk_length = len(json_bytes)
        json_chunk_padding = (4 - json_chunk_length % 4) % 4

        binary_chunk_length = len(binary_buffer_data)
        binary_chunk_padding = (4 - binary_chunk_length % 4) % 4

        total_length = 12 + 8 + json_chunk_length + json_chunk_padding
        if binary_buffer_data:
            total_length += 8 + binary_chunk_length + binary_chunk_padding

        magic = b'glTF'
        version = 2

        stream.write(struct.pack('<4sII', magic, version, total_length))

        stream.write(struct.pack('<II', json_chunk_length, 0x4E4F534A))
        stream.write(json_bytes)
        stream.write(b'\x00' * json_chunk_padding)

        if binary_buffer_data:
            stream.write(struct.pack('<II', binary_chunk_length, 0x004E4942))
            stream.write(binary_buffer_data)
            stream.write(b'\x00' * binary_chunk_padding)
