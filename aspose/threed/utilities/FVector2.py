from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .vector3 import Vector3
    from .vector4 import Vector4


class FVector2:
    def __init__(self, x=None, y=0.0):
        if x is None:
            self._x = 0.0
            self._y = 0.0
        elif isinstance(x, float):
            self._x = float(x)
            self._y = float(y)
        else:
            raise TypeError(f"Invalid type for FVector2: {type(x)}")
    
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
    
    def __repr__(self) -> str:
        return f"FVector2({self._x}, {self._y})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, FVector2):
            return False
        return self._x == other._x and self._y == other._y
    
    def __add__(self, other: 'FVector2') -> 'FVector2':
        if not isinstance(other, FVector2):
            raise TypeError("Can only add another FVector2")
        return FVector2(self._x + other._x, self._y + other._y)
    
    def __sub__(self, other: 'FVector2') -> 'FVector2':
        if not isinstance(other, FVector2):
            raise TypeError("Can only subtract another FVector2")
        return FVector2(self._x - other._x, self._y - other._y)
    
    def __mul__(self, scalar: float) -> 'FVector2':
        return FVector2(self._x * scalar, self._y * scalar)
    
    def __truediv__(self, scalar: float) -> 'FVector2':
        if scalar == 0:
            raise ZeroDivisionError()
        return FVector2(self._x / scalar, self._y / scalar)
    
    def length(self) -> float:
        return (self._x ** 2 + self._y ** 2) ** 0.5
    
    def normalize(self) -> 'FVector2':
        length = self.length()
        if length > 0:
            return FVector2(self._x / length, self._y / length)
        else:
            return FVector2(0.0, 0.0)
    
    def dot(self, other: 'FVector2') -> float:
        return self._x * other._x + self._y * other._y
    
    @staticmethod
    def parse(input: str):
        parts = input.strip().split()
        if len(parts) != 2:
            raise ValueError(f"Invalid Vector2 format: {input}")
        return FVector2(float(parts[0]), float(parts[1]))