from .A3DObject import A3DObject


class CustomObject(A3DObject):
    def __init__(self, name: str = None):
        super().__init__(name)
