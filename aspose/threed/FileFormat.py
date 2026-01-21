from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .formats import LoadOptions, SaveOptions
    import io


class FileFormat:
    FBX6100ASCII = None
    FBX6100_BINARY = None
    FBX7200ASCII = None
    FBX7200_BINARY = None
    FBX7300ASCII = None
    FBX7300_BINARY = None
    FBX7400ASCII = None
    FBX7400_BINARY = None
    FBX7500ASCII = None
    FBX7500_BINARY = None
    FBX7600ASCII = None
    FBX7600_BINARY = None
    FBX7700ASCII = None
    FBX7700_BINARY = None
    MAYA_ASCII = None
    MAYA_BINARY = None
    STL_BINARY = None
    STLASCII = None
    
    _wavefront_obj_instance = None
    
    @staticmethod
    def WAVEFRONT_OBJ():
        if FileFormat._wavefront_obj_instance is None:
            from .formats._obj_formats.ObjFormat import ObjFormat
            FileFormat._wavefront_obj_instance = ObjFormat()
        return FileFormat._wavefront_obj_instance
    
    DISCREET_3DS = None
    COLLADA = None
    UNIVERSAL_3D = None
    GLTF = None
    GLTF2 = None
    GLTF_BINARY = None
    GLTF2_BINARY = None
    PDF = None
    BLENDER = None
    DXF = None
    PLY = None
    X_BINARY = None
    X_TEXT = None
    DRACO = None
    MICROSOFT_3MF = None
    RVM_TEXT = None
    RVM_BINARY = None
    ASE = None
    IFC = None
    SIEMENS_JT8 = None
    SIEMENS_JT9 = None
    AMF = None
    VRML = None
    ASPOSE_3D_WEB = None
    HTML5 = None
    ZIP = None
    USD = None
    USDA = None
    USDZ = None
    XYZ = None
    PCD = None
    PCD_BINARY = None

    def __init__(self):
        pass

    @property
    def extension(self) -> str:
        return ""

    @property
    def extensions(self) -> List[str]:
        return []

    @property
    def content_type(self) -> str:
        return ""

    @property
    def file_format_type(self):
        return None

    @property
    def version(self) -> str:
        return ""

    @property
    def can_export(self) -> bool:
        return False

    @property
    def can_import(self) -> bool:
        return False

    @property
    def formats(self) -> List['FileFormat']:
        return []

    @staticmethod
    def detect(stream: 'io._IOBase' = None, file_name: Optional[str] = None) -> Optional['FileFormat']:
        from .formats.IOService import IOService
        io_service = IOService()
        if stream is not None:
            return io_service.detect_format(stream, file_name or "")
        return None

    @staticmethod
    def get_format_by_extension(extension_name: str) -> Optional['FileFormat']:
        if not extension_name:
            return None
        ext = extension_name.lower()
        if ext.startswith('.'):
            ext = ext[1:]
        
        if ext == 'obj':
            from .formats.obj.ObjFormat import ObjFormat
            return ObjFormat()
        elif ext == 'stl':
            from .formats.stl.StlFormat import StlFormat
            return StlFormat()
        return None

    def create_load_options(self) -> 'LoadOptions':
        from .formats import IOService
        
        if hasattr(self, 'file_format_type') and self.file_format_type is not None:
            plugin = IOService().get_plugin_for_format(self)
            if plugin is not None:
                return plugin.create_load_options()
        
        from .formats import LoadOptions
        options = LoadOptions()
        from .formats.IOConfig import IOConfig
        IOConfig._file_format.fset(self, self)
        return options

    def create_save_options(self) -> 'SaveOptions':
        from .formats import IOService
        
        if hasattr(self, 'file_format_type') and self.file_format_type is not None:
            plugin = IOService().get_plugin_for_format(self)
            if plugin is not None:
                options = plugin.create_save_options()
                from .formats.IOConfig import IOConfig
                IOConfig._file_format.fset(self, self)
                return options
        
        from .formats import SaveOptions
        options = SaveOptions()
        from .formats.IOConfig import IOConfig
        IOConfig._file_format.fset(self, self)
        return options
