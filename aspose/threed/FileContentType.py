class FileContentType:
    """File content type"""

    def __init__(self, value: int = None, name: str = None):
        self._value = value
        self._name = name

    def __str__(self):
        return self._name

    def __repr__(self):
        return f"FileContentType.{self._name}" if self._name else f"FileContentType({self._value})"


FileContentType.BINARY = FileContentType(0, "BINARY")
FileContentType.ASCII = FileContentType(1, "ASCII")
