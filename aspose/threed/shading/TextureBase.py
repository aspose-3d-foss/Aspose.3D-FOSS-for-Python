class TextureBase:
    """Base class for all texture types."""
    
    def __init__(self):
        raise NotImplementedError("TextureBase is not implemented")
    
    @property
    def name(self):
        raise NotImplementedError("TextureBase.name is not implemented")
    
    @name.setter
    def name(self, value):
        raise NotImplementedError("TextureBase.name setter is not implemented")
