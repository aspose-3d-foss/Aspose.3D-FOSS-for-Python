import unittest
import io
import zipfile
from aspose.threed import Scene
from aspose.threed.formats import ThreeMfPlugin

class Test3MFMaterialImport(unittest.TestCase):
    def setUp(self):
        self.plugin = ThreeMfPlugin()
        self.format = self.plugin.get_file_format()

    def test_material_import(self):
        scene = Scene()
        options = self.plugin.create_load_options()
        
        model_content = '''<?xml version="1.0" encoding="UTF-8"?>
<model unit="millimeter" xmlns="http://schemas.microsoft.com/3dmanufacturing/2013/01">
  <resources>
    <color id="0" value="#FFFFFF" />
    <color id="1" value="#FF0000" />
    <color id="2" value="#0000FF" />
    <material id="3" colorid="0" />
    <material id="4" colorid="1" />
    <material id="5" colorid="2" />
    <object id="1" name="white_cube" materialid="3">
      <mesh>
        <vertices>
          <vertex x="0" y="0" z="0"/>
          <vertex x="10" y="0" z="0"/>
          <vertex x="10" y="10" z="0"/>
          <vertex x="0" y="10" z="0"/>
          <vertex x="0" y="0" z="10"/>
          <vertex x="0" y="10" z="10"/>
          <vertex x="10" y="10" z="10"/>
          <vertex x="10" y="0" z="10"/>
          <vertex x="0" y="0" z="10"/>
        </vertices>
        <triangles>
          <triangle v1="0" v2="1" v3="2" materialid="3"/>
          <triangle v1="0" v2="2" v3="3" materialid="3"/>
          <triangle v1="0" v2="3" v3="4" materialid="3"/>
          <triangle v1="0" v2="4" v3="5" materialid="3"/>
          <triangle v1="0" v2="5" v3="6" materialid="3"/>
          <triangle v1="0" v2="6" v3="7" materialid="3"/>
          <triangle v1="0" v2="7" v3="3" materialid="3"/>
          <triangle v1="0" v2="7" v3="1" materialid="3"/>
        </triangles>
      </mesh>
    </object>
    <object id="2" name="red_cube" materialid="4">
      <mesh>
        <vertices>
          <vertex x="10" y="0" z="0"/>
          <vertex x="20" y="0" z="0"/>
          <vertex x="20" y="10" z="0"/>
          <vertex x="10" y="10" z="0"/>
          <vertex x="10" y="0" z="10"/>
          <vertex x="10" y="10" z="10"/>
          <vertex x="20" y="10" z="10"/>
          <vertex x="20" y="0" z="10"/>
        </vertices>
        <triangles>
          <triangle v1="0" v2="1" v3="2" />
          <triangle v1="0" v2="2" v3="3" />
          <triangle v1="0" v2="3" v3="4" />
          <triangle v1="0" v2="4" v3="5" />
          <triangle v1="0" v2="5" v3="6" />
          <triangle v1="0" v2="6" v3="7" />
          <triangle v1="0" v2="7" v3="1" />
          <triangle v1="0" v2="7" v3="2" />
          <triangle v1="0" v2="7" v3="3" />
        </triangles>
      </mesh>
    </object>
    <object id="3" name="blue_cube">
      <mesh>
        <vertices>
          <vertex x="0" y="0" z="20"/>
          <vertex x="10" y="0" z="20"/>
          <vertex x="10" y="10" z="20"/>
          <vertex x="0" y="10" z="20"/>
        </vertices>
        <triangles>
          <triangle v1="0" v2="1" v3="2" materialid="5"/>
          <triangle v1="0" v2="2" v3="3" materialid="5"/>
          <triangle v1="0" v2="3" v3="0" materialid="5"/>
          <triangle v1="0" v2="3" v3="1" materialid="5"/>
        </triangles>
      </mesh>
    </object>
  </resources>
  <build>
    <item objectid="1"/>
    <item objectid="2"/>
    <item objectid="3"/>
  </build>
</model>'''
        
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
            zf.writestr('3D/3dmodel.model', model_content)
        
        zip_buffer.seek(0)
        scene.open(zip_buffer, options)
        
        self.assertEqual(len(scene.root_node.child_nodes), 3)
        
        white_cube_node = scene.root_node.child_nodes[0]
        self.assertEqual(white_cube_node.name, 'white_cube')
        self.assertIsNotNone(white_cube_node.material)
        self.assertEqual(white_cube_node.material.diffuse_color.x, 1.0)
        self.assertEqual(white_cube_node.material.diffuse_color.y, 1.0)
        self.assertEqual(white_cube_node.material.diffuse_color.z, 1.0)
        
        red_cube_node = scene.root_node.child_nodes[1]
        self.assertEqual(red_cube_node.name, 'red_cube')
        self.assertIsNotNone(red_cube_node.material)
        self.assertEqual(red_cube_node.material.diffuse_color.x, 1.0)
        self.assertEqual(red_cube_node.material.diffuse_color.y, 0.0)
        self.assertEqual(red_cube_node.material.diffuse_color.z, 0.0)
        
        blue_cube_node = scene.root_node.child_nodes[2]
        self.assertEqual(blue_cube_node.name, 'blue_cube')
        self.assertIsNotNone(blue_cube_node.material)
        self.assertEqual(blue_cube_node.material.diffuse_color.x, 0.0)
        self.assertEqual(blue_cube_node.material.diffuse_color.y, 0.0)
        self.assertEqual(blue_cube_node.material.diffuse_color.z, 1.0)

    def test_per_triangle_materials(self):
        scene = Scene()
        options = self.plugin.create_load_options()
        
        model_content = '''<?xml version="1.0" encoding="UTF-8"?>
<model unit="millimeter" xmlns="http://schemas.microsoft.com/3dmanufacturing/2013/01">
  <resources>
    <color id="0" value="#FFFFFF" />
    <color id="1" value="#FF0000" />
    <object id="1" name="multicolor_cube">
      <mesh>
        <vertices>
          <vertex x="0" y="0" z="0"/>
          <vertex x="10" y="0" z="0"/>
          <vertex x="10" y="10" z="0"/>
          <vertex x="0" y="10" z="0"/>
        </vertices>
        <triangles>
          <triangle v1="0" v2="1" v3="2" materialid="0"/>
          <triangle v1="0" v2="2" v3="3" materialid="1"/>
          <triangle v1="0" v2="3" v3="0" materialid="0"/>
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
        
        self.assertEqual(len(scene.root_node.child_nodes), 1)
        multicolor_cube_node = scene.root_node.child_nodes[0]
        self.assertEqual(multicolor_cube_node.name, 'multicolor_cube')
        
        mesh = multicolor_cube_node.entity
        from aspose.threed.entities import VertexElementVertexColor
        vertex_color_element = None
        for elem in mesh._vertex_elements:
            if isinstance(elem, VertexElementVertexColor):
                vertex_color_element = elem
                break
        
        self.assertIsNotNone(vertex_color_element)
        colors = vertex_color_element.data
        self.assertEqual(len(colors), 3)
        
        self.assertEqual(colors[0].x, 1.0)
        self.assertEqual(colors[0].y, 1.0)
        self.assertEqual(colors[0].z, 1.0)
        
        self.assertEqual(colors[1].x, 1.0)
        self.assertEqual(colors[1].y, 0.0)
        self.assertEqual(colors[1].z, 0.0)
        
        self.assertEqual(colors[2].x, 1.0)
        self.assertEqual(colors[2].y, 1.0)
        self.assertEqual(colors[2].z, 1.0)


if __name__ == '__main__':
    unittest.main()
