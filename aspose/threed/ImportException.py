class ImportException(Exception):
    """Exception when Aspose.3D failed to open the specified source."""

    def __init__(self, msg: str):
        super().__init__(msg)
