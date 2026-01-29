from typing import TYPE_CHECKING

from ..FormatDetector import FormatDetector

if TYPE_CHECKING:
    from aspose.threed import FileFormat


class ColladaFormatDetector(FormatDetector):
    def __init__(self):
        super().__init__()

    def detect(self, stream, file_name: str) -> 'FileFormat':
        if file_name and file_name.lower().endswith('.dae'):
            from .ColladaFormat import ColladaFormat
            return ColladaFormat()

        if stream is not None:
            try:
                if hasattr(stream, 'read'):
                    stream.seek(0)
                    header = stream.read(500)
                    stream.seek(0)

                    if isinstance(header, str):
                        header_str = header.lower()
                    else:
                        header_str = header.decode('utf-8', errors='ignore').lower()

                    if '<collada' in header_str or 'collada.org' in header_str:
                        from .ColladaFormat import ColladaFormat
                        return ColladaFormat()
            except Exception:
                pass

        return None
