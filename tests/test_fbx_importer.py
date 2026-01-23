import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from aspose.threed import Scene
from aspose.threed.formats.fbx import FbxImporter, FbxFormat, FbxLoadOptions


class TestFbxImporter(unittest.TestCase):
    def test_cube_import(self):
        scene = Scene()
        file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'examples', 'fbx7400ascii', 'cube.fbx')

        if os.path.exists(file_path):
            scene.open(file_path)

            self.assertIsNotNone(scene.root_node)
            self.assertGreater(len(scene.root_node.child_nodes), 0)

            has_mesh = False
            for child in scene.root_node.child_nodes:
                if child.entity is not None:
                    has_mesh = True
                    break

            self.assertTrue(has_mesh)

    def test_format_detection(self):
        file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'examples', 'fbx7400ascii', 'cube.fbx')

        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                from aspose.threed.formats import IOService
                io_service = IOService()
                format_detected = io_service.detect_format(f, file_path)

                self.assertIsNotNone(format_detected)
                self.assertEqual(format_detected.extension, 'fbx')


if __name__ == '__main__':
    unittest.main()
