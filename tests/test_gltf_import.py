import unittest
import sys
import os
import io

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from aspose.threed import Scene
from aspose.threed.formats.gltf import GltfLoadOptions


class TestGltfImport(unittest.TestCase):
    def test_gltf_load_options(self):
        options = GltfLoadOptions()
        self.assertIsNotNone(options)
        self.assertTrue(options.flip_tex_coord_v)

    def test_gltf_load_options_flip_property(self):
        options = GltfLoadOptions()
        options.flip_tex_coord_v = False
        self.assertFalse(options.flip_tex_coord_v)

    def test_gltf_format_detection(self):
        from aspose.threed import FileFormat

        gltf_format = FileFormat.get_format_by_extension('.gltf')
        self.assertIsNotNone(gltf_format)
        self.assertEqual(gltf_format.extension, 'gltf')

        glb_format = FileFormat.get_format_by_extension('.glb')
        self.assertIsNotNone(glb_format)

    def test_gltf_format_properties(self):
        from aspose.threed.formats.gltf import GltfFormat

        gltf_format = GltfFormat()
        self.assertTrue(gltf_format.can_import)
        self.assertTrue(gltf_format.can_export)
        self.assertEqual(gltf_format.version, '2.0')
        self.assertIn('gltf', gltf_format.extensions)
        self.assertIn('glb', gltf_format.extensions)

    def test_gltf_plugin_registered(self):
        from aspose.threed.formats import IOService
        from aspose.threed.formats.gltf import GltfPlugin

        io_service = IOService()
        gltf_plugin = io_service.get_plugin_for_extension('.gltf')
        self.assertIsNotNone(gltf_plugin)
        self.assertIsInstance(gltf_plugin, GltfPlugin)


if __name__ == '__main__':
    unittest.main()
