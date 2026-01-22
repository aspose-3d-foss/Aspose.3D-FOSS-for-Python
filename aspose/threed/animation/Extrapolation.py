from typing import TYPE_CHECKING
from .ExtrapolationType import ExtrapolationType


class Extrapolation:
    def __init__(self):
        self._type = ExtrapolationType.CONSTANT
        self._repeat_count = 0

    @property
    def type(self) -> ExtrapolationType:
        return self._type

    @type.setter
    def type(self, value: ExtrapolationType):
        self._type = value

    @property
    def repeat_count(self) -> int:
        return self._repeat_count

    @repeat_count.setter
    def repeat_count(self, value: int):
        self._repeat_count = value
