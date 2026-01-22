from enum import Enum


class Interpolation(Enum):
    CONSTANT = 0
    LINEAR = 1
    BEZIER = 2
    B_SPLINE = 3
    CARDINAL_SPLINE = 4
    TCB_SPLINE = 5
