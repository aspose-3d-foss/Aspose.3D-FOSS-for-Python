from typing import TYPE_CHECKING

from .Curve import Curve

if TYPE_CHECKING:
    from .utilities.Vector4 import Vector4
    from .CurveDimension import CurveDimension
    from .NurbsType import NurbsType


class NurbsCurve(Curve):
    def __init__(self, name: str = None):
        if name is None:
            name = "NurbsCurve"
        super().__init__(name)
        self._control_points = []
        self._multiplicity = []
        self._knot_vectors = []
        self._order = 2
        self._curve_type = None
        self._dimension = None
        self._rational = False
        self._init_defaults()

    def _init_defaults(self):
        from .NurbsType import NurbsType
        from .CurveDimension import CurveDimension
        self._curve_type = NurbsType.OPEN
        self._dimension = CurveDimension.THREE_DIMENSIONAL

    @property
    def control_points(self):
        return self._control_points

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
        return self._order - 1

    @degree.setter
    def degree(self, value: int):
        self._order = value + 1

    @property
    def dimension(self) -> 'CurveDimension':
        return self._dimension

    @dimension.setter
    def dimension(self, value: 'CurveDimension'):
        self._dimension = value

    @property
    def curve_type(self) -> 'NurbsType':
        return self._curve_type

    @curve_type.setter
    def curve_type(self, value: 'NurbsType'):
        self._curve_type = value

    @property
    def knot_vectors(self):
        return self._knot_vectors

    @property
    def rational(self) -> bool:
        return self._rational

    @rational.setter
    def rational(self, value: bool):
        self._rational = bool(value)

    def evaluate(self, steps: int):
        raise NotImplementedError("NURBS curve evaluation is not implemented")

    def evaluate_at(self, u: float):
        raise NotImplementedError("NURBS curve evaluation is not implemented")
