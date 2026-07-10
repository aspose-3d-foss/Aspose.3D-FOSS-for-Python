class ColladaLoadOptions:
    """Load options for Collada"""

    def __init__(self):
        self._flip_coordinate_system = False
        self._enable_materials = True

    @property
    def flip_coordinate_system(self) -> bool:
        return self._flip_coordinate_system

    @flip_coordinate_system.setter
    def flip_coordinate_system(self, value: bool):
        self._flip_coordinate_system = bool(value)

    @property
    def enable_materials(self) -> bool:
        return self._enable_materials

    @enable_materials.setter
    def enable_materials(self, value: bool):
        self._enable_materials = bool(value)
