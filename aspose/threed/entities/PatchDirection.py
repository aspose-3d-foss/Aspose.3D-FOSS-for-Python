class PatchDirection:
    def __init__(self):
        self._type = None
        self._divisions = 0
        self._control_points = 0
        self._closed = False

    @property
    def type(self) -> 'PatchDirectionType':
        return self._type

    @type.setter
    def type(self, value: 'PatchDirectionType'):
        self._type = value

    @property
    def divisions(self) -> int:
        return self._divisions

    @divisions.setter
    def divisions(self, value: int):
        self._divisions = value

    @property
    def control_points(self) -> int:
        return self._control_points

    @control_points.setter
    def control_points(self, value: int):
        self._control_points = value

    @property
    def closed(self) -> bool:
        return self._closed

    @closed.setter
    def closed(self, value: bool):
        self._closed = value
