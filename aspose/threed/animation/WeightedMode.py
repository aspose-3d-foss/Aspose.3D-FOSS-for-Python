from enum import Enum


class WeightedMode(Enum):
    NONE = 0
    OUT_WEIGHT = 1
    NEXT_IN_WEIGHT = 2
    BOTH = 3
