from enum import Enum


class DiscountType(Enum):
    DEFAULT = 0
    VISIBLE = 1
    COMPOSITE = 2
    CONDITIONAL = 3
