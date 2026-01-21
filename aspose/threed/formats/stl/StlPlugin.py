from typing import TYPE_CHECKING

from ..Plugin import Plugin

if TYPE_CHECKING:
    from .Importer import Importer
    from .Exporter import Exporter
    from .FormatDetector import FormatDetector
    from .LoadOptions import LoadOptions
    from .SaveOptions import SaveOptions
    from .StlLoadOptions import StlLoadOptions
    from .StlSaveOptions import StlSaveOptions
    from .StlFormat import StlFormat


class StlPlugin(Plugin):
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        from .StlImporter import StlImporter
        from .StlExporter import StlExporter
        from .StlFormatDetector import StlFormatDetector
        
        self._importer = StlImporter()
        self._exporter = StlExporter()
        self._format_detector = StlFormatDetector()
    
    def get_file_format(self) -> 'StlFormat':
        from .StlFormat import StlFormat
        return StlFormat()
    
    def get_importer(self) -> 'Importer':
        return self._importer
    
    def get_exporter(self) -> 'Exporter':
        return self._exporter
    
    def get_format_detector(self) -> 'FormatDetector':
        return self._format_detector
    
    def create_load_options(self) -> 'StlLoadOptions':
        from .StlLoadOptions import StlLoadOptions
        return StlLoadOptions()
    
    def create_save_options(self) -> 'StlSaveOptions':
        from .StlSaveOptions import StlSaveOptions
        return StlSaveOptions()
