from typing import TYPE_CHECKING
from .Interpolation import Interpolation
from .WeightedMode import WeightedMode
from .StepMode import StepMode


if TYPE_CHECKING:
    from .KeyframeSequence import KeyframeSequence
    from aspose.threed.utilities import Vector2


class KeyFrame:
    def __init__(self, curve: 'KeyframeSequence', time: float):
        self._curve = curve
        self._time = time
        self._value = 0.0
        self._interpolation = Interpolation.LINEAR
        self._tangent_weight_mode = WeightedMode.NONE
        self._step_mode = StepMode.PREVIOUS_VALUE
        self._next_in_tangent = None
        self._out_tangent = None
        self._out_weight = 0.0
        self._next_in_weight = 0.0
        self._tension = 0.0
        self._continuity = 0.0
        self._bias = 0.0
        self._independent_tangent = False
        self._flat = False
        self._time_independent_tangent = False

    @property
    def time(self) -> float:
        return self._time

    @time.setter
    def time(self, value: float):
        self._time = value

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value: float):
        self._value = value

    @property
    def interpolation(self) -> Interpolation:
        return self._interpolation

    @interpolation.setter
    def interpolation(self, value: Interpolation):
        self._interpolation = value

    @property
    def tangent_weight_mode(self) -> WeightedMode:
        return self._tangent_weight_mode

    @tangent_weight_mode.setter
    def tangent_weight_mode(self, value: WeightedMode):
        self._tangent_weight_mode = value

    @property
    def step_mode(self) -> StepMode:
        return self._step_mode

    @step_mode.setter
    def step_mode(self, value: StepMode):
        self._step_mode = value

    @property
    def next_in_tangent(self) -> 'Vector2':
        return self._next_in_tangent

    @next_in_tangent.setter
    def next_in_tangent(self, value: 'Vector2'):
        self._next_in_tangent = value

    @property
    def out_tangent(self) -> 'Vector2':
        return self._out_tangent

    @out_tangent.setter
    def out_tangent(self, value: 'Vector2'):
        self._out_tangent = value

    @property
    def out_weight(self) -> float:
        return self._out_weight

    @out_weight.setter
    def out_weight(self, value: float):
        self._out_weight = value

    @property
    def next_in_weight(self) -> float:
        return self._next_in_weight

    @next_in_weight.setter
    def next_in_weight(self, value: float):
        self._next_in_weight = value

    @property
    def tension(self) -> float:
        return self._tension

    @tension.setter
    def tension(self, value: float):
        self._tension = value

    @property
    def continuity(self) -> float:
        return self._continuity

    @continuity.setter
    def continuity(self, value: float):
        self._continuity = value

    @property
    def bias(self) -> float:
        return self._bias

    @bias.setter
    def bias(self, value: float):
        self._bias = value

    @property
    def independent_tangent(self) -> bool:
        return self._independent_tangent

    @independent_tangent.setter
    def independent_tangent(self, value: bool):
        self._independent_tangent = value

    @property
    def flat(self) -> bool:
        return self._flat

    @flat.setter
    def flat(self, value: bool):
        self._flat = value

    @property
    def time_independent_tangent(self) -> bool:
        return self._time_independent_tangent

    @time_independent_tangent.setter
    def time_independent_tangent(self, value: bool):
        self._time_independent_tangent = value
