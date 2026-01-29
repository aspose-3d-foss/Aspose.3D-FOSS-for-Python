import unittest
import sys
import os
import io
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from aspose.threed import Scene
from aspose.threed.entities import Mesh
from aspose.threed.utilities import Vector4, Vector3
from aspose.threed.formats import ColladaSaveOptions
from aspose.threed.shading import PhongMaterial, LambertMaterial


class TestColladaExporter(unittest.TestCase):
    def test_simple_triangle_export(self):
        scene = Scene()
        mesh = Mesh('TestMesh')

        mesh._control_points.append(Vector4(0.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(1.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(0.0, 1.0, 0.0, 1.0))
        mesh.create_polygon(0, 1, 2)

        scene.root_node.create_child_node('TestNode').entity = mesh

        stream = io.BytesIO()
        options = ColladaSaveOptions()
        options.file_name = 'test.dae'

        from aspose.threed.formats.collada.ColladaExporter import ColladaExporter
        exporter = ColladaExporter()
        exporter.export(scene, stream, options)

        stream.seek(0)
        content = stream.read().decode('utf-8')

        root = ET.fromstring(content)
        self.assertEqual(root.tag, '{http://www.collada.org/2005/11/COLLADASchema}COLLADA')
        self.assertEqual(root.get('version'), '1.4.1')

        asset = root.find('{http://www.collada.org/2005/11/COLLADASchema}asset')
        self.assertIsNotNone(asset)

        library_geometries = root.find('{http://www.collada.org/2005/11/COLLADASchema}library_geometries')
        self.assertIsNotNone(library_geometries)

        library_visual_scenes = root.find('{http://www.collada.org/2005/11/COLLADASchema}library_visual_scenes')
        self.assertIsNotNone(library_visual_scenes)

    def test_export_with_material(self):
        scene = Scene()
        mesh = Mesh('TestMesh')

        mesh._control_points.append(Vector4(0.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(1.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(0.0, 1.0, 0.0, 1.0))
        mesh.create_polygon(0, 1, 2)

        material = PhongMaterial('RedMaterial')
        material.diffuse_color = Vector3(1.0, 0.0, 0.0)
        material.specular_color = Vector3(1.0, 1.0, 1.0)
        material.shininess = 32.0

        node = scene.root_node.create_child_node('TestNode')
        node.entity = mesh
        node.material = material

        stream = io.BytesIO()
        options = ColladaSaveOptions()
        options.file_name = 'test.dae'

        from aspose.threed.formats.collada.ColladaExporter import ColladaExporter
        exporter = ColladaExporter()
        exporter.export(scene, stream, options)

        stream.seek(0)
        content = stream.read().decode('utf-8')

        root = ET.fromstring(content)

        library_materials = root.find('{http://www.collada.org/2005/11/COLLADASchema}library_materials')
        self.assertIsNotNone(library_materials)

        library_effects = root.find('{http://www.collada.org/2005/11/COLLADASchema}library_effects')
        self.assertIsNotNone(library_effects)

    def test_export_lambert_material(self):
        scene = Scene()
        mesh = Mesh('TestMesh')

        mesh._control_points.append(Vector4(0.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(1.0, 0.0, 0.0, 1.0))
        mesh._control_points.append(Vector4(0.0, 1.0, 0.0, 1.0))
        mesh.create_polygon(0, 1, 2)

        material = LambertMaterial('BlueMaterial')
        material.diffuse_color = Vector3(0.0, 0.0, 1.0)

        node = scene.root_node.create_child_node('TestNode')
        node.entity = mesh
        node.material = material

        stream = io.BytesIO()
        options = ColladaSaveOptions()
        options.file_name = 'test.dae'

        from aspose.threed.formats.collada.ColladaExporter import ColladaExporter
        exporter = ColladaExporter()
        exporter.export(scene, stream, options)

        stream.seek(0)
        content = stream.read().decode('utf-8')

        root = ET.fromstring(content)

        library_effects = root.find('{http://www.collada.org/2005/11/COLLADASchema}library_effects')
        self.assertIsNotNone(library_effects)

        effect = library_effects.find('{http://www.collada.org/2005/11/COLLADASchema}effect')
        self.assertIsNotNone(effect)

        profile_common = effect.find('{http://www.collada.org/2005/11/COLLADASchema}profile_COMMON')
        self.assertIsNotNone(profile_common)

        technique = profile_common.find('{http://www.collada.org/2005/11/COLLADASchema}technique')
        self.assertIsNotNone(technique)

        lambert = technique.find('{http://www.collada.org/2005/11/COLLADASchema}lambert')
        self.assertIsNotNone(lambert)

    def test_collada_save_options(self):
        options = ColladaSaveOptions()

        self.assertEqual(options.flip_coordinate_system, False)
        self.assertEqual(options.enable_materials, True)
        self.assertEqual(options.indented, True)

        options.flip_coordinate_system = True
        self.assertEqual(options.flip_coordinate_system, True)

        options.indented = False
        self.assertEqual(options.indented, False)

    def test_collada_format_can_export(self):
        from aspose.threed.formats.collada.ColladaFormat import ColladaFormat

        collada_format = ColladaFormat()
        self.assertTrue(collada_format.can_export)


if __name__ == '__main__':
    unittest.main()
