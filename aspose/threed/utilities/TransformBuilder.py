class TransformBuilder:
    """The TransformBuilder is used to build transform matrix by a chain of transformations."""

    def __init__(self, initial: 'Matrix4' = None, order: 'ComposeOrder' = None):
        raise NotImplementedError("__init__ is not implemented")

    def scale(self, s: float) -> 'TransformBuilder':
        raise NotImplementedError("scale is not implemented")

    def scale(self, x: float, y: float, z: float) -> 'TransformBuilder':
        raise NotImplementedError("scale is not implemented")

    def scale(self, s: 'Vector3') -> 'TransformBuilder':
        raise NotImplementedError("scale is not implemented")

    def rotate_degree(self, angle: float, axis: 'Vector3') -> 'TransformBuilder':
        raise NotImplementedError("rotate_degree is not implemented")

    def rotate_degree(self, rot: 'Vector3', order: 'RotationOrder'):
        raise NotImplementedError("rotate_degree is not implemented")

    def rotate_radian(self, angle: float, axis: 'Vector3') -> 'TransformBuilder':
        raise NotImplementedError("rotate_radian is not implemented")

    def rotate_radian(self, rot: 'Vector3', order: 'RotationOrder'):
        raise NotImplementedError("rotate_radian is not implemented")

    def rotate_euler_radian(self, x: float, y: float, z: float) -> 'TransformBuilder':
        raise NotImplementedError("rotate_euler_radian is not implemented")

    def rotate_euler_radian(self, r: 'Vector3') -> 'TransformBuilder':
        raise NotImplementedError("rotate_euler_radian is not implemented")

    def translate(self, tx: float, ty: float, tz: float) -> 'TransformBuilder':
        raise NotImplementedError("translate is not implemented")

    def translate(self, v: 'Vector3') -> 'TransformBuilder':
        raise NotImplementedError("translate is not implemented")

    def compose(self, m: 'Matrix4'):
        raise NotImplementedError("compose is not implemented")

    def append(self, m: 'Matrix4') -> 'TransformBuilder':
        raise NotImplementedError("append is not implemented")

    def prepend(self, m: 'Matrix4') -> 'TransformBuilder':
        raise NotImplementedError("prepend is not implemented")

    def rearrange(self, new_x: 'Axis', new_y: 'Axis', new_z: 'Axis') -> 'TransformBuilder':
        raise NotImplementedError("rearrange is not implemented")

    def rotate(self, q: 'Quaternion') -> 'TransformBuilder':
        raise NotImplementedError("rotate is not implemented")

    def rotate_euler_degree(self, deg_x: float, deg_y: float, deg_z: float) -> 'TransformBuilder':
        raise NotImplementedError("rotate_euler_degree is not implemented")

    def reset(self):
        raise NotImplementedError("reset is not implemented")

    @property
    def matrix(self) -> 'Matrix4':
        raise NotImplementedError("matrix is not implemented")

    @matrix.setter
    def matrix(self, value: 'Matrix4'):
        raise NotImplementedError("matrix setter is not implemented")

    @property
    def compose_order(self) -> 'ComposeOrder':
        raise NotImplementedError("compose_order is not implemented")

    @compose_order.setter
    def compose_order(self, value: 'ComposeOrder'):
        raise NotImplementedError("compose_order setter is not implemented")
