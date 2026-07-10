from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .NurbsType import NurbsType


class NurbsDirection:
    def __init__(self):
        self._knot_vectors = []
        self._multiplicity = []
        self._order = 3
        self._degree = 2
        self._divisions = 10
        self._type = None
        self._count = 4

    @property
    def knot_vectors(self):
        return self._knot_vectors

    @property
    def multiplicity(self):
        return self._multiplicity

    @property
    def order(self) -> int:
        return self._order

    @order.setter
    def order(self, value: int):
        self._order = value

    @property
    def degree(self) -> int:
        return self._degree

    @degree.setter
    def degree(self, value: int):
        self._degree = value

    @property
    def divisions(self) -> int:
        return self._divisions

    @divisions.setter
    def divisions(self, value: int):
        self._divisions = value

    @property
    def type(self) -> 'NurbsType':
        return self._type

    @type.setter
    def type(self, value: 'NurbsType'):
        self._type = value

    @property
    def count(self) -> int:
        return self._count

    @count.setter
    def count(self, value: int):
        self._count = value
