from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aspose.threed import Scene
    from aspose.threed.formats import LoadOptions
    from aspose.threed import FileFormat


class Importer:
    def __init__(self):
        pass

    def supports_format(self, file_format: 'FileFormat') -> bool:
        raise NotImplementedError("supports_format is not implemented")

    def import_scene(self, scene: 'Scene', stream, options: 'LoadOptions'):
        raise NotImplementedError("import_scene is not implemented")
