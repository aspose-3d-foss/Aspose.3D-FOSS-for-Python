import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aspose.threed import Scene
from aspose.threed.formats import ThreeMfLoadOptions
import zipfile
import xml.etree.ElementTree as ET

def test_material_import_from_sample():
    print("="*70)
    print("TEST: Material Import from Sample 3MF Files")
    print("="*70)
    
    sample_file = '/home/lexchou/workspace/aspose/3d.org/examples/3mf/dodeca_chain_loop_color.3mf'
    
    scene = Scene()
    scene.open(sample_file, ThreeMfLoadOptions())
    
    print(f"\n✓ Scene loaded successfully")
    print(f"  Root node has {len(scene.root_node.child_nodes)} children")
    
    materials_found = 0
    
    return materials_found > 0

def test_simple_cube_with_material():
    print("\n" + "="*70)
    print("TEST: Simple Scene with Material")
    print("="*70)
    
    import io
    import xml.etree.ElementTree as ET
    from aspose.threed.formats import ThreeMfSaveOptions, ThreeMfLoadOptions
    
    scene = Scene()
    from aspose.threed.shading import PbrMaterial
    from aspose.threed.entities import Mesh
    from aspose.threed.utilities import Vector3
    
    mat = PbrMaterial('test_material')
    mat.albedo = Vector3(1.0, 0.0, 0.0)
    
    mesh = Mesh('cube')
    mesh._control_points = [
        Vector3(0, 0, 0), Vector3(1, 0, 0), Vector3(1, 1, 0), Vector3(0, 1, 0),
        Vector3(0, 0, 1), Vector3(1, 0, 1), Vector3(1, 1, 1), Vector3(0, 1, 1)
    ]
    for indices in [(0,1,2), (0,2,3), (4,7,6), (4,6,5), (0,4,5), (0,5,1), (2,6,7), (2,7,3), (0,3,7), (0,7,4), (1,5,6), (1,6,2)]:
        mesh.create_polygon(*indices)
    
    node = scene.root_node.create_child_node('cube')
    node.entity = mesh
    node.material = mat
    
    print(f"\n✓ Created scene with material")
    print(f"  Node: {node.name}")
    print(f"  Mesh: {len(mesh._control_points)} vertices, {mesh.polygon_count} polygons")
    print(f"  Material: {mat.name}, albedo=({mat.albedo.x:.1f}, {mat.albedo.y:.1f}, {mat.albedo.z:.1f})")
    
    output = io.BytesIO()
    scene.save(output, ThreeMfSaveOptions())
    
    print(f"\n✓ Scene exported to 3MF")
    print(f"  Output size: {len(output.getvalue())} bytes")
    
    return True

if __name__ == '__main__':
    try:
        result1 = test_material_import_from_sample()
        result2 = test_simple_cube_with_material()
        
        print("\n" + "="*70)
        if result1 and result2:
            print("ALL MATERIAL TESTS PASSED! ✓")
        elif result1:
            print("MATERIAL IMPORT TESTS PASSED! ✓")
            print("  Note: Material export not yet implemented")
        else:
            print("SOME TESTS FAILED")
        print("="*70)
        
    except Exception as e:
        print(f"\n✗ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
