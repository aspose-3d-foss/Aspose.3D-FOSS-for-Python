#!/usr/bin/env python3
"""Test Mesh.triangulate method"""

print("Testing Mesh.triangulate method...")

try:
    from aspose.threed import Mesh
    from aspose.threed.utilities import Vector4

    print("✓ Imports successful")

    print("\nTest 1: Triangle mesh (already triangulated)")
    triangle_mesh = Mesh("triangle")
    triangle_mesh._control_points = [
        Vector4(0, 0, 0, 1),
        Vector4(1, 0, 0, 1),
        Vector4(0, 1, 0, 1)
    ]
    triangle_mesh.create_polygon(0, 1, 2)
    print(f"✓ Created triangle mesh: {triangle_mesh.polygon_count} polygons")

    triangulated = triangle_mesh.triangulate()
    print(f"✓ Triangulated mesh: {triangulated.polygon_count} polygons")
    assert triangulated.polygon_count == 1, f"Expected 1 triangle, got {triangulated.polygon_count}"
    print(f"✓ Polygons: {triangulated.polygons}")

    print("\nTest 2: Quad mesh")
    quad_mesh = Mesh("quad")
    quad_mesh._control_points = [
        Vector4(0, 0, 0, 1),
        Vector4(1, 0, 0, 1),
        Vector4(0, 1, 0, 1),
        Vector4(1, 1, 0, 1)
    ]
    quad_mesh.create_polygon(0, 1, 3, 2)
    print(f"✓ Created quad mesh: {quad_mesh.polygon_count} polygons")

    triangulated = quad_mesh.triangulate()
    print(f"✓ Triangulated mesh: {triangulated.polygon_count} polygons")
    assert triangulated.polygon_count == 2, f"Expected 2 triangles, got {triangulated.polygon_count}"
    print(f"✓ Polygons: {triangulated.polygons}")

    print("\nTest 3: Pentagon mesh")
    pent_mesh = Mesh("pentagon")
    pent_mesh._control_points = [
        Vector4(0, 0, 0, 1),
        Vector4(1, 0, 0, 1),
        Vector4(1.5, 0.5, 0, 1),
        Vector4(1, 1, 0, 1),
        Vector4(0, 1, 0, 1)
    ]
    pent_mesh.create_polygon([0, 1, 2, 3, 4])
    print(f"✓ Created pentagon mesh: {pent_mesh.polygon_count} polygons")

    triangulated = pent_mesh.triangulate()
    print(f"✓ Triangulated mesh: {triangulated.polygon_count} polygons")
    assert triangulated.polygon_count == 3, f"Expected 3 triangles, got {triangulated.polygon_count}"
    print(f"✓ Polygons: {triangulated.polygons}")

    print("\nTest 4: Mixed polygon mesh")
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
    print(f"✓ Created mixed mesh: {mixed_mesh.polygon_count} polygons")

    triangulated = mixed_mesh.triangulate()
    print(f"✓ Triangulated mesh: {triangulated.polygon_count} polygons")
    assert triangulated.polygon_count == 4, f"Expected 4 triangles, got {triangulated.polygon_count}"
    print(f"✓ Polygons: {triangulated.polygons}")

    print("\nTest 5: Original mesh unchanged")
    print(f"✓ Original mesh still has {mixed_mesh.polygon_count} polygons")
    assert mixed_mesh.polygon_count == 3, "Original mesh should be unchanged"

    print("\nTest 6: Control points preserved")
    assert len(triangulated.control_points) == len(mixed_mesh.control_points)
    print(f"✓ Control points preserved: {len(triangulated.control_points)} points")
    for i, (orig, new) in enumerate(zip(mixed_mesh.control_points, triangulated.control_points)):
        assert orig.x == new.x and orig.y == new.y and orig.z == new.z, f"Control point {i} changed"
    print(f"✓ All control points match")

    print("\nTest 7: Edge polygon (less than 3 vertices)")
    edge_mesh = Mesh("edge")
    edge_mesh._control_points = [Vector4(0, 0, 0, 1), Vector4(1, 0, 0, 1)]
    edge_mesh.create_polygon([0, 1])
    print(f"✓ Created edge mesh: {edge_mesh.polygon_count} polygons")

    triangulated = edge_mesh.triangulate()
    print(f"✓ Triangulated mesh: {triangulated.polygon_count} polygons")
    assert triangulated.polygon_count == 0, f"Expected 0 polygons for edge, got {triangulated.polygon_count}"

    print("\nAll tests passed!")
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
