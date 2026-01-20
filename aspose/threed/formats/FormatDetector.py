from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aspose.threed import FileFormat


class FormatDetector:
    def __init__(self):
        pass

    def detect(self, stream, file_name: str) -> 'FileFormat':
        raise NotImplementedError("detect is not implemented")
