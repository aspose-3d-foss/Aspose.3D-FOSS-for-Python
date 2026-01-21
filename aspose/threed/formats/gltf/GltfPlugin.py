from typing import TYPE_CHECKING

from ..Plugin import Plugin

if TYPE_CHECKING:
    from .Importer import Importer
    from .Exporter import Exporter
    from .FormatDetector import FormatDetector
    from .LoadOptions import LoadOptions
    from .SaveOptions import SaveOptions
    from .GltfLoadOptions import GltfLoadOptions
    from .GltfSaveOptions import GltfSaveOptions
    from .GltfFormat import GltfFormat


class GltfPlugin(Plugin):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        from .GltfImporter import GltfImporter
        from .GltfExporter import GltfExporter
        from .GltfFormatDetector import GltfFormatDetector

        self._importer = GltfImporter()
        self._exporter = GltfExporter()
        self._format_detector = GltfFormatDetector()

    def get_file_format(self) -> 'GltfFormat':
        from .GltfFormat import GltfFormat
        return GltfFormat()

    def get_importer(self) -> 'Importer':
        return self._importer

    def get_exporter(self) -> 'Exporter':
        return self._exporter

    def get_format_detector(self) -> 'FormatDetector':
        return self._format_detector

    def create_load_options(self) -> 'GltfLoadOptions':
        from .GltfLoadOptions import GltfLoadOptions
        return GltfLoadOptions()

    def create_save_options(self) -> 'GltfSaveOptions':
        from .GltfSaveOptions import GltfSaveOptions
        return GltfSaveOptions()
