from typing import TYPE_CHECKING

from ..SaveOptions import SaveOptions

if TYPE_CHECKING:
    from ..AxisSystem import AxisSystem


class ObjSaveOptions(SaveOptions):
    def __init__(self):
        super().__init__()
        self._apply_unit_scale = False
        self._point_cloud = False
        self._verbose = False
        self._serialize_w = False
        self._enable_materials = True
        self._flip_coordinate_system = False
        self._axis_system = None

    @property
    def apply_unit_scale(self) -> bool:
        return self._apply_unit_scale

    @apply_unit_scale.setter
    def apply_unit_scale(self, value: bool):
        self._apply_unit_scale = bool(value)

    @property
    def point_cloud(self) -> bool:
        return self._point_cloud

    @point_cloud.setter
    def point_cloud(self, value: bool):
        self._point_cloud = bool(value)

    @property
    def verbose(self) -> bool:
        return self._verbose

    @verbose.setter
    def verbose(self, value: bool):
        self._verbose = bool(value)

    @property
    def serialize_w(self) -> bool:
        return self._serialize_w

    @serialize_w.setter
    def serialize_w(self, value: bool):
        self._serialize_w = bool(value)

    @property
    def enable_materials(self) -> bool:
        return self._enable_materials

    @enable_materials.setter
    def enable_materials(self, value: bool):
        self._enable_materials = bool(value)

    @property
    def flip_coordinate_system(self) -> bool:
        return self._flip_coordinate_system

    @flip_coordinate_system.setter
    def flip_coordinate_system(self, value: bool):
        self._flip_coordinate_system = bool(value)

    @property
    def axis_system(self) -> 'AxisSystem':
        return self._axis_system

    @axis_system.setter
    def axis_system(self, value: 'AxisSystem'):
        self._axis_system = value
