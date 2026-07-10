class SemanticAttribute:
    """Allow user to use their own structure for static declaration of VertexDeclaration"""

    def __init__(self, semantic: 'VertexFieldSemantic', alias: str = None):
        self._semantic = semantic
        self._alias = alias if alias is not None else ""

    @property
    def semantic(self) -> 'VertexFieldSemantic':
        return self._semantic

    @property
    def alias(self) -> str:
        return self._alias
