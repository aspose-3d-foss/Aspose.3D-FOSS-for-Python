class LightType:
    """Light types."""

    def __init__(self, name: str = None):
        self._name = name

    def __str__(self):
        return self._name


LightType.POINT = LightType("POINT")
LightType.DIRECTIONAL = LightType("DIRECTIONAL")
LightType.SPOT = LightType("SPOT")
LightType.AREA = LightType("AREA")
LightType.VOLUME = LightType("VOLUME")
