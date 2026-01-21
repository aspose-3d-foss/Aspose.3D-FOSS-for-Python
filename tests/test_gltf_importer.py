import unittest
import sys
import os
import json
import struct
import io

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from aspose.threed import Scene
from aspose.threed.formats.gltf import GltfLoadOptions


class TestGltfImporterFunctional(unittest.TestCase):
    def test_simple_gltf_json(self):
        gltf_data = {
            "asset": {
                "version": "2.0",
                "generator": "test"
            },
            "scene": 0,
            "scenes": [
                {
                    "nodes": [0]
                }
            ],
            "nodes": [
                {
                    "name": "TestNode",
                    "mesh": 0
                }
            ],
            "meshes": [
                {
                    "name": "TestMesh",
                    "primitives": [
                        {
                            "attributes": {
                                "POSITION": 0
                            },
                            "mode": 4
                        }
                    ]
                }
            ],
            "accessors": [
                {
                    "bufferView": 0,
                    "componentType": 5126,
                    "count": 3,
                    "type": "VEC3"
                }
            ],
            "bufferViews": [
                {
                    "buffer": 0,
                    "byteOffset": 0,
                    "byteLength": 36
                }
            ],
            "buffers": [
                {
                    "byteLength": 36,
                    "uri": "data:application/octet-stream;base64,AAAAAAAAAAAAAAAAAACAPwAAAAAAAAAAAAAAAAAAgD8AAAAA"
                }
            ]
        }

        scene = Scene()
        json_str = json.dumps(gltf_data)
        stream = io.BytesIO(json_str.encode('utf-8'))
        options = GltfLoadOptions()

        try:
            from aspose.threed.formats.gltf import GltfImporter
            importer = GltfImporter()
            importer.import_scene(scene, stream, options)

            self.assertEqual(len(scene.root_node.child_nodes), 1)
            node = scene.root_node.child_nodes[0]
            self.assertEqual(node.name, 'TestNode')
            self.assertIsNotNone(node.entity)
        except Exception as e:
            self.fail(f"Failed to import glTF: {e}")

    def test_gltf_binary_format(self):
        scene = Scene()
        stream = io.BytesIO()

        magic = b'glTF'
        version = 2
        total_length = 12 + 8 + len(b'{"asset":{"version":"2.0"}}') + 8 + len(b'')

        stream.write(struct.pack('<4sII', magic, version, total_length))

        json_chunk = b'{"asset":{"version":"2.0"},"scene":0,"scenes":[{"nodes":[0]}],"nodes":[{"name":"TestNode"}]}'
        json_chunk_type = 0x4E4F534A
        json_chunk_length = len(json_chunk)

        stream.write(struct.pack('<II', json_chunk_length, json_chunk_type))
        stream.write(json_chunk)

        binary_chunk_type = 0x004E4942
        binary_chunk_length = 0

        stream.write(struct.pack('<II', binary_chunk_length, binary_chunk_type))

        stream.seek(0)
        options = GltfLoadOptions()

        try:
            from aspose.threed.formats.gltf import GltfImporter
            importer = GltfImporter()
            importer.import_scene(scene, stream, options)

            self.assertEqual(len(scene.root_node.child_nodes), 1)
            node = scene.root_node.child_nodes[0]
            self.assertEqual(node.name, 'TestNode')
        except Exception as e:
            self.fail(f"Failed to import binary glTF: {e}")


if __name__ == '__main__':
    unittest.main()
