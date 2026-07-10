class EntityRendererKey:
    """The key of registered entity renderer."""
    
    def __init__(self, name: str):
        self._name = name
    
    def __repr__(self):
        return f"EntityRendererKey({self._name!r})"
    
    def __str__(self):
        return self._name
    
    def __eq__(self, other):
        if isinstance(other, EntityRendererKey):
            return self._name == other._name
        return False
    
    def __hash__(self):
        return hash(self._name)
