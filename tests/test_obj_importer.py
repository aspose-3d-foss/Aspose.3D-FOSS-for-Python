import unittest
import io
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from aspose.threed import Scene
from aspose.threed.formats.obj import ObjLoadOptions, ObjFormat, ObjImporter, ObjExporter, ObjFormatDetector


class TestObjImporter(unittest.TestCase):
    def test_basic_cube_import(self):
        obj_content = """# Simple cube OBJ
v 0.0 0.0 0.0
v 1.0 0.0 0.0
v 1.0 1.0 0.0
v 0.0 1.0 0.0
f 1 2 3 4
f 5 6 7 8
"""
        scene = Scene()
        stream = io.StringIO(obj_content)
        options = ObjLoadOptions()
        options.file_name = "test.obj"
        
        importer = ObjImporter()
        importer.import_scene(scene, stream, options)
        
        self.assertIsNotNone(scene.root_node)
        self.assertGreater(len(scene.root_node.child_nodes), 0)
        
        node = scene.root_node.child_nodes[0]
        self.assertIsNotNone(node.entity)
        
        mesh = node.entity
        self.assertEqual(len(mesh.control_points), 8)
        self.assertEqual(mesh.polygon_count, 2)

    def test_multiple_objects(self):
        obj_content = """# Multiple objects
o Cube1
v 0.0 0.0 0.0
v 1.0 0.0 0.0
v 1.0 1.0 0.0
v 0.0 1.0 0.0
f 1 2 3 4

o Cube2
v 2.0 0.0 0.0
v 3.0 0.0 0.0
v 3.0 1.0 0.0
v 2.0 1.0 0.0
f 5 6 7 8
"""
        scene = Scene()
        stream = io.StringIO(obj_content)
        options = ObjLoadOptions()
        options.file_name = "test.obj"
        
        importer = ObjImporter()
        importer.import_scene(scene, stream, options)
        
        self.assertGreaterEqual(len(scene.root_node.child_nodes), 2)

    def test_groups(self):
        obj_content = """# Groups
o MyObject
g Group1
v 0.0 0.0 0.0
v 1.0 0.0 0.0
v 1.0 1.0 0.0
v 0.0 1.0 0.0
f 1 2 3 4

g Group2
v 2.0 0.0 0.0
v 3.0 0.0 0.0
v 3.0 1.0 0.0
v 2.0 1.0 0.0
f 5 6 7 8
"""
        scene = Scene()
        stream = io.StringIO(obj_content)
        options = ObjLoadOptions()
        options.file_name = "test.obj"
        
        importer = ObjImporter()
        importer.import_scene(scene, stream, options)
        
        self.assertGreater(len(scene.root_node.child_nodes), 0)

    def test_normals_and_uvs(self):
        obj_content = """# With normals and UVs
v 0.0 0.0 0.0
v 1.0 0.0 0.0
v 1.0 1.0 0.0
v 0.0 1.0 0.0
vt 0.0 0.0
vt 1.0 0.0
vt 1.0 1.0
vt 0.0 1.0
vt 0.0 1.0
vn 0.0 0.0 1.0
f 1/1/1 2/2/1 3/3/1 4/4/1
"""
        scene = Scene()
        stream = io.StringIO(obj_content)
        options = ObjLoadOptions()
        options.file_name = "test.obj"
        
        importer = ObjImporter()
        importer.import_scene(scene, stream, options)
        
        self.assertGreater(len(scene.root_node.child_nodes), 0)
        
        node = scene.root_node.child_nodes[0]
        self.assertIsNotNone(node.entity)
        
        mesh = node.entity
        self.assertEqual(len(mesh.control_points), 4)

    def test_face_variants(self):
        obj_content = """# Different face formats
v 0.0 0.0 0.0
v 1.0 0.0 0.0
v 1.0 1.0 0.0
v 0.0 1.0 0.0

f 1 2 3 4

v 2.0 0.0 0.0
v 3.0 0.0 0.0
v 3.0 1.0 0.0
f 5/1 6/2 7/2/1

v 4.0 0.0 0.0
v 5.0 0.0 0.0
v 5.0 1.0 0.0
f 9/10/1 11/2/1

v 6.0 0.0 0.0
v 7.0 0.0 0.0
v 7.0 1.0 0.0
vn 0.0 0.0 1.0
f 13/14/1 15/1
"""
        scene = Scene()
        stream = io.StringIO(obj_content)
        options = ObjLoadOptions()
        options.file_name = "test.obj"
        
        importer = ObjImporter()
        importer.import_scene(scene, stream, options)
        
        self.assertGreater(len(scene.root_node.child_nodes), 0)

    def test_flip_coordinate_system(self):
        obj_content = """# Test coordinate flip
v 1.0 2.0 3.0
v 2.0 3.0 4.0
v 3.0 4.0 5.0
f 1 2 3
"""
        scene = Scene()
        stream = io.StringIO(obj_content)
        options = ObjLoadOptions()
        options.flip_coordinate_system = True
        
        importer = ObjImporter()
        importer.import_scene(scene, stream, options)
        
        self.assertGreater(len(scene.root_node.child_nodes), 0)
        
        node = scene.root_node.child_nodes[0]
        self.assertIsNotNone(node.entity)
        
        mesh = node.entity
        first_point = mesh.control_points[0]
        self.assertAlmostEqual(first_point.x, 1.0)
        self.assertAlmostEqual(first_point.y, 3.0)
        self.assertAlmostEqual(first_point.z, 2.0)

    def test_scale(self):
        obj_content = """# Test scaling
o TestMesh
v 1.0 1.0 1.0
v 2.0 2.0 2.0
v 3.0 2.0 2.0
f 1 2 3
"""
        scene = Scene()
        stream = io.StringIO(obj_content)
        options = ObjLoadOptions()
        options.scale = 2.0
        
        importer = ObjImporter()
        importer.import_scene(scene, stream, options)
        
        self.assertGreater(len(scene.root_node.child_nodes), 0)
        
        node = scene.root_node.child_nodes[0]
        self.assertIsNotNone(node.entity)
        
        mesh = node.entity
        first_point = mesh.control_points[0]
        self.assertAlmostEqual(first_point.x, 2.0)
        self.assertAlmostEqual(first_point.y, 2.0)
        self.assertAlmostEqual(first_point.z, 2.0)

    def test_smoothing_groups(self):
        obj_content = """# Test smoothing groups
o TestMesh
v 0.0 0.0 0.0
v 1.0 0.0 0.0
v 1.0 1.0 0.0
v 0.0 1.0 0.0
f 1 2 3 4

s 1
v 2.0 0.0 0.0
v 3.0 0.0 0.0
f 5 6 7 8
"""
        scene = Scene()
        stream = io.StringIO(obj_content)
        options = ObjLoadOptions()
        
        importer = ObjImporter()
        importer.import_scene(scene, stream, options)
        
        self.assertGreater(len(scene.root_node.child_nodes), 0)

    def test_disable_materials(self):
        obj_content = """# Test disable materials
o TestMesh
usemtl MyMaterial
v 0.0 0.0 0.0
v 1.0 0.0 0.0
f 1 2 3
"""
        scene = Scene()
        stream = io.StringIO(obj_content)
        options = ObjLoadOptions()
        options.enable_materials = False
        
        importer = ObjImporter()
        importer.import_scene(scene, stream, options)
        
        if len(scene.root_node.child_nodes) > 0:
            node = scene.root_node.child_nodes[0]
            self.assertIsNone(node.material)
        else:
            self.fail("No child nodes created")

    def test_obj_format_detection(self):
        obj_format = ObjFormat()
        self.assertTrue(obj_format.can_import)
        self.assertFalse(obj_format.can_export)
        self.assertEqual(obj_format.extension, "obj")
        self.assertIn("obj", obj_format.extensions)

    def test_load_options_properties(self):
        options = ObjLoadOptions()
        
        self.assertFalse(options.flip_coordinate_system)
        self.assertTrue(options.enable_materials)
        self.assertAlmostEqual(options.scale, 1.0)
        self.assertTrue(options.normalize_normal)
        
        options.flip_coordinate_system = True
        options.enable_materials = False
        options.scale = 2.5
        options.normalize_normal = False
        
        self.assertTrue(options.flip_coordinate_system)
        self.assertFalse(options.enable_materials)
        self.assertAlmostEqual(options.scale, 2.5)
        self.assertFalse(options.normalize_normal)


if __name__ == '__main__':
    unittest.main()
