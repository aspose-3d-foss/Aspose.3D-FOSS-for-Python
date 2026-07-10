class ShaderStage:
    """Shader stage."""
    
    VERTEX = None
    FRAGMENT = None
    GEOMETRY = None
    TESSELLATION_CONTROL = None
    TESSELLATION_EVALUATION = None
    COMPUTE = None


# Initialize enum values
ShaderStage.VERTEX = ShaderStage()
ShaderStage.FRAGMENT = ShaderStage()
ShaderStage.GEOMETRY = ShaderStage()
ShaderStage.TESSELLATION_CONTROL = ShaderStage()
ShaderStage.TESSELLATION_EVALUATION = ShaderStage()
ShaderStage.COMPUTE = ShaderStage()
