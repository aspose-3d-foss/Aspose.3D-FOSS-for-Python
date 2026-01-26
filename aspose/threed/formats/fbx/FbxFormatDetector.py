from typing import TYPE_CHECKING, Optional
import io

from ..FormatDetector import FormatDetector

if TYPE_CHECKING:
    from .FbxFormat import FbxFormat


class FbxFormatDetector(FormatDetector):
    def detect(self, stream, file_name: str) -> 'FbxFormat':
        from .FbxFormat import FbxFormat

        pos = stream.tell()
        stream.seek(0)

        header = stream.read(23).decode('utf-8', errors='ignore')
        stream.seek(pos)

        if 'Kaydara FBX Binary' in header:
            return FbxFormat()

        if '; FBX' in header[:100]:
            return FbxFormat()

        return FbxFormat()
