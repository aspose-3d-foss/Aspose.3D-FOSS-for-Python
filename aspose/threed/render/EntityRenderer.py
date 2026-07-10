class EntityRenderer:
    """Base class for rendering entities."""
    
    def __init__(self):
        raise NotImplementedError("EntityRenderer is not implemented")
    
    @property
    def name(self):
        raise NotImplementedError("EntityRenderer.name is not implemented")
    
    def begin(self):
        raise NotImplementedError("EntityRenderer.begin is not implemented")
    
    def render(self, entity, context):
        raise NotImplementedError("EntityRenderer.render is not implemented")
    
    def end(self):
        raise NotImplementedError("EntityRenderer.end is not implemented")
