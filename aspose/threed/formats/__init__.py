from .Exporter import Exporter
from .Importer import Importer
from .FormatDetector import FormatDetector
from .IOService import IOService
from .IOConfig import IOConfig
from .LoadOptions import LoadOptions
from .SaveOptions import SaveOptions
from .Plugin import Plugin
from .obj.ObjLoadOptions import ObjLoadOptions
from .obj.ObjSaveOptions import ObjSaveOptions
from .stl.StlLoadOptions import StlLoadOptions
from .stl.StlSaveOptions import StlSaveOptions
from .obj.ObjPlugin import ObjPlugin
from .stl.StlPlugin import StlPlugin
from .gltf.GltfLoadOptions import GltfLoadOptions
from .gltf.GltfSaveOptions import GltfSaveOptions
from .gltf.GltfPlugin import GltfPlugin


def _register_plugins():
    io_service = IOService()
    io_service.register_plugin(ObjPlugin())
    io_service.register_plugin(StlPlugin())
    io_service.register_plugin(GltfPlugin())


_register_plugins()

__all__ = [
    'Exporter',
    'Importer',
    'FormatDetector',
    'IOService',
    'IOConfig',
    'LoadOptions',
    'SaveOptions',
    'Plugin',
    'ObjLoadOptions',
    'ObjSaveOptions',
    'StlLoadOptions',
    'StlSaveOptions',
    'GltfLoadOptions',
    'GltfSaveOptions'
]
