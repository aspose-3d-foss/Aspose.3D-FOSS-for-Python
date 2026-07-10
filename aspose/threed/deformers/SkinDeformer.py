from typing import TYPE_CHECKING

from .Deformer import Deformer

if TYPE_CHECKING:
    from .Bone import Bone


class SkinDeformer(Deformer):
    def __init__(self, name: str = None):
        if name is None:
            name = "SkinDeformer"
        super().__init__(name)
        self._bones = []

    @property
    def bones(self) -> 'list[Bone]':
        return self._bones
