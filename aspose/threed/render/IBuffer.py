class IBuffer:
    """Interface for vertex/index buffer."""
    
    def __init__(self):
        raise NotImplementedError("IBuffer is not implemented")
    
    @property
    def size(self):
        raise NotImplementedError("IBuffer.size is not implemented")
    
    def map(self, access):
        raise NotImplementedError("IBuffer.map is not implemented")
    
    def unmap(self):
        raise NotImplementedError("IBuffer.unmap is not implemented")
