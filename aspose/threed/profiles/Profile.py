from typing import TYPE_CHECKING

from ..Entity import Entity

if TYPE_CHECKING:
    from .Curve import Curve


class Profile(Entity):
    """2D Profile in xy plane."""
    
    def __init__(self, name: str = None):
        super().__init__(name)
    
    def get_entity_renderer_key(self):
        from ..render import EntityRendererKey
        return EntityRendererKey("Profile")
