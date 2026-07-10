class IOExtension:
    """Utilities to write matrix/vector to binary writer"""

    @staticmethod
    def write(writer, mat):
        """Write a matrix to binary writer"""
        if hasattr(mat, 'm00'):  # Matrix4 or FMatrix4
            writer.write(mat.m00)
            writer.write(mat.m01)
            writer.write(mat.m02)
            writer.write(mat.m03)
            writer.write(mat.m10)
            writer.write(mat.m11)
            writer.write(mat.m12)
            writer.write(mat.m13)
            writer.write(mat.m20)
            writer.write(mat.m21)
            writer.write(mat.m22)
            writer.write(mat.m23)
            writer.write(mat.m30)
            writer.write(mat.m31)
            writer.write(mat.m32)
            writer.write(mat.m33)
        elif hasattr(mat, 'x'):  # Vector types
            writer.write(mat.x)
            writer.write(mat.y)
            if hasattr(mat, 'z'):
                writer.write(mat.z)
                if hasattr(mat, 'w'):
                    writer.write(mat.w)
