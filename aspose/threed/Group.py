from typing import TYPE_CHECKING

from .A3DObject import A3DObject

if TYPE_CHECKING:
    from .Node import Node


class Group(A3DObject):
    """A Group represents the logical relationships of Node."""

    def __init__(self, name: str):
        super().__init__(name if name is not None else "Group")
        self._parent = None
        self._groups = []
        self._nodes = []

    @property
    def parent(self) -> 'Group':
        """Parent group of current group."""
        return self._parent

    @property
    def groups(self):
        """Sub-groups."""
        return list(self._groups)

    @property
    def nodes(self):
        """The nodes in this group."""
        return list(self._nodes)

    def __repr__(self) -> str:
        return f"Group({self._name})"
