from typing import TYPE_CHECKING

from aspose.threed.Entity import Entity

if TYPE_CHECKING:
    from .BooleanOperand import BooleanOperand
    from .BooleanOperation import BooleanOperation
    from aspose.threed import A3DObject


class BooleanOperator(Entity):
    """Boolean operator allows you to apply Boolean operation on two IMeshConvertible instances."""

    def __init__(self, operation=None, first=None, second=None):
        super().__init__()
        self._operator = operation
        self._first = first
        self._second = second

    @property
    def operator(self) -> "BooleanOperation":
        """The Boolean operator used in the operation."""
        return self._operator

    @operator.setter
    def operator(self, value: "BooleanOperation"):
        self._operator = value

    @property
    def first(self) -> "BooleanOperand":
        """The first operand of the Boolean operator."""
        return self._first

    @first.setter
    def first(self, value: "BooleanOperand"):
        self._first = value

    @property
    def second(self) -> "BooleanOperand":
        """The second operand of the Boolean operator."""
        return self._second

    @second.setter
    def second(self, value: "BooleanOperand"):
        self._second = value
