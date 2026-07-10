class ApertureMode:
    """Camera aperture modes.
The aperture mode determines which values drive the camera aperture.
If the aperture mode is HorizAndVert, Horizontal, or Vertical, then the field of view is used.
If the aperture mode is FocalLength, then the focal length is used."""

    def __init__(self, name: str = None):
        self._name = name

    def __str__(self):
        return self._name


ApertureMode.HORIZ_AND_VERT = ApertureMode("HORIZ_AND_VERT")
ApertureMode.HORIZONTAL = ApertureMode("HORIZONTAL")
ApertureMode.VERTICAL = ApertureMode("VERTICAL")
ApertureMode.FOCAL_LENGTH = ApertureMode("FOCAL_LENGTH")
