from typing import TYPE_CHECKING

from ..FormatDetector import FormatDetector

if TYPE_CHECKING:
    from aspose.threed import FileFormat


class ThreeMfFormatDetector(FormatDetector):
    def __init__(self):
        super().__init__()

    def detect(self, stream, file_name: str) -> 'FileFormat':
        if file_name and file_name.lower().endswith('.3mf'):
            from .ThreeMfFormat import ThreeMfFormat
            return ThreeMfFormat()
        
        if stream is not None:
            try:
                if hasattr(stream, 'read'):
                    stream.seek(0)
                    header = stream.read(4)
                    stream.seek(0)
                    
                    if isinstance(header, str):
                        header_bytes = header.encode('utf-8')
                    else:
                        header_bytes = header
                    
                    if len(header_bytes) >= 4 and header_bytes[:2] == b'PK':
                        from .ThreeMfFormat import ThreeMfFormat
                        return ThreeMfFormat()
            except Exception:
                pass
        
        return None
