import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from aspose.threed.formats import IOService
from aspose.threed.formats.obj import ObjPlugin
from aspose.threed.formats.stl import StlPlugin


class TestPluginSystem(unittest.TestCase):
    def test_plugin_registration(self):
        io_service = IOService()
        self.assertEqual(len(io_service._plugins), 4)

        obj_plugin = io_service.get_plugin_for_extension('.obj')
        stl_plugin = io_service.get_plugin_for_extension('.stl')
        gltf_plugin = io_service.get_plugin_for_extension('.gltf')
        threemf_plugin = io_service.get_plugin_for_extension('.3mf')

        self.assertIsNotNone(obj_plugin)
        self.assertIsNotNone(stl_plugin)
        self.assertIsNotNone(gltf_plugin)
        self.assertIsNotNone(threemf_plugin)
        
    def test_get_plugin_by_format(self):
        from aspose.threed.formats.obj import ObjFormat
        from aspose.threed.formats.stl import StlFormat

        io_service = IOService()
        obj_fmt = ObjFormat()
        stl_fmt = StlFormat()
        threemf_fmt = io_service.get_plugin_for_extension('.3mf').get_file_format()

        obj_plugin = io_service.get_plugin_for_format(obj_fmt)
        stl_plugin = io_service.get_plugin_for_format(stl_fmt)
        threemf_plugin = io_service.get_plugin_for_format(threemf_fmt)
        
        obj_plugin_class = type(obj_plugin)
        stl_plugin_class = type(stl_plugin)
        threemf_plugin_class = type(threemf_plugin)
        
        self.assertIsInstance(obj_plugin, obj_plugin_class)
        self.assertIsInstance(stl_plugin, stl_plugin_class)
        self.assertIsInstance(threemf_plugin, threemf_plugin_class)
        
    def test_get_plugin_by_extension(self):
        io_service = IOService()
        obj_plugin = io_service.get_plugin_for_extension('.obj')
        stl_plugin = io_service.get_plugin_for_extension('.stl')
        
        obj_plugin_class = type(obj_plugin)
        stl_plugin_class = type(stl_plugin)
        
        self.assertIsInstance(obj_plugin, obj_plugin_class)
        self.assertIsInstance(stl_plugin, stl_plugin_class)
        
    def test_get_plugin_by_extension_case_insensitive(self):
        io_service = IOService()
        obj_plugin1 = io_service.get_plugin_for_extension('.obj')
        obj_plugin2 = io_service.get_plugin_for_extension('.OBJ')
        obj_plugin3 = io_service.get_plugin_for_extension('.Obj')
        
        self.assertIs(obj_plugin1, obj_plugin2)
        self.assertIs(obj_plugin1, obj_plugin3)
        
    def test_plugin_creates_load_options(self):
        io_service = IOService()
        obj_plugin = io_service.get_plugin_for_extension('.obj')
        stl_plugin = io_service.get_plugin_for_extension('.stl')
        
        from aspose.threed.formats.obj import ObjLoadOptions
        from aspose.threed.formats.stl import StlLoadOptions
        
        obj_load_opts = obj_plugin.create_load_options()
        stl_load_opts = stl_plugin.create_load_options()
        
        self.assertIsInstance(obj_load_opts, ObjLoadOptions)
        self.assertIsInstance(stl_load_opts, StlLoadOptions)
        
    def test_plugin_creates_save_options(self):
        io_service = IOService()
        obj_plugin = io_service.get_plugin_for_extension('.obj')
        stl_plugin = io_service.get_plugin_for_extension('.stl')
        
        from aspose.threed.formats.obj import ObjSaveOptions
        from aspose.threed.formats.stl import StlSaveOptions
        
        obj_save_opts = obj_plugin.create_save_options()
        stl_save_opts = stl_plugin.create_save_options()
        
        self.assertIsInstance(obj_save_opts, ObjSaveOptions)
        self.assertIsInstance(stl_save_opts, StlSaveOptions)
        
    def test_plugin_registers_components(self):
        io_service = IOService()
        
        obj_plugin = io_service.get_plugin_for_extension('.obj')
        stl_plugin = io_service.get_plugin_for_extension('.stl')
        
        obj_importer = obj_plugin.get_importer()
        obj_exporter = obj_plugin.get_exporter()
        obj_detector = obj_plugin.get_format_detector()
        
        stl_importer = stl_plugin.get_importer()
        stl_exporter = stl_plugin.get_exporter()
        stl_detector = stl_plugin.get_format_detector()
        
        self.assertIn(obj_importer, io_service._importers)
        self.assertIn(obj_exporter, io_service._exporters)
        self.assertIn(obj_detector, io_service._detectors)
        
        self.assertIn(stl_importer, io_service._importers)
        self.assertIn(stl_exporter, io_service._exporters)
        self.assertIn(stl_detector, io_service._detectors)
        
    def test_plugin_singleton(self):
        io_service = IOService()
        obj_plugin1 = io_service.get_plugin_for_extension('.obj')
        obj_plugin2 = io_service.get_plugin_for_extension('.obj')
        
        self.assertIs(obj_plugin1, obj_plugin2)
        
        stl_plugin1 = io_service.get_plugin_for_extension('.stl')
        stl_plugin2 = io_service.get_plugin_for_extension('.stl')
        
        self.assertIs(stl_plugin1, stl_plugin2)


if __name__ == '__main__':
    unittest.main()
