from .utilities import Vector3, Quaternion, Matrix4


class GlobalTransform:
    def __init__(self, matrix: Matrix4):
        self._matrix = matrix
        translation = [None]
        scaling = [None]
        rotation = [None]
        matrix.decompose(translation, scaling, rotation)
        self._translation = translation[0]
        self._scale = scaling[0]
        self._rotation = rotation[0]

    @property
    def translation(self) -> Vector3:
        return self._translation

    @property
    def scale(self) -> Vector3:
        return self._scale

    @property
    def euler_angles(self) -> Vector3:
        return self._rotation.euler_angles()

    @property
    def rotation(self) -> Quaternion:
        return self._rotation

    @property
    def transform_matrix(self) -> Matrix4:
        return self._matrix

    def __repr__(self) -> str:
        return f"GlobalTransform(translation={self._translation}, scale={self._scale})"
