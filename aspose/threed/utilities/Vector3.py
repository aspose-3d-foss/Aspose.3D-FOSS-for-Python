import math


class Vector3:
    def __init__(self, x=None, y=0.0, z=0.0):
        if x is None:
            self._x = 0.0
            self._y = 0.0
            self._z = 0.0
        elif isinstance(x, (int, float)):
            self._x = float(x)
            self._y = float(y)
            self._z = float(z)
        elif isinstance(x, Vector3):
            self._x = x._x
            self._y = x._y
            self._z = x._z
        else:
            raise TypeError(f"Invalid type for Vector3 initialization: {type(x)}")

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float):
        self._x = float(value)

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float):
        self._y = float(value)

    @property
    def z(self) -> float:
        return self._z

    @z.setter
    def z(self, value: float):
        self._z = float(value)

    def set(self, new_x: float, new_y: float, new_z: float) -> None:
        self._x = float(new_x)
        self._y = float(new_y)
        self._z = float(new_z)

    @property
    def length(self) -> float:
        return math.sqrt(self._x ** 2 + self._y ** 2 + self._z ** 2)

    @property
    def length2(self) -> float:
        return self._x ** 2 + self._y ** 2 + self._z ** 2

    @property
    def zero(self) -> 'Vector3':
        return Vector3(0, 0, 0)

    @property
    def one(self) -> 'Vector3':
        return Vector3(1, 1, 1)

    @property
    def unit_x(self) -> 'Vector3':
        return Vector3(1, 0, 0)

    @property
    def unit_y(self) -> 'Vector3':
        return Vector3(0, 1, 0)

    @property
    def unit_z(self) -> 'Vector3':
        return Vector3(0, 0, 1)

    def dot(self, rhs: 'Vector3') -> float:
        return self._x * rhs._x + self._y * rhs._y + self._z * rhs._z

    def cross(self, rhs: 'Vector3') -> 'Vector3':
        return Vector3(
            self._y * rhs._z - self._z * rhs._y,
            self._z * rhs._x - self._x * rhs._z,
            self._x * rhs._y - self._y * rhs._x
        )

    def normalize(self) -> 'Vector3':
        len_sq = self.length2
        if len_sq == 0:
            return Vector3(0, 0, 0)
        length = math.sqrt(len_sq)
        return Vector3(self._x / length, self._y / length, self._z / length)

    def angle_between(self, dir: 'Vector3', up=None) -> float:
        if up is None:
            self_n = self.normalize()
            dir_n = dir.normalize()
            dot = self_n.dot(dir_n)
            dot = max(-1.0, min(1.0, dot))
            return math.acos(dot)
        else:
            proj = self - up * self.dot(up)
            dir_proj = dir - up * dir.dot(up)
            proj_n = proj.normalize()
            dir_proj_n = dir_proj.normalize()
            dot = proj_n.dot(dir_proj_n)
            dot = max(-1.0, min(1.0, dot))
            return math.acos(dot)

    def sin(self) -> 'Vector3':
        return Vector3(math.sin(self._x), math.sin(self._y), math.sin(self._z))

    def cos(self) -> 'Vector3':
        return Vector3(math.cos(self._x), math.cos(self._y), math.cos(self._z))

    def compare_to(self, other: 'Vector3') -> int:
        if self._x < other._x:
            return -1
        elif self._x > other._x:
            return 1
        elif self._y < other._y:
            return -1
        elif self._y > other._y:
            return 1
        elif self._z < other._z:
            return -1
        elif self._z > other._z:
            return 1
        else:
            return 0

    @staticmethod
    def parse(input: str) -> 'Vector3':
        parts = input.strip().split()
        if len(parts) != 3:
            raise ValueError(f"Invalid Vector3 format: {input}")
        return Vector3(float(parts[0]), float(parts[1]), float(parts[2]))

    def __getitem__(self, key: int) -> float:
        if key == 0:
            return self._x
        elif key == 1:
            return self._y
        elif key == 2:
            return self._z
        else:
            raise IndexError("Vector3 index out of range")

    def __setitem__(self, key: int, value: float):
        if key == 0:
            self._x = float(value)
        elif key == 1:
            self._y = float(value)
        elif key == 2:
            self._z = float(value)
        else:
            raise IndexError("Vector3 index out of range")

    def __repr__(self) -> str:
        return f"Vector3({self._x}, {self._y}, {self._z})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector3):
            return False
        return self._x == other._x and self._y == other._y and self._z == other._z
