from typing import TYPE_CHECKING

from ..A3DObject import A3DObject

if TYPE_CHECKING:
    from .BoneLinkMode import BoneLinkMode
    from ..Node import Node
    from ..utilities.Matrix4 import Matrix4


class Bone(A3DObject):
    def __init__(self, name: str = None):
        super().__init__(name)
        self._link_mode = None
        self._weights = []
        self._transform = None
        self._bone_transform = None
        self._node = None

    @property
    def link_mode(self) -> 'BoneLinkMode':
        return self._link_mode

    @link_mode.setter
    def link_mode(self, value: 'BoneLinkMode'):
        self._link_mode = value

    def __getitem__(self, key: int) -> float:
        return self.get_weight(key)

    def __setitem__(self, key: int, value: float):
        self.set_weight(key, value)

    @property
    def weight_count(self) -> int:
        return len(self._weights)

    @property
    def transform(self) -> 'Matrix4':
        return self._transform

    @transform.setter
    def transform(self, value: 'Matrix4'):
        self._transform = value

    @property
    def bone_transform(self) -> 'Matrix4':
        return self._bone_transform

    @bone_transform.setter
    def bone_transform(self, value: 'Matrix4'):
        self._bone_transform = value

    @property
    def node(self) -> 'Node':
        if self._node is None:
            raise RuntimeError("Node is not set")
        return self._node

    @node.setter
    def node(self, value: 'Node'):
        self._node = value

    def get_weight(self, index: int) -> float:
        if index < 0 or index >= len(self._weights):
            return 0.0
        return self._weights[index]

    def set_weight(self, index: int, weight: float):
        while len(self._weights) <= index:
            self._weights.append(0.0)
        self._weights[index] = weight
