import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from aspose.threed import Scene
from aspose.threed.formats.stl import StlLoadOptions


class TestSceneOpenSTL(unittest.TestCase):
    def test_scene_open_ascii_stl_file(self):
        scene = Scene.from_file('examples/stl/stl_ascii.stl')
        
        self.assertIsNotNone(scene.root_node)
        self.assertEqual(len(scene.root_node.child_nodes), 1)
        
        node = scene.root_node.child_nodes[0]
        self.assertIsNotNone(node.entity)
        
        mesh = node.entity
        self.assertEqual(len(mesh.control_points), 6000)
        self.assertEqual(mesh.polygon_count, 2000)
        self.assertEqual(node.name, "Object01")
        
    def test_scene_open_binary_stl_file(self):
        scene = Scene.from_file('examples/stl/stl_binary.stl')
        
        self.assertIsNotNone(scene.root_node)
        self.assertEqual(len(scene.root_node.child_nodes), 1)
        
        node = scene.root_node.child_nodes[0]
        self.assertIsNotNone(node.entity)
        
        mesh = node.entity
        self.assertEqual(len(mesh.control_points), 6000)
        self.assertEqual(mesh.polygon_count, 2000)
        
    def test_scene_open_ascii_with_options(self):
        from aspose.threed.formats.stl import StlFormat
        
        scene = Scene()
        options = StlLoadOptions()
        options.scale = 0.5
        options.file_name = 'examples/stl/stl_ascii.stl'
        
        format_obj = StlFormat()
        importer = format_obj.create_load_options()
        
        scene.open('examples/stl/stl_ascii.stl', options)
        
        self.assertEqual(len(scene.root_node.child_nodes), 1)
        node = scene.root_node.child_nodes[0]
        mesh = node.entity
        first_point = mesh.control_points[0]
        self.assertAlmostEqual(first_point.x, 0.202713 * 0.5)
        self.assertAlmostEqual(first_point.y, 14.538760 * 0.5)
        self.assertAlmostEqual(first_point.z, 33.063510 * 0.5)


if __name__ == '__main__':
    unittest.main()
