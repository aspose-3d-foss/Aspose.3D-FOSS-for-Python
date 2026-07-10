class Rect:
    """A class to represent the rectangle"""

    def __init__(self, x: int = 0, y: int = 0, width: int = 0, height: int = 0):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = int(value)

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = int(value)

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int):
        self._x = int(value)

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int):
        self._y = int(value)

    @property
    def left(self) -> int:
        return self._x

    @property
    def right(self) -> int:
        return self._x + self._width

    @property
    def top(self) -> int:
        return self._y

    @property
    def bottom(self) -> int:
        return self._y + self._height

    def contains(self, x: int, y: int) -> bool:
        return self._x <= x < self._x + self._width and self._y <= y < self._y + self._height
