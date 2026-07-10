from typing import TYPE_CHECKING
import math

from .Primitive import Primitive

if TYPE_CHECKING:
    from ..utilities.Vector4 import Vector4
    from ..utilities.Vector2 import Vector2
    from ..utilities.Vector3 import Vector3
    from .Mesh import Mesh


class Cylinder(Primitive):
    def __init__(self, name: str = None, radius_top: float = 1.0, radius_bottom: float = 1.0,
                 height: float = 1.0, radial_segments: int = 32, height_segments: int = 1,
                 open_ended: bool = False, theta_start: float = 0.0, theta_length: float = math.pi * 2):
        if name is None:
            name = "Cylinder"
        super().__init__(name)
        self._radius_top = radius_top
        self._radius_bottom = radius_bottom
        self._height = height
        self._radial_segments = radial_segments
        self._height_segments = height_segments
        self._open_ended = open_ended
        self._theta_start = theta_start
        self._theta_length = theta_length
        self._generate_fan_cylinder = False
        self._shear_top = None
        self._shear_bottom = None
        self._offset_top = None
        self._offset_bottom = None
        self._init_defaults()

    def _init_defaults(self):
        from ..utilities.Vector3 import Vector3
        from ..utilities.Vector2 import Vector2
        self._offset_bottom = Vector3(0, 0, 0)
        self._offset_top = Vector3(0, 0, 0)
        self._shear_bottom = Vector2(0, 0)
        self._shear_top = Vector2(0, 0)

    @property
    def offset_bottom(self):
        if self._offset_bottom is None:
            from ..utilities.Vector3 import Vector3
            self._offset_bottom = Vector3(0, 0, 0)
        return self._offset_bottom

    @offset_bottom.setter
    def offset_bottom(self, value):
        self._offset_bottom = value

    @property
    def offset_top(self):
        if self._offset_top is None:
            from ..utilities.Vector3 import Vector3
            self._offset_top = Vector3(0, 0, 0)
        return self._offset_top

    @offset_top.setter
    def offset_top(self, value):
        self._offset_top = value

    @property
    def generate_fan_cylinder(self) -> bool:
        return self._generate_fan_cylinder

    @generate_fan_cylinder.setter
    def generate_fan_cylinder(self, value: bool):
        self._generate_fan_cylinder = value

    @property
    def shear_bottom(self):
        if self._shear_bottom is None:
            from ..utilities.Vector2 import Vector2
            self._shear_bottom = Vector2(0, 0)
        return self._shear_bottom

    @shear_bottom.setter
    def shear_bottom(self, value):
        self._shear_bottom = value

    @property
    def shear_top(self):
        if self._shear_top is None:
            from ..utilities.Vector2 import Vector2
            self._shear_top = Vector2(0, 0)
        return self._shear_top

    @shear_top.setter
    def shear_top(self, value):
        self._shear_top = value

    @property
    def radius_top(self) -> float:
        return self._radius_top

    @radius_top.setter
    def radius_top(self, value: float):
        self._radius_top = value

    @property
    def radius_bottom(self) -> float:
        return self._radius_bottom

    @radius_bottom.setter
    def radius_bottom(self, value: float):
        self._radius_bottom = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        self._height = value

    @property
    def radial_segments(self) -> int:
        return self._radial_segments

    @radial_segments.setter
    def radial_segments(self, value: int):
        self._radial_segments = value

    @property
    def height_segments(self) -> int:
        return self._height_segments

    @height_segments.setter
    def height_segments(self, value: int):
        self._height_segments = value

    @property
    def open_ended(self) -> bool:
        return self._open_ended

    @open_ended.setter
    def open_ended(self, value: bool):
        self._open_ended = bool(value)

    @property
    def theta_start(self) -> float:
        return self._theta_start

    @theta_start.setter
    def theta_start(self, value: float):
        self._theta_start = value

    @property
    def theta_length(self) -> float:
        return self._theta_length

    @theta_length.setter
    def theta_length(self, value: float):
        self._theta_length = value

    def to_mesh(self):
        from ..utilities.Vector4 import Vector4
        from .Mesh import Mesh
        mesh = Mesh(self.name)

        radius_top = self._radius_top
        radius_bottom = self._radius_bottom
        height = self._height
        half_height = height / 2

        top_center = Vector4(self._offset_top.x, half_height + self._offset_top.y, self._offset_top.z, 1)
        bottom_center = Vector4(self._offset_bottom.x, -half_height + self._offset_bottom.y, self._offset_bottom.z, 1)

        for i in range(self._radial_segments + 1):
            angle = self._theta_start + self._theta_length * i / self._radial_segments
            sin_angle = math.sin(angle)
            cos_angle = math.cos(angle)

            x = radius_top * cos_angle
            z = radius_top * sin_angle
            mesh._control_points.append(Vector4(x, half_height, z, 1))

        for i in range(self._radial_segments + 1):
            angle = self._theta_start + self._theta_length * i / self._radial_segments
            sin_angle = math.sin(angle)
            cos_angle = math.cos(angle)

            x = radius_bottom * cos_angle
            z = radius_bottom * sin_angle
            mesh._control_points.append(Vector4(x, -half_height, z, 1))

        for i in range(self._radial_segments):
            mesh.create_polygon(i, i + 1, self._radial_segments + i + 2, self._radial_segments + i + 1)

        if not self._open_ended and radius_top > 0:
            top_index = len(mesh._control_points)
            mesh._control_points.append(top_center)
            for i in range(self._radial_segments):
                mesh.create_polygon(top_index, i, i + 1)

        if not self._open_ended and radius_bottom > 0:
            bottom_index = len(mesh._control_points)
            mesh._control_points.append(bottom_center)
            bottom_start = self._radial_segments + 1
            for i in range(self._radial_segments):
                mesh.create_polygon(bottom_index, bottom_start + i + 1, bottom_start + i)

        return mesh
