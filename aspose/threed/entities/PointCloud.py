from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aspose.threed.utilities import EntityRendererKey
    from aspose.threed.utilities.Vector2 import Vector2
    from .Geometry import Geometry


class PointCloud:
    def __init__(self, name: str = None):
        if name is None:
            name = "PointCloud"
        from .Geometry import Geometry
        super().__init__(name)
        self._dimension = None

    @property
    def dimension(self) -> 'Vector2':
        return self._dimension

    @dimension.setter
    def dimension(self, value: 'Vector2'):
        self._dimension = value

    def get_entity_renderer_key(self) -> 'EntityRendererKey':
        from aspose.threed.render import EntityRendererKey
        return EntityRendererKey("PointCloud")

    @staticmethod
    def from_geometry(g: 'Geometry') -> 'PointCloud':
        raise NotImplementedError("PointCloud.from_geometry is not implemented")

    @staticmethod
    def from_geometry_with_density(g: 'Geometry', density: int) -> 'PointCloud':
        raise NotImplementedError("PointCloud.from_geometry_with_density is not implemented")
