#!/usr/bin/env python3
"""Test ear-clipping algorithm with concave polygon"""

print("Testing ear-clipping with concave polygon...")

try:
    from aspose.threed import Mesh
    from aspose.threed.entities import PolygonModifier
    from aspose.threed.utilities import Vector4, Vector3

    print("✓ Imports successful")

    print("\nTest 1: Concave polygon (arrow shape)")
    concave_mesh = Mesh("concave")
    concave_mesh._control_points = [
        Vector4(0, 0, 0, 1),      # 0: bottom left
        Vector4(2, 0, 0, 1),      # 1: bottom right
        Vector4(2, 1, 0, 1),      # 2: right middle
        Vector4(1, 1, 0, 1),      # 3: indentation (concave)
        Vector4(1, 2, 0, 1),      # 4: top
        Vector4(0, 2, 0, 1),      # 5: top left
    ]
    concave_mesh.create_polygon([0, 1, 2, 3, 4, 5])
    print(f"✓ Created concave mesh: {concave_mesh.polygon_count} polygons")

    triangulated = concave_mesh.triangulate()
    print(f"✓ Triangulated mesh: {triangulated.polygon_count} polygons")
    print(f"✓ Polygons: {triangulated.polygons}")

    print("\nTest 2: Star shape (highly concave)")
    star_mesh = Mesh("star")
    star_mesh._control_points = [
        Vector4(0, 1, 0, 1),      # 0: top
        Vector4(0.3, 0.3, 0, 1),  # 1: upper right inner
        Vector4(1, 0.3, 0, 1),    # 2: right
        Vector4(0.4, -0.1, 0, 1), # 3: lower right inner
        Vector4(0.5, -0.6, 0, 1), # 4: bottom
        Vector4(0.2, -0.2, 0, 1), # 5: lower left inner
        Vector4(-0.5, -0.6, 0, 1),# 6: bottom left
        Vector4(-0.1, -0.1, 0, 1), # 7: lower middle inner
        Vector4(-1, 0.3, 0, 1),    # 8: left
        Vector4(-0.3, 0.3, 0, 1),  # 9: upper left inner
    ]
    star_mesh.create_polygon([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(f"✓ Created star mesh: {star_mesh.polygon_count} polygons")

    triangulated = star_mesh.triangulate()
    print(f"✓ Triangulated mesh: {triangulated.polygon_count} polygons")
    assert triangulated.polygon_count == 8, f"Expected 8 triangles, got {triangulated.polygon_count}"
    print(f"✓ Polygons: {triangulated.polygons}")

    print("\nTest 3: Verify vertex elements are copied")
    test_mesh = Mesh("test")
    test_mesh._control_points = [
        Vector4(0, 0, 0, 1),
        Vector4(1, 0, 0, 1),
        Vector4(0, 1, 0, 1),
        Vector4(1, 1, 0, 1),
    ]
    test_mesh.create_polygon(0, 1, 3, 2)

    from aspose.threed.entities import VertexElementType, MappingMode, ReferenceMode
    normal_elem = test_mesh.create_element(VertexElementType.NORMAL, MappingMode.CONTROL_POINT, None)
    print(f"✓ Added normal element to source mesh")

    triangulated = test_mesh.triangulate()
    print(f"✓ Triangulated mesh: {triangulated.polygon_count} polygons")

    has_normals = False
    for ve in triangulated.vertex_elements:
        if ve.vertex_element_type == VertexElementType.NORMAL:
            has_normals = True
            print(f"✓ Normal element copied to triangulated mesh")
            break

    assert has_normals, "Normal element should be copied to triangulated mesh"

    print("\nAll tests passed!")
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
