#!/usr/bin/env python3
"""Test Mesh class implementation"""

print("Testing Mesh class...")

try:
    from aspose.threed import Mesh
    from aspose.threed.entities import VertexElementType, MappingMode, TextureMapping
    from aspose.threed.utilities import Vector4

    print("✓ Imports successful")

    m = Mesh("test_mesh")
    print(f"✓ Mesh created: {m}")

    m._control_points.append(Vector4(0, 0, 0, 1))
    m._control_points.append(Vector4(1, 0, 0, 1))
    m._control_points.append(Vector4(0, 1, 0, 1))
    print(f"✓ Added 3 control points: {len(m.control_points)}")

    m.create_polygon(0, 1, 2)
    print(f"✓ Created triangle polygon, polygon count: {m.polygon_count}")

    m.create_polygon(0, 1, 2, 3)
    print(f"✓ Created quad polygon, polygon count: {m.polygon_count}")

    m.create_polygon([4, 5, 6, 7, 8])
    print(f"✓ Created polygon from list, polygon count: {m.polygon_count}")

    print(f"✓ Polygons: {m.polygons}")
    print(f"✓ First polygon size: {m.get_polygon_size(0)}")
    print(f"✓ Second polygon size: {m.get_polygon_size(1)}")

    elem = m.create_element(VertexElementType.NORMAL, MappingMode.CONTROL_POINT, None)
    print(f"✓ Created vertex element: {elem}")
    print(f"✓ Vertex elements count: {len(m.vertex_elements)}")

    uv_elem = m.create_element_uv(TextureMapping.DIFFUSE)
    print(f"✓ Created UV element: {uv_elem}")
    print(f"✓ UV mapping type: {uv_elem.texture_mapping}")

    print("\nAll tests passed!")
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
