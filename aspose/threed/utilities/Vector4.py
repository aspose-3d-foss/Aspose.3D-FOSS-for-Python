class Vector4:
    def __init__(self, *args):
        if len(args) == 0:
            self._x = 0.0
            self._y = 0.0
            self._z = 0.0
            self._w = 1.0
        elif len(args) == 1:
            arg = args[0]
            from .vector3 import Vector3
            if isinstance(arg, Vector3):
                self._x = arg.x
                self._y = arg.y
                self._z = arg.z
                self._w = 1.0
            else:
                raise TypeError(f"Invalid single argument for Vector4: {type(arg)}")
        elif len(args) == 2:
            vec, w = args
            from .vector3 import Vector3
            if isinstance(vec, Vector3):
                self._x = vec.x
                self._y = vec.y
                self._z = vec.z
                self._w = float(w)
            else:
                raise TypeError(f"First argument must be Vector3, got {type(vec)}")
        elif len(args) == 3:
            self._x = float(args[0])
            self._y = float(args[1])
            self._z = float(args[2])
            self._w = 1.0
        elif len(args) == 4:
            self._x = float(args[0])
            self._y = float(args[1])
            self._z = float(args[2])
            self._w = float(args[3])
        else:
            raise TypeError(f"Invalid number of arguments for Vector4: {len(args)}")

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

    def set(self, new_x: float, new_y: float, new_z: float, new_w: float = 1.0) -> None:
        self._x = float(new_x)
        self._y = float(new_y)
        self._z = float(new_z)
        self._w = float(new_w)

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
            raise IndexError("Vector4 index out of range")

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
            raise IndexError("Vector4 index out of range")

    def __repr__(self) -> str:
        return f"Vector4({self._x}, {self._y}, {self._z}, {self._w})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector4):
            return False
        return (self._x == other._x and self._y == other._y and
                self._z == other._z and self._w == other._w)
