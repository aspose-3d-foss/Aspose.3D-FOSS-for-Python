class BooleanOperand:
    """This class encapsulates the transformed mesh as Boolean operation's operand."""

    def __init__(self, operand=None):
        self._operand = operand

    @staticmethod
    def of(node) -> "BooleanOperand":
        """Construct a BooleanOperand instance from a node."""
        return BooleanOperand(node)

    @staticmethod
    def of(mesh, transform=None) -> "BooleanOperand":
        """Construct a BooleanOperand instance from a mesh."""
        return BooleanOperand(mesh)

    @property
    def operand(self):
        """Gets the operand."""
        return self._operand
