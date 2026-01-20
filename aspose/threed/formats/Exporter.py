from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aspose.threed import Scene
    from aspose.threed.formats import SaveOptions
    from aspose.threed import FileFormat


class Exporter:
    def __init__(self):
        pass

    def supports_format(self, file_format: 'FileFormat') -> bool:
        raise NotImplementedError("supports_format is not implemented")

    def export(self, scene: 'Scene', stream, options: 'SaveOptions'):
        raise NotImplementedError("export is not implemented")
