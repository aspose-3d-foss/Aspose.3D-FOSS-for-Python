from typing import TYPE_CHECKING
import json
import struct
import io

from ..Importer import Importer

if TYPE_CHECKING:
    from aspose.threed import Scene
    from .GltfLoadOptions import GltfLoadOptions


class GltfImporter(Importer):
    def __init__(self):
        super().__init__()

    def supports_format(self, file_format) -> bool:
        from .GltfFormat import GltfFormat
        return isinstance(file_format, GltfFormat)

    def import_scene(self, scene: 'Scene', stream, options: 'GltfLoadOptions'):
        from .GltfLoadOptions import GltfLoadOptions
        from aspose.threed import Node
        from aspose.threed.entities import Mesh
        from aspose.threed.utilities import Vector4

        if not isinstance(options, GltfLoadOptions):
            options = GltfLoadOptions()

        content = self._read_stream(stream)
        if len(content) == 0:
            return

        is_binary = self._is_binary_gltf(content)

        if is_binary:
            gltf_json, binary_data = self._parse_binary_gltf(content)
        else:
            gltf_json = json.loads(content.decode('utf-8'))
            binary_data = b''

        self._build_scene(scene, gltf_json, binary_data, options)

    def _read_stream(self, stream) -> bytes:
        if hasattr(stream, 'read'):
            if hasattr(stream, 'seek'):
                stream.seek(0)
            data = stream.read()
            if isinstance(data, str):
                return data.encode('utf-8', errors='ignore')
            return data
        raise TypeError("Stream must support read() method")

    def _is_binary_gltf(self, content: bytes) -> bool:
        if len(content) < 12:
            return False
        magic = content[:4]
        return magic == b'glTF'

    def _parse_binary_gltf(self, content: bytes):
        magic, version, length = struct.unpack('<4sII', content[:12])

        if magic != b'glTF':
            raise ValueError("Invalid glTF binary file magic")

        if version != 2:
            raise ValueError(f"Unsupported glTF version: {version}")

        chunk_offset = 12
        json_chunk = None
        binary_chunk = None

        while chunk_offset < length:
            if chunk_offset + 8 > len(content):
                break

            chunk_length, chunk_type = struct.unpack('<II', content[chunk_offset:chunk_offset + 8])

            chunk_data = content[chunk_offset + 8:chunk_offset + 8 + chunk_length]

            if chunk_type == 0x4E4F534A:
                json_chunk = chunk_data
            elif chunk_type == 0x004E4942:
                binary_chunk = chunk_data

            chunk_offset += 8 + chunk_length

        if json_chunk is None:
            raise ValueError("Missing JSON chunk in glTF binary file")

        gltf_json = json.loads(json_chunk.decode('utf-8'))
        return gltf_json, binary_chunk if binary_chunk else b''

    def _build_scene(self, scene, gltf_json, binary_data, options):
        from aspose.threed import Node
        from aspose.threed.entities import Mesh
        from aspose.threed.utilities import Vector4

        buffers = self._load_buffers(gltf_json, binary_data)
        buffer_views = gltf_json.get('bufferViews', [])
        accessors = gltf_json.get('accessors', [])
        meshes = gltf_json.get('meshes', [])
        nodes = gltf_json.get('nodes', [])

        mesh_objects = {}

        for mesh_idx, mesh_data in enumerate(meshes):
            mesh_name = mesh_data.get('name', f'mesh_{mesh_idx}')
            mesh = Mesh(mesh_name)

            for primitive in mesh_data.get('primitives', []):
                self._build_primitive(mesh, primitive, accessors, buffer_views, buffers, options)

            mesh_objects[mesh_idx] = mesh

        node_objects = {}

        for node_idx, node_data in enumerate(nodes):
            node_name = node_data.get('name', f'node_{node_idx}')
            node = Node(node_name)

            if 'mesh' in node_data:
                mesh_idx = node_data['mesh']
                if mesh_idx in mesh_objects:
                    node.entity = mesh_objects[mesh_idx]

            if 'translation' in node_data:
                translation = node_data['translation']
                node.transform.translation = Vector4(translation[0], translation[1], translation[2], 1)

            if 'rotation' in node_data:
                rotation = node_data['rotation']
                quaternion = node.transform.euler
                quaternion.x = rotation[0]
                quaternion.y = rotation[1]
                quaternion.z = rotation[2]
                quaternion.w = rotation[3]

            if 'scale' in node_data:
                scale = node_data['scale']
                node.transform.scale = Vector4(scale[0], scale[1], scale[2], 1)

            node_objects[node_idx] = node

        for node_idx, node_data in enumerate(nodes):
            if 'children' in node_data:
                parent_node = node_objects[node_idx]
                for child_idx in node_data['children']:
                    if child_idx in node_objects:
                        child_node = node_objects[child_idx]
                        child_node.parent_node = parent_node

        scene_index = gltf_json.get('scene', 0)
        scenes = gltf_json.get('scenes', [])

        if scene_index < len(scenes):
            scene_root = scenes[scene_index]
            for node_idx in scene_root.get('nodes', []):
                if node_idx in node_objects:
                    node_objects[node_idx].parent_node = scene.root_node

    def _build_primitive(self, mesh, primitive, accessors, buffer_views, buffers, options):
        from aspose.threed.utilities import Vector4

        attributes = primitive.get('attributes', {})
        indices_accessor_idx = primitive.get('indices')
        mode = primitive.get('mode', 4)

        if mode != 4:
            return

        position_accessor_idx = attributes.get('POSITION')
        normal_accessor_idx = attributes.get('NORMAL')
        tangent_accessor_idx = attributes.get('TANGENT')
        texcoord_accessor_idx = attributes.get('TEXCOORD_0')
        color_accessor_idx = attributes.get('COLOR_0')

        if position_accessor_idx is None:
            return

        position_accessor = accessors[position_accessor_idx]
        positions = self._read_accessor_data(position_accessor, buffer_views, buffers, 'VEC3')

        vertex_count = len(positions)
        base_vertex_index = len(mesh._control_points)

        for position in positions:
            mesh._control_points.append(Vector4(position[0], position[1], position[2], 1))

        if normal_accessor_idx is not None:
            self._add_normals_to_mesh(mesh, accessors[normal_accessor_idx], buffer_views, buffers, vertex_count, base_vertex_index)

        if tangent_accessor_idx is not None:
            self._add_tangents_to_mesh(mesh, accessors[tangent_accessor_idx], buffer_views, buffers, vertex_count, base_vertex_index)

        if texcoord_accessor_idx is not None:
            self._add_uvs_to_mesh(mesh, accessors[texcoord_accessor_idx], buffer_views, buffers, vertex_count, base_vertex_index, options)

        if color_accessor_idx is not None:
            self._add_colors_to_mesh(mesh, accessors[color_accessor_idx], buffer_views, buffers, vertex_count, base_vertex_index)

        if indices_accessor_idx is not None:
            indices_accessor = accessors[indices_accessor_idx]
            indices = self._read_accessor_data(indices_accessor, buffer_views, buffers, 'SCALAR')

            if indices_accessor.get('componentType') == 5123:
                for i in range(0, len(indices), 3):
                    mesh.create_polygon(base_vertex_index + indices[i],
                                       base_vertex_index + indices[i + 1],
                                       base_vertex_index + indices[i + 2])
            else:
                for i in range(0, len(indices), 3):
                    mesh.create_polygon(base_vertex_index + int(indices[i]),
                                       base_vertex_index + int(indices[i + 1]),
                                       base_vertex_index + int(indices[i + 2]))
        else:
            for i in range(0, vertex_count, 3):
                mesh.create_polygon(base_vertex_index + i,
                                   base_vertex_index + i + 1,
                                   base_vertex_index + i + 2)

    def _load_buffers(self, gltf_json, binary_data):
        buffers = gltf_json.get('buffers', [])
        loaded_buffers = []

        for buffer in buffers:
            uri = buffer.get('uri')
            byte_length = buffer.get('byteLength', 0)

            if uri is None:
                loaded_buffers.append(binary_data)
            elif uri.startswith('data:'):
                loaded_buffers.append(self._decode_data_uri(uri))
            else:
                loaded_buffers.append(b'')

        return loaded_buffers

    def _decode_data_uri(self, uri):
        import base64
        header, data = uri.split(',', 1)
        return base64.b64decode(data)

    def _read_accessor_data(self, accessor, buffer_views, buffers, expected_type):
        buffer_view_idx = accessor.get('bufferView')
        byte_offset = accessor.get('byteOffset', 0)
        count = accessor.get('count', 0)
        accessor_type = accessor.get('type')

        if buffer_view_idx is None or buffer_view_idx >= len(buffer_views):
            return []

        buffer_view = buffer_views[buffer_view_idx]
        buffer_idx = buffer_view.get('buffer', 0)
        view_byte_offset = buffer_view.get('byteOffset', 0)
        view_byte_length = buffer_view.get('byteLength', 0)

        if buffer_idx >= len(buffers):
            return []

        buffer = buffers[buffer_idx]
        data_start = view_byte_offset + byte_offset
        data_end = data_start + view_byte_length
        data = buffer[data_start:data_end]

        return self._decode_buffer(data, accessor.get('componentType'), accessor_type, count)

    def _decode_buffer(self, data, component_type, accessor_type, count):
        components_per_value = 1
        if accessor_type == 'VEC2':
            components_per_value = 2
        elif accessor_type == 'VEC3':
            components_per_value = 3
        elif accessor_type == 'VEC4':
            components_per_value = 4

        total_components = count * components_per_value

        if component_type == 5120:
            fmt = '<{}b'.format(total_components)
            values = struct.unpack(fmt, data[:total_components])
        elif component_type == 5121:
            fmt = '<{}B'.format(total_components)
            values = struct.unpack(fmt, data[:total_components])
        elif component_type == 5122:
            fmt = '<{}h'.format(total_components)
            values = struct.unpack(fmt, data[:total_components * 2])
        elif component_type == 5123:
            fmt = '<{}H'.format(total_components)
            values = struct.unpack(fmt, data[:total_components * 2])
        elif component_type == 5125:
            fmt = '<{}i'.format(total_components)
            values = struct.unpack(fmt, data[:total_components * 4])
        elif component_type == 5126:
            fmt = '<{}f'.format(total_components)
            values = struct.unpack(fmt, data[:total_components * 4])
        else:
            return []

        if accessor_type == 'SCALAR':
            return list(values)
        elif accessor_type == 'VEC2':
            return [(values[i], values[i + 1]) for i in range(0, len(values), 2)]
        elif accessor_type == 'VEC3':
            return [(values[i], values[i + 1], values[i + 2]) for i in range(0, len(values), 3)]
        elif accessor_type == 'VEC4':
            return [(values[i], values[i + 1], values[i + 2], values[i + 3]) for i in range(0, len(values), 4)]
        else:
            return []

    def _add_normals_to_mesh(self, mesh, accessor, buffer_views, buffers, vertex_count, base_vertex_index):
        from aspose.threed.entities import VertexElementNormal
        from aspose.threed.utilities.FVector4 import FVector4

        normals = self._read_accessor_data(accessor, buffer_views, buffers, 'VEC3')

        if len(normals) < vertex_count:
            return

        normal_element = VertexElementNormal()
        for i in range(vertex_count):
            normal = normals[i]
            normal_element._data.append(FVector4(normal[0], normal[1], normal[2], 0))

        mesh._vertex_elements.append(normal_element)

    def _add_tangents_to_mesh(self, mesh, accessor, buffer_views, buffers, vertex_count, base_vertex_index):
        from aspose.threed.entities import VertexElementTangent
        from aspose.threed.utilities.FVector4 import FVector4

        tangents = self._read_accessor_data(accessor, buffer_views, buffers, 'VEC3')

        if len(tangents) < vertex_count:
            return

        tangent_element = VertexElementTangent()
        for i in range(vertex_count):
            tangent = tangents[i]
            tangent_element._data.append(FVector4(tangent[0], tangent[1], tangent[2], 0))

        mesh._vertex_elements.append(tangent_element)

    def _add_uvs_to_mesh(self, mesh, accessor, buffer_views, buffers, vertex_count, base_vertex_index, options):
        from aspose.threed.entities import VertexElementUV
        from aspose.threed.utilities.FVector4 import FVector4

        uvs = self._read_accessor_data(accessor, buffer_views, buffers, 'VEC2')

        if len(uvs) < vertex_count:
            return

        uv_element = VertexElementUV()
        for i in range(vertex_count):
            uv = uvs[i]
            v = uv[1] if options.flip_tex_coord_v else -uv[1]
            uv_element._data.append(FVector4(uv[0], v, 0.0, 0.0))

        mesh._vertex_elements.append(uv_element)

    def _add_colors_to_mesh(self, mesh, accessor, buffer_views, buffers, vertex_count, base_vertex_index):
        from aspose.threed.entities import VertexElementVertexColor
        from aspose.threed.utilities.FVector4 import FVector4

        colors = self._read_accessor_data(accessor, buffer_views, buffers, 'VEC3')
        if len(colors) < vertex_count:
            colors = self._read_accessor_data(accessor, buffer_views, buffers, 'VEC4')

        if len(colors) < vertex_count:
            return

        color_element = VertexElementVertexColor()
        for i in range(vertex_count):
            color = colors[i]
            if len(color) == 3:
                color_element._data.append(FVector4(color[0], color[1], color[2], 1.0))
            else:
                color_element._data.append(FVector4(color[0], color[1], color[2], color[3]))

        mesh._vertex_elements.append(color_element)
