class SplitMeshPolicy:
    """Share vertex/control point data between sub-meshes or each sub-mesh has its own compacted data."""

    def __init__(self, name: str = None):
        self._name = name

    def __str__(self):
        return self._name


SplitMeshPolicy.CLONE_DATA = SplitMeshPolicy("CLONE_DATA")
SplitMeshPolicy.COMPACT_DATA = SplitMeshPolicy("COMPACT_DATA")
