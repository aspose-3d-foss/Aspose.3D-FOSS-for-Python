class ShaderTechnique:
    """A technique in shader material describes the concrete rendering details."""
    
    def __init__(self):
        raise NotImplementedError("ShaderTechnique is not implemented")
    
    @property
    def name(self):
        raise NotImplementedError("ShaderTechnique.name is not implemented")
    
    @name.setter
    def name(self, value):
        raise NotImplementedError("ShaderTechnique.name setter is not implemented")
