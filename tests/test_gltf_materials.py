import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from aspose.threed import Scene
from aspose.threed.formats.gltf import GltfLoadOptions
from aspose.threed.shading import PbrMaterial


class TestGltfMaterialImport(unittest.TestCase):
    def test_material_import_from_boombox(self):
        scene = Scene()
        options = GltfLoadOptions()
        scene.open('examples/gltf2/BoomBox/glTF/BoomBox.gltf', options)

        self.assertEqual(len(scene.root_node.child_nodes), 1)

        node = scene.root_node.child_nodes[0]
        self.assertIsNotNone(node.material)
        self.assertIsInstance(node.material, PbrMaterial)

        material = node.material
        self.assertEqual(material.name, 'BoomBox_Mat')

        from aspose.threed.utilities import Vector3
        self.assertEqual(material.albedo, Vector3(1.0, 1.0, 1.0))
        self.assertEqual(material.metallic_factor, 0.0)
        self.assertEqual(material.roughness_factor, 1.0)
        self.assertEqual(material.transparency, 0.0)

    def test_material_properties_from_corset(self):
        scene = Scene()
        options = GltfLoadOptions()
        scene.open('examples/gltf2/Corset/glTF/Corset.gltf', options)

        node = scene.root_node.child_nodes[0]
        if node and node.material:
            material = node.material
            self.assertIsInstance(material, PbrMaterial)
            self.assertEqual(material.name, 'Corset_O')

            from aspose.threed.utilities import Vector3
            self.assertEqual(material.metallic_factor, 0.0)
            self.assertEqual(material.roughness_factor, 1.0)

    def test_pbr_material_creation(self):
        from aspose.threed.shading import PbrMaterial
        from aspose.threed.utilities import Vector3

        albedo = Vector3(0.5, 0.6, 0.7)
        material = PbrMaterial('TestMaterial', albedo)

        self.assertEqual(material.name, 'TestMaterial')
        self.assertEqual(material.albedo, albedo)
        self.assertEqual(material.metallic_factor, 0.0)
        self.assertEqual(material.roughness_factor, 0.0)
        self.assertEqual(material.transparency, 0.0)

    def test_material_property_setters(self):
        from aspose.threed.shading import PbrMaterial
        from aspose.threed.utilities import Vector3

        material = PbrMaterial()

        new_albedo = Vector3(1.0, 0.5, 0.2)
        material.albedo = new_albedo
        self.assertEqual(material.albedo, new_albedo)

        material.metallic_factor = 0.8
        self.assertEqual(material.metallic_factor, 0.8)

        material.roughness_factor = 0.3
        self.assertEqual(material.roughness_factor, 0.3)

        material.transparency = 0.5
        self.assertEqual(material.transparency, 0.5)

        new_emissive = Vector3(0.1, 0.2, 0.3)
        material.emissive_color = new_emissive
        self.assertEqual(material.emissive_color, new_emissive)


if __name__ == '__main__':
    unittest.main()
