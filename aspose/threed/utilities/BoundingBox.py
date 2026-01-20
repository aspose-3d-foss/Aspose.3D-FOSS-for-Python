import math


class BoundingBox:
    def __init__(self, *args):
        if len(args) == 0:
            self._minimum = None
            self._maximum = None
            self._is_null = True
        elif len(args) == 2:
            from .vector3 import Vector3
            min_arg, max_arg = args

            if isinstance(min_arg, Vector3):
                self._minimum = Vector3(min_arg.x, min_arg.y, min_arg.z)
            elif isinstance(min_arg, list) and len(min_arg) >= 3:
                self._minimum = Vector3(min_arg[0], min_arg[1], min_arg[2])
            else:
                self._minimum = Vector3(float(min_arg[0]), float(min_arg[1]), float(min_arg[2]))

            if isinstance(max_arg, Vector3):
                self._maximum = Vector3(max_arg.x, max_arg.y, max_arg.z)
            elif isinstance(max_arg, list) and len(max_arg) >= 3:
                self._maximum = Vector3(max_arg[0], max_arg[1], max_arg[2])
            else:
                self._maximum = Vector3(float(max_arg[0]), float(max_arg[1]), float(max_arg[2]))

            self._is_null = False
        elif len(args) == 6:
            min_x, min_y, min_z, max_x, max_y, max_z = args
            self._minimum = Vector3(float(min_x), float(min_y), float(min_z))
            self._maximum = Vector3(float(max_x), float(max_y), float(max_z))
            self._is_null = False
        else:
            raise TypeError(f"Invalid arguments for BoundingBox: {len(args)}")

    @property
    def minimum(self):
        if self._is_null:
            from .vector3 import Vector3
            return Vector3(float('inf'), float('inf'), float('inf'))
        return self._minimum

    @property
    def maximum(self):
        if self._is_null:
            from .vector3 import Vector3
            return Vector3(float('-inf'), float('-inf'), float('-inf'))
        return self._maximum

    @property
    def center(self):
        if self._is_null:
            from .vector3 import Vector3
            return Vector3(0, 0, 0)
        return Vector3(
            (self._minimum.x + self._maximum.x) * 0.5,
            (self._minimum.y + self._maximum.y) * 0.5,
            (self._minimum.z + self._maximum.z) * 0.5
        )

    @property
    def size(self):
        if self._is_null:
            from .vector3 import Vector3
            return Vector3(0, 0, 0)
        return Vector3(
            self._maximum.x - self._minimum.x,
            self._maximum.y - self._minimum.y,
            self._maximum.z - self._minimum.z
        )

    @staticmethod
    def get_null() -> 'BoundingBox':
        bb = BoundingBox()
        bb._is_null = True
        bb._minimum = None
        bb._maximum = None
        return bb

    null = property(get_null)

    @staticmethod
    def get_infinite() -> 'BoundingBox':
        from .vector3 import Vector3
        return BoundingBox(
            Vector3(float('-inf'), float('-inf'), float('-inf')),
            Vector3(float('inf'), float('inf'), float('inf'))
        )

    infinite = property(get_infinite)

    def merge(self, *args):
        from .vector3 import Vector3
        from .vector4 import Vector4

        if self._is_null:
            if len(args) == 1:
                arg = args[0]
                if isinstance(arg, (Vector3, Vector4)):
                    self._minimum = Vector3(arg.x, arg.y, arg.z)
                    self._maximum = Vector3(arg.x, arg.y, arg.z)
                elif isinstance(arg, BoundingBox):
                    self._minimum = Vector3(arg._minimum.x, arg._minimum.y, arg._minimum.z)
                    self._maximum = Vector3(arg._maximum.x, arg._maximum.y, arg._maximum.z)
                elif len(arg) >= 3:
                    self._minimum = Vector3(float(arg[0]), float(arg[1]), float(arg[2]))
                    self._maximum = Vector3(float(arg[0]), float(arg[1]), float(arg[2]))
            elif len(args) == 3:
                x, y, z = args
                self._minimum = Vector3(float(x), float(y), float(z))
                self._maximum = Vector3(float(x), float(y), float(z))
            self._is_null = False
            return

        if len(args) == 1:
            arg = args[0]
            if isinstance(arg, (Vector3, Vector4)):
                x, y, z = arg.x, arg.y, arg.z
                self._minimum.x = min(self._minimum.x, x)
                self._minimum.y = min(self._minimum.y, y)
                self._minimum.z = min(self._minimum.z, z)
                self._maximum.x = max(self._maximum.x, x)
                self._maximum.y = max(self._maximum.y, y)
                self._maximum.z = max(self._maximum.z, z)
            elif isinstance(arg, BoundingBox):
                self._minimum.x = min(self._minimum.x, arg._minimum.x)
                self._minimum.y = min(self._minimum.y, arg._minimum.y)
                self._minimum.z = min(self._minimum.z, arg._minimum.z)
                self._maximum.x = max(self._maximum.x, arg._maximum.x)
                self._maximum.y = max(self._maximum.y, arg._maximum.y)
                self._maximum.z = max(self._maximum.z, arg._maximum.z)
            elif len(arg) >= 3:
                x, y, z = float(arg[0]), float(arg[1]), float(arg[2])
                self._minimum.x = min(self._minimum.x, x)
                self._minimum.y = min(self._minimum.y, y)
                self._minimum.z = min(self._minimum.z, z)
                self._maximum.x = max(self._maximum.x, x)
                self._maximum.y = max(self._maximum.y, y)
                self._maximum.z = max(self._maximum.z, z)
        elif len(args) == 3:
            x, y, z = float(args[0]), float(args[1]), float(args[2])
            self._minimum.x = min(self._minimum.x, x)
            self._minimum.y = min(self._minimum.y, y)
            self._minimum.z = min(self._minimum.z, z)
            self._maximum.x = max(self._maximum.x, x)
            self._maximum.y = max(self._maximum.y, y)
            self._maximum.z = max(self._maximum.z, z)

    def contains(self, arg):
        from .vector3 import Vector3

        if isinstance(arg, BoundingBox):
            return (self._minimum.x <= arg._minimum.x and
                    self._minimum.y <= arg._minimum.y and
                    self._minimum.z <= arg._minimum.z and
                    self._maximum.x >= arg._maximum.x and
                    self._maximum.y >= arg._maximum.y and
                    self._maximum.z >= arg._maximum.z)
        elif isinstance(arg, Vector3):
            return (self._minimum.x <= arg.x <= self._maximum.x and
                    self._minimum.y <= arg.y <= self._maximum.y and
                    self._minimum.z <= arg.z <= self._maximum.z)
        elif len(arg) >= 3:
            x, y, z = arg[0], arg[1], arg[2]
            return (self._minimum.x <= x <= self._maximum.x and
                    self._minimum.y <= y <= self._maximum.y and
                    self._minimum.z <= z <= self._maximum.z)

        return False

    def overlaps_with(self, box: 'BoundingBox') -> bool:
        return not (self._maximum.x < box._minimum.x or
                   box._maximum.x < self._minimum.x or
                   self._maximum.y < box._minimum.y or
                   box._maximum.y < self._minimum.y or
                   self._maximum.z < box._minimum.z or
                   box._maximum.z < self._minimum.z)

    def scale(self) -> float:
        if self._is_null:
            return 0.0
        max_x = max(abs(self._minimum.x), abs(self._maximum.x))
        max_y = max(abs(self._minimum.y), abs(self._maximum.y))
        max_z = max(abs(self._minimum.z), abs(self._maximum.z))
        return max(max_x, max_y, max_z)

    @staticmethod
    def from_geometry(geometry):
        raise NotImplementedError("from_geometry is not implemented")

    @property
    def extent(self):
        from .bounding_box_extent import BoundingBoxExtent
        if self._is_null:
            return BoundingBoxExtent(0, 0, 0)
        center = self.center
        size = self.size
        return BoundingBoxExtent(
            abs(size.x * 0.5),
            abs(size.y * 0.5),
            abs(size.z * 0.5)
        )

    def __repr__(self) -> str:
        if self._is_null:
            return f"BoundingBox(null)"
        return f"BoundingBox({self._minimum}, {self._maximum})"


class BoundingBoxExtent:
    def __init__(self, extent_x: float = 0.0, extent_y: float = 0.0, extent_z: float = 0.0):
        self._extent_x = float(extent_x)
        self._extent_y = float(extent_y)
        self._extent_z = float(extent_z)

    @property
    def extent_x(self) -> float:
        return self._extent_x

    @property
    def extent_y(self) -> float:
        return self._extent_y

    @property
    def extent_z(self) -> float:
        return self._extent_z

    def __repr__(self) -> str:
        return f"BoundingBoxExtent({self._extent_x}, {self._extent_y}, {self._extent_z})"
