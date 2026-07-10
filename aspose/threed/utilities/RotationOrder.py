class RotationOrder:
    """The order controls which rx ry rz are applied in the transformation matrix."""
    XYZ = None
    XZY = None
    YZX = None
    YXZ = None
    ZXY = None
    ZYX = None


# Initialize enum values
RotationOrder.XYZ = RotationOrder()
RotationOrder.XZY = RotationOrder()
RotationOrder.YZX = RotationOrder()
RotationOrder.YXZ = RotationOrder()
RotationOrder.ZXY = RotationOrder()
RotationOrder.ZYX = RotationOrder()
