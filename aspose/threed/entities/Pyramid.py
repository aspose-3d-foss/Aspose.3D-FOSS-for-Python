from typing import TYPE_CHECKING

from .Primitive import Primitive
from ..utilities.Vector4 import Vector4
from ..utilities.Vector2 import Vector2
from ..utilities.Vector3 import Vector3

if TYPE_CHECKING:
    from .Mesh import Mesh


class Pyramid(Primitive):
    """Parameterized pyramid."""

    def __init__(self, name: str = None, xbottom: float = 10.0, ybottom: float = 10.0,
                 xtop: float = 5.0, ytop: float = 5.0, height: float = 5.0):
        """Constructor of Pyramid."""
        if name is None:
            name = "Pyramid"
        super().__init__(name)
        self._bottom_area = Vector2(xbottom, ybottom)
        self._top_area = Vector2(xtop, ytop)
        self._bottom_offset = Vector3()
        self._height = height

    @property
    def bottom_area(self) -> Vector2:
        """Gets the bottom area."""
        return self._bottom_area

    @bottom_area.setter
    def bottom_area(self, value: Vector2):
        """Sets the bottom area."""
        self._bottom_area = value

    @property
    def top_area(self) -> Vector2:
        """Gets the top area."""
        return self._top_area

    @top_area.setter
    def top_area(self, value: Vector2):
        """Sets the top area."""
        self._top_area = value

    @property
    def bottom_offset(self) -> Vector3:
        """Gets the bottom offset."""
        return self._bottom_offset

    @bottom_offset.setter
    def bottom_offset(self, value: Vector3):
        """Sets the bottom offset."""
        self._bottom_offset = value

    @property
    def height(self) -> float:
        """Gets the height."""
        return self._height

    @height.setter
    def height(self, value: float):
        """Sets the height."""
        self._height = value

    def to_mesh(self) -> 'Mesh':
        """Convert current object to mesh."""
        from .Mesh import Mesh
        mesh = Mesh(self.name)
        bottom_width = float(self._bottom_area.x)
        bottom_height = float(self._bottom_area.y)
        top_width = float(self._top_area.x)
        top_height = float(self._top_area.y)
        pyramid_height = float(self._height)
        bottom_offset_x = float(self._bottom_offset.x)
        bottom_offset_y = float(self._bottom_offset.y)

        # Bottom face vertices (clockwise)
        mesh.control_points.append(Vector4(-bottom_width / 2 + bottom_offset_x, -bottom_height / 2 + bottom_offset_y, 0, 1))
        mesh.control_points.append(Vector4(bottom_width / 2 + bottom_offset_x, -bottom_height / 2 + bottom_offset_y, 0, 1))
        mesh.control_points.append(Vector4(bottom_width / 2 + bottom_offset_x, bottom_height / 2 + bottom_offset_y, 0, 1))
        mesh.control_points.append(Vector4(-bottom_width / 2 + bottom_offset_x, bottom_height / 2 + bottom_offset_y, 0, 1))

        # Top face vertices (clockwise, centered)
        mesh.control_points.append(Vector4(-top_width / 2, -top_height / 2, pyramid_height, 1))
        mesh.control_points.append(Vector4(top_width / 2, -top_height / 2, pyramid_height, 1))
        mesh.control_points.append(Vector4(top_width / 2, top_height / 2, pyramid_height, 1))
        mesh.control_points.append(Vector4(-top_width / 2, top_height / 2, pyramid_height, 1))

        # Bottom face
        mesh.create_polygon(0, 3, 2, 1)
        # Top face
        mesh.create_polygon(4, 5, 6, 7)
        # Front face
        mesh.create_polygon(1, 2, 6, 5)
        # Back face
        mesh.create_polygon(0, 3, 7, 4)
        # Left face
        mesh.create_polygon(0, 1, 5, 4)
        # Right face
        mesh.create_polygon(2, 3, 7, 6)

        return mesh
