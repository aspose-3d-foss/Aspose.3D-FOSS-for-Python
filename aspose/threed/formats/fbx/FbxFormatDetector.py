from typing import TYPE_CHECKING

from ..FormatDetector import FormatDetector

if TYPE_CHECKING:
    from aspose.threed import FileFormat


class FbxFormatDetector(FormatDetector):
    def __init__(self):
        super().__init__()

    def detect(self, stream, file_name: str) -> 'FileFormat':
        if file_name and file_name.lower().endswith('.fbx'):
            if stream is not None:
                try:
                    if hasattr(stream, 'read'):
                        stream.seek(0)
                        header = stream.read(50)
                        stream.seek(0)

                        if isinstance(header, str):
                            header_str = header.lower()
                        else:
                            header_str = header.decode('utf-8', errors='ignore').lower()

                        if '; fbx 7.4.0 project file' in header_str or '; fbx 7.3.0 project file' in header_str:
                            from .FbxFormat import FbxFormat
                            return FbxFormat()
                        
                        if not isinstance(header, str) and header.startswith(b'Kaydara FBX Binary  '):
                            from .FbxFormat import FbxFormat
                            return FbxFormat()
                except Exception:
                    pass
            else:
                from .FbxFormat import FbxFormat
                return FbxFormat()

        return None
