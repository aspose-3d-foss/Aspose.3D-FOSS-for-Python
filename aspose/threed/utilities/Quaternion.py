import math


class Quaternion:
    def __init__(self, w=None, x=0.0, y=0.0, z=0.0):
        if w is None:
            self._w = 1.0
            self._x = 0.0
            self._y = 0.0
            self._z = 0.0
        else:
            self._w = float(w)
            self._x = float(x)
            self._y = float(y)
            self._z = float(z)

    @property
    def w(self) -> float:
        return self._w

    @w.setter
    def w(self, value: float):
        self._w = float(value)

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float):
        self._x = float(value)

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float):
        self._y = float(value)

    @property
    def z(self) -> float:
        return self._z

    @z.setter
    def z(self, value: float):
        self._z = float(value)

    @property
    def length(self) -> float:
        return math.sqrt(self._w ** 2 + self._x ** 2 + self._y ** 2 + self._z ** 2)

    @staticmethod
    def get_IDENTITY() -> 'Quaternion':
        return Quaternion(1.0, 0.0, 0.0, 0.0)

    IDENTITY = property(get_IDENTITY)

    def normalize(self) -> 'Quaternion':
        len_sq = self._w ** 2 + self._x ** 2 + self._y ** 2 + self._z ** 2
        if len_sq == 0:
            return Quaternion(1.0, 0.0, 0.0, 0.0)
        length = math.sqrt(len_sq)
        return Quaternion(self._w / length, self._x / length,
                       self._y / length, self._z / length)

    def conjugate(self) -> 'Quaternion':
        return Quaternion(self._w, -self._x, -self._y, -self._z)

    def inverse(self) -> 'Quaternion':
        len_sq = self._w ** 2 + self._x ** 2 + self._y ** 2 + self._z ** 2
        if len_sq == 0:
            raise ValueError("Cannot inverse zero-length quaternion")
        conj = self.conjugate()
        inv_len = 1.0 / len_sq
        return Quaternion(conj._w * inv_len, conj._x * inv_len,
                       conj._y * inv_len, conj._z * inv_len)

    def dot(self, q: 'Quaternion') -> float:
        return (self._w * q._w + self._x * q._x +
                self._y * q._y + self._z * q._z)

    def concat(self, rhs: 'Quaternion') -> 'Quaternion':
        return Quaternion(
            self._w * rhs._w - self._x * rhs._x - self._y * rhs._y - self._z * rhs._z,
            self._w * rhs._x + self._x * rhs._w + self._y * rhs._z - self._z * rhs._y,
            self._w * rhs._y - self._x * rhs._z + self._y * rhs._w + self._z * rhs._x,
            self._w * rhs._z + self._x * rhs._y - self._y * rhs._x + self._z * rhs._w
        )

    def euler_angles(self) -> 'Vector3':
        from .Vector3 import Vector3

        sin_x = 2.0 * (self._w * self._x + self._y * self._z)
        cos_x = 1.0 - 2.0 * (self._x ** 2 + self._y ** 2)
        rx = math.atan2(sin_x, cos_x)

        sin_y = 2.0 * (self._w * self._y - self._z * self._x)
        if abs(sin_y) >= 1.0:
            ry = math.copysign(math.pi / 2.0, sin_y)
        else:
            ry = math.asin(sin_y)

        sin_z = 2.0 * (self._w * self._z + self._x * self._y)
        cos_z = 1.0 - 2.0 * (self._y ** 2 + self._z ** 2)
        rz = math.atan2(sin_z, cos_z)

        return Vector3(rx, ry, rz)

    def to_matrix(self, translation=None) -> 'Matrix4':
        from .Matrix4 import Matrix4
        from .Vector3 import Vector3

        xx = self._x * self._x
        xy = self._x * self._y
        xz = self._x * self._z
        xw = self._x * self._w
        yy = self._y * self._y
        yz = self._y * self._z
        yw = self._y * self._w
        zz = self._z * self._z
        zw = self._z * self._w

        m00 = 1.0 - 2.0 * (yy + zz)
        m01 = 2.0 * (xy - zw)
        m02 = 2.0 * (xz + yw)
        m10 = 2.0 * (xy + zw)
        m11 = 1.0 - 2.0 * (xx + zz)
        m12 = 2.0 * (yz - xw)
        m20 = 2.0 * (xz - yw)
        m21 = 2.0 * (yz + xw)
        m22 = 1.0 - 2.0 * (xx + yy)

        if translation is not None:
            if isinstance(translation, Vector3):
                tx, ty, tz = translation.x, translation.y, translation.z
            else:
                tx, ty, tz = translation[0], translation[1], translation[2]
            return Matrix4(
                m00, m01, m02, tx,
                m10, m11, m12, ty,
                m20, m21, m22, tz,
                0.0, 0.0, 0.0, 1.0
            )
        else:
            return Matrix4(
                m00, m01, m02, 0.0,
                m10, m11, m12, 0.0,
                m20, m21, m22, 0.0,
                0.0, 0.0, 0.0, 1.0
            )

    def to_angle_axis(self, angle, axis):
        from .Vector3 import Vector3

        q = self.normalize()
        if q._w > 1.0:
            q = q.normalize()

        angle[0] = 2.0 * math.acos(q._w)
        s = math.sqrt(1.0 - q._w * q._w)

        if s < 0.001:
            axis[0] = Vector3(1.0, 0.0, 0.0)
        else:
            axis[0] = Vector3(q._x / s, q._y / s, q._z / s)

    @staticmethod
    def from_euler_angle(pitch, yaw, roll) -> 'Quaternion':
        from .Vector3 import Vector3

        if isinstance(pitch, Vector3):
            pitch, yaw, roll = pitch.x, pitch.y, pitch.z

        cy = math.cos(yaw * 0.5)
        sy = math.sin(yaw * 0.5)
        cp = math.cos(pitch * 0.5)
        sp = math.sin(pitch * 0.5)
        cr = math.cos(roll * 0.5)
        sr = math.sin(roll * 0.5)

        w = cr * cp * cy + sr * sp * sy
        x = sr * cp * cy - cr * sp * sy
        y = cr * sp * cy + sr * cp * sy
        z = cr * cp * sy - sr * sp * cy

        return Quaternion(w, x, y, z)

    @staticmethod
    def from_angle_axis(a: float, axis) -> 'Quaternion':
        from .Vector3 import Vector3

        half_angle = a * 0.5
        s = math.sin(half_angle)

        if isinstance(axis, Vector3):
            nx, ny, nz = axis.x, axis.y, axis.z
        else:
            nx, ny, nz = axis[0], axis[1], axis[2]

        return Quaternion(
            math.cos(half_angle),
            nx * s,
            ny * s,
            nz * s
        )

    @staticmethod
    def from_rotation(orig, dest) -> 'Quaternion':
        orig_n = orig.normalize()
        dest_n = dest.normalize()

        dot = orig_n.dot(dest_n)

        if dot < -0.999999:
            from .Vector3 import Vector3
            axis = Vector3(1.0, 0.0, 0.0)
            if abs(orig_n.x) < 0.9:
                axis = Vector3(0.0, 1.0, 0.0)
            cross = orig_n.cross(axis).normalize()
            return Quaternion.from_angle_axis(math.pi, cross)
        elif dot > 0.999999:
            return Quaternion(1.0, 0.0, 0.0, 0.0)

        s = math.sqrt((1.0 + dot) * 2.0)
        invs = 1.0 / s
        cross = orig_n.cross(dest_n)

        return Quaternion(
            s * 0.5,
            cross.x * invs,
            cross.y * invs,
            cross.z * invs
        )

    @staticmethod
    def interpolate(t: float, from_q: 'Quaternion', to_q: 'Quaternion') -> 'Quaternion':
        from_q_n = from_q.normalize()
        to_q_n = to_q.normalize()

        dot = from_q_n.dot(to_q_n)

        if dot < 0.0:
            to_q_n = Quaternion(-to_q_n._w, -to_q_n._x, -to_q_n._y, -to_q_n._z)
            dot = -dot

        if dot > 0.9995:
            result = Quaternion(
                from_q_n._w + t * (to_q_n._w - from_q_n._w),
                from_q_n._x + t * (to_q_n._x - from_q_n._x),
                from_q_n._y + t * (to_q_n._y - from_q_n._y),
                from_q_n._z + t * (to_q_n._z - from_q_n._z)
            )
            return result.normalize()

        theta_0 = math.acos(dot)
        theta = theta_0 * t
        sin_theta = math.sin(theta)
        sin_theta_0 = math.sin(theta_0)

        s0 = math.cos(theta) - dot * sin_theta / sin_theta_0
        s1 = sin_theta / sin_theta_0

        return Quaternion(
            s0 * from_q_n._w + s1 * to_q_n._w,
            s0 * from_q_n._x + s1 * to_q_n._x,
            s0 * from_q_n._y + s1 * to_q_n._y,
            s0 * from_q_n._z + s1 * to_q_n._z
        )

    @staticmethod
    def slerp(t: float, v1: 'Quaternion', v2: 'Quaternion') -> 'Quaternion':
        return Quaternion.interpolate(t, v1, v2)

    def get_keyframe_sequence(self, anim, create):
        raise NotImplementedError("get_keyframe_sequence is not implemented")

    def get_bind_point(self, anim, create):
        raise NotImplementedError("get_bind_point is not implemented")

    def __repr__(self) -> str:
        return f"Quaternion({self._w}, {self._x}, {self._y}, {self._z})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Quaternion):
            return False
        return (self._w == other._w and self._x == other._x and
                self._y == other._y and self._z == other._z)
