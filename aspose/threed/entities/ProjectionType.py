class ProjectionType:
    """Camera's projection types."""

    def __init__(self, name: str = None):
        self._name = name

    def __str__(self):
        return self._name


ProjectionType.PERSPECTIVE = ProjectionType("PERSPECTIVE")
ProjectionType.ORTHOGRAPHIC = ProjectionType("ORTHOGRAPHIC")
