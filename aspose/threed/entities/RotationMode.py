class RotationMode:
    """The frustum's rotation mode."""

    def __init__(self, name: str = None):
        self._name = name

    def __str__(self):
        return self._name


RotationMode.FIXED_TARGET = RotationMode("FIXED_TARGET")
RotationMode.FIXED_DIRECTION = RotationMode("FIXED_DIRECTION")
