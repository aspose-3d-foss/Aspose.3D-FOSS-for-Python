import unittest
import io
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from aspose.threed.formats import Exporter, Importer, FormatDetector, IOService, LoadOptions, SaveOptions
from aspose.threed import FileFormat, Scene


class TestFormats(unittest.TestCase):
    def test_exporter_creation(self):
        exporter = Exporter()
        self.assertIsNotNone(exporter)

    def test_importer_creation(self):
        importer = Importer()
        self.assertIsNotNone(importer)

    def test_format_detector_creation(self):
        detector = FormatDetector()
        self.assertIsNotNone(detector)

    def test_io_service_singleton(self):
        service1 = IOService()
        service2 = IOService()
        self.assertIs(service1, service2)

    def test_load_options_creation(self):
        options = LoadOptions()
        self.assertIsNotNone(options)
        self.assertIsNone(options.encoding)
        self.assertIsNone(options.file_name)
        self.assertEqual(options.lookup_paths, [])

    def test_save_options_creation(self):
        options = SaveOptions()
        self.assertIsNotNone(options)
        self.assertFalse(options.export_textures)

    def test_load_options_properties(self):
        options = LoadOptions()
        options.encoding = 'utf-8'
        options.file_name = 'test.obj'
        options.lookup_paths = ['/path1', '/path2']
        
        self.assertEqual(options.encoding, 'utf-8')
        self.assertEqual(options.file_name, 'test.obj')
        self.assertEqual(options.lookup_paths, ['/path1', '/path2'])

    def test_save_options_properties(self):
        options = SaveOptions()
        options.export_textures = True
        
        self.assertTrue(options.export_textures)

    def test_io_service_registration(self):
        service = IOService()
        exporter = Exporter()
        importer = Importer()
        detector = FormatDetector()
        
        service.register_exporter(exporter)
        service.register_importer(importer)
        service.register_detector(detector)
        
        self.assertIn(exporter, service._exporters)
        self.assertIn(importer, service._importers)
        self.assertIn(detector, service._detectors)

    def test_file_format_create_options(self):
        file_format = FileFormat()
        load_options = file_format.create_load_options()
        save_options = file_format.create_save_options()
        
        self.assertIsInstance(load_options, LoadOptions)
        self.assertIsInstance(save_options, SaveOptions)
        self.assertEqual(load_options.file_format, file_format)
        self.assertEqual(save_options.file_format, file_format)


if __name__ == '__main__':
    unittest.main()
