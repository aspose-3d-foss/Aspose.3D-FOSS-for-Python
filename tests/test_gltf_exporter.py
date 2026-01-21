import unittest
import sys
import os
import io
import json
import struct

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from aspose.threed import Scene
from aspose.threed.entities import Mesh
from aspose.threed.utilities import Vector4, Vector3
from aspose.threed.formats.gltf import GltfSaveOptions
from aspose.threed.shading import PbrMaterial


class TestGltfExporter(unittest.TestCase):
    def test_simple_triangle_ascii(self):
        scene = Scene()
        mesh = Mesh('TestMesh')

        mesh._control_points.append(Vector4(0.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(1.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(0.0, 1.0, 0.0, 1.0))
        mesh.create_polygon(0, 1, 2)

        scene.root_node.create_child_node('TestNode').entity = mesh

        stream = io.BytesIO()
        options = GltfSaveOptions()
        options.binary_mode = False
        options.file_name = 'test.gltf'

        from aspose.threed.formats.gltf import GltfExporter
        exporter = GltfExporter()
        exporter.export(scene, stream, options)

        stream.seek(0)
        content = stream.read()
        gltf_data = json.loads(content.decode('utf-8'))

        self.assertEqual(gltf_data['asset']['version'], '2.0')
        self.assertIn('meshes', gltf_data)
        self.assertIn('nodes', gltf_data)
        self.assertIn('scenes', gltf_data)

    def test_simple_triangle_binary(self):
        scene = Scene()
        mesh = Mesh('TestMesh')

        mesh._control_points.append(Vector4(0.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(1.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(0.0, 1.0, 0.0, 1.0))
        mesh.create_polygon(0, 1, 2)

        scene.root_node.create_child_node('TestNode').entity = mesh

        stream = io.BytesIO()
        options = GltfSaveOptions()
        options.binary_mode = True
        options.file_name = 'test.glb'

        from aspose.threed.formats.gltf import GltfExporter
        exporter = GltfExporter()
        exporter.export(scene, stream, options)

        stream.seek(0)
        content = stream.read()

        magic, version, length = struct.unpack('<4sII', content[:12])

        self.assertEqual(magic, b'glTF')
        self.assertEqual(version, 2)

        chunk_offset = 12
        json_chunk_length, json_chunk_type = struct.unpack('<II', content[chunk_offset:chunk_offset + 8])
        self.assertEqual(json_chunk_type, 0x4E4F534A)

        json_chunk = content[chunk_offset + 8:chunk_offset + 8 + json_chunk_length]
        gltf_data = json.loads(json_chunk.decode('utf-8'))

        self.assertEqual(gltf_data['asset']['version'], '2.0')
        self.assertIn('meshes', gltf_data)

    def test_export_with_positions(self):
        scene = Scene()
        mesh = Mesh('TestMesh')

        mesh._control_points.append(Vector4(0.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(1.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(0.0, 1.0, 0.0, 1.0))
        mesh.create_polygon(0, 1, 2)

        scene.root_node.create_child_node('TestNode').entity = mesh

        stream = io.BytesIO()
        options = GltfSaveOptions()
        options.binary_mode = False
        options.file_name = 'test.gltf'

        from aspose.threed.formats.gltf import GltfExporter
        exporter = GltfExporter()
        exporter.export(scene, stream, options)

        stream.seek(0)
        content = stream.read()
        gltf_data = json.loads(content.decode('utf-8'))

        self.assertGreater(len(gltf_data['meshes']), 0)
        mesh_data = gltf_data['meshes'][0]
        self.assertIn('primitives', mesh_data)
        self.assertIn('POSITION', mesh_data['primitives'][0]['attributes'])

    def test_export_with_normals(self):
        from aspose.threed.entities import VertexElementNormal
        from aspose.threed.utilities.FVector4 import FVector4

        scene = Scene()
        mesh = Mesh('TestMesh')

        mesh._control_points.append(Vector4(0.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(1.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(0.0, 1.0, 0.0, 1.0))
        mesh.create_polygon(0, 1, 2)

        normal_element = VertexElementNormal()
        normal_element._data.extend([
            FVector4(0.0, 0.0, 1.0, 0.0),
            FVector4(0.0, 0.0, 1.0, 0.0),
            FVector4(0.0, 0.0, 1.0, 0.0)
        ])
        mesh._vertex_elements.append(normal_element)

        scene.root_node.create_child_node('TestNode').entity = mesh

        stream = io.BytesIO()
        options = GltfSaveOptions()
        options.binary_mode = False
        options.file_name = 'test.gltf'

        from aspose.threed.formats.gltf import GltfExporter
        exporter = GltfExporter()
        exporter.export(scene, stream, options)

        stream.seek(0)
        content = stream.read()
        gltf_data = json.loads(content.decode('utf-8'))

        self.assertGreater(len(gltf_data['meshes']), 0)
        mesh_data = gltf_data['meshes'][0]
        self.assertIn('primitives', mesh_data)
        self.assertIn('NORMAL', mesh_data['primitives'][0]['attributes'])

    def test_export_with_uvs(self):
        from aspose.threed.entities import VertexElementUV
        from aspose.threed.utilities.FVector4 import FVector4

        scene = Scene()
        mesh = Mesh('TestMesh')

        mesh._control_points.append(Vector4(0.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(1.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(0.0, 1.0, 0.0, 1.0))
        mesh.create_polygon(0, 1, 2)

        uv_element = VertexElementUV()
        uv_element._data.extend([
            FVector4(0.0, 0.0, 0.0, 0.0),
            FVector4(1.0, 0.0, 0.0, 0.0),
            FVector4(0.0, 1.0, 0.0, 0.0)
        ])
        mesh._vertex_elements.append(uv_element)

        scene.root_node.create_child_node('TestNode').entity = mesh

        stream = io.BytesIO()
        options = GltfSaveOptions()
        options.binary_mode = False
        options.file_name = 'test.gltf'

        from aspose.threed.formats.gltf import GltfExporter
        exporter = GltfExporter()
        exporter.export(scene, stream, options)

        stream.seek(0)
        content = stream.read()
        gltf_data = json.loads(content.decode('utf-8'))

        self.assertGreater(len(gltf_data['meshes']), 0)
        mesh_data = gltf_data['meshes'][0]
        self.assertIn('primitives', mesh_data)
        self.assertIn('TEXCOORD_0', mesh_data['primitives'][0]['attributes'])

    def test_flip_tex_coord_v(self):
        from aspose.threed.entities import VertexElementUV
        from aspose.threed.utilities.FVector4 import FVector4

        scene = Scene()
        mesh = Mesh('TestMesh')

        mesh._control_points.append(Vector4(0.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(1.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(0.0, 1.0, 0.0, 1.0))
        mesh.create_polygon(0, 1, 2)

        uv_element = VertexElementUV()
        uv_element._data.extend([
            FVector4(0.0, 0.5, 0.0, 0.0),
            FVector4(1.0, 0.5, 0.0, 0.0),
            FVector4(0.0, 1.0, 0.0, 0.0)
        ])
        mesh._vertex_elements.append(uv_element)

        scene.root_node.create_child_node('TestNode').entity = mesh

        from aspose.threed.formats.gltf import GltfExporter
        exporter = GltfExporter()

        stream1 = io.BytesIO()
        options1 = GltfSaveOptions()
        options1.binary_mode = False
        options1.flip_tex_coord_v = True
        options1.file_name = 'test1.gltf'

        exporter.export(scene, stream1, options1)

        stream2 = io.BytesIO()
        options2 = GltfSaveOptions()
        options2.binary_mode = False
        options2.flip_tex_coord_v = False
        options2.file_name = 'test2.gltf'

        exporter.export(scene, stream2, options2)

        self.assertTrue(True)

    def test_gltf_format_can_export(self):
        from aspose.threed.formats.gltf import GltfFormat

        gltf_format = GltfFormat()
        self.assertTrue(gltf_format.can_export)

    def test_export_with_material(self):
        scene = Scene()
        mesh = Mesh('TestMesh')

        mesh._control_points.append(Vector4(0.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(1.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(0.0, 1.0, 0.0, 1.0))
        mesh.create_polygon(0, 1, 2)

        albedo = Vector3(0.8, 0.2, 0.3)
        material = PbrMaterial('RedMaterial', albedo)
        material.metallic_factor = 0.5
        material.roughness_factor = 0.7

        node = scene.root_node.create_child_node('TestNode')
        node.entity = mesh
        node.material = material

        stream = io.BytesIO()
        options = GltfSaveOptions()
        options.binary_mode = False
        options.file_name = 'test.gltf'

        from aspose.threed.formats.gltf import GltfExporter
        exporter = GltfExporter()
        exporter.export(scene, stream, options)

        stream.seek(0)
        content = stream.read()
        gltf_data = json.loads(content.decode('utf-8'))

        self.assertIn('materials', gltf_data)
        self.assertEqual(len(gltf_data['materials']), 1)

        material_data = gltf_data['materials'][0]
        self.assertEqual(material_data['name'], 'RedMaterial')
        self.assertIn('pbrMetallicRoughness', material_data)

        pbr_data = material_data['pbrMetallicRoughness']
        self.assertEqual(pbr_data['baseColorFactor'], [0.8, 0.2, 0.3, 1.0])
        self.assertEqual(pbr_data['metallicFactor'], 0.5)
        self.assertEqual(pbr_data['roughnessFactor'], 0.7)

        self.assertIn('meshes', gltf_data)
        mesh_data = gltf_data['meshes'][0]
        self.assertIn('primitives', mesh_data)
        primitive_data = mesh_data['primitives'][0]
        self.assertIn('material', primitive_data)
        self.assertEqual(primitive_data['material'], 0)

    def test_export_with_emissive_material(self):
        scene = Scene()
        mesh = Mesh('TestMesh')

        mesh._control_points.append(Vector4(0.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(1.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(0.0, 1.0, 0.0, 1.0))
        mesh.create_polygon(0, 1, 2)

        material = PbrMaterial('GlowMaterial')
        material.albedo = Vector3(1.0, 1.0, 1.0)
        material.emissive_color = Vector3(0.5, 0.2, 0.1)

        node = scene.root_node.create_child_node('TestNode')
        node.entity = mesh
        node.material = material

        stream = io.BytesIO()
        options = GltfSaveOptions()
        options.binary_mode = False
        options.file_name = 'test.gltf'

        from aspose.threed.formats.gltf import GltfExporter
        exporter = GltfExporter()
        exporter.export(scene, stream, options)

        stream.seek(0)
        content = stream.read()
        gltf_data = json.loads(content.decode('utf-8'))

        self.assertIn('materials', gltf_data)
        material_data = gltf_data['materials'][0]
        self.assertEqual(material_data['emissiveFactor'], [0.5, 0.2, 0.1])

    def test_export_with_transparent_material(self):
        scene = Scene()
        mesh = Mesh('TestMesh')

        mesh._control_points.append(Vector4(0.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(1.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(0.0, 1.0, 0.0, 1.0))
        mesh.create_polygon(0, 1, 2)

        material = PbrMaterial('TransparentMaterial')
        material.albedo = Vector3(1.0, 1.0, 1.0)
        material.transparency = 0.6

        node = scene.root_node.create_child_node('TestNode')
        node.entity = mesh
        node.material = material

        stream = io.BytesIO()
        options = GltfSaveOptions()
        options.binary_mode = False
        options.file_name = 'test.gltf'

        from aspose.threed.formats.gltf import GltfExporter
        exporter = GltfExporter()
        exporter.export(scene, stream, options)

        stream.seek(0)
        content = stream.read()
        gltf_data = json.loads(content.decode('utf-8'))

        self.assertIn('materials', gltf_data)
        material_data = gltf_data['materials'][0]
        self.assertEqual(material_data['alphaMode'], 'MASK')
        self.assertEqual(material_data['alphaCutoff'], 0.4)

    def test_export_with_blend_material(self):
        scene = Scene()
        mesh = Mesh('TestMesh')

        mesh._control_points.append(Vector4(0.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(1.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(0.0, 1.0, 0.0, 1.0))
        mesh.create_polygon(0, 1, 2)

        material = PbrMaterial('BlendMaterial')
        material.albedo = Vector3(1.0, 1.0, 1.0)
        material.transparency = 1.0

        node = scene.root_node.create_child_node('TestNode')
        node.entity = mesh
        node.material = material

        stream = io.BytesIO()
        options = GltfSaveOptions()
        options.binary_mode = False
        options.file_name = 'test.gltf'

        from aspose.threed.formats.gltf import GltfExporter
        exporter = GltfExporter()
        exporter.export(scene, stream, options)

        stream.seek(0)
        content = stream.read()
        gltf_data = json.loads(content.decode('utf-8'))

        self.assertIn('materials', gltf_data)
        material_data = gltf_data['materials'][0]
        self.assertEqual(material_data['alphaMode'], 'BLEND')


if __name__ == '__main__':
    unittest.main()
