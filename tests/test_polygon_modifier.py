#!/usr/bin/env python3
"""Test PolygonModifier class implementation"""

print("Testing PolygonModifier class...")

try:
    from aspose.threed.entities import PolygonModifier, Mesh
    from aspose.threed.utilities import Vector4
    from aspose.threed import Scene, Node

    print("✓ Imports successful")

    control_points = [
        Vector4(0, 0, 0, 1),
        Vector4(1, 0, 0, 1),
        Vector4(0, 1, 0, 1),
        Vector4(1, 1, 0, 1),
        Vector4(0.5, 1.5, 0, 1)
    ]

    triangle = [0, 1, 2]
    quad = [0, 1, 3, 2]
    pentagon = [0, 1, 3, 4, 2]

    print("Testing triangulate with control points and polygon lists...")
    triangles = PolygonModifier.triangulate(control_points, [triangle, quad, pentagon])
    print(f"✓ Triangulated polygons: {len(triangles)} triangles")
    assert len(triangles) == 6, f"Expected 6 triangles, got {len(triangles)}"
    print(f"✓ Triangles: {triangles}")

    print("\nTesting triangulate with single polygon...")
    single_triangle = PolygonModifier.triangulate(control_points, [triangle])
    print(f"✓ Single triangulated polygon: {single_triangle}")
    assert len(single_triangle) == 1

    quad_triangles = PolygonModifier.triangulate(control_points, [quad])
    print(f"✓ Quad triangulated: {quad_triangles}")
    assert len(quad_triangles) == 2

    print("\nTesting triangulate with mesh...")
    mesh = Mesh("test_quad")
    mesh._control_points = list(control_points)
    mesh.create_polygon(0, 1, 3, 2)
    print(f"✓ Created mesh with quad: {mesh.polygon_count} polygons")

    triangulated_mesh = PolygonModifier.triangulate(mesh)
    print(f"✓ Triangulated mesh: {triangulated_mesh.polygon_count} polygons")
    assert triangulated_mesh.polygon_count == 2, f"Expected 2 triangles, got {triangulated_mesh.polygon_count}"
    print(f"✓ Triangulated polygons: {triangulated_mesh.polygons}")

    print("\nTesting triangulate with mesh with multiple polygons...")
    mesh2 = Mesh("test_multi")
    mesh2._control_points = [
        Vector4(0, 0, 0, 1),
        Vector4(1, 0, 0, 1),
        Vector4(0, 1, 0, 1),
        Vector4(1, 1, 0, 1),
        Vector4(0.5, 0.5, 1, 1),
        Vector4(1.5, 0.5, 1, 1),
        Vector4(0.5, 1.5, 1, 1),
        Vector4(1.5, 1.5, 1, 1)
    ]
    mesh2.create_polygon(0, 1, 2)
    mesh2.create_polygon(1, 3, 2)
    mesh2.create_polygon(4, 5, 7, 6)
    mesh2.create_polygon(0, 1, 5, 4)
    print(f"✓ Created mesh with mixed polygons: {mesh2.polygon_count} polygons")

    triangulated_mesh2 = PolygonModifier.triangulate(mesh2)
    print(f"✓ Triangulated mesh2: {triangulated_mesh2.polygon_count} polygons")
    assert triangulated_mesh2.polygon_count == 6, f"Expected 6 triangles, got {triangulated_mesh2.polygon_count}"
    print(f"✓ Triangulated polygons: {triangulated_mesh2.polygons}")

    print("\nTesting triangulate with scene...")
    scene = Scene()
    mesh_node = Node("mesh_node")
    mesh_node.entity = mesh2
    scene.root_node.add_child_node(mesh_node)
    print(f"✓ Created scene with mesh node")

    PolygonModifier.triangulate(scene)
    print(f"✓ Triangulated scene")
    print(f"✓ Mesh node now has {mesh_node.entity.polygon_count} polygons")
    assert mesh_node.entity.polygon_count == 6

    print("\nTesting triangulate with normals...")
    from aspose.threed.utilities import Vector3
    nor_out = []
    triangles_with_normals = PolygonModifier.triangulate(control_points, [quad], True, [nor_out])
    print(f"✓ Triangulated with normals: {len(triangles_with_normals)} triangles")
    print(f"✓ Generated {len(nor_out)} normals")
    assert len(triangles_with_normals) == 2
    assert len(nor_out) == 2
    for i, normal in enumerate(nor_out):
        print(f"  Triangle {i} normal: {normal}")

    print("\nTesting triangulate with just control points...")
    empty_triangles = PolygonModifier.triangulate(control_points)
    print(f"✓ Triangulated empty polygons: {len(empty_triangles)} triangles")
    assert len(empty_triangles) == 0

    print("\nTesting triangulate with control points and polygon size...")
    from_size_triangles = PolygonModifier.triangulate(control_points, 4)
    print(f"✓ Triangulated from size: {len(from_size_triangles)} triangles")
    assert len(from_size_triangles) == 2

    print("\nAll tests passed!")
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
