from typing import TYPE_CHECKING, Optional, List, Dict, Any
import io

from ..Importer import Importer

if TYPE_CHECKING:
    from .FbxLoadOptions import FbxLoadOptions
    from aspose.threed import Scene


class FbxImporter(Importer):
    def __init__(self):
        super().__init__()

    def supports_format(self, file_format) -> bool:
        from .FbxFormat import FbxFormat
        return isinstance(file_format, FbxFormat)

    def open(self, filename: str, options: Optional['FbxLoadOptions'] = None) -> 'Scene':
        if options is None:
            from .FbxLoadOptions import FbxLoadOptions
            options = FbxLoadOptions()

        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        from .parser import FbxParser
        from .tokenizer import FbxTokenizer

        tokenizer = FbxTokenizer(content)
        tokens = tokenizer.tokenize()
        parser = FbxParser(tokens)

        from aspose.threed import Scene
        scene = Scene()

        self.import_scene(scene, io.StringIO(content), options)

        return scene

    def open_from_stream(self, stream: io.IOBase, options: Optional['FbxLoadOptions'] = None) -> 'Scene':
        if options is None:
            from .FbxLoadOptions import FbxLoadOptions
            options = FbxLoadOptions()

        content = stream.read()
        if isinstance(content, bytes):
            content = content.decode('utf-8')

        from .parser import FbxParser
        from .tokenizer import FbxTokenizer

        tokenizer = FbxTokenizer(content)
        tokens = tokenizer.tokenize()
        parser = FbxParser(tokens)

        from aspose.threed import Scene
        scene = Scene()

        self.import_scene(scene, io.StringIO(content), options)

        return scene

    def import_scene(self, scene: 'Scene', stream: io.IOBase, options: 'FbxLoadOptions'):
        from .parser import FbxParser
        from .tokenizer import FbxTokenizer

        content = stream.read()
        if isinstance(content, bytes):
            content = content.decode('utf-8')

        tokenizer = FbxTokenizer(content)
        tokens = tokenizer.tokenize()
        parser = FbxParser(tokens)

        self._parse_scene(parser.root_scope, scene)

    def _parse_scene(self, root_scope, scene):
        objects_element = root_scope.get_first_element('Objects')
        if objects_element is None or objects_element.compound is None:
            return

        objects_scope = objects_element.compound
        self._object_map = {}

        geometry_elements = objects_scope.get_elements('Geometry')
        model_elements = objects_scope.get_elements('Model')
        material_elements = objects_scope.get_elements('Material')

        self._parse_geometries(geometry_elements, scene)
        self._parse_models(model_elements, scene)
        self._parse_materials(material_elements, scene)
        self._parse_connections(root_scope, scene)

    def _parse_geometries(self, geometry_elements, scene):
        from aspose.threed.entities import Mesh
        from aspose.threed.utilities import Vector4

        for geom_elem in geometry_elements:
            geom_scope = geom_elem.compound
            if geom_scope is None:
                continue

            geom_id = self._parse_id(geom_elem.tokens[0].text) if len(geom_elem.tokens) > 0 else None
            if geom_id is None:
                continue

            mesh = Mesh()
            self._object_map[geom_id] = mesh

            vertices_element = geom_scope.get_first_element('Vertices')
            if vertices_element and vertices_element.compound:
                a_elem = vertices_element.compound.get_first_element('a')
                if a_elem:
                    vertices = self._parse_float_array_from_tokens(a_elem.tokens)
                    for i in range(0, len(vertices), 3):
                        if i + 2 < len(vertices):
                            mesh._control_points.append(Vector4(vertices[i], vertices[i + 1], vertices[i + 2], 1.0))

            polygon_element = geom_scope.get_first_element('PolygonVertexIndex')
            if polygon_element and polygon_element.compound:
                a_elem = polygon_element.compound.get_first_element('a')
                if a_elem:
                    indices = self._parse_int_array_from_tokens(a_elem.tokens)
                    for idx in indices:
                        if idx < 0:
                            mesh._polygons.append(abs(idx) - 1)
                            mesh._polygons.append(0xFFFFFFFF)
                        else:
                            mesh._polygons.append(idx)

            normal_element = geom_scope.get_first_element('Normals')
            if normal_element and normal_element.compound:
                a_elem = normal_element.compound.get_first_element('a')
                if a_elem:
                    normals = self._parse_float_array_from_tokens(a_elem.tokens)
                    from aspose.threed.entities import VertexElementNormal
                    vertex_element = mesh.create_element(VertexElementNormal)
                    vertex_element.mapping_mode = VertexElementNormal.MappingMode.CONTROL_POINT
                    for i in range(0, len(normals), 3):
                        if i + 2 < len(normals):
                            vertex_element.data.append((normals[i], normals[i + 1], normals[i + 2]))

            uv_element = geom_scope.get_first_element('UV')
            if uv_element and uv_element.compound:
                a_elem = uv_element.compound.get_first_element('a')
                if a_elem:
                    uvs = self._parse_float_array_from_tokens(a_elem.tokens)
                    from aspose.threed.entities import VertexElementUV
                    vertex_element = mesh.create_element(VertexElementUV)
                    vertex_element.mapping_mode = VertexElementUV.MappingMode.CONTROL_POINT
                    for i in range(0, len(uvs), 2):
                        if i + 1 < len(uvs):
                            vertex_element.data.append((uvs[i], uvs[i + 1]))

    def _parse_models(self, model_elements, scene):
        from aspose.threed import Node

        for model_elem in model_elements:
            model_id = self._parse_id(model_elem.tokens[0].text) if len(model_elem.tokens) > 0 else None
            if model_id is None:
                continue

            node = Node()
            self._object_map[model_id] = node

            if len(model_elem.tokens) > 1:
                node.name = model_elem.tokens[1].text.strip('"')

    def _parse_materials(self, material_elements, scene):
        from aspose.threed.shading import LambertMaterial

        for mat_elem in material_elements:
            mat_id = self._parse_id(mat_elem.tokens[0].text) if len(mat_elem.tokens) > 0 else None
            if mat_id is None:
                continue

            material = LambertMaterial()
            self._object_map[mat_id] = material

            if len(mat_elem.tokens) > 1:
                material.name = mat_elem.tokens[1].text.strip('"')

            mat_scope = mat_elem.compound
            if mat_scope is None:
                continue

            shading_elem = mat_scope.get_first_element('ShadingModel')
            if shading_elem and shading_elem.tokens:
                material.shading_model = shading_elem.tokens[0].text.strip('"')

    def _parse_connections(self, root_scope, scene):
        connections_element = root_scope.get_first_element('Connections')
        if connections_element is None or connections_element.compound is None:
            return

        connections_scope = connections_element.compound
        connection_elements = connections_scope.get_elements('C')

        for conn_elem in connection_elements:
            if len(conn_elem.tokens) < 3:
                continue

            conn_type = conn_elem.tokens[0].text.strip('"')
            if conn_type == 'OO':
                child_id = self._parse_id(conn_elem.tokens[1].text)
                parent_id = self._parse_id(conn_elem.tokens[2].text)

                self._connect_objects(child_id, parent_id, scene)

    def _connect_objects(self, child_id, parent_id, scene):
        if child_id is None:
            return

        child_obj = self._object_map.get(child_id)
        if child_obj is None:
            return

        if parent_id == 0:
            parent_obj = scene.root_node
        else:
            parent_obj = self._object_map.get(parent_id)
            if parent_obj is None:
                return

        from aspose.threed.entities import Mesh
        from aspose.threed import Node
        from aspose.threed.shading import Material

        if isinstance(child_obj, Mesh) and isinstance(parent_obj, Node):
            parent_obj._entities.append(child_obj)
        elif isinstance(child_obj, Material) and isinstance(parent_obj, Node):
            parent_obj._materials.append(child_obj)
        elif isinstance(child_obj, Node) and isinstance(parent_obj, Node):
            parent_obj._child_nodes.append(child_obj)

    def _parse_id(self, text):
        try:
            return int(text)
        except ValueError:
            return None

    def _parse_int_array_from_tokens(self, tokens):
        values = []
        for token in tokens:
            text = token.text
            if text.startswith('*'):
                continue
            if text.startswith('a:'):
                text = text[2:]
            import re
            found = re.findall(r'-?\d+', text)
            for v in found:
                values.append(int(v))
        return values

    def _parse_float_array_from_tokens(self, tokens):
        values = []
        for token in tokens:
            text = token.text
            if text.startswith('*'):
                continue
            if text.startswith('a:'):
                text = text[2:]
            import re
            found = re.findall(r'-?\d+\.?\d*', text)
            for v in found:
                values.append(float(v))
        return values

    def _parse_float_array(self, text):
        import re
        if text.startswith('a:'):
            text = text[2:]
        values = re.findall(r'-?\d+\.?\d*', text)
        return [float(v) for v in values]

    def _parse_int_array(self, text):
        import re
        if text.startswith('a:'):
            text = text[2:]
        values = re.findall(r'-?\d+', text)
        return [int(v) for v in values]
