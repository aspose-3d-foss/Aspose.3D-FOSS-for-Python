from typing import TYPE_CHECKING

from ..Exporter import Exporter

if TYPE_CHECKING:
    from aspose.threed import Scene
    from .FbxSaveOptions import FbxSaveOptions


class FbxExporter(Exporter):
    def __init__(self):
        super().__init__()

    def supports_format(self, file_format) -> bool:
        from .FbxFormat import FbxFormat
        return isinstance(file_format, FbxFormat)

    def export_scene(self, scene: 'Scene', stream, options: 'FbxSaveOptions'):
        from .FbxSaveOptions import FbxSaveOptions

        if not isinstance(options, FbxSaveOptions):
            options = FbxSaveOptions()

        raise NotImplementedError("export_scene is not implemented")
