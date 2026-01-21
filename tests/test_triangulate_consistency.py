#!/usr/bin/env python3
"""Verify PolygonModifier.triangulate(mesh) and Mesh.triangulate() produce same results"""

print("Verifying PolygonModifier and Mesh.triangulate consistency...")

try:
    from aspose.threed import Mesh
    from aspose.threed.entities import PolygonModifier
    from aspose.threed.utilities import Vector4

    print("✓ Imports successful")

    print("\nTest: Quad mesh")
    quad_mesh = Mesh("quad")
    quad_mesh._control_points = [
        Vector4(0, 0, 0, 1),
        Vector4(1, 0, 0, 1),
        Vector4(0, 1, 0, 1),
        Vector4(1, 1, 0, 1)
    ]
    quad_mesh.create_polygon(0, 1, 3, 2)

    result1 = quad_mesh.triangulate()
    result2 = PolygonModifier.triangulate(quad_mesh)

    print(f"Mesh.triangulate(): {result1.polygon_count} polygons, {result1.polygons}")
    print(f"PolygonModifier.triangulate(): {result2.polygon_count} polygons, {result2.polygons}")

    assert result1.polygon_count == result2.polygon_count, "Polygon count mismatch"
    assert result1.polygons == result2.polygons, "Polygon indices mismatch"
    print(f"✓ Results match!")

    print("\nTest: Mixed polygon mesh")
    mixed_mesh = Mesh("mixed")
    mixed_mesh._control_points = [
        Vector4(0, 0, 0, 1),
        Vector4(1, 0, 0, 1),
        Vector4(0, 1, 0, 1),
        Vector4(1, 1, 0, 1),
        Vector4(2, 0, 0, 1),
        Vector4(2, 1, 0, 1)
    ]
    mixed_mesh.create_polygon(0, 1, 2)
    mixed_mesh.create_polygon(1, 3, 2)
    mixed_mesh.create_polygon([1, 3, 5, 4])

    result1 = mixed_mesh.triangulate()
    result2 = PolygonModifier.triangulate(mixed_mesh)

    print(f"Mesh.triangulate(): {result1.polygon_count} polygons")
    print(f"PolygonModifier.triangulate(): {result2.polygon_count} polygons")

    assert result1.polygon_count == result2.polygon_count, "Polygon count mismatch"
    assert result1.polygons == result2.polygons, "Polygon indices mismatch"
    print(f"✓ Results match!")

    print("\nAll tests passed!")
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
