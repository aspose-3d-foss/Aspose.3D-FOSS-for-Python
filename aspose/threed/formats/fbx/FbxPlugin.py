from typing import TYPE_CHECKING

from ..Plugin import Plugin

if TYPE_CHECKING:
    from .Importer import Importer
    from .Exporter import Exporter
    from .FormatDetector import FormatDetector
    from .LoadOptions import LoadOptions
    from .SaveOptions import SaveOptions
    from .FbxFormat import FbxFormat
    from .FbxLoadOptions import FbxLoadOptions
    from .FbxSaveOptions import FbxSaveOptions


class FbxPlugin(Plugin):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        from .FbxImporter import FbxImporter
        from .FbxFormatDetector import FbxFormatDetector

        self._importer = FbxImporter()
        self._exporter = None
        self._format_detector = FbxFormatDetector()

    def get_file_format(self) -> 'FbxFormat':
        from .FbxFormat import FbxFormat
        return FbxFormat()

    def get_importer(self) -> 'Importer':
        return self._importer

    def get_exporter(self) -> 'Exporter':
        return self._exporter

    def get_format_detector(self) -> 'FormatDetector':
        return self._format_detector

    def create_load_options(self) -> 'FbxLoadOptions':
        from .FbxLoadOptions import FbxLoadOptions
        return FbxLoadOptions()

    def create_save_options(self) -> 'FbxSaveOptions':
        from .FbxSaveOptions import FbxSaveOptions
        return FbxSaveOptions()
