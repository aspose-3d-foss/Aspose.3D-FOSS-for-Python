from typing import TYPE_CHECKING, List, Optional, Any
import struct

from ..Importer import Importer

if TYPE_CHECKING:
    from aspose.threed import Scene
    from aspose.threed.formats import LoadOptions
    from aspose.threed.formats.fbx import FbxLoadOptions


class FbxNode:
    def __init__(self, name: str = ""):
        self.name: str = name
        self.properties: List[Any] = []
        self.children: List['FbxNode'] = []


class FbxImporter(Importer):
    MAGIC = b'Kaydara FBX Binary  \x00'
    FOOTER_SIZE = 27

    def __init__(self):
        super().__init__()
        self._document: Optional[FbxNode] = None

    def supports_format(self, file_format) -> bool:
        from .FbxFormat import FbxFormat
        return isinstance(file_format, FbxFormat)

    def import_scene(self, scene: 'Scene', stream, options: 'FbxLoadOptions'):
        from .FbxLoadOptions import FbxLoadOptions
        from aspose.threed import Node
        from aspose.threed.entities import Mesh

        if not isinstance(options, FbxLoadOptions):
            options = FbxLoadOptions()

        if not hasattr(stream, 'read'):
            raise TypeError("Stream must support read() method")

        if hasattr(stream, 'seek'):
            stream.seek(0)

        data = stream.read()
        if isinstance(data, str):
            data = data.encode('utf-8')

        root_node = self._parse_binary(data)

        if root_node:
            self._build_scene(scene, root_node, options)

    def _parse_binary(self, data: bytes) -> Optional[FbxNode]:
        if not data.startswith(self.MAGIC):
            raise ValueError("Invalid FBX binary file")

        reader = _BinaryReader(data)
        reader.pos = self.FOOTER_SIZE

        root = FbxNode("FBXHeader")
        node_count = 0
        max_nodes = 1000
        last_pos = reader.pos
        
        while reader.pos < len(data) and node_count < max_nodes:
            node = self._read_node(reader)
            if node:
                root.children.append(node)
                node_count += 1
                last_pos = reader.pos
            else:
                if reader.pos >= len(data) - 1 or reader.pos == last_pos:
                    break

        return root

    def _read_node(self, reader: '_BinaryReader') -> Optional[FbxNode]:
        start_pos = reader.pos
        end_offset = reader.read_uint32()

        if end_offset == 0:
            reader.skip(9)
            return None

        if end_offset > len(reader.data):
            return None

        num_properties = reader.read_uint32()
        property_list_len = reader.read_uint32()
        name_len = reader.read_uint8()
        name = reader.read_bytes(name_len).decode('utf-8', errors='ignore')

        node = FbxNode(name)

        properties_start = reader.pos
        for i in range(num_properties):
            prop = self._read_property(reader)
            if prop is not None:
                node.properties.append(prop)
            else:
                break
        
        if reader.pos < properties_start + property_list_len:
            reader.pos = properties_start + property_list_len

        safety_count = 0
        max_safety = 10000
        while reader.pos < end_offset and safety_count < max_safety:
            child = self._read_node(reader)
            if child is not None:
                node.children.append(child)
            safety_count += 1
            
            if reader.pos == start_pos:
                break

        return node

    def _read_property(self, reader: '_BinaryReader') -> Any:
        if reader.pos >= len(reader.data):
            return None

        prop_type = reader.data[reader.pos:reader.pos + 1]
        reader.pos += 1

        if prop_type == b'Y':
            return reader.read_int16()
        elif prop_type == b'C':
            return bool(reader.data[reader.pos])
        elif prop_type == b'I':
            return reader.read_int32()
        elif prop_type == b'F':
            return reader.read_float32()
        elif prop_type == b'D':
            return reader.read_float64()
        elif prop_type == b'L':
            return reader.read_int64()
        elif prop_type == b'i':
            count = reader.read_uint32()
            values = []
            for _ in range(count):
                values.append(reader.read_int32())
            return values
        elif prop_type == b'f':
            count = reader.read_uint32()
            values = []
            for _ in range(count):
                values.append(reader.read_float32())
            return values
        elif prop_type == b'd':
            count = reader.read_uint32()
            values = []
            for _ in range(count):
                values.append(reader.read_float64())
            return values
        elif prop_type == b'l':
            count = reader.read_uint32()
            values = []
            for _ in range(count):
                values.append(reader.read_int64())
            return values
        elif prop_type == b'b':
            count = reader.read_uint32()
            values = []
            for _ in range(count):
                values.append(bool(reader.data[reader.pos]))
                reader.pos += 1
            return values
        elif prop_type == b'S':
            length = reader.read_uint32()
            return reader.read_bytes(length)
        elif prop_type == b'R':
            length = reader.read_uint32()
            return reader.read_bytes(length)
        else:
            return None

    def _build_scene(self, scene: 'Scene', root: FbxNode, options):
        from aspose.threed import Node
        from aspose.threed.entities import Mesh
        from aspose.threed.utilities import Vector4

        for child in root.children:
            if child.name == "Objects":
                for obj in child.children:
                    if obj.name == "Geometry":
                        model_node = Node("Model")
                        mesh = Mesh("Mesh")
                        model_node.entity = mesh

                        for geom_child in obj.children:
                            if geom_child.name == "Vertices" and geom_child.properties:
                                vertices_data = geom_child.properties[0]
                                if isinstance(vertices_data, list):
                                    for i in range(0, len(vertices_data), 3):
                                        if i + 2 < len(vertices_data):
                                            x = vertices_data[i]
                                            y = vertices_data[i + 1]
                                            z = vertices_data[i + 2]
                                            mesh._control_points.append(Vector4(x, y, z, 1.0))

                            elif geom_child.name == "PolygonVertexIndex" and geom_child.properties:
                                indices = geom_child.properties[0]
                                if isinstance(indices, list):
                                    polygon = []
                                    for idx in indices:
                                        if idx < 0:
                                            polygon.append(-(idx + 1))
                                            if len(polygon) >= 3:
                                                mesh.create_polygon(list(polygon))
                                            polygon = []
                                        else:
                                            polygon.append(idx)
                                    if len(polygon) >= 3:
                                        mesh.create_polygon(list(polygon))

                        if mesh._control_points or mesh.polygons:
                            scene.root_node.add_child_node(model_node)

    def _parse_double_array(self, data: bytes) -> List[float]:
        reader = _BinaryReader(data)
        values = []
        while reader.pos + 8 <= len(data):
            values.append(reader.read_float64())
        return values


class _BinaryReader:
    def __init__(self, data: bytes):
        self.data = data
        self.pos = 0

    def read_uint8(self) -> int:
        if self.pos + 1 > len(self.data):
            return 0
        value = self.data[self.pos]
        self.pos += 1
        return value

    def read_uint32(self) -> int:
        if self.pos + 4 > len(self.data):
            return 0
        value = struct.unpack('<I', self.data[self.pos:self.pos + 4])[0]
        self.pos += 4
        return value

    def read_int32(self) -> int:
        if self.pos + 4 > len(self.data):
            return 0
        value = struct.unpack('<i', self.data[self.pos:self.pos + 4])[0]
        self.pos += 4
        return value

    def read_int16(self) -> int:
        if self.pos + 2 > len(self.data):
            return 0
        value = struct.unpack('<h', self.data[self.pos:self.pos + 2])[0]
        self.pos += 2
        return value

    def read_int64(self) -> int:
        if self.pos + 8 > len(self.data):
            return 0
        value = struct.unpack('<q', self.data[self.pos:self.pos + 8])[0]
        self.pos += 8
        return value

    def read_float32(self) -> float:
        if self.pos + 4 > len(self.data):
            return 0.0
        value = struct.unpack('<f', self.data[self.pos:self.pos + 4])[0]
        self.pos += 4
        return value

    def read_float64(self) -> float:
        if self.pos + 8 > len(self.data):
            return 0.0
        value = struct.unpack('<d', self.data[self.pos:self.pos + 8])[0]
        self.pos += 8
        return value

    def read_string(self) -> str:
        end = self.data.find(b'\x00', self.pos)
        if end == -1:
            result = self.data[self.pos:].decode('utf-8', errors='ignore')
            self.pos = len(self.data)
        else:
            result = self.data[self.pos:end].decode('utf-8', errors='ignore')
            self.pos = end + 1
        return result

    def read_bytes(self, length: int) -> bytes:
        if self.pos + length > len(self.data):
            length = len(self.data) - self.pos
        result = self.data[self.pos:self.pos + length]
        self.pos += length
        return result

    def skip(self, count: int):
        self.pos += count
