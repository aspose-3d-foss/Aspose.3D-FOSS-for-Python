class VertexDeclaration:
    """The declaration of a custom defined vertex's structure"""

    def __init__(self):
        raise NotImplementedError("__init__ is not implemented")

    def clear(self):
        raise NotImplementedError("clear is not implemented")

    def add_field(self, data_type: 'VertexFieldDataType', semantic: 'VertexFieldSemantic', index: int, alias: str) -> 'VertexField':
        raise NotImplementedError("add_field is not implemented")

    @staticmethod
    def from_geometry(geometry: 'Geometry', use_float: bool) -> 'VertexDeclaration':
        raise NotImplementedError("from_geometry is not implemented")

    def compare_to(self, other: 'VertexDeclaration') -> int:
        raise NotImplementedError("compare_to is not implemented")

    @property
    def sealed(self) -> bool:
        raise NotImplementedError("sealed is not implemented")

    @property
    def count(self) -> int:
        raise NotImplementedError("count is not implemented")

    @property
    def size(self) -> int:
        raise NotImplementedError("size is not implemented")

    def __getitem__(self, key: int) -> 'VertexField':
        raise NotImplementedError("__getitem__ is not implemented")
