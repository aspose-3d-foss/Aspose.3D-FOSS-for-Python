from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from .TextureBase import TextureBase
    from .AlphaSource import AlphaSource
    from .WrapMode import WrapMode
    from .TextureFilter import TextureFilter


class Texture:
    """This class defines the texture from an external file."""
    
    def __init__(self, *args):
        raise NotImplementedError("Texture is not implemented")
    
    def set_translation(self, u: float, v: float) -> None:
        raise NotImplementedError("Texture.set_translation is not implemented")
    
    def set_scale(self, u: float, v: float) -> None:
        raise NotImplementedError("Texture.set_scale is not implemented")
    
    def set_rotation(self, u: float, v: float) -> None:
        raise NotImplementedError("Texture.set_rotation is not implemented")
    
    @property
    def name(self) -> str:
        raise NotImplementedError("Texture.name is not implemented")
    
    @name.setter
    def name(self, value: str) -> None:
        raise NotImplementedError("Texture.name setter is not implemented")
    
    @property
    def alpha(self) -> float:
        raise NotImplementedError("Texture.alpha is not implemented")
    
    @alpha.setter
    def alpha(self, value: float) -> None:
        raise NotImplementedError("Texture.alpha setter is not implemented")
    
    @property
    def alpha_source(self) -> 'AlphaSource':
        raise NotImplementedError("Texture.alpha_source is not implemented")
    
    @alpha_source.setter
    def alpha_source(self, value: 'AlphaSource') -> None:
        raise NotImplementedError("Texture.alpha_source setter is not implemented")
    
    @property
    def wrap_mode_u(self) -> 'WrapMode':
        raise NotImplementedError("Texture.wrap_mode_u is not implemented")
    
    @wrap_mode_u.setter
    def wrap_mode_u(self, value: 'WrapMode') -> None:
        raise NotImplementedError("Texture.wrap_mode_u setter is not implemented")
    
    @property
    def wrap_mode_v(self) -> 'WrapMode':
        raise NotImplementedError("Texture.wrap_mode_v is not implemented")
    
    @wrap_mode_v.setter
    def wrap_mode_v(self, value: 'WrapMode') -> None:
        raise NotImplementedError("Texture.wrap_mode_v setter is not implemented")
    
    @property
    def wrap_mode_w(self) -> 'WrapMode':
        raise NotImplementedError("Texture.wrap_mode_w is not implemented")
    
    @wrap_mode_w.setter
    def wrap_mode_w(self, value: 'WrapMode') -> None:
        raise NotImplementedError("Texture.wrap_mode_w setter is not implemented")
    
    @property
    def min_filter(self) -> 'TextureFilter':
        raise NotImplementedError("Texture.min_filter is not implemented")
    
    @min_filter.setter
    def min_filter(self, value: 'TextureFilter') -> None:
        raise NotImplementedError("Texture.min_filter setter is not implemented")
    
    @property
    def mag_filter(self) -> 'TextureFilter':
        raise NotImplementedError("Texture.mag_filter is not implemented")
    
    @mag_filter.setter
    def mag_filter(self, value: 'TextureFilter') -> None:
        raise NotImplementedError("Texture.mag_filter setter is not implemented")
    
    @property
    def mip_filter(self) -> 'TextureFilter':
        raise NotImplementedError("Texture.mip_filter is not implemented")
    
    @mip_filter.setter
    def mip_filter(self, value: 'TextureFilter') -> None:
        raise NotImplementedError("Texture.mip_filter setter is not implemented")
    
    @property
    def uv_rotation(self):
        raise NotImplementedError("Texture.uv_rotation is not implemented")
    
    @uv_rotation.setter
    def uv_rotation(self, value):
        raise NotImplementedError("Texture.uv_rotation setter is not implemented")
    
    @property
    def uv_scale(self):
        raise NotImplementedError("Texture.uv_scale is not implemented")
    
    @uv_scale.setter
    def uv_scale(self, value):
        raise NotImplementedError("Texture.uv_scale setter is not implemented")
    
    @property
    def uv_translation(self):
        raise NotImplementedError("Texture.uv_translation is not implemented")
    
    @uv_translation.setter
    def uv_translation(self, value):
        raise NotImplementedError("Texture.uv_translation setter is not implemented")
    
    @property
    def enable_mip_map(self) -> bool:
        raise NotImplementedError("Texture.enable_mip_map is not implemented")
    
    @enable_mip_map.setter
    def enable_mip_map(self, value: bool) -> None:
        raise NotImplementedError("Texture.enable_mip_map setter is not implemented")
    
    @property
    def content(self) -> List[int]:
        raise NotImplementedError("Texture.content is not implemented")
    
    @content.setter
    def content(self, value: List[int]) -> None:
        raise NotImplementedError("Texture.content setter is not implemented")
    
    @property
    def file_name(self) -> str:
        raise NotImplementedError("Texture.file_name is not implemented")
    
    @file_name.setter
    def file_name(self, value: str) -> None:
        raise NotImplementedError("Texture.file_name setter is not implemented")
