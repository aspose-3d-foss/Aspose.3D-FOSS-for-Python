from typing import List, TYPE_CHECKING

from ..SceneObject import SceneObject


if TYPE_CHECKING:
    from .AnimationNode import AnimationNode


class AnimationClip(SceneObject):
    def __init__(self, name: str = None):
        super().__init__(name)
        self._animations: List[AnimationNode] = []
        self._description = ""
        self._start = 0.0
        self._stop = 0.0

    def create_animation_node(self, node_name: str) -> 'AnimationNode':
        from .AnimationNode import AnimationNode
        node = AnimationNode(node_name)
        self._animations.append(node)
        return node

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
    def animations(self) -> List['AnimationNode']:
        return list(self._animations)

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value

    @property
    def start(self) -> float:
        return self._start

    @start.setter
    def start(self, value: float):
        self._start = value

    @property
    def stop(self) -> float:
        return self._stop

    @stop.setter
    def stop(self, value: float):
        self._stop = value
