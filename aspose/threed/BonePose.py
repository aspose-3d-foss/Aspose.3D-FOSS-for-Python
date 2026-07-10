from aspose.threed import A3DObject
from aspose.threed import Node
from aspose.threed.utilities import Matrix4


class BonePose(A3DObject):
    def __init__(self):
        super().__init__()
        self._node = None
        self._matrix = Matrix4()
        self._is_local = False

    @property
    def node(self) -> Node:
        return self._node

    @node.setter
    def node(self, value: Node):
        self._node = value

    @property
    def matrix(self) -> Matrix4:
        return self._matrix

    @matrix.setter
    def matrix(self, value: Matrix4):
        self._matrix = value

    @property
    def is_local(self) -> bool:
        return self._is_local

    @is_local.setter
    def is_local(self, value: bool):
        self._is_local = value
