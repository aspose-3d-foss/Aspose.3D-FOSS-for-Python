from typing import TYPE_CHECKING

from ..Plugin import Plugin

if TYPE_CHECKING:
    from .Importer import Importer
    from .Exporter import Exporter
    from .FormatDetector import FormatDetector
    from .LoadOptions import LoadOptions
    from .SaveOptions import SaveOptions
    from .ColladaLoadOptions import ColladaLoadOptions
    from .ColladaFormat import ColladaFormat


class ColladaPlugin(Plugin):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        from .ColladaImporter import ColladaImporter
        from .ColladaExporter import ColladaExporter
        from .ColladaFormatDetector import ColladaFormatDetector

        self._importer = ColladaImporter()
        self._exporter = ColladaExporter()
        self._format_detector = ColladaFormatDetector()

    def get_file_format(self) -> 'ColladaFormat':
        from .ColladaFormat import ColladaFormat
        return ColladaFormat()

    def get_importer(self) -> 'Importer':
        return self._importer

    def get_exporter(self) -> 'Exporter':
        return self._exporter

    def get_format_detector(self) -> 'FormatDetector':
        return self._format_detector

    def create_load_options(self) -> 'ColladaLoadOptions':
        from .ColladaLoadOptions import ColladaLoadOptions
        return ColladaLoadOptions()

    def create_save_options(self) -> 'SaveOptions':
        from .ColladaSaveOptions import ColladaSaveOptions
        return ColladaSaveOptions()
