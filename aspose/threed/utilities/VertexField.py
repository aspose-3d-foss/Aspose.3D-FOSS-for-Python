class VertexField:
    """Vertex's field memory layout description."""

    def compare_to(self, other: 'VertexField') -> int:
        raise NotImplementedError("compare_to is not implemented")

    @property
    def data_type(self) -> 'VertexFieldDataType':
        raise NotImplementedError("data_type is not implemented")

    @property
    def semantic(self) -> 'VertexFieldSemantic':
        raise NotImplementedError("semantic is not implemented")

    @property
    def alias(self) -> str:
        raise NotImplementedError("alias is not implemented")

    @property
    def index(self) -> int:
        raise NotImplementedError("index is not implemented")

    @property
    def offset(self) -> int:
        raise NotImplementedError("offset is not implemented")

    @property
    def size(self) -> int:
        raise NotImplementedError("size is not implemented")
