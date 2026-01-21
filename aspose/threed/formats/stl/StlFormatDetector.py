from typing import TYPE_CHECKING, Optional
import io
import struct
from ..FormatDetector import FormatDetector

if TYPE_CHECKING:
    from aspose.threed import FileFormat


class StlFormatDetector(FormatDetector):
    def detect(self, stream: io.IOBase, file_name: str) -> Optional['FileFormat']:
        from aspose.threed.formats.stl.StlFormat import StlFormat
        
        if not hasattr(stream, 'read'):
            return None
        
        has_stl_extension = file_name and file_name.lower().endswith('.stl')
        
        try:
            if hasattr(stream, 'seek'):
                stream.seek(0)
            data = stream.read(5)
            if hasattr(stream, 'seek'):
                stream.seek(0)
            
            if not data:
                return None
            
            data_str = data.decode('utf-8', errors='ignore').lower()
            
            if data_str.startswith('solid'):
                if has_stl_extension:
                    return StlFormat()
                return None
            else:
                try:
                    if hasattr(stream, 'seek'):
                        stream.seek(80)
                    count_data = stream.read(4)
                    if hasattr(stream, 'seek'):
                        stream.seek(0)
                    
                    if len(count_data) == 4:
                        count = struct.unpack('<I', count_data)[0]
                        if has_stl_extension:
                            return StlFormat()
                        return None
                except:
                    pass
        except:
            pass
        
        return None
