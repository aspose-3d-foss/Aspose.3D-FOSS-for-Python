import unittest
import io
import zipfile
import xml.etree.ElementTree as ET
from aspose.threed import Scene, Node
from aspose.threed.formats import ThreeMfSaveOptions, ThreeMfPlugin
from aspose.threed.entities import Mesh
from aspose.threed.utilities import Vector4


class Test3MFExporter(unittest.TestCase):
    def setUp(self):
        self.plugin = ThreeMfPlugin()
        self.format = self.plugin.get_file_format()

    def test_save_options(self):
        options = self.plugin.create_save_options()
        self.assertIsInstance(options, ThreeMfSaveOptions)
        self.assertTrue(options.enable_compression)
        self.assertTrue(options.build_all)
        self.assertFalse(options.flip_coordinate_system)
        
        options.enable_compression = False
        self.assertFalse(options.enable_compression)
        
        options.flip_coordinate_system = True
        self.assertTrue(options.flip_coordinate_system)

    def test_simple_cube_export(self):
        scene = Scene()
        options = self.plugin.create_save_options()
        options.enable_compression = False
        
        mesh = Mesh('cube')
        
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
        
        node = Node('cube')
        node.entity = mesh
        node.parent_node = scene.root_node
        
        output_buffer = io.BytesIO()
        scene.save(output_buffer, options)
        
        output_buffer.seek(0)
        
        zip_file = zipfile.ZipFile(output_buffer, 'r')
        model_content = zip_file.read('3D/3dmodel.model').decode('utf-8')
        zip_file.close()
        
        root = ET.fromstring(model_content)
        
        self.assertEqual(root.tag, '{http://schemas.microsoft.com/3dmanufacturing/core/2015/02}model')
        self.assertEqual(root.get('unit'), 'millimeter')
        
        resources = root.find('{http://schemas.microsoft.com/3dmanufacturing/core/2015/02}resources')
        self.assertIsNotNone(resources)
        
        obj = resources.find('{http://schemas.microsoft.com/3dmanufacturing/core/2015/02}object')
        self.assertIsNotNone(obj)
        self.assertEqual(obj.get('id'), '1')
        self.assertEqual(obj.get('name'), 'cube')
        self.assertEqual(obj.get('type'), 'model')
        
        mesh_elem = obj.find('{http://schemas.microsoft.com/3dmanufacturing/core/2015/02}mesh')
        self.assertIsNotNone(mesh_elem)
        
        vertices = mesh_elem.find('{http://schemas.microsoft.com/3dmanufacturing/core/2015/02}vertices')
        self.assertIsNotNone(vertices)
        
        vertex_elems = vertices.findall('{http://schemas.microsoft.com/3dmanufacturing/core/2015/02}vertex')
        self.assertEqual(len(vertex_elems), 8)
        
        triangles = mesh_elem.find('{http://schemas.microsoft.com/3dmanufacturing/core/2015/02}triangles')
        self.assertIsNotNone(triangles)
        
        triangle_elems = triangles.findall('{http://schemas.microsoft.com/3dmanufacturing/core/2015/02}triangle')
        self.assertEqual(len(triangle_elems), 12)
        
        build = root.find('{http://schemas.microsoft.com/3dmanufacturing/core/2015/02}build')
        self.assertIsNotNone(build)
        
        item = build.find('{http://schemas.microsoft.com/3dmanufacturing/core/2015/02}item')
        self.assertIsNotNone(item)
        self.assertEqual(item.get('objectid'), '1')


if __name__ == '__main__':
    unittest.main()
