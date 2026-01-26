from typing import TYPE_CHECKING
import io

from ..Exporter import Exporter

if TYPE_CHECKING:
    from .FbxSaveOptions import FbxSaveOptions
    from aspose.threed import Scene


class FbxExporter(Exporter):
    def save(self, filename: str, scene: 'Scene', options: 'FbxSaveOptions' = None):
        raise NotImplementedError("FBX export is not implemented")

    def save_to_stream(self, stream: io.IOBase, scene: 'Scene', options: 'FbxSaveOptions' = None):
        raise NotImplementedError("FBX export is not implemented")
