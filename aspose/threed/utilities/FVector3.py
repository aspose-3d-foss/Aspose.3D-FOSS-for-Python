from typing import TYPE_CHECKING
import math

if TYPE_CHECKING:
    from .vector3 import Vector3
    from .vector4 import Vector4
    from .fvector2 import FVector2
    from .fvector4 import FVector4


class FVector3:
    def __init__(self, x=None, y=0.0, z=0.0):
        if x is None:
            self._x = 0.0
            self._y = 0.0
            self._z = 0.0
        elif isinstance(x, float):
            self._x = x
            self._y = float(y)
            self._z = float(z)
        elif isinstance(x, FVector2):
            self._x = x.x
            self._y = x.y
            self._z = float(z)
        else:
            from .vector3 import Vector3
            from .vector4 import Vector4
            from .fvector4 import FVector4
            if isinstance(x, Vector3):
                self._x = float(x.x)
                self._y = float(x.y)
                self._z = float(x.z)
            elif isinstance(x, Vector4):
                self._x = float(x.x)
                self._y = float(x.y)
                self._z = float(x.z)
            elif isinstance(x, FVector4):
                self._x = x.x
                self._y = x.y
                self._z = x.z
            else:
                raise TypeError(f"Invalid type for FVector3 initialization: {type(x)}")

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

    @staticmethod
    def zero() -> 'FVector3':
        return FVector3(0.0, 0.0, 0.0)

    @staticmethod
    def one() -> 'FVector3':
        return FVector3(1.0, 1.0, 1.0)

    @staticmethod
    def unit_x() -> 'FVector3':
        return FVector3(1.0, 0.0, 0.0)

    @staticmethod
    def unit_y() -> 'FVector3':
        return FVector3(0.0, 1.0, 0.0)

    @staticmethod
    def unit_z() -> 'FVector3':
        return FVector3(0.0, 0.0, 1.0)

    def normalize(self) -> 'FVector3':
        len_sq = self._x ** 2 + self._y ** 2 + self._z ** 2
        if len_sq == 0:
            return FVector3(0.0, 0.0, 0.0)
        length = math.sqrt(len_sq)
        return FVector3(self._x / length, self._y / length, self._z / length)

    def __getitem__(self, key: int) -> float:
        if key == 0:
            return self._x
        elif key == 1:
            return self._y
        elif key == 2:
            return self._z
        else:
            raise IndexError("FVector3 index out of range")

    def __setitem__(self, key: int, value: float):
        if key == 0:
            self._x = float(value)
        elif key == 1:
            self._y = float(value)
        elif key == 2:
            self._z = float(value)
        else:
            raise IndexError("FVector3 index out of range")

    def __repr__(self) -> str:
        return f"FVector3({self._x}, {self._y}, {self._z})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, FVector3):
            return False
        return self._x == other._x and self._y == other._y and self._z == other._z
