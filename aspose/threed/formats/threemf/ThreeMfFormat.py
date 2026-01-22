from typing import List, Optional
from aspose.threed.utilities import Matrix4


class ThreeMfFormat:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def extension(self) -> str:
        return "3mf"

    @property
    def extensions(self) -> List[str]:
        return ["3mf"]

    @property
    def content_type(self) -> str:
        return "model/3mf"

    @property
    def file_format_type(self):
        return None

    @property
    def version(self) -> str:
        return "1.4.0"

    @property
    def can_export(self) -> bool:
        return True

    @property
    def can_import(self) -> bool:
        return True

    @property
    def formats(self) -> List:
        return []

    def create_load_options(self):
        from .ThreeMfLoadOptions import ThreeMfLoadOptions
        return ThreeMfLoadOptions()

    def create_save_options(self):
        from .ThreeMfSaveOptions import ThreeMfSaveOptions
        return ThreeMfSaveOptions()

    def is_buildable(self, node) -> bool:
        from aspose.threed import Node
        if not isinstance(node, Node):
            return False
        
        buildable_key = '3mf_buildable'
        buildable_value = node.get_property(buildable_key)
        return buildable_value if buildable_value is not None else True

    def get_transform_for_build(self, node) -> Optional[Matrix4]:
        from aspose.threed import Node
        if not isinstance(node, Node):
            return None
        
        transform_key = '3mf_build_transform'
        return node.get_property(transform_key)

    def set_buildable(self, node, value: bool, transform: Optional[Matrix4] = None):
        from aspose.threed import Node
        if not isinstance(node, Node):
            return
        
        node.set_property('3mf_buildable', value)
        
        if transform is not None:
            node.set_property('3mf_build_transform', transform)

    def set_object_type(self, node, model_type: str):
        from aspose.threed import Node
        if not isinstance(node, Node):
            return
        
        valid_types = ['model', 'surface', 'solidsupport', 'support', 'other']
        if model_type not in valid_types:
            raise ValueError(f'Invalid object type. Must be one of: {valid_types}')
        
        node.set_property('3mf_object_type', model_type)

    def get_object_type(self, node) -> str:
        from aspose.threed import Node
        if not isinstance(node, Node):
            return 'model'
        
        object_type = node.get_property('3mf_object_type')
        return object_type if object_type is not None else 'model'
