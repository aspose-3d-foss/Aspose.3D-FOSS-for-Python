from enum import Enum


class ExtrapolationType(Enum):
    CONSTANT = 0
    GRADIENT = 1
    CYCLE = 2
    CYCLE_RELATIVE = 3
    OSCILLATE = 4
