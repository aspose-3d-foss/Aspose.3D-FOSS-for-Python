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
from .threemf.ThreeMfLoadOptions import ThreeMfLoadOptions
from .threemf.ThreeMfSaveOptions import ThreeMfSaveOptions
from .threemf.ThreeMfPlugin import ThreeMfPlugin
from .threemf.ThreeMfFormat import ThreeMfFormat
from .fbx.FbxLoadOptions import FbxLoadOptions
from .fbx.FbxSaveOptions import FbxSaveOptions
from .fbx.FbxPlugin import FbxPlugin
from .collada.ColladaLoadOptions import ColladaLoadOptions
from .collada.ColladaSaveOptions import ColladaSaveOptions
from .collada.ColladaPlugin import ColladaPlugin


def _register_plugins():
    io_service = IOService()
    io_service.register_plugin(ObjPlugin())
    io_service.register_plugin(StlPlugin())
    io_service.register_plugin(GltfPlugin())
    io_service.register_plugin(ThreeMfPlugin())
    io_service.register_plugin(FbxPlugin())
    io_service.register_plugin(ColladaPlugin())


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
    'GltfSaveOptions',
    'ThreeMfLoadOptions',
    'ThreeMfSaveOptions',
    'ThreeMfFormat',
    'FbxLoadOptions',
    'FbxSaveOptions',
    'ColladaLoadOptions',
    'ColladaSaveOptions'
]
