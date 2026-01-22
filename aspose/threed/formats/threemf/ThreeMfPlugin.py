from typing import TYPE_CHECKING

from ..Plugin import Plugin

if TYPE_CHECKING:
    from .Importer import Importer
    from .Exporter import Exporter
    from .FormatDetector import FormatDetector
    from .LoadOptions import LoadOptions
    from .SaveOptions import SaveOptions
    from .ThreeMfLoadOptions import ThreeMfLoadOptions
    from .ThreeMfSaveOptions import ThreeMfSaveOptions
    from .ThreeMfFormat import ThreeMfFormat


class ThreeMfPlugin(Plugin):
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        from .ThreeMfImporter import ThreeMfImporter
        from .ThreeMfExporter import ThreeMfExporter
        from .ThreeMfFormatDetector import ThreeMfFormatDetector
        
        self._importer = ThreeMfImporter()
        self._exporter = ThreeMfExporter()
        self._format_detector = ThreeMfFormatDetector()
    
    def get_file_format(self) -> 'ThreeMfFormat':
        from .ThreeMfFormat import ThreeMfFormat
        return ThreeMfFormat()
    
    def get_importer(self) -> 'Importer':
        return self._importer
    
    def get_exporter(self) -> 'Exporter':
        return self._exporter
    
    def get_format_detector(self) -> 'FormatDetector':
        return self._format_detector
    
    def create_load_options(self) -> 'ThreeMfLoadOptions':
        from .ThreeMfLoadOptions import ThreeMfLoadOptions
        return ThreeMfLoadOptions()
    
    def create_save_options(self) -> 'ThreeMfSaveOptions':
        from .ThreeMfSaveOptions import ThreeMfSaveOptions
        return ThreeMfSaveOptions()
