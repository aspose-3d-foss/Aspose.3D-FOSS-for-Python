class IDescriptorSet:
    """Interface for descriptor set."""
    
    def __init__(self):
        raise NotImplementedError("IDescriptorSet is not implemented")
    
    def set_buffer(self, binding, buffer):
        raise NotImplementedError("IDescriptorSet.set_buffer is not implemented")
    
    def set_texture(self, binding, texture):
        raise NotImplementedError("IDescriptorSet.set_texture is not implemented")
