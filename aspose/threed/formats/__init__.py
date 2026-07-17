from .Exporter import Exporter
from .Importer import Importer
from .FormatDetector import FormatDetector
from .IOService import IOService
from .IOConfig import IOConfig
from .LoadOptions import LoadOptions
from .BasicLoadOptions import BasicLoadOptions
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
from .ColladaTransformStyle import ColladaTransformStyle
from .DracoCompressionLevel import DracoCompressionLevel
from .PdfFormat import PdfFormat
from .PdfLightingScheme import PdfLightingScheme
from .PdfRenderMode import PdfRenderMode
from .PlyFormat import PlyFormat
from .RvmFormat import RvmFormat
from .Microsoft3MFFormat import Microsoft3MFFormat
from .GltfEmbeddedImageFormat import GltfEmbeddedImageFormat
from .ColladaSaveOptions import ColladaSaveOptions
from .FbxSaveOptions import FbxSaveOptions
from .GltfSaveOptions import GltfSaveOptions
from .PdfSaveOptions import PdfSaveOptions
from .StlSaveOptions import StlSaveOptions
from .ObjSaveOptions import ObjSaveOptions
from .AmfSaveOptions import AmfSaveOptions
from .A3dwSaveOptions import A3dwSaveOptions
from .DracoSaveOptions import DracoSaveOptions
from .Html5SaveOptions import Html5SaveOptions
from .UsdSaveOptions import UsdSaveOptions
from .XLoadOptions import XLoadOptions
from .U3dLoadOptions import U3dLoadOptions
from .U3dSaveOptions import U3dSaveOptions
from .RvmLoadOptions import RvmLoadOptions
from .RvmSaveOptions import RvmSaveOptions
from .PlyLoadOptions import PlyLoadOptions
from .PlySaveOptions import PlySaveOptions
from .PdfLoadOptions import PdfLoadOptions
from .GltfLoadOptions import GltfLoadOptions
from .FbxLoadOptions import FbxLoadOptions
from .ColladaLoadOptions import ColladaLoadOptions
from .ObjLoadOptions import ObjLoadOptions
from .StlLoadOptions import StlLoadOptions
from .DracoFormat import DracoFormat
from .Discreet3dsLoadOptions import Discreet3dsLoadOptions
from .Discreet3dsSaveOptions import Discreet3dsSaveOptions
from .Microsoft3MFSaveOptions import Microsoft3MFSaveOptions
from .JtLoadOptions import JtLoadOptions


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
    'Exporter', 'Importer', 'FormatDetector', 'IOService', 'IOConfig',
    'LoadOptions', 'SaveOptions', 'Plugin',
    'ObjLoadOptions', 'ObjSaveOptions',
    'StlLoadOptions', 'StlSaveOptions',
    'GltfLoadOptions', 'GltfSaveOptions',
    'ThreeMfLoadOptions', 'ThreeMfSaveOptions', 'ThreeMfFormat',
    'FbxLoadOptions', 'FbxSaveOptions',
    'ColladaLoadOptions', 'ColladaSaveOptions', 'ColladaTransformStyle',
    'DracoCompressionLevel', 'PdfFormat', 'PdfLightingScheme', 'PdfRenderMode',
    'PlyFormat', 'RvmFormat', 'Microsoft3MFFormat',
    'GltfEmbeddedImageFormat',
    'ColladaSaveOptions', 'FbxSaveOptions', 'GltfSaveOptions',
    'PdfSaveOptions', 'StlSaveOptions', 'ObjSaveOptions',
    'AmfSaveOptions', 'A3dwSaveOptions', 'DracoSaveOptions',
    'Html5SaveOptions', 'UsdSaveOptions',    'LoadOptions', 'SaveOptions',    'RvmLoadOptions', 'RvmSaveOptions',
    'PlyLoadOptions', 'PlySaveOptions',
    'PdfLoadOptions', 'GltfLoadOptions',
    'FbxLoadOptions', 'ColladaLoadOptions',
    'ObjLoadOptions', 'StlLoadOptions',
    'DracoFormat', 'Discreet3dsLoadOptions', 'Discreet3dsSaveOptions',
    'Microsoft3MFSaveOptions', 'JtLoadOptions'
]
