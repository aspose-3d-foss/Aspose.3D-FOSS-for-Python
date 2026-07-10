from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .RenderParameters import RenderParameters
    from .WindowHandle import WindowHandle
    from .VertexBuffer import IVertexBuffer
    from .IndexBuffer import IIndexBuffer
    from .ShaderProgram import ShaderProgram
    from .Pipeline import IPipeline
    from .Buffer import IBuffer
    from .DescriptorSet import IDescriptorSet
    from .TextureUnit import ITextureUnit
    from .RenderTexture import IRenderTexture
    from .RenderWindow import IRenderWindow


class RenderFactory:
    """RenderFactory creates all resources that represented in rendering pipeline."""
    
    def __init__(self):
        raise NotImplementedError("RenderFactory is not implemented")
    
    def create_render_texture(self, parameters, targets: int, width: int, height: int):
        raise NotImplementedError("RenderFactory.create_render_texture is not implemented")
    
    def create_render_texture(self, parameters, width: int, height: int):
        raise NotImplementedError("RenderFactory.create_render_texture is not implemented")
    
    def create_texture_unit(self, texture_type=None):
        raise NotImplementedError("RenderFactory.create_texture_unit is not implemented")
    
    def create_descriptor_set(self, shader):
        raise NotImplementedError("RenderFactory.create_descriptor_set is not implemented")
    
    def create_cube_render_texture(self, parameters, width: int, height: int):
        raise NotImplementedError("RenderFactory.create_cube_render_texture is not implemented")
    
    def create_render_window(self, parameters, handle):
        raise NotImplementedError("RenderFactory.create_render_window is not implemented")
    
    def create_vertex_buffer(self, declaration):
        raise NotImplementedError("RenderFactory.create_vertex_buffer is not implemented")
    
    def create_index_buffer(self):
        raise NotImplementedError("RenderFactory.create_index_buffer is not implemented")
    
    def create_shader_program(self, shader_source):
        raise NotImplementedError("RenderFactory.create_shader_program is not implemented")
    
    def create_pipeline(self, shader, render_state, vertex_declaration, draw_operation):
        raise NotImplementedError("RenderFactory.create_pipeline is not implemented")
    
    def create_uniform_buffer(self, size: int):
        raise NotImplementedError("RenderFactory.create_uniform_buffer is not implemented")
