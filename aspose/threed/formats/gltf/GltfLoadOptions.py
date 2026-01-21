from typing import TYPE_CHECKING

from ..LoadOptions import LoadOptions

if TYPE_CHECKING:
    pass


class GltfLoadOptions(LoadOptions):
    def __init__(self):
        super().__init__()
        self._flip_tex_coord_v = True

    @property
    def flip_tex_coord_v(self) -> bool:
        return self._flip_tex_coord_v

    @flip_tex_coord_v.setter
    def flip_tex_coord_v(self, value: bool):
        self._flip_tex_coord_v = bool(value)
