import unittest
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from aspose.threed.entities import Box, Cylinder, Sphere, Pyramid, Torus, Dish, Mesh


class GeometryToMeshTests(unittest.TestCase):
    """Tests for geometry ToMesh() method."""

    def test_box_to_mesh_should_create_mesh(self):
        """Test Box.ToMesh() creates a valid mesh."""
        box = Box(10, 20, 30)
        mesh = box.to_mesh()
        
        self.assertIsNotNone(mesh)
        self.assertEqual(8, len(mesh.control_points))

    def test_cylinder_to_mesh_should_create_mesh(self):
        """Test Cylinder.ToMesh() creates a valid mesh."""
        cylinder = Cylinder(5, 5, 20)
        mesh = cylinder.to_mesh()
        
        self.assertIsNotNone(mesh)
        self.assertGreater(len(mesh.control_points), 0)

    def test_sphere_to_mesh_should_create_mesh(self):
        """Test Sphere.ToMesh() creates a valid mesh."""
        sphere = Sphere(10, 32, 16)
        mesh = sphere.to_mesh()
        
        self.assertIsNotNone(mesh)
        self.assertGreater(len(mesh.control_points), 0)

    def test_pyramid_to_mesh_should_create_mesh(self):
        """Test Pyramid.ToMesh() creates a valid mesh."""
        pyramid = Pyramid(10, 10, 20)
        mesh = pyramid.to_mesh()
        
        self.assertIsNotNone(mesh)
        self.assertGreaterEqual(len(mesh.control_points), 4)

    def test_torus_to_mesh_should_create_mesh(self):
        """Test Torus.ToMesh() creates a valid mesh."""
        torus = Torus(10, 3)
        mesh = torus.to_mesh()
        
        self.assertIsNotNone(mesh)
        self.assertGreater(len(mesh.control_points), 0)

    def test_dish_to_mesh_should_create_mesh(self):
        """Test Dish.ToMesh() creates a valid mesh."""
        dish = Dish(10, 5)
        mesh = dish.to_mesh()
        
        self.assertIsNotNone(mesh)
        self.assertGreater(len(mesh.control_points), 0)

    def test_mesh_to_mesh_should_return_same_mesh(self):
        """Test Mesh.ToMesh() returns the same mesh."""
        mesh = Mesh()
        mesh.create_polygon([0, 1, 2])
        
        result = mesh.to_mesh()
        
        self.assertIsNotNone(result)
        self.assertEqual(mesh, result)


if __name__ == '__main__':
    unittest.main()
