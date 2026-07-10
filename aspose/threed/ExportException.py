class ExportException(Exception):
    """Exceptions when Aspose.3D failed to export the scene to file."""

    def __init__(self, msg: str):
        super().__init__(msg)
