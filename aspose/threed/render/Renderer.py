from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .PostProcessing import PostProcessing
    from .IRenderTarget import IRenderTarget
    from .ShaderSet import ShaderSet
    from .RendererVariableManager import RendererVariableManager
    from .PresetShaders import PresetShaders
    from .RenderFactory import RenderFactory
    from .RenderStage import RenderStage
    from .EntityRenderer import EntityRenderer
    from .ShaderProgram import ShaderProgram
    from .shading.Material import Material
    from .IRenderTarget import IRenderTarget
    from ..Node import Node
    from ..entities.Frustum import Frustum


class Renderer:
    """The context about renderer."""
    
    def __init__(self):
        raise NotImplementedError("Renderer is not implemented")
    
    def clear_cache(self) -> None:
        raise NotImplementedError("Renderer.clear_cache is not implemented")
    
    def get_post_processing(self, name: str):
        raise NotImplementedError("Renderer.get_post_processing is not implemented")
    
    def execute(self, post_processing, result) -> None:
        raise NotImplementedError("Renderer.execute is not implemented")
    
    @staticmethod
    def create_renderer() -> 'Renderer':
        raise NotImplementedError("Renderer.create_renderer is not implemented")
    
    def register_entity_renderer(self, renderer) -> None:
        raise NotImplementedError("Renderer.register_entity_renderer is not implemented")
    
    def render(self, render_target) -> None:
        raise NotImplementedError("Renderer.render is not implemented")
    
    @property
    def shader_set(self) -> 'ShaderSet':
        raise NotImplementedError("Renderer.shader_set is not implemented")
    
    @shader_set.setter
    def shader_set(self, value: 'ShaderSet') -> None:
        raise NotImplementedError("Renderer.shader_set setter is not implemented")
    
    @property
    def variables(self) -> 'RendererVariableManager':
        raise NotImplementedError("Renderer.variables is not implemented")
    
    @property
    def preset_shaders(self) -> 'PresetShaders':
        raise NotImplementedError("Renderer.preset_shaders is not implemented")
    
    @preset_shaders.setter
    def preset_shaders(self, value: 'PresetShaders') -> None:
        raise NotImplementedError("Renderer.preset_shaders setter is not implemented")
    
    @property
    def render_factory(self) -> 'RenderFactory':
        raise NotImplementedError("Renderer.render_factory is not implemented")
    
    @property
    def asset_directories(self):
        raise NotImplementedError("Renderer.asset_directories is not implemented")
    
    @property
    def post_processings(self):
        raise NotImplementedError("Renderer.post_processings is not implemented")
    
    @property
    def enable_shadows(self) -> bool:
        raise NotImplementedError("Renderer.enable_shadows is not implemented")
    
    @enable_shadows.setter
    def enable_shadows(self, value: bool) -> None:
        raise NotImplementedError("Renderer.enable_shadows setter is not implemented")
    
    @property
    def render_target(self):
        raise NotImplementedError("Renderer.render_target is not implemented")
    
    @property
    def node(self) -> 'Node':
        raise NotImplementedError("Renderer.node is not implemented")
    
    @node.setter
    def node(self, value: 'Node') -> None:
        raise NotImplementedError("Renderer.node setter is not implemented")
    
    @property
    def frustum(self) -> 'Frustum':
        raise NotImplementedError("Renderer.frustum is not implemented")
    
    @frustum.setter
    def frustum(self, value: 'Frustum') -> None:
        raise NotImplementedError("Renderer.frustum setter is not implemented")
    
    @property
    def render_stage(self) -> 'RenderStage':
        raise NotImplementedError("Renderer.render_stage is not implemented")
    
    @property
    def material(self):
        raise NotImplementedError("Renderer.material is not implemented")
    
    @material.setter
    def material(self, value) -> None:
        raise NotImplementedError("Renderer.material setter is not implemented")
    
    @property
    def shader(self) -> 'ShaderProgram':
        raise NotImplementedError("Renderer.shader is not implemented")
    
    @shader.setter
    def shader(self, value: 'ShaderProgram') -> None:
        raise NotImplementedError("Renderer.shader setter is not implemented")
    
    @property
    def fallback_entity_renderer(self) -> 'EntityRenderer':
        raise NotImplementedError("Renderer.fallback_entity_renderer is not implemented")
    
    @fallback_entity_renderer.setter
    def fallback_entity_renderer(self, value: 'EntityRenderer') -> None:
        raise NotImplementedError("Renderer.fallback_entity_renderer setter is not implemented")
