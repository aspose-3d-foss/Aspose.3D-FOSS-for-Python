import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from aspose.threed import Scene
from aspose.threed.formats import ColladaLoadOptions


class TestColladaImporter(unittest.TestCase):
    def test_import_real_cube(self):
        scene = Scene()
        options = ColladaLoadOptions()

        file_path = os.path.join(os.path.dirname(__file__), '..', 'examples', 'collada', 'cube_triangulate.dae')
        
        if os.path.exists(file_path):
            scene.open(file_path, options)

            self.assertIsNotNone(scene.root_node)
            self.assertTrue(len(scene.root_node.child_nodes) > 0)
        else:
            self.skipTest(f"File not found: {file_path}")

    def test_collada_load_options(self):
        options = ColladaLoadOptions()

        self.assertEqual(options.flip_coordinate_system, False)
        self.assertEqual(options.enable_materials, True)
        self.assertEqual(options.scale, 1.0)
        self.assertEqual(options.normalize_normal, True)

        options.flip_coordinate_system = True
        self.assertEqual(options.flip_coordinate_system, True)

        options.scale = 2.0
        self.assertEqual(options.scale, 2.0)


if __name__ == '__main__':
    unittest.main()
