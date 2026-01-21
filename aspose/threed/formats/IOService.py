from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .Exporter import Exporter
    from .Importer import Importer
    from .FormatDetector import FormatDetector
    from .Plugin import Plugin
    from aspose.threed import FileFormat
    import io


class IOService:
    _instance = None
    _exporters = []
    _importers = []
    _detectors = []
    _plugins = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        pass

    def register_exporter(self, exporter: 'Exporter'):
        IOService._exporters.append(exporter)

    def register_importer(self, importer: 'Importer'):
        IOService._importers.append(importer)

    def register_detector(self, detector: 'FormatDetector'):
        IOService._detectors.append(detector)

    def register_plugin(self, plugin: 'Plugin'):
        if plugin not in IOService._plugins:
            IOService._plugins.append(plugin)
            self.register_importer(plugin.get_importer())
            self.register_exporter(plugin.get_exporter())
            self.register_detector(plugin.get_format_detector())

    def detect_format(self, stream, file_name: str):
        for detector in self._detectors:
            result = detector.detect(stream, file_name)
            if result is not None:
                return result
        return None

    def create_exporter(self, format_type: 'FileFormat'):
        for exporter in self._exporters:
            if exporter.supports_format(format_type):
                return exporter
        raise RuntimeError(f"No exporter found for format: {format_type}")

    def create_importer(self, format_type: 'FileFormat'):
        for importer in self._importers:
            if importer.supports_format(format_type):
                return importer
        raise RuntimeError(f"No importer found for format: {format_type}")

    def get_plugin_for_format(self, file_format):
        for plugin in self._plugins:
            plugin_format = plugin.get_file_format()
            if plugin_format.__class__ == file_format.__class__:
                return plugin
        return None

    def get_plugin_for_extension(self, extension: str):
        ext_lower = extension.lower()
        if ext_lower.startswith('.'):
            ext_lower = ext_lower[1:]
        
        for plugin in self._plugins:
            plugin_format = plugin.get_file_format()
            for fmt_ext in plugin_format.extensions:
                if fmt_ext.lower() == ext_lower:
                    return plugin
        return None

    def get_all_plugins(self):
        return list(self._plugins)
