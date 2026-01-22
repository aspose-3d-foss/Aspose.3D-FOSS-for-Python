from typing import TYPE_CHECKING, Any

from .KeyframeSequence import KeyframeSequence
from .Interpolation import Interpolation


if TYPE_CHECKING:
    from .BindPoint import BindPoint
    from .KeyFrame import KeyFrame


class AnimationChannel(KeyframeSequence):
    def __init__(self, name: str = None):
        super().__init__(name)
        self._component_type = None
        self._default_value = None
        self._keyframe_sequence: KeyframeSequence = None

    @property
    def component_type(self):
        return self._component_type

    @property
    def default_value(self) -> Any:
        return self._default_value

    @default_value.setter
    def default_value(self, value: Any):
        self._default_value = value

    @property
    def keyframe_sequence(self) -> KeyframeSequence:
        return self._keyframe_sequence

    @keyframe_sequence.setter
    def keyframe_sequence(self, value: KeyframeSequence):
        self._keyframe_sequence = value
