import math
from .A3DObject import A3DObject
from .utilities import Vector3, Quaternion, Matrix4


class Transform(A3DObject):
    def __init__(self, name: str = None):
        super().__init__(name)
        self._translation = Vector3(0, 0, 0)
        self._scaling = Vector3(1, 1, 1)
        self._rotation = Quaternion(1, 0, 0, 0)
        self._euler_angles = Vector3(0, 0, 0)
        self._scaling_offset = Vector3(0, 0, 0)
        self._scaling_pivot = Vector3(0, 0, 0)
        self._rotation_offset = Vector3(0, 0, 0)
        self._rotation_pivot = Vector3(0, 0, 0)
        self._pre_rotation = Vector3(0, 0, 0)
        self._post_rotation = Vector3(0, 0, 0)
        self._geometric_translation = Vector3(0, 0, 0)
        self._geometric_scaling = Vector3(1, 1, 1)
        self._geometric_rotation = Vector3(0, 0, 0)
        self._cached_matrix = None

    @property
    def translation(self) -> Vector3:
        return self._translation

    @translation.setter
    def translation(self, value: Vector3):
        self._translation = value
        self._invalidate_cache()

    @property
    def scaling(self) -> Vector3:
        return self._scaling

    @scaling.setter
    def scaling(self, value: Vector3):
        self._scaling = value
        self._invalidate_cache()

    @property
    def rotation(self) -> Quaternion:
        return self._rotation

    @rotation.setter
    def rotation(self, value: Quaternion):
        self._rotation = value
        self._euler_angles = value.euler_angles()
        self._invalidate_cache()

    @property
    def euler_angles(self) -> Vector3:
        return self._euler_angles

    @euler_angles.setter
    def euler_angles(self, value: Vector3):
        self._euler_angles = value
        self._rotation = Quaternion.from_euler_angle(value)
        self._invalidate_cache()

    @property
    def scaling_offset(self) -> Vector3:
        return self._scaling_offset

    @scaling_offset.setter
    def scaling_offset(self, value: Vector3):
        self._scaling_offset = value
        self._invalidate_cache()

    @property
    def scaling_pivot(self) -> Vector3:
        return self._scaling_pivot

    @scaling_pivot.setter
    def scaling_pivot(self, value: Vector3):
        self._scaling_pivot = value
        self._invalidate_cache()

    @property
    def rotation_offset(self) -> Vector3:
        return self._rotation_offset

    @rotation_offset.setter
    def rotation_offset(self, value: Vector3):
        self._rotation_offset = value
        self._invalidate_cache()

    @property
    def rotation_pivot(self) -> Vector3:
        return self._rotation_pivot

    @rotation_pivot.setter
    def rotation_pivot(self, value: Vector3):
        self._rotation_pivot = value
        self._invalidate_cache()

    @property
    def pre_rotation(self) -> Vector3:
        return self._pre_rotation

    @pre_rotation.setter
    def pre_rotation(self, value: Vector3):
        self._pre_rotation = value
        self._invalidate_cache()

    @property
    def post_rotation(self) -> Vector3:
        return self._post_rotation

    @post_rotation.setter
    def post_rotation(self, value: Vector3):
        self._post_rotation = value
        self._invalidate_cache()

    @property
    def geometric_translation(self) -> Vector3:
        return self._geometric_translation

    @geometric_translation.setter
    def geometric_translation(self, value: Vector3):
        self._geometric_translation = value
        self._invalidate_cache()

    @property
    def geometric_scaling(self) -> Vector3:
        return self._geometric_scaling

    @geometric_scaling.setter
    def geometric_scaling(self, value: Vector3):
        self._geometric_scaling = value
        self._invalidate_cache()

    @property
    def geometric_rotation(self) -> Vector3:
        return self._geometric_rotation

    @geometric_rotation.setter
    def geometric_rotation(self, value: Vector3):
        self._geometric_rotation = value
        self._invalidate_cache()

    @property
    def transform_matrix(self) -> Matrix4:
        if self._cached_matrix is None:
            self._cached_matrix = self._compute_matrix()
        return self._cached_matrix

    @transform_matrix.setter
    def transform_matrix(self, value: Matrix4):
        translation = [None]
        scaling = [None]
        rotation = [None]
        value.decompose(translation, scaling, rotation)
        self._translation = translation[0]
        self._scaling = scaling[0]
        self._rotation = rotation[0]
        self._euler_angles = rotation[0].euler_angles()
        self._invalidate_cache()

    def _compute_matrix(self) -> Matrix4:
        result = Matrix4()

        translation_mat = Matrix4.translate(self._translation)

        scaling_mat = Matrix4.scale(self._scaling)
        scaling_offset_mat = Matrix4.translate(self._scaling_offset)
        scaling_pivot_mat = Matrix4.translate(self._scaling_pivot)
        scaling_pivot_inv_mat = Matrix4.translate(-self._scaling_pivot.x, -self._scaling_pivot.y, -self._scaling_pivot.z)

        rotation_mat = self._rotation.to_matrix()
        rotation_offset_mat = Matrix4.translate(self._rotation_offset)
        rotation_pivot_mat = Matrix4.translate(self._rotation_pivot)
        rotation_pivot_inv_mat = Matrix4.translate(-self._rotation_pivot.x, -self._rotation_pivot.y, -self._rotation_pivot.z)

        pre_rot_mat = Matrix4.rotate_from_euler(self._pre_rotation)
        post_rot_mat = Matrix4.rotate_from_euler(self._post_rotation)

        geo_trans_mat = Matrix4.translate(self._geometric_translation)
        geo_scale_mat = Matrix4.scale(self._geometric_scaling)
        geo_rot_mat = Matrix4.rotate_from_euler(self._geometric_rotation)

        scale_part = scaling_offset_mat.concatenate(scaling_mat).concatenate(scaling_pivot_inv_mat)
        scale_part = scale_part.concatenate(scaling_pivot_mat)

        rotation_part = rotation_offset_mat.concatenate(rotation_mat).concatenate(rotation_pivot_inv_mat)
        rotation_part = pre_rot_mat.concatenate(rotation_part).concatenate(rotation_pivot_mat)
        rotation_part = rotation_part.concatenate(post_rot_mat)

        geometric_part = geo_rot_mat.concatenate(geo_scale_mat).concatenate(geo_trans_mat)

        result = translation_mat.concatenate(scale_part).concatenate(rotation_part).concatenate(geometric_part)

        return result

    def _invalidate_cache(self):
        self._cached_matrix = None

    def set_translation(self, tx: float, ty: float, tz: float) -> 'Transform':
        self._translation = Vector3(float(tx), float(ty), float(tz))
        self._invalidate_cache()
        return self

    def set_scale(self, sx: float, sy: float, sz: float) -> 'Transform':
        self._scaling = Vector3(float(sx), float(sy), float(sz))
        self._invalidate_cache()
        return self

    def set_euler_angles(self, rx: float, ry: float, rz: float) -> 'Transform':
        self._euler_angles = Vector3(float(rx), float(ry), float(rz))
        self._rotation = Quaternion.from_euler_angle(self._euler_angles)
        self._invalidate_cache()
        return self

    def set_rotation(self, rw: float, rx: float, ry: float, rz: float) -> 'Transform':
        self._rotation = Quaternion(float(rw), float(rx), float(ry), float(rz))
        self._euler_angles = self._rotation.euler_angles()
        self._invalidate_cache()
        return self

    def set_pre_rotation(self, rx: float, ry: float, rz: float) -> 'Transform':
        self._pre_rotation = Vector3(float(rx), float(ry), float(rz))
        self._invalidate_cache()
        return self

    def set_post_rotation(self, rx: float, ry: float, rz: float) -> 'Transform':
        self._post_rotation = Vector3(float(rx), float(ry), float(rz))
        self._invalidate_cache()
        return self

    def set_geometric_translation(self, x: float, y: float, z: float) -> 'Transform':
        self._geometric_translation = Vector3(float(x), float(y), float(z))
        self._invalidate_cache()
        return self

    def set_geometric_scaling(self, sx: float, sy: float, sz: float) -> 'Transform':
        self._geometric_scaling = Vector3(float(sx), float(sy), float(sz))
        self._invalidate_cache()
        return self

    def set_geometric_rotation(self, rx: float, ry: float, rz: float) -> 'Transform':
        self._geometric_rotation = Vector3(float(rx), float(ry), float(rz))
        self._invalidate_cache()
        return self

    def __repr__(self) -> str:
        return f"Transform(translation={self._translation})"
