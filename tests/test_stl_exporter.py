import unittest
import io
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from aspose.threed import Scene, Node
from aspose.threed.entities import Mesh
from aspose.threed.utilities import Vector4
from aspose.threed.formats.stl import StlExporter, StlSaveOptions, StlFormat


class TestStlExporter(unittest.TestCase):
    def test_basic_triangle_export_ascii(self):
        scene = Scene()
        mesh = Mesh("test_mesh")
        mesh._control_points = [
            Vector4(0.0, 0.0, 0.0, 1.0),
            Vector4(1.0, 0.0, 0.0, 1.0),
            Vector4(1.0, 1.0, 0.0, 1.0),
        ]
        mesh.create_polygon(0, 1, 2)
        
        node = Node("test_node")
        node.entity = mesh
        node.parent_node = scene.root_node
        
        stream = io.StringIO()
        options = StlSaveOptions()
        options.binary_mode = False
        
        exporter = StlExporter()
        exporter.export(scene, stream, options)
        
        content = stream.getvalue()
        self.assertIn("solid", content)
        self.assertIn("facet normal", content)
        self.assertIn("vertex", content)
        self.assertIn("endsolid", content)
        
    def test_basic_triangle_export_binary(self):
        scene = Scene()
        mesh = Mesh("test_mesh")
        mesh._control_points = [
            Vector4(0.0, 0.0, 0.0, 1.0),
            Vector4(1.0, 0.0, 0.0, 1.0),
            Vector4(1.0, 1.0, 0.0, 1.0),
        ]
        mesh.create_polygon(0, 1, 2)
        
        node = Node("test_node")
        node.entity = mesh
        node.parent_node = scene.root_node
        
        stream = io.BytesIO()
        options = StlSaveOptions()
        options.binary_mode = True
        
        exporter = StlExporter()
        exporter.export(scene, stream, options)
        
        content = stream.getvalue()
        self.assertEqual(len(content), 84 + 50)
        
    def test_quad_triangulation(self):
        scene = Scene()
        mesh = Mesh("test_mesh")
        mesh._control_points = [
            Vector4(0.0, 0.0, 0.0, 1.0),
            Vector4(1.0, 0.0, 0.0, 1.0),
            Vector4(1.0, 1.0, 0.0, 1.0),
            Vector4(0.0, 1.0, 0.0, 1.0),
        ]
        mesh.create_polygon(0, 1, 2, 3)
        
        node = Node("test_node")
        node.entity = mesh
        node.parent_node = scene.root_node
        
        stream = io.StringIO()
        options = StlSaveOptions()
        options.binary_mode = False
        
        exporter = StlExporter()
        exporter.export(scene, stream, options)
        
        content = stream.getvalue()
        facet_count = content.count("facet normal")
        self.assertEqual(facet_count, 2)
        
    def test_scale_export(self):
        scene = Scene()
        mesh = Mesh("test_mesh")
        mesh._control_points = [
            Vector4(1.0, 1.0, 1.0, 1.0),
            Vector4(2.0, 1.0, 1.0, 1.0),
            Vector4(2.0, 2.0, 1.0, 1.0),
        ]
        mesh.create_polygon(0, 1, 2)
        
        node = Node("test_node")
        node.entity = mesh
        node.parent_node = scene.root_node
        
        stream = io.StringIO()
        options = StlSaveOptions()
        options.binary_mode = False
        options.scale = 2.0
        
        exporter = StlExporter()
        exporter.export(scene, stream, options)
        
        content = stream.getvalue()
        self.assertIn("vertex 2.000000e+00 2.000000e+00 2.000000e+00", content)
        
    def test_flip_coordinate_system_export(self):
        scene = Scene()
        mesh = Mesh("test_mesh")
        mesh._control_points = [
            Vector4(1.0, 2.0, 3.0, 1.0),
            Vector4(2.0, 3.0, 4.0, 1.0),
            Vector4(3.0, 4.0, 5.0, 1.0),
        ]
        mesh.create_polygon(0, 1, 2)
        
        node = Node("test_node")
        node.entity = mesh
        node.parent_node = scene.root_node
        
        stream = io.StringIO()
        options = StlSaveOptions()
        options.binary_mode = False
        options.flip_coordinate_system = True
        
        exporter = StlExporter()
        exporter.export(scene, stream, options)
        
        content = stream.getvalue()
        self.assertIn("vertex 1.000000e+00 3.000000e+00 2.000000e+00", content)
        
    def test_save_options_properties(self):
        options = StlSaveOptions()
        
        self.assertFalse(options.flip_coordinate_system)
        self.assertFalse(options.binary_mode)
        self.assertAlmostEqual(options.scale, 1.0)
        
        options.flip_coordinate_system = True
        options.binary_mode = True
        options.scale = 2.5
        
        self.assertTrue(options.flip_coordinate_system)
        self.assertTrue(options.binary_mode)
        self.assertAlmostEqual(options.scale, 2.5)
        
    def test_export_format_support(self):
        stl_format = StlFormat()
        self.assertTrue(stl_format.can_export)
        self.assertTrue(stl_format.can_import)
        
    def test_exporter_supports_format(self):
        exporter = StlExporter()
        stl_format = StlFormat()
        self.assertTrue(exporter.supports_format(stl_format))
        
    def test_roundtrip_ascii(self):
        scene = Scene()
        mesh = Mesh("test_mesh")
        mesh._control_points = [
            Vector4(0.0, 0.0, 0.0, 1.0),
            Vector4(1.0, 0.0, 0.0, 1.0),
            Vector4(1.0, 1.0, 0.0, 1.0),
        ]
        mesh.create_polygon(0, 1, 2)
        
        node = Node("test_node")
        node.entity = mesh
        node.parent_node = scene.root_node
        
        stream = io.StringIO()
        options = StlSaveOptions()
        options.binary_mode = False
        
        exporter = StlExporter()
        exporter.export(scene, stream, options)
        
        content = stream.getvalue()
        
        scene2 = Scene()
        stream2 = io.StringIO(content)
        options2 = StlSaveOptions()
        
        from aspose.threed.formats.stl import StlLoadOptions
        importer_options = StlLoadOptions()
        
        from aspose.threed.formats.stl import StlImporter
        importer = StlImporter()
        importer.import_scene(scene2, stream2, importer_options)
        
        self.assertEqual(len(scene2.root_node.child_nodes), 1)
        mesh2 = scene2.root_node.child_nodes[0].entity
        self.assertEqual(mesh2.polygon_count, 1)


if __name__ == '__main__':
    unittest.main()
