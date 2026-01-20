from .A3DObject import A3DObject


class SceneObject(A3DObject):
    def __init__(self, name: str = None):
        super().__init__(name)
        self._scene = None

    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
