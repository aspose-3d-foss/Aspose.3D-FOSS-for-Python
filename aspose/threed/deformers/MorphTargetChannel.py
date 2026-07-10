from typing import TYPE_CHECKING

from ..A3DObject import A3DObject

if TYPE_CHECKING:
    from ..entities.Shape import Shape


class MorphTargetChannel(A3DObject):
    DEFAULT_WEIGHT = 1.0

    def __init__(self, name: str = None):
        super().__init__(name)
        self._weights = []
        self._channel_weight = 0.0
        self._targets = []

    @property
    def weights(self) -> 'list[float]':
        return self._weights

    @property
    def channel_weight(self) -> float:
        return self._channel_weight

    @channel_weight.setter
    def channel_weight(self, value: float):
        self._channel_weight = value

    @property
    def targets(self) -> 'list[Shape]':
        return self._targets

    def __getitem__(self, key: int) -> float:
        return self.get_weight(key)

    def __setitem__(self, key: int, value: float):
        self.set_weight(key, value)

    def get_weight(self, target: 'Shape') -> float:
        try:
            index = self._targets.index(target)
        except ValueError:
            index = -1
        if index < 0 or index >= len(self._weights):
            return 0.0
        return self._weights[index]

    def set_weight(self, target: 'Shape', weight: float):
        try:
            index = self._targets.index(target)
        except ValueError:
            index = -1
        if index < 0:
            self._targets.append(target)
            self._weights.append(weight)
        else:
            self._weights[index] = weight

    def get_weight(self, index: int) -> float:
        if index < 0 or index >= len(self._weights):
            return 0.0
        return self._weights[index]

    def set_weight(self, index: int, weight: float):
        while len(self._weights) <= index:
            self._weights.append(0.0)
        self._weights[index] = weight
