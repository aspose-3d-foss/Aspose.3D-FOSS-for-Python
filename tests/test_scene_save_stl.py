import unittest
import io
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from aspose.threed import Scene, Node
from aspose.threed.entities import Mesh
from aspose.threed.utilities import Vector4
from aspose.threed.formats.stl import StlFormat


class TestSceneSaveSTL(unittest.TestCase):
    def test_scene_save_to_file_ascii(self):
        scene = Scene()
        mesh = Mesh("test_mesh")
        mesh._control_points = [
            Vector4(0.0, 0.0, 0.0, 1.0),
            Vector4(1.0, 0.0, 0.0, 1.0),
            Vector4(1.0, 1.0, 0.0, 1.0),
            Vector4(0.0, 1.0, 0.0, 1.0),
        ]
        mesh.create_polygon(0, 1, 2)
        mesh.create_polygon(0, 2, 3)
        
        node = Node("test_node")
        node.entity = mesh
        node.parent_node = scene.root_node
        
        scene.save('/tmp/test_ascii.stl')
        
        with open('/tmp/test_ascii.stl', 'r') as f:
            content = f.read()
            self.assertIn("solid", content)
            self.assertIn("endsolid", content)
            
    def test_scene_save_to_file_binary(self):
        from aspose.threed.formats.stl import StlSaveOptions, StlFormat
        
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
        
        stl_format = StlFormat()
        options = stl_format.create_save_options()
        options.binary_mode = True
        
        scene.save('/tmp/test_binary.stl', options)
        
        with open('/tmp/test_binary.stl', 'rb') as f:
            content = f.read()
            self.assertEqual(len(content), 84 + 50)
            
    def test_scene_save_with_format(self):
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
        
        stl_format = StlFormat()
        scene.save('/tmp/test_with_format.stl', stl_format)
        
        with open('/tmp/test_with_format.stl', 'r') as f:
            content = f.read()
            self.assertIn("solid", content)
            
    def test_roundtrip_file(self):
        scene1 = Scene()
        mesh1 = Mesh("original")
        mesh1._control_points = [
            Vector4(0.0, 0.0, 0.0, 1.0),
            Vector4(1.0, 0.0, 0.0, 1.0),
            Vector4(1.0, 1.0, 0.0, 1.0),
        ]
        mesh1.create_polygon(0, 1, 2)
        
        node1 = Node("original_node")
        node1.entity = mesh1
        node1.parent_node = scene1.root_node
        
        scene1.save('/tmp/test_roundtrip.stl')
        
        scene2 = Scene.from_file('/tmp/test_roundtrip.stl')
        
        self.assertEqual(len(scene2.root_node.child_nodes), 1)
        node2 = scene2.root_node.child_nodes[0]
        mesh2 = node2.entity
        self.assertEqual(mesh2.polygon_count, 1)


if __name__ == '__main__':
    unittest.main()
