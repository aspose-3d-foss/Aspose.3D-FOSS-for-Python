import unittest
import io
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from aspose.threed import Scene
from aspose.threed.formats.stl import StlLoadOptions, StlFormat, StlImporter, StlFormatDetector


class TestStlImporter(unittest.TestCase):
    def test_ascii_stl_import(self):
        stl_content = """solid TestCube
  facet normal 0.0 0.0 -1.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 1.0 0.0 0.0
      vertex 1.0 1.0 0.0
    endloop
  endfacet
  facet normal 0.0 0.0 -1.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 1.0 1.0 0.0
      vertex 0.0 1.0 0.0
    endloop
  endfacet
endsolid TestCube
"""
        scene = Scene()
        stream = io.StringIO(stl_content)
        options = StlLoadOptions()
        
        importer = StlImporter()
        importer.import_scene(scene, stream, options)
        
        self.assertIsNotNone(scene.root_node)
        self.assertEqual(len(scene.root_node.child_nodes), 1)
        
        node = scene.root_node.child_nodes[0]
        self.assertIsNotNone(node.entity)
        
        mesh = node.entity
        self.assertEqual(len(mesh.control_points), 6)
        self.assertEqual(mesh.polygon_count, 2)
        
    def test_binary_stl_import(self):
        import struct
        
        header = b"BinarySTL\x00" + b"\x00" * 70
        facet_count = 2
        facets = b""
        
        for _ in range(facet_count):
            normal = struct.pack('<3f', 0.0, 0.0, -1.0)
            v1 = struct.pack('<3f', 0.0, 0.0, 0.0)
            v2 = struct.pack('<3f', 1.0, 0.0, 0.0)
            v3 = struct.pack('<3f', 1.0, 1.0, 0.0)
            attr = struct.pack('<H', 0)
            facets += normal + v1 + v2 + v3 + attr
        
        content = header + struct.pack('<I', facet_count) + facets
        
        scene = Scene()
        stream = io.BytesIO(content)
        options = StlLoadOptions()
        
        importer = StlImporter()
        importer.import_scene(scene, stream, options)
        
        self.assertIsNotNone(scene.root_node)
        self.assertEqual(len(scene.root_node.child_nodes), 1)
        
        node = scene.root_node.child_nodes[0]
        self.assertIsNotNone(node.entity)
        
        mesh = node.entity
        self.assertEqual(len(mesh.control_points), 6)
        self.assertEqual(mesh.polygon_count, 2)
        
    def test_stl_format(self):
        stl_format = StlFormat()
        self.assertTrue(stl_format.can_import)
        self.assertTrue(stl_format.can_export)
        self.assertEqual(stl_format.extension, "stl")
        self.assertIn("stl", stl_format.extensions)
        
    def test_load_options_properties(self):
        options = StlLoadOptions()
        
        self.assertFalse(options.flip_coordinate_system)
        self.assertAlmostEqual(options.scale, 1.0)
        
        options.flip_coordinate_system = True
        options.scale = 2.5
        
        self.assertTrue(options.flip_coordinate_system)
        self.assertAlmostEqual(options.scale, 2.5)
        
    def test_flip_coordinate_system(self):
        stl_content = """solid Test
  facet normal 0.0 1.0 2.0
    outer loop
      vertex 1.0 2.0 3.0
      vertex 2.0 3.0 4.0
      vertex 3.0 4.0 5.0
    endloop
  endfacet
endsolid Test
"""
        scene = Scene()
        stream = io.StringIO(stl_content)
        options = StlLoadOptions()
        options.flip_coordinate_system = True
        
        importer = StlImporter()
        importer.import_scene(scene, stream, options)
        
        self.assertGreater(len(scene.root_node.child_nodes), 0)
        
        node = scene.root_node.child_nodes[0]
        mesh = node.entity
        first_point = mesh.control_points[0]
        self.assertAlmostEqual(first_point.x, 1.0)
        self.assertAlmostEqual(first_point.y, 3.0)
        self.assertAlmostEqual(first_point.z, 2.0)
        
    def test_scale(self):
        stl_content = """solid Test
  facet normal 0.0 0.0 -1.0
    outer loop
      vertex 1.0 1.0 1.0
      vertex 2.0 2.0 2.0
      vertex 3.0 2.0 2.0
    endloop
  endfacet
endsolid Test
"""
        scene = Scene()
        stream = io.StringIO(stl_content)
        options = StlLoadOptions()
        options.scale = 2.0
        
        importer = StlImporter()
        importer.import_scene(scene, stream, options)
        
        self.assertGreater(len(scene.root_node.child_nodes), 0)
        
        node = scene.root_node.child_nodes[0]
        mesh = node.entity
        first_point = mesh.control_points[0]
        self.assertAlmostEqual(first_point.x, 2.0)
        self.assertAlmostEqual(first_point.y, 2.0)
        self.assertAlmostEqual(first_point.z, 2.0)


if __name__ == '__main__':
    unittest.main()
