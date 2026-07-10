class FileFormatType:
    """File format type"""

    def __init__(self, extension: str = None):
        self._extension = extension or ""

    @property
    def extension(self) -> str:
        """The extension name of this file format, started with ."""
        return self._extension

    def __str__(self):
        return self._extension


# Static instances set on the class itself
FileFormatType.MAYA = FileFormatType(".mb")
FileFormatType.BLENDER = FileFormatType(".blend")
FileFormatType.FBX = FileFormatType(".fbx")
FileFormatType.STL = FileFormatType(".stl")
FileFormatType.WAVEFRONT_OBJ = FileFormatType(".obj")
FileFormatType.DISCREET_3DS = FileFormatType(".3ds")
FileFormatType.COLLADA = FileFormatType(".dae")
FileFormatType.UNIVERSAL_3D = FileFormatType(".u3d")
FileFormatType.PDF = FileFormatType(".pdf")
FileFormatType.GLTF = FileFormatType(".gltf")
FileFormatType.DXF = FileFormatType(".dxf")
FileFormatType.PLY = FileFormatType(".ply")
FileFormatType.X = FileFormatType(".x")
FileFormatType.DRACO = FileFormatType(".draco")
FileFormatType.MICROSOFT_3MF = FileFormatType(".3mf")
FileFormatType.RVM = FileFormatType(".rvm")
FileFormatType.ASE = FileFormatType(".ase")
FileFormatType.ZIP = FileFormatType(".zip")
FileFormatType.USD = FileFormatType(".usd")
FileFormatType.PCD = FileFormatType(".pcd")
FileFormatType.XYZ = FileFormatType(".xyz")
FileFormatType.IFC = FileFormatType(".ifc")
FileFormatType.SIEMENS_JT = FileFormatType(".jt")
FileFormatType.AMF = FileFormatType(".amf")
FileFormatType.VRML = FileFormatType(".wrl")
FileFormatType.HTML5 = FileFormatType(".html")
FileFormatType.ASPOSE_3D_WEB = FileFormatType(".a3dw")
