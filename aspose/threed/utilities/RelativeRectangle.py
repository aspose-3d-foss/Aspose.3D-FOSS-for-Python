class RelativeRectangle:
    """Relative rectangle
    The formula between relative component to absolute value is:
    Scale * (Reference Width) + offset
    So if we want it to represent an absolute value, leave all scale fields zero, and use offset fields instead."""

    def __init__(self, left: int = 0, top: int = 0, width: int = 0, height: int = 0):
        self._scale_x = 0.0
        self._scale_y = 0.0
        self._scale_width = 0.0
        self._scale_height = 0.0
        self._offset_x = left
        self._offset_y = top
        self._offset_width = width
        self._offset_height = height

    def to_absolute(self, left: int, top: int, width: int, height: int) -> 'Rect':
        """Convert to absolute rectangle using the given reference values"""
        from .Rect import Rect
        x = int(self._scale_x * width + self._offset_x)
        y = int(self._scale_y * height + self._offset_y)
        w = int(self._scale_width * width + self._offset_width)
        h = int(self._scale_height * height + self._offset_height)
        return Rect(x, y, w, h)

    @property
    def scale_x(self) -> float:
        return self._scale_x

    @scale_x.setter
    def scale_x(self, value: float):
        self._scale_x = float(value)

    @property
    def scale_y(self) -> float:
        return self._scale_y

    @scale_y.setter
    def scale_y(self, value: float):
        self._scale_y = float(value)

    @property
    def scale_width(self) -> float:
        return self._scale_width

    @scale_width.setter
    def scale_width(self, value: float):
        self._scale_width = float(value)

    @property
    def scale_height(self) -> float:
        return self._scale_height

    @scale_height.setter
    def scale_height(self, value: float):
        self._scale_height = float(value)

    @property
    def offset_x(self) -> int:
        return self._offset_x

    @offset_x.setter
    def offset_x(self, value: int):
        self._offset_x = int(value)

    @property
    def offset_y(self) -> int:
        return self._offset_y

    @offset_y.setter
    def offset_y(self, value: int):
        self._offset_y = int(value)

    @property
    def offset_width(self) -> int:
        return self._offset_width

    @offset_width.setter
    def offset_width(self, value: int):
        self._offset_width = int(value)

    @property
    def offset_height(self) -> int:
        return self._offset_height

    @offset_height.setter
    def offset_height(self, value: int):
        self._offset_height = int(value)
