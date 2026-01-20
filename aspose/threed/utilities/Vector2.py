import math


class Vector2:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self._x = float(x)
        self._y = float(y)

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

    def set(self, new_x: float, new_y: float) -> None:
        self._x = float(new_x)
        self._y = float(new_y)

    @property
    def length(self) -> float:
        return math.sqrt(self._x ** 2 + self._y ** 2)

    @property
    def length2(self) -> float:
        return self._x ** 2 + self._y ** 2

    @staticmethod
    def parse(input: str):
        parts = input.strip().split()
        if len(parts) != 2:
            raise ValueError(f"Invalid Vector2 format: {input}")
        return Vector2(float(parts[0]), float(parts[1]))

    def __getitem__(self, key: int) -> float:
        if key == 0:
            return self._x
        elif key == 1:
            return self._y
        else:
            raise IndexError("Vector2 index out of range")

    def __setitem__(self, key: int, value: float):
        if key == 0:
            self._x = float(value)
        elif key == 1:
            self._y = float(value)
        else:
            raise IndexError("Vector2 index out of range")

    def __repr__(self) -> str:
        return f"Vector2({self._x}, {self._y})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector2):
            return False
        return self._x == other._x and self._y == other._y
