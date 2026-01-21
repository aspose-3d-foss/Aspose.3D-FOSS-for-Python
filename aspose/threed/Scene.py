from typing import List, Optional, TYPE_CHECKING

from .SceneObject import SceneObject
from .Entity import Entity
from .AssetInfo import AssetInfo
from .CustomObject import CustomObject
from .ImageRenderOptions import ImageRenderOptions

if TYPE_CHECKING:
    from .FileFormat import FileFormat
    from .Node import Node


class Scene(SceneObject):
    VERSION = "24.12.0"

    def __init__(self, entity: Optional[Entity] = None, parent_scene=None, name: Optional[str] = None):
        super().__init__(name)
        self._sub_scenes: List[Scene] = []
        self._library: List[CustomObject] = []
        self._asset_info = AssetInfo()

        from .Node import Node
        self._root_node = Node()

        if entity is not None:
            self._root_node.entity = entity

        self._propagate_scene()

        if parent_scene is not None:
            parent_scene._sub_scenes.append(self)

        if entity is not None:
            self._root_node.entity = entity

        self._propagate_scene()

    @property
    def root_node(self):
        return self._root_node

    @property
    def sub_scenes(self) -> List['Scene']:
        return list(self._sub_scenes)

    @property
    def library(self) -> List[CustomObject]:
        return list(self._library)

    @property
    def asset_info(self) -> AssetInfo:
        return self._asset_info

    @asset_info.setter
    def asset_info(self, value: AssetInfo):
        self._asset_info = value

    @property
    def animation_clips(self) -> List:
        return []

    @property
    def current_animation_clip(self):
        return None

    @current_animation_clip.setter
    def current_animation_clip(self, value):
        pass

    @property
    def poses(self) -> List:
        return []

    def clear(self):
        from .Node import Node
        self._root_node = Node()
        self._sub_scenes.clear()
        self._library.clear()
        self._propagate_scene()

    def create_animation_clip(self, name: str):
        raise NotImplementedError("create_animation_clip is not implemented")

    def get_animation_clip(self, name: str):
        raise NotImplementedError("get_animation_clip is not implemented")

    def open(self, file_or_stream, options=None):
        self.clear()
        from .formats import IOService, LoadOptions
        from .FileFormat import FileFormat

        io_service = IOService()
        stream = None
        file_name = None

        if hasattr(file_or_stream, 'read'):
            stream = file_or_stream
            detected_format = io_service.detect_format(stream, "")
            if detected_format is None:
                raise RuntimeError("Unable to detect file format from stream")
        else:
            file_name = file_or_stream
            detected_format = FileFormat.get_format_by_extension('.' + file_name.split('.')[-1])
            if detected_format is None:
                raise RuntimeError(f"Unable to detect file format from file name: {file_name}")
            stream = open(file_name, 'rb')

        try:
            if options is None:
                options = detected_format.create_load_options()
            elif not isinstance(options, LoadOptions):
                options = detected_format.create_load_options()

            if hasattr(options, 'file_name') and options.file_name is None:
                options.file_name = file_name

            importer = io_service.create_importer(detected_format)
            importer.import_scene(self, stream, options)
        finally:
            if file_name is not None and stream is not None:
                stream.close()

    def save(self, file_or_stream, format_or_options=None):
        from .formats import IOService, SaveOptions
        from .FileFormat import FileFormat

        io_service = IOService()
        stream = None
        file_name = None
        detected_format = None
        options = None

        if hasattr(file_or_stream, 'write'):
            stream = file_or_stream
            if isinstance(format_or_options, SaveOptions):
                detected_format = format_or_options.file_format
                options = format_or_options
            else:
                detected_format = format_or_options
        else:
            file_name = file_or_stream
            if isinstance(format_or_options, SaveOptions):
                detected_format = format_or_options.file_format
                options = format_or_options
                if detected_format is None:
                    detected_format = FileFormat.get_format_by_extension('.' + file_name.split('.')[-1])
            elif format_or_options is not None:
                detected_format = format_or_options
            else:
                detected_format = FileFormat.get_format_by_extension('.' + file_name.split('.')[-1])
            
            stream = open(file_name, 'wb')

        try:
            if options is None:
                options = detected_format.create_save_options()
            elif not isinstance(options, SaveOptions):
                options = detected_format.create_save_options()

            if hasattr(options, 'file_name') and options.file_name is None:
                options.file_name = file_name

            exporter = io_service.create_exporter(detected_format)
            exporter.export(self, stream, options)
        finally:
            if file_name is not None and stream is not None:
                stream.close()

    def render(self, camera, file_name_or_bitmap, size=None, format=None, options=None):
        raise NotImplementedError("render is not implemented")

    @staticmethod
    def from_file(file_name: str):
        scene = Scene()
        scene.open(file_name)
        return scene

    def _propagate_scene(self):
        self.scene = self
        if self._root_node is not None:
            self._root_node.scene = self
            self._root_node._propagate_scene(self)
        for sub_scene in self._sub_scenes:
            sub_scene.scene = self

    def __repr__(self) -> str:
        root_name = self._root_node.name if self._root_node is not None else "None"
        return f"Scene({self.name}, root={root_name})"
