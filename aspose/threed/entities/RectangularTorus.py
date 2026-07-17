import math

from typing import TYPE_CHECKING

from .Primitive import Primitive

if TYPE_CHECKING:
    from .Mesh import Mesh


class RectangularTorus(Primitive):
    """Parameterized rectangular torus entity."""

    def __init__(self, name: str = None, inner_radius: float = 17.0, outer_radius: float = 20.0, 
                 height: float = 20.0, arc: float = math.pi, angle_start: float = 0.0, 
                 radial_segments: int = 10):
        """Constructor of RectangularTorus.
        
        Args:
            name: Name of the rectangular torus
            inner_radius: Inner radius of the rectangular torus
            outer_radius: Outer radius of the rectangular torus
            height: Height of the rectangular torus
            arc: Total angle of the arc, measured in radian
            angle_start: Start angle of the arc
            radial_segments: Number of radial segments
        """
        if name is None:
            name = "RectangularTorus"
        super().__init__(name)
        self._inner_radius = inner_radius
        self._outer_radius = outer_radius
        self._height = height
        self._arc = arc
        self._angle_start = angle_start
        self._radial_segments = radial_segments

    @property
    def inner_radius(self) -> float:
        """Gets the inner radius of the rectangular torus."""
        return self._inner_radius

    @inner_radius.setter
    def inner_radius(self, value: float):
        """Sets the inner radius of the rectangular torus."""
        self._inner_radius = value

    @property
    def outer_radius(self) -> float:
        """Gets the outer radius of the rectangular torus."""
        return self._outer_radius

    @outer_radius.setter
    def outer_radius(self, value: float):
        """Sets the outer radius of the rectangular torus."""
        self._outer_radius = value

    @property
    def height(self) -> float:
        """Gets the height of the rectangular torus."""
        return self._height

    @height.setter
    def height(self, value: float):
        """Sets the height of the rectangular torus."""
        self._height = value

    @property
    def arc(self) -> float:
        """Gets the total angle of the arc, measured in radian."""
        return self._arc

    @arc.setter
    def arc(self, value: float):
        """Sets the total angle of the arc, measured in radian."""
        self._arc = value

    @property
    def angle_start(self) -> float:
        """Gets the start angle of the arc, measured in radian."""
        return self._angle_start

    @angle_start.setter
    def angle_start(self, value: float):
        """Sets the start angle of the arc, measured in radian."""
        self._angle_start = value

    @property
    def radial_segments(self) -> int:
        """Gets the radial segments."""
        return self._radial_segments

    @radial_segments.setter
    def radial_segments(self, value: int):
        """Sets the radial segments."""
        self._radial_segments = value

    def to_mesh(self) -> 'Mesh':
        """Convert this primitive to mesh."""
        from .Mesh import Mesh
        mesh = Mesh(self.name)
        inner_radius = self._inner_radius
        outer_radius = self._outer_radius
        height = self._height
        arc = self._arc
        angle_start = self._angle_start
        radial_segments = self._radial_segments

        for i in range(radial_segments + 1):
            angle = angle_start + (i / radial_segments) * arc
            cos_angle = math.cos(angle)
            sin_angle = math.sin(angle)

            # Bottom-left corner (inner radius, -height/2)
            x1 = inner_radius * cos_angle
            y1 = inner_radius * sin_angle
            z1 = -height / 2
            mesh.control_points.append((x1, y1, z1, 1))

            # Bottom-right corner (outer radius, -height/2)
            x2 = outer_radius * cos_angle
            y2 = outer_radius * sin_angle
            z2 = -height / 2
            mesh.control_points.append((x2, y2, z2, 1))

            # Top-right corner (outer radius, height/2)
            x3 = outer_radius * cos_angle
            y3 = outer_radius * sin_angle
            z3 = height / 2
            mesh.control_points.append((x3, y3, z3, 1))

            # Top-left corner (inner radius, height/2)
            x4 = inner_radius * cos_angle
            y4 = inner_radius * sin_angle
            z4 = height / 2
            mesh.control_points.append((x4, y4, z4, 1))

        # Create polygons connecting adjacent vertices
        for i in range(radial_segments):
            base_idx = i * 4

            # Connect the four sides of the rectangular ring
            mesh.create_polygon([base_idx + 0, base_idx + 4, base_idx + 5, base_idx + 1])
            mesh.create_polygon([base_idx + 1, base_idx + 5, base_idx + 6, base_idx + 2])
            mesh.create_polygon([base_idx + 2, base_idx + 6, base_idx + 7, base_idx + 3])
            mesh.create_polygon([base_idx + 3, base_idx + 7, base_idx + 4, base_idx + 0])

        # Close the ring by connecting the last segment to the first
        if radial_segments > 0:
            last_base = (radial_segments - 1) * 4
            first_base = 0

            mesh.create_polygon([last_base + 0, first_base + 4, first_base + 5, last_base + 1])
            mesh.create_polygon([last_base + 1, first_base + 5, first_base + 6, last_base + 2])
            mesh.create_polygon([last_base + 2, first_base + 6, first_base + 7, last_base + 3])
            mesh.create_polygon([last_base + 3, first_base + 7, first_base + 4, last_base + 0])

        return mesh
