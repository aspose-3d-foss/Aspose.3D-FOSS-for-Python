from typing import List, Optional, TYPE_CHECKING

from .SceneObject import SceneObject
from .utilities import BoundingBox

if TYPE_CHECKING:
    from .Node import Node


class Entity(SceneObject):
    def __init__(self, name: str = None):
        super().__init__(name)
        self._parent_nodes: List['Node'] = []
        self._excluded = False

    @property
    def parent_nodes(self) -> List['Node']:
        return list(self._parent_nodes)

    @property
    def parent_node(self) -> Optional['Node']:
        return self._parent_nodes[0] if self._parent_nodes else None

    @parent_node.setter
    def parent_node(self, value: Optional['Node']):
        if value in self._parent_nodes:
            if len(self._parent_nodes) > 1 or self._parent_nodes[0] != value:
                self._parent_nodes.clear()
                self._parent_nodes.append(value)
        elif value is not None:
            self._parent_nodes.clear()
            self._parent_nodes.append(value)

    @property
    def excluded(self) -> bool:
        return self._excluded

    @excluded.setter
    def excluded(self, value: bool):
        self._excluded = bool(value)

    def get_bounding_box(self) -> BoundingBox:
        raise NotImplementedError("get_bounding_box is not implemented for base Entity class")

    def get_entity_renderer_key(self):
        raise NotImplementedError("get_entity_renderer_key is not implemented for base Entity class")
