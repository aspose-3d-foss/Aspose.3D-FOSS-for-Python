class ParseException(Exception):
    """Exception when Aspose.3D failed to parse the input."""

    def __init__(self, msg: str):
        super().__init__(msg)
