import unittest
import io
import zipfile
import xml.etree.ElementTree as ET
from aspose.threed import Scene, Node
from aspose.threed.formats import ThreeMfLoadOptions, ThreeMfPlugin
from aspose.threed.entities import Mesh
from aspose.threed.utilities import Vector4, Matrix4


class Test3MFImporter(unittest.TestCase):
    def setUp(self):
        self.plugin = ThreeMfPlugin()
        self.format = self.plugin.get_file_format()

    def test_format_detection(self):
        self.assertEqual(self.format.extension, '3mf')
        self.assertIn('3mf', self.format.extensions)
        self.assertTrue(self.format.can_import)
        self.assertTrue(self.format.can_export)

    def test_load_options(self):
        options = self.plugin.create_load_options()
        self.assertIsInstance(options, ThreeMfLoadOptions)
        self.assertFalse(options.flip_coordinate_system)
        
        options.flip_coordinate_system = True
        self.assertTrue(options.flip_coordinate_system)

    def test_simple_cube_import(self):
        scene = Scene()
        options = self.plugin.create_load_options()
        
        model_content = '''<?xml version="1.0" encoding="UTF-8"?>
<model unit="millimeter" xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02">
  <resources>
    <object id="1" name="cube">
      <mesh>
        <vertices>
          <vertex x="0" y="0" z="0"/>
          <vertex x="10" y="0" z="0"/>
          <vertex x="10" y="10" z="0"/>
          <vertex x="0" y="10" z="0"/>
          <vertex x="0" y="0" z="10"/>
          <vertex x="10" y="0" z="10"/>
          <vertex x="10" y="10" z="10"/>
          <vertex x="0" y="10" z="10"/>
        </vertices>
        <triangles>
          <triangle v1="0" v2="1" v3="2"/>
          <triangle v1="0" v2="2" v3="3"/>
          <triangle v1="4" v2="7" v3="6"/>
          <triangle v1="4" v2="6" v3="5"/>
          <triangle v1="0" v2="4" v3="5"/>
          <triangle v1="0" v2="5" v3="1"/>
          <triangle v1="2" v2="6" v3="7"/>
          <triangle v1="2" v2="7" v3="3"/>
          <triangle v1="0" v2="3" v3="7"/>
          <triangle v1="0" v2="7" v3="4"/>
          <triangle v1="1" v2="5" v3="6"/>
          <triangle v1="1" v2="6" v3="2"/>
        </triangles>
      </mesh>
    </object>
  </resources>
  <build>
    <item objectid="1"/>
  </build>
</model>'''
        
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
            zf.writestr('3D/3dmodel.model', model_content)
        
        zip_buffer.seek(0)
        scene.open(zip_buffer, options)
        
        self.assertGreater(len(scene.root_node.child_nodes), 0)
        child_node = scene.root_node.child_nodes[0]
        self.assertIsInstance(child_node.entity, Mesh)
        mesh = child_node.entity
        self.assertEqual(len(mesh.control_points), 8)


if __name__ == '__main__':
    unittest.main()
