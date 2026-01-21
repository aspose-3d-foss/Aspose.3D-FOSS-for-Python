from typing import TYPE_CHECKING

from ..Plugin import Plugin

if TYPE_CHECKING:
    from .Importer import Importer
    from .Exporter import Exporter
    from .FormatDetector import FormatDetector
    from .LoadOptions import LoadOptions
    from .SaveOptions import SaveOptions
    from .ObjLoadOptions import ObjLoadOptions
    from .ObjSaveOptions import ObjSaveOptions
    from .ObjFormat import ObjFormat


class ObjPlugin(Plugin):
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        from .ObjImporter import ObjImporter
        from .ObjExporter import ObjExporter
        from .ObjFormatDetector import ObjFormatDetector
        
        self._importer = ObjImporter()
        self._exporter = ObjExporter()
        self._format_detector = ObjFormatDetector()
    
    def get_file_format(self) -> 'ObjFormat':
        from .ObjFormat import ObjFormat
        return ObjFormat()
    
    def get_importer(self) -> 'Importer':
        return self._importer
    
    def get_exporter(self) -> 'Exporter':
        return self._exporter
    
    def get_format_detector(self) -> 'FormatDetector':
        return self._format_detector
    
    def create_load_options(self) -> 'ObjLoadOptions':
        from .ObjLoadOptions import ObjLoadOptions
        return ObjLoadOptions()
    
    def create_save_options(self) -> 'ObjSaveOptions':
        from .ObjSaveOptions import ObjSaveOptions
        return ObjSaveOptions()
