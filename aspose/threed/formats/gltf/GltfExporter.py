from typing import TYPE_CHECKING
from ..Exporter import Exporter

if TYPE_CHECKING:
    from aspose.threed import Scene
    from aspose.threed.formats import SaveOptions


class GltfExporter(Exporter):
    def __init__(self):
        super().__init__()

    def supports_format(self, file_format) -> bool:
        from .GltfFormat import GltfFormat
        return isinstance(file_format, GltfFormat)

    def export(self, scene: 'Scene', stream, options: 'SaveOptions'):
        raise NotImplementedError("export is not implemented")
