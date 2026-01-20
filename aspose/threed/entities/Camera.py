from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ..Entity import Entity

from ..Entity import Entity


class Camera(Entity):
    def __init__(self, name: str = None, projection_type=None):
        super().__init__(name)
        self._projection_type = projection_type if projection_type is not None else "PERSPECTIVE"
        self._aperture_mode = None

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = str(value)

    @property
    def parent_nodes(self):
        return []

    @property
    def excluded(self) -> bool:
        return False

    @excluded.setter
    def excluded(self, value: bool):
        pass

    @property
    def parent_node(self):
        return None

    @parent_node.setter
    def parent_node(self, value):
        pass

    @property
    def rotation_mode(self):
        return None

    @rotation_mode.setter
    def rotation_mode(self, value):
        pass

    @property
    def near_plane(self) -> float:
        return 0.1

    @near_plane.setter
    def near_plane(self, value: float):
        pass

    @property
    def far_plane(self) -> float:
        return 1000.0

    @far_plane.setter
    def far_plane(self, value: float):
        pass

    @property
    def aspect(self) -> float:
        return 1.0

    @aspect.setter
    def aspect(self, value: float):
        pass

    @property
    def ortho_height(self) -> float:
        return 100.0

    @ortho_height.setter
    def ortho_height(self, value: float):
        pass

    @property
    def up(self):
        return None

    @up.setter
    def up(self, value):
        pass

    @property
    def look_at(self):
        return None

    @look_at.setter
    def look_at(self, value):
        pass

    @property
    def direction(self):
        return None

    @direction.setter
    def direction(self, value):
        pass

    @property
    def target(self):
        return None

    @target.setter
    def target(self, value):
        pass

    @property
    def aperture_mode(self):
        return None

    @aperture_mode.setter
    def aperture_mode(self, value):
        pass

    @property
    def field_of_view(self) -> float:
        return 0.0

    @field_of_view.setter
    def field_of_view(self, value: float):
        pass

    @property
    def field_of_view_x(self) -> float:
        return 0.0

    @field_of_view_x.setter
    def field_of_view_x(self, value: float):
        pass

    @property
    def field_of_view_y(self) -> float:
        return 0.0

    @field_of_view_y.setter
    def field_of_view_y(self, value: float):
        pass

    @property
    def width(self) -> float:
        return 0.0

    @width.setter
    def width(self, value: float):
        pass

    @property
    def height(self) -> float:
        return 0.0

    @height.setter
    def height(self, value: float):
        pass

    @property
    def aspect_ratio(self) -> float:
        return 1.0

    @aspect_ratio.setter
    def aspect_ratio(self, value: float):
        pass

    @property
    def magnification(self):
        return None

    @magnification.setter
    def magnification(self, value):
        pass

    @property
    def projection_type(self) -> str:
        return self._projection_type

    @projection_type.setter
    def projection_type(self, value: str):
        self._projection_type = value

    def move_forward(self, distance: float):
        pass

    def get_bounding_box(self):
        return None

    def get_entity_renderer_key(self):
        raise NotImplementedError("get_entity_renderer_key is not implemented for Camera")

    def remove_property(self, property):
        return False

    def remove_property(self, property_name: str):
        return False

    def get_property(self, property: str):
        return None

    def set_property(self, property: str, value):
        pass

    def find_property(self, property: str):
        return None
