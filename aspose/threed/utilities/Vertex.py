class Vertex:
    """Vertex reference, used to access the raw vertex in TriMesh."""

    def compare_to(self, other: 'Vertex') -> int:
        raise NotImplementedError("compare_to is not implemented")

    def read_vector4(self, field: 'VertexField') -> 'Vector4':
        raise NotImplementedError("read_vector4 is not implemented")

    def read_f_vector4(self, field: 'VertexField') -> 'FVector4':
        raise NotImplementedError("read_f_vector4 is not implemented")

    def read_vector3(self, field: 'VertexField') -> 'Vector3':
        raise NotImplementedError("read_vector3 is not implemented")

    def read_f_vector3(self, field: 'VertexField') -> 'FVector3':
        raise NotImplementedError("read_f_vector3 is not implemented")

    def read_vector2(self, field: 'VertexField') -> 'Vector2':
        raise NotImplementedError("read_vector2 is not implemented")

    def read_f_vector2(self, field: 'VertexField') -> 'FVector2':
        raise NotImplementedError("read_f_vector2 is not implemented")

    def read_double(self, field: 'VertexField') -> float:
        raise NotImplementedError("read_double is not implemented")

    def read_float(self, field: 'VertexField') -> float:
        raise NotImplementedError("read_float is not implemented")
