class IRenderTarget:
    """Interface for render target."""
    
    def __init__(self):
        raise NotImplementedError("IRenderTarget is not implemented")
    
    @property
    def width(self):
        raise NotImplementedError("IRenderTarget.width is not implemented")
    
    @property
    def height(self):
        raise NotImplementedError("IRenderTarget.height is not implemented")
