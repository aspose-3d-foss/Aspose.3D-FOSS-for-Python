from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .Exporter import Exporter
    from .Importer import Importer
    from .FormatDetector import FormatDetector
    from aspose.threed import FileFormat
    import io


class IOService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._exporters: List['Exporter'] = []
            cls._instance._importers: List['Importer'] = []
            cls._instance._detectors: List['FormatDetector'] = []
        return cls._instance

    def register_exporter(self, exporter: 'Exporter'):
        self._exporters.append(exporter)

    def register_importer(self, importer: 'Importer'):
        self._importers.append(importer)

    def register_detector(self, detector: 'FormatDetector'):
        self._detectors.append(detector)

    def detect_format(self, stream, file_name: str) -> 'FileFormat':
        for detector in self._detectors:
            result = detector.detect(stream, file_name)
            if result is not None:
                return result
        return None

    def create_exporter(self, format_type: 'FileFormat') -> 'Exporter':
        for exporter in self._exporters:
            if exporter.supports_format(format_type):
                return exporter
        raise RuntimeError(f"No exporter found for format: {format_type}")

    def create_importer(self, format_type: 'FileFormat') -> 'Importer':
        for importer in self._importers:
            if importer.supports_format(format_type):
                return importer
        raise RuntimeError(f"No importer found for format: {format_type}")
