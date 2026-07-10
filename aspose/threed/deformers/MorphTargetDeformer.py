from typing import TYPE_CHECKING

from .Deformer import Deformer

if TYPE_CHECKING:
    from .MorphTargetChannel import MorphTargetChannel


class MorphTargetDeformer(Deformer):
    def __init__(self, name: str = None):
        if name is None:
            name = "MorphTargetDeformer"
        super().__init__(name)
        self._channels = []

    @property
    def channels(self) -> 'list[MorphTargetChannel]':
        return self._channels

    def __getitem__(self, key: int) -> float:
        if len(self._channels) > key:
            return self._channels[key].channel_weight
        return 0.0

    def __setitem__(self, key: int, value: float):
        while len(self._channels) <= key:
            self._channels.append(MorphTargetChannel())
        self._channels[key].channel_weight = value
