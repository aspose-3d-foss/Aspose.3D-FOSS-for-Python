from typing import List, TYPE_CHECKING, Any

from ..A3DObject import A3DObject
from .Interpolation import Interpolation
from .Extrapolation import Extrapolation


if TYPE_CHECKING:
    from .BindPoint import BindPoint
    from .KeyFrame import KeyFrame


class KeyframeSequence(A3DObject):
    def __init__(self, name: str = None):
        super().__init__(name)
        self._key_frames: List['KeyFrame'] = []
        self._bind_point: 'BindPoint' = None
        self._pre_behavior = Extrapolation()
        self._post_behavior = Extrapolation()

    def reset(self):
        self._key_frames.clear()
        self._pre_behavior = Extrapolation()
        self._post_behavior = Extrapolation()

    def add(self, time: float, value: float, interpolation: Interpolation = Interpolation.LINEAR):
        from .KeyFrame import KeyFrame
        key_frame = KeyFrame(self, time)
        key_frame.value = value
        key_frame.interpolation = interpolation
        self._key_frames.append(key_frame)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def properties(self):
        return self._properties

    @property
    def bind_point(self) -> 'BindPoint':
        return self._bind_point

    @property
    def key_frames(self) -> List['KeyFrame']:
        return list(self._key_frames)

    @property
    def post_behavior(self) -> Extrapolation:
        return self._post_behavior

    @property
    def pre_behavior(self) -> Extrapolation:
        return self._pre_behavior
