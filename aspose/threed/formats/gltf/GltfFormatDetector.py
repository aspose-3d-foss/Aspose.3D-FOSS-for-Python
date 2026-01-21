from typing import TYPE_CHECKING
from ..FormatDetector import FormatDetector

if TYPE_CHECKING:
    from aspose.threed import FileFormat
    import io


class GltfFormatDetector(FormatDetector):
    def __init__(self):
        super().__init__()

    def detect(self, stream: 'io._IOBase', file_name: str) -> 'FileFormat':
        from .GltfFormat import GltfFormat

        if file_name:
            file_name_lower = file_name.lower()
            if file_name_lower.endswith('.gltf') or file_name_lower.endswith('.glb'):
                return GltfFormat()

        if hasattr(stream, 'read') and hasattr(stream, 'seek'):
            pos = stream.tell()
            stream.seek(0)
            header = stream.read(4)
            stream.seek(pos)

            if len(header) >= 4:
                header_str = header.decode('ascii', errors='ignore')
                if header_str == 'glTF':
                    from .GltfFormat import GltfFormat
                    return GltfFormat()

        return None
