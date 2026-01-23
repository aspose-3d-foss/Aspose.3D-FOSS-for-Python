from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .vector3 import Vector3
    from .vector4 import Vector4
    from .fvector3 import FVector3


class FVector4:
    def __init__(self, x=None, y=0.0, z=0.0, w=0.0):
        if x is None:
            self._x = 0.0
            self._y = 0.0
            self._z = 0.0
            self._w = 0.0
        elif isinstance(x, float):
            if z is None:
                self._x = x
                self._y = float(y)
                self._z = 0.0
                self._w = float(w)
            else:
                self._x = x
                self._y = float(y)
                self._z = float(z)
                self._w = float(w)
        else:
            from .vector3 import Vector3
            from .vector4 import Vector4
            from .fvector3 import FVector3
            if isinstance(x, FVector3):
                self._x = x.x
                self._y = x.y
                self._z = x.z
                self._w = float(w)
            elif isinstance(x, Vector3):
                self._x = float(x.x)
                self._y = float(x.y)
                self._z = float(x.z)
                self._w = float(w)
            elif isinstance(x, Vector4):
                self._x = float(x.x)
                self._y = float(x.y)
                self._z = float(x.z)
                self._w = float(x.w)
            elif isinstance(x, Vector3):
                self._x = float(x.x)
                self._y = float(x.y)
                self._z = float(x.z)
                self._w = float(w)
            else:
                raise TypeError(f"Invalid type for FVector4 initialization: {type(x)}")

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

    @property
    def w(self) -> float:
        return self._w

    @w.setter
    def w(self, value: float):
        self._w = float(value)

    def __getitem__(self, key: int) -> float:
        if key == 0:
            return self._x
        elif key == 1:
            return self._y
        elif key == 2:
            return self._z
        elif key == 3:
            return self._w
        else:
            raise IndexError("FVector4 index out of range")

    def __setitem__(self, key: int, value: float):
        if key == 0:
            self._x = float(value)
        elif key == 1:
            self._y = float(value)
        elif key == 2:
            self._z = float(value)
        elif key == 3:
            self._w = float(value)
        else:
            raise IndexError("FVector4 index out of range")

    def __repr__(self) -> str:
        return f"FVector4({self._x}, {self._y}, {self._z}, {self._w})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, FVector4):
            return False
        return self._x == other._x and self._y == other._y and self._z == other._z and self._w == other._w
