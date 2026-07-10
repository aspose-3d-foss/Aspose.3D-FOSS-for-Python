from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aspose.threed.entities.Mesh import Mesh


class InvalidOperationException(Exception):
    pass


class PolygonBuilder:
    def __init__(self, mesh: 'Mesh'):
        self._mesh = mesh
        self._current_polygon = None

    def begin(self):
        self._current_polygon = []

    def add_vertex(self, index: int):
        if self._current_polygon is None:
            raise InvalidOperationException(
                "Call begin() first")
        self._current_polygon.append(index)

    def end(self):
        if self._current_polygon is None:
            raise InvalidOperationException(
                "Call begin() first")
        self._mesh.create_polygon(self._current_polygon)
        self._current_polygon = None
