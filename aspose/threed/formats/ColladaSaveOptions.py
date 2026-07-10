class ColladaSaveOptions:
    """Save options for collada"""

    def __init__(self):
        self._indented = True
        self._transform_style = None
        self._flip_coordinate_system = False
        self._enable_materials = True

    @property
    def indented(self) -> bool:
        return self._indented

    @indented.setter
    def indented(self, value: bool):
        self._indented = bool(value)

    @property
    def transform_style(self):
        return self._transform_style

    @transform_style.setter
    def transform_style(self, value):
        self._transform_style = value

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
