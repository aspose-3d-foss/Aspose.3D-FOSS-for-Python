import math


class Matrix4:
    def __init__(self, *args):
        if len(args) == 0:
            self._m = [1.0, 0.0, 0.0, 0.0,
                       0.0, 1.0, 0.0, 0.0,
                       0.0, 0.0, 1.0, 0.0,
                       0.0, 0.0, 0.0, 1.0]
        elif len(args) == 1:
            arg = args[0]
            if isinstance(arg, list):
                if len(arg) != 16:
                    raise ValueError(f"Matrix requires 16 elements, got {len(arg)}")
                self._m = [float(x) for x in arg]
            else:
                raise TypeError(f"Invalid single argument for Matrix4: {type(arg)}")
        elif len(args) == 16:
            self._m = [float(x) for x in args]
        else:
            raise TypeError(f"Invalid number of arguments for Matrix4: {len(args)}")

    def __getitem__(self, key: int) -> float:
        return self._m[key]

    def __setitem__(self, key: int, value: float):
        self._m[key] = float(value)

    @property
    def m00(self) -> float:
        return self._m[0]

    @m00.setter
    def m00(self, value: float):
        self._m[0] = float(value)

    @property
    def m01(self) -> float:
        return self._m[1]

    @m01.setter
    def m01(self, value: float):
        self._m[1] = float(value)

    @property
    def m02(self) -> float:
        return self._m[2]

    @m02.setter
    def m02(self, value: float):
        self._m[2] = float(value)

    @property
    def m03(self) -> float:
        return self._m[3]

    @m03.setter
    def m03(self, value: float):
        self._m[3] = float(value)

    @property
    def m10(self) -> float:
        return self._m[4]

    @m10.setter
    def m10(self, value: float):
        self._m[4] = float(value)

    @property
    def m11(self) -> float:
        return self._m[5]

    @m11.setter
    def m11(self, value: float):
        self._m[5] = float(value)

    @property
    def m12(self) -> float:
        return self._m[6]

    @m12.setter
    def m12(self, value: float):
        self._m[6] = float(value)

    @property
    def m13(self) -> float:
        return self._m[7]

    @m13.setter
    def m13(self, value: float):
        self._m[7] = float(value)

    @property
    def m20(self) -> float:
        return self._m[8]

    @m20.setter
    def m20(self, value: float):
        self._m[8] = float(value)

    @property
    def m21(self) -> float:
        return self._m[9]

    @m21.setter
    def m21(self, value: float):
        self._m[9] = float(value)

    @property
    def m22(self) -> float:
        return self._m[10]

    @m22.setter
    def m22(self, value: float):
        self._m[10] = float(value)

    @property
    def m23(self) -> float:
        return self._m[11]

    @m23.setter
    def m23(self, value: float):
        self._m[11] = float(value)

    @property
    def m30(self) -> float:
        return self._m[12]

    @m30.setter
    def m30(self, value: float):
        self._m[12] = float(value)

    @property
    def m31(self) -> float:
        return self._m[13]

    @m31.setter
    def m31(self, value: float):
        self._m[13] = float(value)

    @property
    def m32(self) -> float:
        return self._m[14]

    @m32.setter
    def m32(self, value: float):
        self._m[14] = float(value)

    @property
    def m33(self) -> float:
        return self._m[15]

    @m33.setter
    def m33(self, value: float):
        self._m[15] = float(value)

    @property
    def determinant(self) -> float:
        m = self._m
        return (
            m[0] * (m[5] * m[10] * m[15] + m[6] * m[11] * m[13] + m[7] * m[9] * m[14] -
                     m[7] * m[10] * m[13] - m[6] * m[9] * m[15] - m[5] * m[11] * m[14]) -
            m[1] * (m[4] * m[10] * m[15] + m[6] * m[11] * m[12] + m[7] * m[8] * m[14] -
                     m[7] * m[10] * m[12] - m[6] * m[8] * m[15] - m[4] * m[11] * m[14]) +
            m[2] * (m[4] * m[9] * m[15] + m[5] * m[11] * m[12] + m[7] * m[8] * m[13] -
                     m[7] * m[9] * m[12] - m[5] * m[8] * m[15] - m[4] * m[11] * m[13]) -
            m[3] * (m[4] * m[9] * m[14] + m[5] * m[10] * m[12] + m[6] * m[8] * m[13] -
                     m[6] * m[9] * m[12] - m[5] * m[8] * m[14] - m[4] * m[10] * m[13])
        )

    def transpose(self) -> 'Matrix4':
        return Matrix4(
            self._m[0], self._m[4], self._m[8], self._m[12],
            self._m[1], self._m[5], self._m[9], self._m[13],
            self._m[2], self._m[6], self._m[10], self._m[14],
            self._m[3], self._m[7], self._m[11], self._m[15]
        )

    def concatenate(self, m2: 'Matrix4') -> 'Matrix4':
        result = Matrix4()
        for i in range(4):
            for j in range(4):
                result[i * 4 + j] = (
                    self[i * 4 + 0] * m2[0 * 4 + j] +
                    self[i * 4 + 1] * m2[1 * 4 + j] +
                    self[i * 4 + 2] * m2[2 * 4 + j] +
                    self[i * 4 + 3] * m2[3 * 4 + j]
                )
        return result

    def normalize(self) -> 'Matrix4':
        m = self._m
        scale_x = math.sqrt(m[0] ** 2 + m[1] ** 2 + m[2] ** 2)
        scale_y = math.sqrt(m[4] ** 2 + m[5] ** 2 + m[6] ** 2)
        scale_z = math.sqrt(m[8] ** 2 + m[9] ** 2 + m[10] ** 2)

        if scale_x == 0 or scale_y == 0 or scale_z == 0:
            return Matrix4(*m)

        return Matrix4(
            m[0] / scale_x, m[1] / scale_x, m[2] / scale_x, m[3],
            m[4] / scale_y, m[5] / scale_y, m[6] / scale_y, m[7],
            m[8] / scale_z, m[9] / scale_z, m[10] / scale_z, m[11],
            m[12], m[13], m[14], m[15]
        )

    def inverse(self) -> 'Matrix4':
        det = self.determinant
        if abs(det) < 1e-10:
            raise ValueError("Matrix is singular and cannot be inverted")

        inv_det = 1.0 / det
        m = self._m

        inv = Matrix4()
        inv._m[0] = inv_det * (
            m[5] * (m[10] * m[15] - m[11] * m[14]) -
            m[6] * (m[9] * m[15] - m[11] * m[13]) +
            m[7] * (m[9] * m[14] - m[10] * m[13])
        )
        inv._m[1] = -inv_det * (
            m[1] * (m[10] * m[15] - m[11] * m[14]) -
            m[2] * (m[9] * m[15] - m[11] * m[13]) +
            m[3] * (m[9] * m[14] - m[10] * m[13])
        )
        inv._m[2] = inv_det * (
            m[1] * (m[6] * m[15] - m[7] * m[14]) -
            m[2] * (m[5] * m[15] - m[7] * m[13]) +
            m[3] * (m[5] * m[14] - m[6] * m[13])
        )
        inv._m[3] = -inv_det * (
            m[1] * (m[6] * m[11] - m[7] * m[10]) -
            m[2] * (m[5] * m[11] - m[7] * m[9]) +
            m[3] * (m[5] * m[10] - m[6] * m[9])
        )
        inv._m[4] = -inv_det * (
            m[4] * (m[10] * m[15] - m[11] * m[14]) -
            m[6] * (m[8] * m[15] - m[11] * m[12]) +
            m[7] * (m[8] * m[14] - m[10] * m[12])
        )
        inv._m[5] = inv_det * (
            m[0] * (m[10] * m[15] - m[11] * m[14]) -
            m[2] * (m[8] * m[15] - m[11] * m[12]) +
            m[3] * (m[8] * m[14] - m[10] * m[12])
        )
        inv._m[6] = -inv_det * (
            m[0] * (m[6] * m[15] - m[7] * m[14]) -
            m[2] * (m[4] * m[15] - m[7] * m[12]) +
            m[3] * (m[4] * m[14] - m[6] * m[12])
        )
        inv._m[7] = inv_det * (
            m[0] * (m[6] * m[11] - m[7] * m[10]) -
            m[2] * (m[4] * m[11] - m[7] * m[8]) +
            m[3] * (m[4] * m[10] - m[6] * m[8])
        )
        inv._m[8] = inv_det * (
            m[4] * (m[9] * m[15] - m[11] * m[13]) -
            m[5] * (m[8] * m[15] - m[11] * m[12]) +
            m[7] * (m[8] * m[13] - m[9] * m[12])
        )
        inv._m[9] = -inv_det * (
            m[0] * (m[9] * m[15] - m[11] * m[13]) -
            m[1] * (m[8] * m[15] - m[11] * m[12]) +
            m[3] * (m[8] * m[13] - m[9] * m[12])
        )
        inv._m[10] = inv_det * (
            m[0] * (m[5] * m[15] - m[7] * m[13]) -
            m[1] * (m[4] * m[15] - m[7] * m[12]) +
            m[3] * (m[4] * m[13] - m[5] * m[12])
        )
        inv._m[11] = -inv_det * (
            m[0] * (m[5] * m[11] - m[7] * m[9]) -
            m[1] * (m[4] * m[11] - m[7] * m[8]) +
            m[3] * (m[4] * m[9] - m[5] * m[8])
        )
        inv._m[12] = -inv_det * (
            m[4] * (m[9] * m[14] - m[10] * m[13]) -
            m[5] * (m[8] * m[14] - m[10] * m[12]) +
            m[6] * (m[8] * m[13] - m[9] * m[12])
        )
        inv._m[13] = inv_det * (
            m[0] * (m[9] * m[14] - m[10] * m[13]) -
            m[1] * (m[8] * m[14] - m[10] * m[12]) +
            m[2] * (m[8] * m[13] - m[9] * m[12])
        )
        inv._m[14] = -inv_det * (
            m[0] * (m[5] * m[14] - m[6] * m[13]) -
            m[1] * (m[4] * m[14] - m[6] * m[12]) +
            m[2] * (m[4] * m[13] - m[5] * m[12])
        )
        inv._m[15] = inv_det * (
            m[0] * (m[5] * m[10] - m[6] * m[9]) -
            m[1] * (m[4] * m[10] - m[6] * m[8]) +
            m[2] * (m[4] * m[9] - m[5] * m[8])
        )

        return inv

    def decompose(self, translation, scaling, rotation):
        from .Vector3 import Vector3
        from .Quaternion import Quaternion

        m = self._m

        scale_x = math.sqrt(m[0] ** 2 + m[1] ** 2 + m[2] ** 2)
        scale_y = math.sqrt(m[4] ** 2 + m[5] ** 2 + m[6] ** 2)
        scale_z = math.sqrt(m[8] ** 2 + m[9] ** 2 + m[10] ** 2)

        if scale_x < 1e-10:
            scale_x = 1.0
        if scale_y < 1e-10:
            scale_y = 1.0
        if scale_z < 1e-10:
            scale_z = 1.0

        rot_mat = Matrix4(
            m[0] / scale_x, m[1] / scale_x, m[2] / scale_x, 0.0,
            m[4] / scale_y, m[5] / scale_y, m[6] / scale_y, 0.0,
            m[8] / scale_z, m[9] / scale_z, m[10] / scale_z, 0.0,
            0.0, 0.0, 0.0, 1.0
        )

        trace = rot_mat[0] + rot_mat[5] + rot_mat[10]
        if trace > 0.0:
            s = math.sqrt(trace + 1.0) * 2.0
            w = 0.25 * s
            x = (rot_mat[9] - rot_mat[6]) / s
            y = (rot_mat[2] - rot_mat[8]) / s
            z = (rot_mat[4] - rot_mat[1]) / s
        elif rot_mat[0] > rot_mat[5] and rot_mat[0] > rot_mat[10]:
            s = math.sqrt(1.0 + rot_mat[0] - rot_mat[5] - rot_mat[10]) * 2.0
            w = (rot_mat[9] - rot_mat[6]) / s
            x = 0.25 * s
            y = (rot_mat[1] + rot_mat[4]) / s
            z = (rot_mat[2] + rot_mat[8]) / s
        elif rot_mat[5] > rot_mat[10]:
            s = math.sqrt(1.0 + rot_mat[5] - rot_mat[0] - rot_mat[10]) * 2.0
            w = (rot_mat[2] - rot_mat[8]) / s
            x = (rot_mat[1] + rot_mat[4]) / s
            y = 0.25 * s
            z = (rot_mat[6] + rot_mat[9]) / s
        else:
            s = math.sqrt(1.0 + rot_mat[10] - rot_mat[0] - rot_mat[5]) * 2.0
            w = (rot_mat[4] - rot_mat[1]) / s
            x = (rot_mat[2] + rot_mat[8]) / s
            y = (rot_mat[6] + rot_mat[9]) / s
            z = 0.25 * s

        translation[0] = Vector3(m[3], m[7], m[11])
        scaling[0] = Vector3(scale_x, scale_y, scale_z)
        rotation[0] = Quaternion(w, x, y, z)

    def set_trs(self, translation, rotation, scale):
        from .Vector3 import Vector3
        from .Quaternion import Quaternion

        if isinstance(translation, Vector3):
            tx, ty, tz = translation.x, translation.y, translation.z
        else:
            tx, ty, tz = translation[0], translation[1], translation[2]

        if isinstance(rotation, Vector3):
            q = Quaternion.from_euler_angle(rotation)
        elif isinstance(rotation, Quaternion):
            q = rotation
        else:
            rx, ry, rz = rotation[0], rotation[1], rotation[2]
            q = Quaternion.from_euler_angle(rx, ry, rz)

        if isinstance(scale, Vector3):
            sx, sy, sz = scale.x, scale.y, scale.z
        else:
            sx, sy, sz = scale[0], scale[1], scale[2]

        rot_mat = q.to_matrix()

        self._m[0] = rot_mat[0] * sx
        self._m[1] = rot_mat[1] * sx
        self._m[2] = rot_mat[2] * sx
        self._m[3] = tx

        self._m[4] = rot_mat[4] * sy
        self._m[5] = rot_mat[5] * sy
        self._m[6] = rot_mat[6] * sy
        self._m[7] = ty

        self._m[8] = rot_mat[8] * sz
        self._m[9] = rot_mat[9] * sz
        self._m[10] = rot_mat[10] * sz
        self._m[11] = tz

        self._m[12] = 0.0
        self._m[13] = 0.0
        self._m[14] = 0.0
        self._m[15] = 1.0

    def to_array(self):
        return list(self._m)

    @staticmethod
    def get_identity() -> 'Matrix4':
        return Matrix4()

    identity = property(get_identity)

    @staticmethod
    def translate(tx, ty=None, tz=None) -> 'Matrix4':
        if ty is None:
            if isinstance(tx, list) and len(tx) >= 3:
                tx, ty, tz = tx[0], tx[1], tx[2]
            elif hasattr(tx, 'x') and hasattr(tx, 'y') and hasattr(tx, 'z'):
                tx, ty, tz = tx.x, tx.y, tx.z
            else:
                tx, ty, tz = tx, tx, tx
        else:
            tx = float(tx)
            ty = float(ty)
            tz = float(tz)

        return Matrix4(
            1.0, 0.0, 0.0, tx,
            0.0, 1.0, 0.0, ty,
            0.0, 0.0, 1.0, tz,
            0.0, 0.0, 0.0, 1.0
        )

    @staticmethod
    def scale(sx, sy=None, sz=None) -> 'Matrix4':
        if sy is None:
            if isinstance(sx, list) and len(sx) >= 3:
                sx, sy, sz = sx[0], sx[1], sx[2]
            elif hasattr(sx, 'x') and hasattr(sx, 'y') and hasattr(sx, 'z'):
                sx, sy, sz = sx.x, sx.y, sx.z
            else:
                sx, sy, sz = sx, sx, sx
        else:
            sx = float(sx)
            sy = float(sy)
            sz = float(sz)

        return Matrix4(
            sx, 0.0, 0.0, 0.0,
            0.0, sy, 0.0, 0.0,
            0.0, 0.0, sz, 0.0,
            0.0, 0.0, 0.0, 1.0
        )

    @staticmethod
    def rotate_from_euler(rx, ry=None, rz=None) -> 'Matrix4':
        from .Quaternion import Quaternion

        if ry is None:
            if hasattr(rx, 'x') and hasattr(rx, 'y') and hasattr(rx, 'z'):
                rx, ry, rz = rx.x, rx.y, rx.z
            elif isinstance(rx, list) and len(rx) >= 3:
                rx, ry, rz = rx[0], rx[1], rx[2]
            else:
                rx, ry, rz = rx, rx, rx

        rx, ry, rz = float(rx), float(ry), float(rz)

        q = Quaternion.from_euler_angle(rx, ry, rz)
        return q.to_matrix()

    @staticmethod
    def rotate(angle, axis=None) -> 'Matrix4':
        from .Quaternion import Quaternion
        from .Vector3 import Vector3

        if isinstance(angle, Quaternion):
            return angle.to_matrix()

        if axis is None:
            raise TypeError("axis must be specified with angle")

        angle = float(angle)
        return Quaternion.from_angle_axis(angle, axis).to_matrix()

    def __repr__(self) -> str:
        return f"Matrix4({self._m})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Matrix4):
            return False
        return self._m == other._m
