import unittest
import sys
import os
import glob

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from aspose.threed import Scene
from aspose.threed.formats import ColladaLoadOptions


class TestColladaImporterMultipleFiles(unittest.TestCase):
    def test_import_multiple_files(self):
        options = ColladaLoadOptions()
        
        examples_dir = os.path.join(os.path.dirname(__file__), '..', 'examples', 'collada')
        
        if os.path.exists(examples_dir):
            dae_files = glob.glob(os.path.join(examples_dir, '*.dae'))[:5]
            
            for dae_file in dae_files:
                try:
                    scene = Scene()
                    scene.open(dae_file, options)
                    
                    self.assertIsNotNone(scene.root_node)
                    self.assertTrue(len(scene.root_node.child_nodes) > 0 or 
                                  len(scene.root_node._entities) > 0,
                                  f"No nodes or entities found in {os.path.basename(dae_file)}")
                except Exception as e:
                    self.fail(f"Failed to import {os.path.basename(dae_file)}: {str(e)}")
        else:
            self.skipTest(f"Examples directory not found: {examples_dir}")


if __name__ == '__main__':
    unittest.main()
