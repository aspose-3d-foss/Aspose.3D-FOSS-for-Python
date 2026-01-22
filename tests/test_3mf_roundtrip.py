import unittest
import io
import zipfile
from aspose.threed import Scene, Node
from aspose.threed.formats import ThreeMfLoadOptions, ThreeMfSaveOptions, ThreeMfPlugin
from aspose.threed.entities import Mesh
from aspose.threed.utilities import Vector4


class Test3MFRoundTrip(unittest.TestCase):
    def setUp(self):
        self.plugin = ThreeMfPlugin()

    def test_round_trip_export_import(self):
        scene = Scene()
        load_options = self.plugin.create_load_options()
        save_options = self.plugin.create_save_options()
        
        mesh = Mesh('test_cube')
        
        mesh._control_points.append(Vector4(0, 0, 0, 1))
        mesh._control_points.append(Vector4(1, 0, 0, 1))
        mesh._control_points.append(Vector4(1, 1, 0, 1))
        mesh._control_points.append(Vector4(0, 1, 0, 1))
        mesh._control_points.append(Vector4(0, 0, 1, 1))
        mesh._control_points.append(Vector4(1, 0, 1, 1))
        mesh._control_points.append(Vector4(1, 1, 1, 1))
        mesh._control_points.append(Vector4(0, 1, 1, 1))
        
        mesh.create_polygon(0, 1, 2)
        mesh.create_polygon(0, 2, 3)
        mesh.create_polygon(4, 7, 6)
        mesh.create_polygon(4, 6, 5)
        mesh.create_polygon(0, 4, 5)
        mesh.create_polygon(0, 5, 1)
        mesh.create_polygon(2, 6, 7)
        mesh.create_polygon(2, 7, 3)
        mesh.create_polygon(0, 3, 7)
        mesh.create_polygon(0, 7, 4)
        mesh.create_polygon(1, 5, 6)
        mesh.create_polygon(1, 6, 2)
        
        node = Node('test_cube')
        node.entity = mesh
        node.parent_node = scene.root_node
        
        original_vertices = len(mesh._control_points)
        original_polygons = mesh.polygon_count
        
        output_buffer = io.BytesIO()
        scene.save(output_buffer, save_options)
        
        output_buffer.seek(0)
        
        new_scene = Scene()
        new_scene.open(output_buffer, load_options)
        
        self.assertGreater(len(new_scene.root_node.child_nodes), 0)
        
        new_mesh = new_scene.root_node.child_nodes[0].entity
        self.assertIsInstance(new_mesh, Mesh)
        
        self.assertEqual(len(new_mesh.control_points), original_vertices)
        self.assertEqual(new_mesh.polygon_count, original_polygons)


if __name__ == '__main__':
    unittest.main()
