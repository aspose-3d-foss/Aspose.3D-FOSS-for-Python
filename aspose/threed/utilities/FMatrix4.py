class FMatrix4:
    """Matrix 4x4 with all component in float type"""

    def __init__(self, m00: float = 0.0, m01: float = 0.0, m02: float = 0.0, m03: float = 0.0,
                 m10: float = 0.0, m11: float = 0.0, m12: float = 0.0, m13: float = 0.0,
                 m20: float = 0.0, m21: float = 0.0, m22: float = 0.0, m23: float = 0.0,
                 m30: float = 0.0, m31: float = 0.0, m32: float = 0.0, m33: float = 0.0):
        self._m00 = float(m00)
        self._m01 = float(m01)
        self._m02 = float(m02)
        self._m03 = float(m03)
        self._m10 = float(m10)
        self._m11 = float(m11)
        self._m12 = float(m12)
        self._m13 = float(m13)
        self._m20 = float(m20)
        self._m21 = float(m21)
        self._m22 = float(m22)
        self._m23 = float(m23)
        self._m30 = float(m30)
        self._m31 = float(m31)
        self._m32 = float(m32)
        self._m33 = float(m33)

    @property
    def m00(self) -> float:
        return self._m00

    @m00.setter
    def m00(self, value: float):
        self._m00 = float(value)

    @property
    def m01(self) -> float:
        return self._m01

    @m01.setter
    def m01(self, value: float):
        self._m01 = float(value)

    @property
    def m02(self) -> float:
        return self._m02

    @m02.setter
    def m02(self, value: float):
        self._m02 = float(value)

    @property
    def m03(self) -> float:
        return self._m03

    @m03.setter
    def m03(self, value: float):
        self._m03 = float(value)

    @property
    def m10(self) -> float:
        return self._m10

    @m10.setter
    def m10(self, value: float):
        self._m10 = float(value)

    @property
    def m11(self) -> float:
        return self._m11

    @m11.setter
    def m11(self, value: float):
        self._m11 = float(value)

    @property
    def m12(self) -> float:
        return self._m12

    @m12.setter
    def m12(self, value: float):
        self._m12 = float(value)

    @property
    def m13(self) -> float:
        return self._m13

    @m13.setter
    def m13(self, value: float):
        self._m13 = float(value)

    @property
    def m20(self) -> float:
        return self._m20

    @m20.setter
    def m20(self, value: float):
        self._m20 = float(value)

    @property
    def m21(self) -> float:
        return self._m21

    @m21.setter
    def m21(self, value: float):
        self._m21 = float(value)

    @property
    def m22(self) -> float:
        return self._m22

    @m22.setter
    def m22(self, value: float):
        self._m22 = float(value)

    @property
    def m23(self) -> float:
        return self._m23

    @m23.setter
    def m23(self, value: float):
        self._m23 = float(value)

    @property
    def m30(self) -> float:
        return self._m30

    @m30.setter
    def m30(self, value: float):
        self._m30 = float(value)

    @property
    def m31(self) -> float:
        return self._m31

    @m31.setter
    def m31(self, value: float):
        self._m31 = float(value)

    @property
    def m32(self) -> float:
        return self._m32

    @m32.setter
    def m32(self, value: float):
        self._m32 = float(value)

    @property
    def m33(self) -> float:
        return self._m33

    @m33.setter
    def m33(self, value: float):
        self._m33 = float(value)

    @property
    def identity(self) -> 'FMatrix4':
        """Returns the identity matrix"""
        from .Matrix4 import Matrix4
        return FMatrix4.from_matrix(Matrix4.identity())

    @staticmethod
    def from_matrix(mat: 'Matrix4') -> 'FMatrix4':
        raise NotImplementedError("from_matrix is not implemented")

    def concatenate(self, m2: 'FMatrix4') -> 'FMatrix4':
        raise NotImplementedError("concatenate is not implemented")

    def concatenate(self, m2: 'Matrix4') -> 'FMatrix4':
        raise NotImplementedError("concatenate is not implemented")

    def transpose(self) -> 'FMatrix4':
        raise NotImplementedError("transpose is not implemented")

    def inverse(self) -> 'FMatrix4':
        raise NotImplementedError("inverse is not implemented")

    def __mul__(self, other):
        from .FVector4 import FVector4
        from .FVector3 import FVector3
        if isinstance(other, FVector4):
            return FVector4(
                self._m00 * other.x + self._m01 * other.y + self._m02 * other.z + self._m03 * other.w,
                self._m10 * other.x + self._m11 * other.y + self._m12 * other.z + self._m13 * other.w,
                self._m20 * other.x + self._m21 * other.y + self._m22 * other.z + self._m23 * other.w,
                self._m30 * other.x + self._m31 * other.y + self._m32 * other.z + self._m33 * other.w
            )
        elif isinstance(other, FVector3):
            return FVector3(
                self._m00 * other.x + self._m01 * other.y + self._m02 * other.z + self._m03,
                self._m10 * other.x + self._m11 * other.y + self._m12 * other.z + self._m13,
                self._m20 * other.x + self._m21 * other.y + self._m22 * other.z + self._m23
            )
        elif isinstance(other, (int, float)):
            return FMatrix4(
                self._m00 * other, self._m01 * other, self._m02 * other, self._m03 * other,
                self._m10 * other, self._m11 * other, self._m12 * other, self._m13 * other,
                self._m20 * other, self._m21 * other, self._m22 * other, self._m23 * other,
                self._m30 * other, self._m31 * other, self._m32 * other, self._m33 * other
            )
        elif isinstance(other, FMatrix4):
            return FMatrix4(
                self._m00 * other._m00 + self._m01 * other._m10 + self._m02 * other._m20 + self._m03 * other._m30,
                self._m00 * other._m01 + self._m01 * other._m11 + self._m02 * other._m21 + self._m03 * other._m31,
                self._m00 * other._m02 + self._m01 * other._m12 + self._m02 * other._m22 + self._m03 * other._m32,
                self._m00 * other._m03 + self._m01 * other._m13 + self._m02 * other._m23 + self._m03 * other._m33,
                self._m10 * other._m00 + self._m11 * other._m10 + self._m12 * other._m20 + self._m13 * other._m30,
                self._m10 * other._m01 + self._m11 * other._m11 + self._m12 * other._m21 + self._m13 * other._m31,
                self._m10 * other._m02 + self._m11 * other._m12 + self._m12 * other._m22 + self._m13 * other._m32,
                self._m10 * other._m03 + self._m11 * other._m13 + self._m12 * other._m23 + self._m13 * other._m33,
                self._m20 * other._m00 + self._m21 * other._m10 + self._m22 * other._m20 + self._m23 * other._m30,
                self._m20 * other._m01 + self._m21 * other._m11 + self._m22 * other._m21 + self._m23 * other._m31,
                self._m20 * other._m02 + self._m21 * other._m12 + self._m22 * other._m22 + self._m23 * other._m32,
                self._m20 * other._m03 + self._m21 * other._m13 + self._m22 * other._m23 + self._m23 * other._m33,
                self._m30 * other._m00 + self._m31 * other._m10 + self._m32 * other._m20 + self._m33 * other._m30,
                self._m30 * other._m01 + self._m31 * other._m11 + self._m32 * other._m21 + self._m33 * other._m31,
                self._m30 * other._m02 + self._m31 * other._m12 + self._m32 * other._m22 + self._m33 * other._m32,
                self._m30 * other._m03 + self._m31 * other._m13 + self._m32 * other._m23 + self._m33 * other._m33
            )
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)
